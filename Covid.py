import sys
from covid_india import states
i = ('State name')
while i != "quit":
    i =input('State Name:')
    print(states.getdata(i))
    if i == 'quit':
        sys.exit()