from slacker import Slacker
import os

farm_names = ['Farmers are friends, not food','Farm to fork',
              'Farmer Land','tekraM s\'remraF','Old MacDonald\'s',
              'Real talk, does Judy have a farm fetish?']

key = os.environ.get('SLACK_API_KEY', None)

slack = Slacker(key)

lunch_poll = 'React with your lunch choice, or else:\n' \
             '1. Cass\n' \
             '2. King\'s Cross\n' \
             '3. %s\n' \
             '4. Spit & Fire\n' \
             '5. Mikey\'s\n' \
             '6. Is Chopstick\'s really even open?' % (farm_names[randint(0,5)])

# Send a message to #botsgonewild channel
slack.chat.post_message('#botsgonewild', lunch_poll, as_user=True)
