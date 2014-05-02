'''
Created on May 2, 2014

@author: John Sabath - /u/_Zaga_
'''
import praw, requests, time, sys

#
# VARIABLES TO CONFIGURE
#
USERNAME = ''
PASSWORD = ''

SUBREDDIT = ''
TWITCH_CHANNEL = ''
#
#
#

USER_AGENT = 'Twitch status bot for /r/%s' % SUBREDDIT

STATUS_CHECK_INTERVAL = 10 #minutes

if __name__ == '__main__':
    online = False

    r = praw.Reddit(user_agent=USER_AGENT)
    r.login(USERNAME, PASSWORD)

    while True:
        try:
            response = requests.get('https://api.twitch.tv/kraken/streams/%s' % TWITCH_CHANNEL)
            data = response.json()

            if data['stream'] != None:
                if not online:
                    print("Stream has come online!")

                    online = True

                    title = "[ONLINE] Playing %s : %s" % (data['stream']['channel']['game'],
                                                          data['stream']['channel']['status'])

                    r.submit(SUBREDDIT, title, url=data['stream']['channel']['url'])
            else:
                if online:
                    print("Stream has gone offline.")
                    online = False

            time.sleep(STATUS_CHECK_INTERVAL * 60)
        except:
            print("Unexpected error:", sys.exc_info()[0])