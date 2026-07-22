#20126596 Daniel Cummings

#imports
import time

#variables
num_of_beers = 99

def s_print(string):
    for i in string:
        time.sleep(0.05)
        print(i, end='')
    print()

while num_of_beers > 0:
    if num_of_beers == 1:
        print(f"There is 1 bottle of beer on the wall!")
        print(f"1 bottle of beer.")
        print(f"Take it down, pass it around.")
        print(f"There are 0 bottles of beer on the wall.")
    else:
        print(f"There are {num_of_beers} bottles of beer on the wall!")
        print(f"{num_of_beers} bottles of beer.")
        print(f"Take one down, pass it around,")
    num_of_beers -= 1
    if num_of_beers == 1:
        print(f"There is 1 bottle of beer on the wall.\n")
    else:
        print(f"There are {num_of_beers} bottles of beer.\n")