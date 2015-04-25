"""
Created on May 2, 2014

@author: John Sabath - /u/_Zaga_
"""
import praw
import requests
import time
import traceback

#
# VARIABLES TO CONFIGURE
#
REDDIT_USERNAME = ''
REDDIT_PASSWORD = ''
SUBREDDIT = ''

TWITCH_CHANNEL = ''
AZUBU_CHANNEL = ''  # Case sensitive
#
#
#

USER_AGENT = 'Twitch status script for /r/%s' % SUBREDDIT

STATUS_CHECK_INTERVAL = 10  # minutes

TWITCH_API = 'https://api.twitch.tv/kraken/streams/%s'
AZUBU_API = 'http://api.azubu.tv/public/channel/%s/info'

twitch_online = False
azubu_online = False

r = praw.Reddit(user_agent=USER_AGENT)
r.login(REDDIT_USERNAME, REDDIT_PASSWORD)


def check_twitch():
    global r
    global twitch_online

    data = requests.get(TWITCH_API % TWITCH_CHANNEL).json()

    if data['stream'] is not None:
        if not twitch_online:
            print("Twitch stream has come online!")

            twitch_online = True

            title = "[TWITCH] %s is online and is playing %s : %s" % (TWITCH_CHANNEL,
                                                                   data['stream']['channel']['game'],
                                                                   data['stream']['channel']['status'])

            r.submit(SUBREDDIT, title, url=data['stream']['channel']['url'], resubmit=True)
    else:
        if twitch_online:
            print("Twitch stream has gone offline.")
            twitch_online = False


def check_azubu():
    global r
    global azubu_online

    data = requests.get(AZUBU_API % AZUBU_CHANNEL).json()

    if data['data']['is_live']:
        if not azubu_online:
            print("Azubu stream has come online!")

            azubu_online = True

            title = "[AZUBU] %s is online and is playing %s" % (AZUBU_CHANNEL,
                                                                data['data']['category']['title'])

            r.submit(SUBREDDIT, title, url="http://www.azubu.tv/" % AZUBU_CHANNEL, resubmit=True)
    else:
        if azubu_online:
            print("Azubu stream has gone offline.")
            azubu_online = False


def main():
    if REDDIT_PASSWORD is '' or REDDIT_USERNAME is '':
        print("Error: Reddit credientials are not set")
        return

    if SUBREDDIT is '':
        print("Error: Subreddit is not set")
        return

    if TWITCH_CHANNEL is not '':
        print("Twitch checking is enabled for '%s'" % TWITCH_CHANNEL)

    if AZUBU_CHANNEL is not '':
        print("Azubu checking is enabled for '%s'" % AZUBU_CHANNEL)

    while True:
        try:
            if TWITCH_CHANNEL is not '':
                check_twitch()

            if AZUBU_CHANNEL is not '':
                check_azubu()

            time.sleep(STATUS_CHECK_INTERVAL * 60)
        except:
            print(traceback.format_exc())


if __name__ == '__main__':
    main()