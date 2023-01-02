# Counts the number of letters in a message

import pprint  # PrettyPrint

message = 'It was a bright cold day in April, and the clocks were striking thirteen'  # String is a list of characters
count = {}

for something in message.upper():  # .upper() returns an uppercase form of the string
    count.setdefault(something, 0)
    count[something] = count[something] + 1

pprint.pprint(count)  # Prettyprints the dictionary
