import random
import time

# Initialize score
total_score = 0

# Delay function for pacing
def print_pause(message):
    print(message)
    time.sleep(2)

# Score display
def display_score():
    print(f"🎯 Current Score: {total_score}\n")

# Increase score
def increase_score():
    global total_score
    total_score += 5

# Decrease score but not below zero
def decrease_score():
    global total_score
    loss = random.choice([1, 2])
    total_score = max(0, total_score - loss)

# Get user choice (1 or 2)
def get_choice(options):
    choice = input(f"\n{options}\nYou can choose 1 or 2: ")
    while choice not in ["1", "2"]:
        print_pause("⚠️ Please choose 1 or 2.")
        choice = input(f"\n{options}\nYou can choose 1 or 2: ")
    return choice

# Game starts here
def start_game():
    global total_score
    total_score = 0
    print_pause("🌟 Welcome to the Haunted House Adventure! 🌟")
    print_pause("You are standing in front of an old, creepy house...")
    print_pause("A long time ago, a rich family disappeared from here...")
    print_pause("It's up to you to find out what happened!")

    choice = get_choice("1 - Go through the front door 🚪\n2 - Walk around the house 🌿")
    if choice == "1":
        enter_house()
    else:
        go_around_house()

# Front door path
def enter_house():
    print_pause("👉 You enter the front door...")
    print_pause("The house is dark, and you hear strange noises from upstairs.")
    display_score()

    choice = get_choice("1 - Go upstairs 🚶‍♂️\n2 - Explore the glowing room 🔦")
    if choice == "1":
        upstairs_path()
    else:
        glow_room_path()

# Upstairs path with multiple events
def upstairs_path():
    print_pause("👻 A ghost appears and warns you to leave!")
    decrease_score()
    display_score()

    choice = get_choice("1 - Confront the ghost ⚔️\n2 - Escape through the hallway 🏃‍♂️")
    if choice == "1":
        fight_ghost()
    else:
        hallway_trap()

# Fight ghost
def fight_ghost():
    print_pause("🧠 You try to fight the ghost...")
    outcome = random.choice(["victory", "defeat"])
    if outcome == "victory":
        increase_score()
        print_pause("🎉 You defeat the ghost and find a hidden map!")
        display_score()
        map_room()
    else:
        decrease_score()
        print_pause("💀 The ghost overpowers you!")
        display_score()
        lose_game()

# Hallway trap
def hallway_trap():
    print_pause("⚠️ You fell into a trapdoor!")
    decrease_score()
    display_score()
    print_pause("You escape into a secret underground room.")
    secret_puzzle()

# Glowing room path
def glow_room_path():
    print_pause("📖 You find a glowing book on a pedestal.")
    choice = get_choice("1 - Read the book 📚\n2 - Ignore it and check the drawer 🔍")
    if choice == "1":
        increase_score()
        print_pause("✨ The book gives you magical clues and a key!")
        display_score()
        secret_puzzle()
    else:
        print_pause("🚪 The drawer has a riddle.")
        riddle_challenge()

# Go around the house
def go_around_house():
    print_pause("🌲 You walk into the garden...")
    display_score()

    outcome = random.choice(["treasure", "trap"])
    if outcome == "treasure":
        increase_score()
        print_pause("🌼 You found a chest hidden in the flowers!")
        display_score()
        secret_puzzle()
    else:
        decrease_score()
        print_pause("😱 A snake bites you! You run back inside.")
        display_score()
        enter_house()

# Secret puzzle to advance
def secret_puzzle():
    print_pause("🧩 You must solve a puzzle to unlock the final room.")
    choice = get_choice("1 - Try to solve it 🧠\n2 - Look for a hint 🔎")
    if choice == "1":
        increase_score()
        print_pause("✅ You solve it and unlock the treasure chamber!")
        display_score()
        win_game()
    else:
        decrease_score()
        print_pause("❌ The hint leads nowhere. You lose time and energy.")
        display_score()
        lose_game()

# Map room leads to treasure
def map_room():
    print_pause("🗺️ The map leads to a hidden room behind a bookshelf.")
    increase_score()
    display_score()
    print_pause("You unlock it and find the ancient treasure!")
    win_game()

# Riddle challenge
def riddle_challenge():
    print_pause("🤔 What has keys but can't open locks?")
    answer = input("Your answer: ").lower()
    if "piano" in answer:
        increase_score()
        print_pause("🎵 Correct! A hidden passage opens.")
        display_score()
        secret_puzzle()
    else:
        decrease_score()
        print_pause("❌ Wrong! The drawer locks again.")
        display_score()
        lose_game()

# Game won
def win_game():
    print_pause("🏆 You found the treasure! Congratulations!")
    print(f"🎯 Final Score: {total_score}")
    play_again()

# Game lost
def lose_game():
    print_pause("💀 You got trapped in the haunted house!")
    print(f"🎯 Final Score: {total_score}")
    play_again()

# Restart option
def play_again():
    choice = get_choice("1 - Play again 🔁\n2 - Exit ❌")
    if choice == "1":
        start_game()
    else:
        print_pause("🎉 Thanks for playing! See you next time!")

# Game entry point
ready = input("ARE YOU READY TO START YOUR ADVENTURE? (Yes/No): ")
while ready.lower() not in ["yes", "no"]:
    print_pause("⚠️ Please type Yes or No.")
    ready = input("ARE YOU READY TO START YOUR ADVENTURE? (Yes/No): ")

if ready.lower() == "yes":
    start_game()
else:
    print_pause("👋 No worries! Come back when you're ready!")
