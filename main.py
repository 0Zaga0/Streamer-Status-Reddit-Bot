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
REDDIT_USERNAME = ''
REDDIT_PASSWORD = ''
SUBREDDIT = ''
#
#
#

USER_AGENT = 'Twitch status script for /r/%s' % SUBREDDIT

STATUS_CHECK_INTERVAL = 10  # minutes

TWITCH_API = 'https://api.twitch.tv/kraken/streams/%s'
AZUBU_API = 'http://api.azubu.tv/public/channel/%s/info'

r = praw.Reddit(user_agent=USER_AGENT)
r.login(REDDIT_USERNAME, REDDIT_PASSWORD)

states = {}
sidebar = ""


def check_twitch(twitch_channel):
    global r
    global states

    data = requests.get(TWITCH_API % twitch_channel).json()

    if 'twitch_'+twitch_channel not in states:
        states['twitch_'+twitch_channel] = None

    if data['stream'] is not None:
        if not states['twitch_'+twitch_channel]:
            print(twitch_channel+"@Twitch is online!")

            states['twitch_'+twitch_channel] = True
            title = "%s is online and is playing %s : %s" % (twitch_channel,
                                                             data['stream']['channel']['game'],
                                                             data['stream']['channel']['status'])

            update_sidebar('twitch_'+twitch_channel, True, title, "http://www.twitch.tv/%s" % twitch_channel)
    else:
        if states['twitch_'+twitch_channel] or states['twitch_'+twitch_channel] is None:
            states['twitch_'+twitch_channel] = False
            update_sidebar('twitch_'+twitch_channel, False, "%s is currently offline" % twitch_channel, "")


def check_azubu(azubu_channel):
    global r
    global states

    data = requests.get(AZUBU_API % azubu_channel).json()

    if 'azubu_'+azubu_channel not in states:
        states['azubu_'+azubu_channel] = None

    if data['data']['is_live']:
        if not states['azubu_'+azubu_channel]:
            print(azubu_channel+"@Azubu is online!")

            states['azubu_'+azubu_channel] = True
            title = "%s is online and is playing %s" % (azubu_channel, data['data']['category']['title'])

            update_sidebar('azubu_'+azubu_channel, True, title, "http://www.azubu.tv/%s" % azubu_channel)
    else:
        if states['azubu_'+azubu_channel] or states['azubu_'+azubu_channel] is None:
            states['azubu_'+azubu_channel] = False
            update_sidebar('azubu_'+azubu_channel, False, "%s is currently offline" % azubu_channel, "")


def update_sidebar(service_name, online, message, stream_url):
    global sidebar

    sidebar = re.sub("\[.*\]\(.*#%s_(online|offline)\)" % service_name,
                     "[%s](%s#%s_%s)" % (message, stream_url, service_name, "online" if online else "offline"),
                     sidebar)


def check_sidebar():
    global r
    global sidebar

    subreddit = r.get_subreddit(SUBREDDIT)
    sidebar = HTMLParser.HTMLParser().unescape(r.get_settings(SUBREDDIT)['description'])

    for res in re.findall("\[.*\]\(.*#(twitch|azubu)_(\w+)_(online|offline)\)", sidebar):
        print("Checking %s for %s" % (res[0], res[1]))
        if res[0] == "twitch":
            check_twitch(res[1])
        if res[1] == "azubu":
            check_azubu(res[1])

    r.update_settings(subreddit, description=sidebar)


def main():
    if REDDIT_PASSWORD is '' or REDDIT_USERNAME is '':
        print("Error: Reddit credientials are not set")
        return

    if SUBREDDIT is '':
        print("Error: Subreddit is not set")
        return

    while True:
        try:
            check_sidebar()
            time.sleep(STATUS_CHECK_INTERVAL * 60)
        except:
            print(traceback.format_exc())

if __name__ == '__main__':
    main()
