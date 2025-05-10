import random
import time

score = 0  # Start with 0 points

def print_pause(message):
    print(message)
    time.sleep(2)

def get_choice(options, valid_choices=["1", "2"]):
    choice = input(f"\n{options}\nChoose a number: ")
    while choice not in valid_choices:
        print_pause("\n⚠️ Please choose a valid option.")
        choice = input(f"\n{options}\nChoose a number: ")
    return choice

def start_game():
    global score
    score = 0  # Reset score at start
    print_pause("🌟 Welcome to the Haunted House Adventure! 🌟")
    print_pause("\nYou are standing in front of an old, creepy house...")
    print_pause("\nA long time ago, a rich family lived here. They disappeared one night, and the house has been empty since.")
    print_pause("\nIt's up to you to find out what happened!")

    choice = get_choice("1 - Go through the front door 🚪\n2 - Walk around the house 🌿", ["1", "2"])
    if choice == "1":
        enter_house()
    else:
        go_around_house()

def enter_house():
    print_pause("\n👉 You enter through the front door...")
    print_pause("\nThe house is dark, and you hear strange noises from upstairs.")
    choice = get_choice("1 - Go upstairs 🚶‍♂️\n2 - Explore the room with the glow 🔦", ["1", "2"])
    if choice == "1":
        meet_ghost()
    else:
        explore_glow_room()

def meet_ghost():
    print_pause("\n👉 You go upstairs and a ghost appears!")
    print_pause("\nThe ghost says, 'Leave now or face the consequences!'")
    choice = get_choice("1 - Fight the ghost ⚔️\n2 - Try to run away 🏃‍♂️", ["1", "2"])
    if choice == "1":
        fight_ghost()
    else:
        lose_game()

def fight_ghost():
    global score
    print_pause("\n👉 You fight the ghost! It is a tough battle...")
    outcome = random.choice(["victory", "defeat"])
    if outcome == "victory":
        print_pause("\n🎉 You defeat the ghost and find the treasure!")
        score += 15
        win_game()
    else:
        print_pause("\n👻 The ghost overpowers you...")
        score -= 5
        lose_game()

def explore_glow_room():
    global score
    print_pause("\n👉 You find a glowing book in a mysterious room...")
    choice = get_choice("1 - Close the book and run 🏃‍♂️\n2 - Read the book 📖", ["1", "2"])
    if choice == "2":
        print_pause("\n👉 The book reveals a hidden key and treasure!")
        score += 10
        win_game()
    else:
        score -= 2
        lose_game()

def go_around_house():
    global score
    print_pause("\n👉 You walk around the house...")
    outcome = random.choice(["garden", "noise"])
    if outcome == "garden":
        print_pause("\n🌸 You find a beautiful garden with treasure!")
        score += 5
        win_game()
    else:
        print_pause("\n😨 You hear creepy noises and run away...")
        score -= 3
        lose_game()

def win_game():
    global score
    print_pause("\n🏆 You found the treasure! Congratulations!")
    print(f"✅ Your final score is: {score}")
    play_again()

def lose_game():
    global score
    print_pause("\n💀 You lost... The house has trapped you!")
    print(f"❌ Your final score is: {score}")
    play_again()

def play_again():
    choice = get_choice("1 - Play again\n2 - Exit", ["1", "2"])
    if choice == "1":
        start_game()
    else:
        print_pause("\n🎉 Thanks for playing! See you next time!")

# The game starts here
ready = input("ARE YOU READY TO START YOUR ADVENTURE? (Yes/No): ")
while ready not in ["Yes", "No"]:
    print_pause("\n⚠️ Please type Yes or No.")
    ready = input("ARE YOU READY TO START YOUR ADVENTURE? (Yes/No): ")

if ready == "Yes":
    start_game()
else:
    print_pause("\n👋 No worries! Come back when you're ready!")
