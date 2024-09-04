"""This code is for a quiz for the MAGS year 11 students."""

# Import
import time

# Variables
german_questions = {"I drank water today.": "Ich habe heute Wasser getrunken.",
                    "He cleans and vacuums.": "Er putzt und saugt.",
                    "at my parents": "bei meinen Eltern",
                    "he became": "er wurde",
                    "they were": "sie waren",
                    "with my friends": "mit meinen Freunden",
                    "behind the house": "hinter dem Haus",
                    "in front of the class": "vor der Klasse",
                    "We did it.": "Wir haben das gemacht.",
                    "He went to the town hall.": "Er bin zum Rathaus gegangen.",
                    "I heard.": "Ich gehört.",
                    "Have you seen that?": "Hast du das gesehen?",
                    "Let's get out of here!": "Nichts wie raus hier!",
                    "I play football, when the weather is good.": "Ich spiele Fußball, wenn das Wetter gut ist.",
                    "It was also very hot.": "Es war auch sehr heiß.",
                    "What do you do in the summer holidays?": "Was machst du in den Sommerferien?",
                    "What happened then?": "Was ist dann passiert?",
                    "Yes, because I was all alone.": "Ja, weil ich ganz alleine war.",
                    "Oh yeah, a bit.": "Na ja, ein bisschen."
                    }
replay = "y"
replay_yes = ["y", "yes", "yep", "yea", "ye", "yeah"]
current_question = 0
questions_wanted = 0
question_completed = 1
score = 0
point = 1
german_to_english = 1
english_to_german = 2
valid_choices = [english_to_german, german_to_english]
waiting = 1.5
sub_subject = 0

# Code
# Welcoming user
print("\nHello and welcome to this German quiz.")
time.sleep(waiting)
print("In this program you can take a quiz with randomized questions")
time.sleep(waiting)
print("It will even mark you as you go and show you your score at the end.")
time.sleep(waiting)

# Subject choosing + Value error
while replay in replay_yes:
    score = 0
    print("\nNow you will choose which type of questions you wish to take a quiz on.")
    while True:
        try:
            sub_subject = int(input("1. German into English    2. English into German     : "))
        except ValueError:
            print("Please enter a valid integer.\n")
        else:
            if sub_subject in valid_choices:
                print("\n")
                break
            else:
                print("Please enter a valid number.\n")

    while True:
        try:
            questions_wanted = int(input(f"How many questions do you want to complete? (1 - {len(german_questions)}): "))
        except ValueError:
            print("Please enter a valid integer.\n")
        else:
            if 1 <= questions_wanted <= len(german_questions):
                print("\n")
                break
            else:
                print("Please enter a valid number.\n")

    # German into English questions and checking answers
    if sub_subject == german_to_english:
        print("Please translate the German into comprehensive English.")
        print("Don't forget your grammar for full sentences!")
        for answer, question in german_questions.items():
            if questions_wanted == current_question:
                break
            time.sleep(waiting)
            user_answer = input(f"{question} : ")
            time.sleep(waiting)
            if user_answer == answer:
                print("You got it right! Congratulations!\n")
                score += point
            else:
                print(f"You got it wrong! The correct answer is '{answer}'.\n")
            current_question += question_completed

    # English into German questions and checking answers
    if sub_subject == english_to_german:
        print("Please translate the English into comprehensive German.")
        print("Don't forget your grammar for full sentences!")
        print("Here are some German characters to copy if needed: ß, ä, ö, and ü.")
        for question, answer in german_questions.items():
            if questions_wanted == current_question:
                break
            time.sleep(waiting)
            user_answer = input(f"{question} : ")
            time.sleep(waiting)
            if user_answer == answer:
                print("You got it right! Congratulations!\n")
                score += point
            else:
                print(f"You got it wrong! The correct answer is '{answer}'.\n")
            current_question += question_completed

    # Finishing off
    time.sleep(waiting)
    print(f"Your final score is {score} out of {questions_wanted}! Congratulations!")
    replay = (input("\nDo you want to play again?  ( Y / N )  ")).lower()
print("\nThank you for playing my German quiz!")
time.sleep(waiting)
print("I hope you have enjoyed the quiz and will play again soon!")
