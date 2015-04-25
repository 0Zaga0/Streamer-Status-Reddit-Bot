from setuptools import setup

setup(name='Reddit Livestream Alerter',
      version='1.0',
      description='Makes a post in a specified subreddit whenever a specified user comes online on Twitch or Azubu',
      author='John Sabath',
      author_email='jcsabath@gmail.com',
      install_requires=[
          'praw>=2.1.21',
          'requests>=2.6.0'
      ]
)