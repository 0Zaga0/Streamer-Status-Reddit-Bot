from setuptools import setup

setup(name='Streamer-Status-Reddit-Bot',
      version='1.0',
      description="Edits a subreddit's sidebar whenever specified streamers come online on Twitch or Azubu",
      author='John Sabath',
      author_email='jcsabath@gmail.com',
      install_requires=[
          'praw>=2.1.21',
          'requests>=2.6.0'
      ]
)