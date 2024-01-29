# Global variables
##################
splash_screen = False
inventory = []
total_inventory = ["A PILE OF HAY",
                   "A SLINGSHOT",
                   "AN OIL CAN",
                   "COWARDLY LION",
                   "JELLYBEANS",
                   "RUBY RED SLIPPERS",
                   "SCARECROW",
                   "TIN MAN",
                   "WITCH'S BROOM"]
current_location = "Kansas"
current_item = ""
all_directions = ["NORTH", "EAST", "SOUTH", "WEST"]
end_of_game = False


# Function Definitions
# ####################
def print_location_description():
    # Execute appropriate location function based on current_location
    if current_location == "Kansas":
        kansas()
    elif current_location == "Munchkinland":
        munchkinland()
    elif current_location == "Yellow Brick Road West":
        yellow_brick_road_west()
    elif current_location == "Cornfield":
        cornfield()
    elif current_location == "Yellow Brick Road Mid-West":
        yellow_brick_road_midwest()
    elif current_location == "Damp Glade":
        damp_glade()
    elif current_location == "Yellow Brick Road Mid-East":
        yellow_brick_road_mideast()
    elif current_location == "Scary Forest":
        scary_forest()
    elif current_location == "Yellow Brick Road East":
        yellow_brick_road_east()
    elif current_location == "Witch's Castle":
        witchs_castle()
    elif current_location == "Emerald City":
        emerald_city()


def is_current_item_in_inventory(item: str):
    # When an available item is not in inventory print text describing the situation or, alternatively,
    # when a companion character has not yet been rescued and Toto does not possess the item needed to
    # save them print text describing that situation
    if item not in inventory:
        print("")
        if current_location == "Munchkinland":
            print("Incidentally, there are a pair of unmoving feet sticking out from under the house that have")
            print("a pair of ruby red slippers on them. Those are some fine shoes!.")
        elif current_location == "Yellow Brick Road West":
            print("There is a pile of hay on the ground. I wonder if that could be of any use?")
        elif current_location == "Cornfield" and "A PILE OF HAY" not in inventory:
            print("You spot a badly under-stuffed scarecrow on the ground.")
            print("'Woe is me!' weeps the scarecrow.")
            print("Wow! This is a talking scarecrow!")
            print("'Please!' begs Scarecrow. 'Will you find some hay to stuff me up with?")
            print("You say 'Bark' sympathetically.")
            print("'I agree' says Dorothy. 'We should help him out.'")
        elif current_location == "Yellow Brick Road Mid-West":
            print("Somebody has carelessly left a can of oil in the middle of nowhere. Better take it and see if")
            print("we can find the owner.")
        elif current_location == "Damp Glade" and "AN OIL CAN" not in inventory:
            print("You see a very rusty metal statue.")
            print("'hmmmmnnnnn?' goes the statue.")
            print("'Wow...' you think, a magical talking statue. Better help it out. You say 'Bark!'")
            print("'I agree.' says Dorothy. 'We need some oil to save this poor fellow.'")
            print("'HMMMN!!!' says the Tin Man emphatically.")
        elif current_location == "Yellow Brick Road Mid-East":
            print("A slingshot is resting in the tall grass along the roadside.")
        elif current_location == "Scary Forest" and "A SLINGSHOT" not in inventory:
            print("'ROOOOAAAAAAR!!!' roars the Cowardly Lion as he jumps out from behind a tree. 'Aw Geez! I")
            print("probably startled you guys. I am SO sorry. WON'T happen again. PLEASE don't be angry.'")
            print("'Bark!' you say in a disgusted tone.")
            print("'I agree' says Dorothy. 'That was not necessary.'")
            print("'Can you guys help me out? I'm trying to find my slingshot' says the Cowardly Lion.")
        elif current_location == "Yellow Brick Road East":
            print("There are some jellybeans just sitting out in the open. They would make great ammunition")
            print("for a slingshot!")
        elif current_location == "Witch's Castle":
            print("As you enter the courtyard you see a group of monkeys with wings! They look like they could be")
            print("trouble, but before you can bark a warning one of them points at Dorothy and says")
            print("'That's the nice lady who got rid of the Wicked Witch of the East! Thanks lady.' The monkeys")
            print("then throw Dorothy an impromptu party with cake and everything.")

        # When the item needed to save a companion character is in inventory and the companion character has not yet
        # been rescued there is different text to print
        if current_location == "Cornfield" \
                and "A PILE OF HAY" in inventory \
                and "SCARECROW" not in inventory:
            print("'Please!' begs Scarecrow. 'I see you have a pile of hay. Will you kindly share it?'")
            print("Your little doggy heart goes out to Scarecrow and you say 'Bark!'")
            print("'I agree.' says Dorothy, and stuffs the scarecrow full of hay.")
            print("Scarecrow says 'I can't believe your kindness. I'll never leave your side.'")
            # Automatically add the companion character to Toto's inventory
            inventory.append("SCARECROW")
        elif current_location == "Damp Glade" \
                and "AN OIL CAN" in inventory \
                and "TIN MAN" not in inventory:
            print("You see a very rusty metal statue.")
            print("'hmmmmnnnnn' goes the statue. 'HMMMMMMMMMNNNN!!!'")
            print("A living statue! Better help it out. You say 'Bark!'")
            print("'I agree. Lubrication will do the trick!' says Dorothy, as she begins to generously")
            print("apply oil to the Tin Man.")
            print("'Thanks... a... ton...' creaks the Tin Man. 'Can I... go with... you?")
            print("'Bark!' you say in warm greeting to the Tin Man.")
            print("'I agree.' says Dorothy.")
            # Automatically add the companion character to Toto's inventory
            inventory.append("TIN MAN")
        elif current_location == "Scary Forest" \
                and "A SLINGSHOT" in inventory \
                and "COWARDLY LION" not in inventory:
            print("A visibly terrified Cowardly Lion approaches and says 'Aw geez! Please don't shoot me with")
            print("the slingshot! I dropped it when I had to run away from a butterfly! Could I pretty please")
            print("have it back? Having the slingshot makes me feel like a big man...")
            print("Grudgingly you say 'Bark.'")
            print("'I agree' says Dorothy. 'I'll give him the slingshot to make him feel better about himself.'")
            print("With gratitude and trembling paws the Cowardly Lion accepts the slingshot.")
            print("'I don't suppose you'd take me with you?' pleads the Cowardly Lion. 'This forest is giving")
            print("me the creeps!")
            print("With some concern you bark your consent to the Cowardly Lion joining.")
            print("'I agree' says Dorothy.")
            # Automatically add the companion character to Toto's inventory
            inventory.append("COWARDLY LION")
    print("")

    # If item/companion character are not in inventory and Toto is not in Kansas then inform the player of the
    # item available to take
    if item not in inventory and current_location != "Kansas":
        # Use formatting to bold the current_item name to make it easier to see
        print(f"You see \033[1m{current_item}\033[0m on the ground.")
    else:
        # Inform player that there are no items available to take at this location
        print("There are no items available to take.")
    print("")


def describe_inventory():
    # Print Toto's inventory following each location description
    print(f"You have the following items: {inventory}")
    print("")


def get_instruction():
    # Prepare to modify global variables
    global current_location
    global current_item
    # Prompt player for two part input; e.g. "GET AN OIL CAN" or "GO NORTH"
    instruction = input("What do you want to do next: GET <item>, or GO <direction>? ")
    print("")
    # Read first three characters of player input and raise them to uppercase
    go_command = instruction[:3].upper()
    # Determine if player input starts with "GO "
    if go_command == "GO ":
        # Read from the 4th character on in the player's input and raise them to uppercase
        direction = instruction[3:].upper()
        # Determine if the value of "direction" variable is a legitimate compass direction
        if direction in all_directions:
            # Assess current_location and "direction" variable to determine new current location
            # NOTE: There is not an option to go east from Munchkinland  to Kansas as Toto should
            # not be able return to Kansas at any point of the story
            if current_location == "Kansas" and direction == "WEST":
                current_location = "Munchkinland"
            elif current_location == "Munchkinland" and direction == "SOUTH":
                current_location = "Yellow Brick Road West"
            elif current_location == "Yellow Brick Road West" and direction == "SOUTH":
                current_location = "Cornfield"
            elif current_location == "Cornfield" and direction == "NORTH":
                current_location = "Yellow Brick Road West"
            elif current_location == "Yellow Brick Road West" and direction == "NORTH":
                current_location = "Munchkinland"
            elif current_location == "Yellow Brick Road West" and direction == "EAST":
                current_location = "Yellow Brick Road Mid-West"
            elif current_location == "Yellow Brick Road Mid-West" and direction == "WEST":
                current_location = "Yellow Brick Road West"
            elif current_location == "Yellow Brick Road Mid-West" and direction == "SOUTH":
                current_location = "Damp Glade"
            elif current_location == "Damp Glade" and direction == "NORTH":
                current_location = "Yellow Brick Road Mid-West"
            elif current_location == "Yellow Brick Road Mid-West" and direction == "EAST":
                current_location = "Yellow Brick Road Mid-East"
            elif current_location == "Yellow Brick Road Mid-East" and direction == "WEST":
                current_location = "Yellow Brick Road Mid-West"
            elif current_location == "Yellow Brick Road Mid-East" and direction == "SOUTH":
                current_location = "Scary Forest"
            elif current_location == "Scary Forest" and direction == "NORTH":
                current_location = "Yellow Brick Road Mid-East"
            elif current_location == "Yellow Brick Road Mid-East" and direction == "EAST":
                current_location = "Yellow Brick Road East"
            elif current_location == "Yellow Brick Road East" and direction == "WEST":
                current_location = "Yellow Brick Road Mid-East"
            elif current_location == "Yellow Brick Road East" and direction == "SOUTH":
                current_location = "Witch's Castle"
            elif current_location == "Witch's Castle" and direction == "NORTH":
                current_location = "Yellow Brick Road East"
            elif current_location == "Yellow Brick Road East" and direction == "NORTH":
                current_location = "Emerald City"
            # Inform user that they have specified a direction that they cannot travel in
            else:
                print(f"Going {direction} is not available here. Try another direction.")
                print("")
        # Inform user that they have specified a non-existent direction; e.g. NORT
        else:
            print(f"Direction {direction} is not understood. Try NORTH, EAST, SOUTH, or WEST.")
            print("")
    # Determine if the player input starts with "GET "
    elif instruction[:4].upper() == "GET ":
        # Read from the 5th character on in the player's input and raise them to uppercase
        item = instruction[4:].upper()
        # Check if the item is the same as the current_item
        if item == current_item:
            # Check if the item is already in Toto's inventory
            if (item == "SCARECROW" and "A PILE OF HAY" not in inventory) or \
                    (item == "TIN MAN" and "AN OIL CAN" not in inventory) or \
                    (item == "COWARDLY LION" and "A SLINGSHOT" not in inventory):
                print(f"You don't have the necessary item to rescue the {item}.")
            # Check that the item is not in Toto's inventory
            elif item not in inventory:
                # Add the item to the player's inventory
                inventory.append(item)
                # Update the current item to reflect that it is no longer available to take from the current location
                current_item = ""
            else:
                # Inform user that the item they typed does not match the item associated with the current location
                # To make it easier to read and understand use formatting to bold the item name
                print(f"Get \033[1m{item}\033[0m is not understood. Try command again.")
    print("")


def print_splash_screen():
    # Splash Screen Graphic
    print("⠀⢐⣯⠉⠙⢶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠞⠉⠹⣿⣄")
    print("⠀⠘⣇⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⠀⠈⢠⠃")
    print("⠀⠀⣿⠀⠀⠀⠀⠀⠙⠦⣄⣠⣤⣤⣤⣀⣠⠟⠀⠀⠀⠀⠀⠀⣼⠀")
    print("⠀⢠⠋⠀⠀⣀⠄⠒⠂⠄⠀⠀⠀⠀⠀⠠⠐⠒⣠⣄⣀⠀⠀⠀⣏⠀")
    print("⠀⣧⣴⠖⠋⠁⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠢⣦⣸⠀")
    print("⠀⡿⠁⠀⠀⢀⠤⠂⢉⡁⠀⠀⠀⠀⠀⢀⡁⠐⠠⢄⠀⠀⠀⠈⢿⠀")
    print("⢸⡇⠀⢠⡞⠁⠀⣾⣧⣿⣆⠀⠀⢀⣸⣿⣼⣷⠀⠀⠑⢄⠀⣄⠸⡀")
    print("⢸⣵⢡⠋⠀⠀⢀⡿⠋⠉⠀⣉⣉⣉⠁⠉⠙⠿⠀⠀⠀⠀⠣⣸⣿⠃")
    print("⠀⢹⠏⠀⠀⠀⠉⠀⠀⠀⠘⢿⣿⠿⠃⠀⠀⠀⠀⠂⠀⠀⠀⢹⡇⠀")
    print("⠀⢸⠀⡄⠀⠀⠀⠀⠀⠠⠀⠤⠶⠤⠀⠤⠀⠀⠀⠀⠆⠀⠀⣨⡇⠀")
    print("⠀⠈⠷⣇⡀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣆⠀⢀⡼⠛⠁⠀")
    print("⠀⠀⠀⠈⢳⣸⣆⡸⡄⢠⠀⠤⠤⠤⠀⡆⠠⢃⡼⣿⠞⠉⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠉⠀⢩⠉⠀⠂⠀⠀⠀⠀⠀⠀⠘⡄⠈⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⢠⡟⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⢳⣤⠶⠲⣦⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⢀⡞⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⣤⣤⡿⠀⠀⠀")
    print("⠀⠀⠀⠀⢠⡞⡇⠀⠀⠑⢄⡐⢄⠀⢀⠊⠀⠀⠀⢸⠀⢹⡆⠀⠀⠀")
    print("⠀⠀⠀⠀⢸⢃⣁⠀⠀⠀⠀⢁⠀⠀⡘⠀⠀⠀⠀⢸⢀⣠⡟⠀⠀⠀ **********************************")
    print("⠀⠀⠀⠀⠈⠙⠻⡄⠀⠀⢀⡼⠟⠛⢇⠀⢀⠀⢠⠧⠾⠋⠀⠀⠀⠀*------TOTO'S BIG ADVENTURE------*")
    print("⠀⠀⠀⠀⠀⠀⠀⠓⠓⠓⠋⠀⠀⠀⠈⠓⠛⠚⠋        **********************************")
    print("")


def kansas():
    # Prepare to modify global variables
    global current_location
    global current_item
    # Modify Global variables
    current_location = "Kansas"
    current_item = ""

    print("************************************************************************************************")
    print("*-------------------------------------------KANSAS---------------------------------------------*")
    print("************************************************************************************************")
    print("")
    print("You are living your best life as a small dog riding in the basket of your owner's bicycle.")
    print("Suddenly you notice a tornado forming on the eastern horizon. You exclaim 'Bark!'")
    print("'I agree' Dorothy replies. 'We'd better get home right away!'")
    print("")
    print("You arrive at home just ahead of the approaching tornado, but Dorothy can't find her aunt or")
    print("uncle! The tornado rips the house from the ground (somehow intact) and you go flying into the")
    print("sky. After several dizzy minutes you land with a thump. ")
    print("How far did that tornado take us? We'd better look. You say 'Bark!'")
    print("'I agree.' Dorothy replies as she dusts herself off. 'We should check outside.'")
    print("")
    print("You see the front door to the WEST.")


def munchkinland():
    # Prepare to modify global variables
    global current_location
    global current_item
    # Modify global variables
    current_location = "Munchkinland"
    current_item = "RUBY RED SLIPPERS"

    print("************************************************************************************************")
    print("*----------------------------------------MUNCHKINLAND------------------------------------------*")
    print("************************************************************************************************")
    print("")
    print("Your little doggy brain is badly shaken by the scene before you; little men and women caper")
    print("around a candy-strewn fantasy land made of psychedelic colors and odors. They are cheering at")
    print("Dorothy because they appear to believe that she deliberately landed the house on a local witch.")
    print("'Thanks for that!' pipes the Munchkin Mayor. 'Now go take care of the Wizard of Oz. That guy is")
    print("one heck of a jerk! He uses us Munchkins as forced labor!'")
    print("")
    print("You see the Yellow Brick Road West to the SOUTH.")


def yellow_brick_road_west():
    # Prepare to modify global variables
    global current_location
    global current_item
    # Modify global variables
    current_location = "Yellow Brick Road West"
    current_item = "A PILE OF HAY"

    print("************************************************************************************************")
    print("*----------------------------------YELLOW BRICK ROAD WEST--------------------------------------*")
    print("************************************************************************************************")
    print("")
    print("This section of the Yellow Brick Road is a rolling plain that is being used to grow corn.")
    print("There is a high hill in the middle of the cornfield to the south.")
    print("")
    print("You see Munchkinland to the NORTH.")
    print("You see the Yellow Brick Road Mid-West to the EAST.")
    print("You see a high hill in the corn field to the SOUTH.")


def cornfield():
    # Prepare to modify global variables
    global current_location
    global current_item
    # Modify global variables
    current_location = "Cornfield"
    current_item = "SCARECROW"

    print("************************************************************************************************")
    print("*-----------------------------------------CORNFIELD--------------------------------------------*")
    print("************************************************************************************************")
    print("")
    print("You enter the cornfield and eventually reach the top of the hill. Quite a view from up here!")
    print("")
    print("You see the Yellow Brick Road West to the NORTH.")


def yellow_brick_road_midwest():
    # Prepare to modify global variables
    global current_location
    global current_item
    # Modify global variables
    current_location = "Yellow Brick Road Mid-West"
    current_item = "AN OIL CAN"

    print("************************************************************************************************")
    print("*---------------------------------YELLOW BRICK ROAD MID-WEST-----------------------------------*")
    print("************************************************************************************************")
    print("")
    print("The Yellow Brick Road meanders near a damp glade just to the south. In the southern")
    print("")
    print("You see the Yellow Brick Road West to the WEST.")
    print("You see the Yellow Brock Road Mid-East to the EAST.")
    print("You see the Damp Glade to the SOUTH.")


def damp_glade():
    # Prepare to modify global variables
    global current_location
    global current_item
    # Modify global variables
    current_location = "Damp Glade"
    current_item = "TIN MAN"

    print("************************************************************************************************")
    print("*-----------------------------------------DAMP GLADE-------------------------------------------*")
    print("************************************************************************************************")
    print("")
    print("You enter the glade and the tall wet grass quickly soaks your fur.")
    print("")
    print("You see the Yellow Brick Road Mid-West to the NORTH.")


def yellow_brick_road_mideast():
    # Prepare to modify global variables
    global current_location
    global current_item
    # Modify global variables
    current_location = "Yellow Brick Road Mid-East"
    current_item = "A SLINGSHOT"

    print("************************************************************************************************")
    print("*---------------------------------YELLOW BRICK ROAD MID-EAST-----------------------------------*")
    print("************************************************************************************************")
    print("")
    print("You walk close by Dorothy as the Yellow Brick Road takes you around the perimeter of a Scary")
    print("Forest. You anxiously say 'Yap yap yap yap yap yap yap yap yap yap yap!!!' but your earnest ")
    print("contribution to the conversation does not seem to be appreciated.")
    print("")
    print("You see the Yellow Brick Road Mid-West to the WEST.")
    print("You see the Yellow Brock Road East to the EAST.")
    print("You see the Scary Forest to the SOUTH.")


def scary_forest():
    # Prepare to modify global variables
    global current_location
    global current_item
    # Modify global variables
    current_location = "Scary Forest"
    current_item = "COWARDLY LION"

    print("************************************************************************************************")
    print("*---------------------------------------SCARY FOREST-------------------------------------------*")
    print("************************************************************************************************")
    print("")
    print("The trees are covered in drooping moss, the air is chill, and the shadows are extra dark.")
    print("")
    print("You see the Yellow Brick Road Mid-East to the NORTH.")


def yellow_brick_road_east():
    # Prepare to modify global variables
    global current_location
    global current_item
    # Modify global variables
    current_location = "Yellow Brick Road East"
    current_item = "JELLYBEANS"

    print("************************************************************************************************")
    print("*-----------------------------------YELLOW BRICK ROAD EAST-------------------------------------*")
    print("************************************************************************************************")
    print("")
    print("The Yellow Brick Road bends to the north here, and you can just see the Emerald City in the")
    print("far distance. To the south, and much closer, looms the Wicked Witch of the East's Castle!")
    print("Since you already dropped a house on her it should probably be safe to approach.")
    print("")
    print("You see the Yellow Brick Road Mid-East to the WEST.")
    print("You see the Witch's Castle to the SOUTH.")
    print("You see the Emerald City to the NORTH.")


def witchs_castle():
    # Prepare to modify global variables
    global current_location
    global current_item
    # Modify global variables
    current_location = "Witch's Castle"
    current_item = "WITCH'S BROOM"

    print("************************************************************************************************")
    print("*--------------------------------------WITCH'S CASTLE------------------------------------------*")
    print("************************************************************************************************")
    print("")
    print("The Witch's Castle looks even scarier up close. 'Bark...' you timidly opine.")
    print("'I agree' whispers Dorothy. 'Let's get out of here as soon as possible.'")
    print("")
    print("You see the Yellow Brick Road East to the NORTH.")


def emerald_city():
    # Prepare to modify global variables
    global inventory
    global end_of_game
    # Alphabetically sort Toto's inventory in preparation of checking it against the total_inventory variable
    inventory = sorted(inventory)
    # Set end_of_game to True
    end_of_game = True

    print("************************************************************************************************")
    print("*---------------------------------------EMERALD CITY-------------------------------------------*")
    print("************************************************************************************************")
    print("")
    print("You arrive at the gates of the Emerald City, more than a little impressed with yourselves.")
    print("'Bark!' you say happily")
    print("'I agree!' says Dorothy. 'We've really come a long way, and now it's time we dealt with this")
    print("jerk who calls himself the Wizard of Oz'.")

    # If the player has collected all the items (the player inventory matches the total_inventory) then
    # they win the game
    if inventory == total_inventory:
        print("Using the Scarecrow's ingenious assault plan, the Tin Man's threatening axe, the Cowardly")
        print("Lion's slingshot, and Dorothy's Ruby Red Slippers along with Witch's Broom you stage a bloodless")
        print("coup of the Emerald City and kick the Wizard of Oz out of town.")
        print("")
        print("Who knew Oz would be so cool? Who needs dumb old Kansas anyhow?")
        print("")
        print("************************************************************************************************")
        print("*----------------------------------YOU HAVE WON THE GAME!!!------------------------------------*")
        print("************************************************************************************************")
    else:
        print("You knock on the huge front door and an indentured Munchkin says 'The Wizard of Oz ain't never")
        print("gonna see nobody nohow! Beat it you losers!'")
        print("Somehow Dorothy convinces the guard to let everyone in to the Emerald City, but this is not good")
        print("news. The Wizard of Oz confiscates all of your items (even the Scarecrow's hay!) and throws")
        print("everyone into the dungeon. It's a dog's life.")
        print("")
        print("************************************************************************************************")
        print("*----------------------------------YOU HAVE LOST THE GAME!!!-----------------------------------*")
        print("************************************************************************************************")


# Main Loop
# #########
while True:
    # Check if the splash screen has been printed one time
    if not splash_screen:
        # Splash screen hasn't been printed yet, so print it
        print_splash_screen()
        # Modify the splash_screen variable too true to prevent further printing of splash screen
        splash_screen = True

    print_location_description()

    if end_of_game:
        quit()

    is_current_item_in_inventory(current_item)
    describe_inventory()
    get_instruction()