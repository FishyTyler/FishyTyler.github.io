# Defines a list of values that can be called for 
# Start of Trivia Game

game_mode = ["Aniversary", "Things"]

# Defines function of users choice
# users_choice = str(input("What Trivia Category would you like to play"))

# Defines function of questions
"""def questions():
    done = ["Fishing", "Kiting", "Cooking", "Kimchi"]
    print (f"Which of these have we done?:{done}")
    answer = input()
    if answer == "Fishing":
        print ("You know us so well!")
    else: 
        print ("U GOT IT WRONG?!?!!?") """

# Making a dictionary with questions and answers
# for things trivia
things = [
    {
        "questions" : "What is the first we done together?",
        "potential_answers" : ["Fishing", "Boba", "Kissing", "Dancing"],
        "correct_answer" : "Dancing"
    },
    {
        "questions" : "When is out dadjadajdad",
        "potential_answers" : ["Fisdadadadahing", "Boadadaba", "Kiadadassing", "Danadadadcing"],
        "correct_answer" : "Dadadadncing"
    }
]
#New function for things trivia
def print_questions():
    print (things[0])
    for i in things:
        print ("Question:", i[things])
        print ("Answers are:", i[things])




# Defines a loop so that game can be player over and over
while True:
    print (game_mode)
    users_choice = str(input("What Trivia Category would you like to play: "))

    if users_choice == "Things":
        print_questions()
    else:
        print ("f")
        exit