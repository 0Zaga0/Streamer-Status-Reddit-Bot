"""
Created on May 2, 2014

@author: John Sabath - /u/_Zaga_
"""
import praw
import requests
import time
import traceback
import re
import HTMLParser

#
# VARIABLES TO CONFIGURE
#
REDDIT_USERNAME = 'LoLFantasyBot'
REDDIT_PASSWORD = '%^fw9DYkus0VT5jq'
SUBREDDIT = 'zagatest'

TWITCH_CHANNEL = 'TSM_WildTurtle'
AZUBU_CHANNEL = 'Faker'  # Case sensitive
#
#
#

USER_AGENT = 'Twitch status script for /r/%s' % SUBREDDIT

STATUS_CHECK_INTERVAL = 10  # minutes

TWITCH_API = 'https://api.twitch.tv/kraken/streams/%s'
AZUBU_API = 'http://api.azubu.tv/public/channel/%s/info'

twitch_online = None
azubu_online = None

r = praw.Reddit(user_agent=USER_AGENT)
r.login(REDDIT_USERNAME, REDDIT_PASSWORD)


def check_twitch():
    global r
    global twitch_online

    data = requests.get(TWITCH_API % TWITCH_CHANNEL).json()

    if data['stream'] is not None:
        if not twitch_online:
            print("Twitch stream is online!")

            twitch_online = True
            title = "%s is online and is playing %s : %s" % (TWITCH_CHANNEL,
                                                             data['stream']['channel']['game'],
                                                             data['stream']['channel']['status'])

            update_sidebar('twitch', twitch_online, title, "http://www.twitch.tv/%s" % TWITCH_CHANNEL)
    else:
        if twitch_online or twitch_online is None:
            print("Twitch stream is offline.")
            twitch_online = False
            update_sidebar('twitch', twitch_online, "%s is currently offline" % TWITCH_CHANNEL, "")


def check_azubu():
    global r
    global azubu_online

    data = requests.get(AZUBU_API % AZUBU_CHANNEL).json()

    if data['data']['is_live']:
        if not azubu_online:
            print("Azubu stream is online!")

            azubu_online = True
            title = "%s is online and is playing %s" % (AZUBU_CHANNEL, data['data']['category']['title'])

            update_sidebar('azubu', azubu_online, title, "http://www.azubu.tv/%s" % AZUBU_CHANNEL)
    else:
        if azubu_online or azubu_online is None:
            print("Azubu stream is offline.")
            azubu_online = False
            update_sidebar('azubu', azubu_online, "%s is currently offline" % AZUBU_CHANNEL, "")


def update_sidebar(service_name, online, message, stream_url):
    global r

    subreddit = r.get_subreddit(SUBREDDIT)
    sidebar = HTMLParser.HTMLParser().unescape(r.get_settings(SUBREDDIT)['description'])
    sidebar = re.sub("\[.*\]\(.*#%s_(online)?(offline)?\)" % service_name,
                     "[%s](%s#%s_%s)" % (message, stream_url, service_name, "online" if online else "offline"),
                     sidebar)

    r.update_settings(subreddit, description=sidebar)


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