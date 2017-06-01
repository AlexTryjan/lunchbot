from slacker import Slacker
from random import randint
import os

farm_names = ['Farmers are friends, not food','Farm to fork',
              'Farmer Land','tekraM s\'remraF','Old MacDonald\'s',
              'Real talk, does Judy have a farm fetish?']

key = os.environ.get('SLACK_API_KEY', None)

slack = Slacker(key)

lunch_poll = 'React with your lunch choice, or else:\n' \
             ':one: Cass\n' \
             ':two: King\'s Cross\n' \
             ':three: %s\n' \
             ':four: Spit & Fire\n' \
             ':five: Mikey\'s\n' \
             ':six: Is Chopstick\'s really even open?' % (farm_names[randint(0,5)])
print(lunch_poll)

# Send a message to #botsgonewild channel
slack.chat.post_message('#food', lunch_poll, as_user=True)
