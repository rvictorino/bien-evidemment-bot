#!/usr/bin/python3

from mastodon import Mastodon
import os
import random
from datetime import datetime

# read config from file
config =

# get token from env variable
token = os.environ['MASTODON_BEARER_TOKEN']

# get API client
mastodon = Mastodon(access_token = token, api_base_url = config['base_url'])

# random answers
def get_random_answer():
  # available answers
  answers = [
    "Bien evidemment !",
    "BIEN EVIDEMMENT !",
    "BIEN EVIDEMM{0}NT !!".format("N" * random.randint(1, 10))
  ]
  return random.choice(answers)


# get all mentions of the bot (@-ed)
notifications = mastodon.notifications()
mentions = filter(lambda n: n['type'] == 'mention')

# answer to all mentions
for mention in mentions:
  # generate a random answer
  ranswer = get_random_answer()

  # posting in reply to mention
  print("{0}: 👤 {1}".format(datetime.now, mention['account']['username']))
  print("{0}: 📯 {1}".format(datetime.now, ranswer))
  mastodon.status_post(ranswer, in_reply_to_id=mention['status'] spoiler_text="bien evidemment")
  print("{0}:  👍".format(datetime.now))

  # dismiss this notification, so it doesn't appear
  # when fetching notifications later
  mastodon.notifications_dismiss(mention)

print("{0}:  👍 😴".format(datetime.now))
