from slacker import Slacker
import os

key = os.environ.get('SLACK_API_KEY', None)

slack = Slacker(key)

# Send a message to #botsgonewild channel
slack.chat.post_message('#botsgonewild', 'Hello fellow robots!', as_user=True)
