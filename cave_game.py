import shelve

# cave_game.py will then use the two shelves instead of dictionaries.
# Apart from opening and closing the shelves, cave_game will need only
# two changes to the actual code - remember that shelf keys MUST be strings!
#
# Just to be clear, cave_game.py will contain the code from line 45, everything
# before that (modified to use shelves) will be in cave_initialise.py.

with shelve.open('locations') as locations:
    with shelve.open('vocabulary') as vocabulary:

        loc = 1
        while True:
            availableExits = ", ".join(locations[str(loc)]["exits"].keys())
            print(locations[str(loc)]["desc"])

            if loc == 0:
                break
            else:
                allExits = locations[str(loc)]["exits"].copy()
                allExits.update(locations[str(loc)]["namedExits"])

            direction = input("Available exits are " + availableExits).upper()
            print()

            # Parse the user input, using our vocabulary dictionary if necessary
            if len(direction) > 1:  # more than 1 letter, so check vocab
                words = direction.split()
                for word in words:
                    if word in vocabulary:  # does it contain a word we know?
                        direction = vocabulary[word]
                        break

            if direction in allExits:
                loc = allExits[direction]
            else:
                print("You cannot go in that direction")