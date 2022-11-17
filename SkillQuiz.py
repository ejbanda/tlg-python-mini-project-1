#!/usr/bin/env python3

# tool data
skill = {"mining": 0, "woodcutting": 0, "crafting": 0, "smithing": 0, "fishing": 0, "firemaking": 0}

# questions/answers
questions = {
        "A goblin you encounter requests a item to win the affection of another. You provide:": [
            "1. A precious ore.",
            "2. Logs of a rare tree.",
            "3. A precious gem.",
            "4. A fine sword.",
            "5. A large fish.",
            "6. A tinderbox."],
        "A great dragon requests an object that could aide in his war against adventurers after his loot. You provide: ": [
            "1. Coal to ensure the strongest flames.",
            "2. A wooden barricade around his loot.",
            "3. Fake jewelry to bait the adventurers.",
            "4. Armour.",
            "5. A large quantity of fish to keep the dragons strength.",
            "6. Oil near the entrance to ensure no exit when ignited."],
        "A small chinchompa requests your service to prevent hunters from hunting their kin. You provide: ": [
            "1. Useless ore.",
            "2. Wooden spike traps.",
            "3. Decoy chinchompa made from leather.",
            "4. A dagger to strap to its head.",
            "5. Rotting fish for the smell to deter the hunters.",
            "6. A candle."],
        "An ogre asks you to give you most value item or they will eat you. You provide: ": [
            "1. Runite ore.",
            "2. Redwood logs.",
            "3. Cut onyx.",
            "4. Rune platebody",
            "5. Manta ray.",
            "6. Bullseye lantern"],
        "You are trapped in a witch's house, and there is one door for an exit. You escape by: ": [
            "1. Tearing down the door with your pickaxe.",
            "2. Tearing down the door with your axe.",
            "3. Use your sewing needle to pick the lock.",
            "4. Break the lock with your hammer.",
            "5. Fish the key out the witch's pocket with your fishing rod.",
            "6. Burn the house down."],
        "A local village is being terrorized by a monster. You aide by: ": [
            "1. Hiding in the mine.",
            "2. Offering torches.",
            "3. Offering leather armour.",
            "4. Offering pitchforks.",
            "5. Offering fish to eat.",
            "6. Offer lighting the torches"],
        "A local farmer sheep have escape. You help by: ": [
            "1. Giving iron ore for his troubles.",
            "2. Mending his fence.",
            "3. To spin the farmer's wool while the farmer gathers the sheep.",
            "4. Offers a prod for the farmer to gather the sheep.",
            "5. Giving a fish to the farmer.",
            "6. Light his fireplace."],
        "A small child by a demonic alter asks you to open a chest. You aide by:": [
            "1. Pry open the chest with your pickaxe.",
            "2. Chop open the chest with your axe.",
            "3. Pay a stranger with jewelry to open it.",
            "4. Whack the chest with your hammer.",
            "5. Whack the chest with a fish.",
            "6. Burn the chest."],
        "Your friend is bored and asks what you want to do. You suggest: ": [
            "1. Mining.",
            "2. Woodcutting.",
            "3. Crafting.",
            "4. Smithing.",
            "5. Fishing.",
            "6. Firemaking."]
        }

# method to extract questions from dictionary
def inputCheck():
    user_input = input("Your choice [1 - 6]\n>")
    
    while (user_input.isdigit() == False):
        print("Do not enter non-single digit input.")
        user_input = input("Your choice [1 - 6]\n>")

    if (int(user_input) < 1 or int(user_input) > 6):
        print("Ensure Your choice is in a valid range 1 - 6.")
        inputCheck()

    return int(user_input)

# convert and add information from question to tools
def collectInformation(selection):
    if selection == 1:
        skill["mining"] += 1
    elif selection == 2:
        skill["woodcutting"] += 1
    elif selection == 3:
        skill["crafting"] += 1
    elif selection == 4:
        skill["smithing"] += 1
    elif selection == 5:
        skill["fishing"] += 1
    else:
        skill["firemaking"] +=1

# Loop through questions
def displayAnswers(question):
    for answer in question:
        print("\t"+ answer)

# Find the max skill value
def findSkill():
    answer = max(skill, key=skill.get)
    print("Your Skill is: " + answer.capitalize())

# method for finding what skill
def main():
    print("What RuneScape Skill are you?")

    for question in questions:
        print("\n" + question)
        displayAnswers(questions[question])
        selection = inputCheck()
        collectInformation(selection)
    findSkill()

if __name__ == "__main__":
    main()
