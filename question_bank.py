#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?"),
        ("What is the nearest star to Earth?"),
        ("What is the powerhouse of the cell?"),
        ("What is the atomic number of oxygen?"),
        ("What is the process by which plants make their food?"),
        ("What is the smallest bone in the human body?"),
        ("What is the study of fossils called?"),
        ("What is the speed of light in a vacuum?"),
        ("What is the force that causes objects to fall to the ground?"),
        ("What is the main function of the lungs?"),
        # Add more questions as tuples (question, answer)
    ],
    "Physics": [
        ("What is the SI unit of force?"),
        ("What is the formula for calculating kinetic energy?"),
        ("What is the acceleration due to gravity on Earth?"),
        ("What is the law that states that for every action, there is an equal and opposite reaction?"),
        ("What is the SI unit of electric charge?"),
        ("What is the force that opposes the motion of objects through air called?"),
        ("What is the formula for calculating work?"),
        ("What is the SI unit of power?"),
        ("What is the SI unit of electric current?"),
        ("What is the bending of light as it passes from one medium to another?"),
    ],
}
answers = {
    "Science": [
        "H2O",
        "Sun",
        "Mitochondria",
        "8",
        "Photosynthesis",
        "Stapes",
        "Paleontology",
        "299,792,458 meters per second",
        "Gravity",
        "Gas exchange",
    ],
    "Physics": [
        "Newton",
        "0.5 * mass * velocity^2",
        "9.81 m/s^2",
        "Newton's third law",
        "Coulomb",
        "Drag",
        "Force * Distance",
        "Watt",
        "Ampere",
        "Refraction",
    ],
}

hints = {
    "Science": [
        "Think about the chemical composition of water.",
        "It's the star at the center of our solar system.",
        "This organelle produces energy in cells.",
        "Check the periodic table.",
        "Plants use sunlight to produce it.",
        "It's located in the ear.",
        "It involves the study of ancient life forms.",
        "It's a constant in physics.",
        "It's what makes things fall downwards.",
        "It involves inhaling oxygen and exhaling carbon dioxide.",
    ],
    "Physics": [
        "Named after a famous scientist.",
        "Think about mass and velocity.",
        "Think about the acceleration experienced by objects in free fall.",
        "It describes the interaction between two objects.",
        "Named after a physicist.",
        "Occurs when objects move through a medium like air or water.",
        "It's calculated by multiplying force and distance.",
        "Named after the unit of power.",
        "It measures the flow of electric charge.",
        "It occurs when light changes speed as it moves from one medium to another.",
    ],
    # Repeat for other categories as needed.
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    # Add your code here
    #------------------------
    if category in questions:
        index = random.randint(0, len(questions[category]) - 1)
        question = questions[category][index]
        answer = answers[category][index]
        hint = hints[category][index] if category in hints else "No hint available"
        return question, answer, hint
    else:
        return "Category not found", None, None

category = "Science"
question, answer, hint = select_random_question(category)
print("Question:", question)
print("Hint:", hint)
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    # Add your code here
    #------------------------
    if player_answer == correct_answer:
        return True

    else:
        return False
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    if category in questions:
        if question in questions[category]:
            questions[category].remove(question)
            index = questions[category].index(question)
            del answers[category][index]
            del hints[category][index]
        else:
            print("Question not found in the category.")
    else:
        print("Category not found.")
    #------------------------
    
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    # Add your code here
    #------------------------
    print(question)
    return input("Your answer: ")
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    # Add your code here
    #------------------------
    if category in hints:
        if question in questions[category]:
            index = questions[category].index(question)
            return hints[category][index]
        else:
            return "Question not found in the category."
    else:
        return "Category not found."
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    if player_answer.lower() == correct_answer.lower():
        print("True")
    else:
        print("False")
        print("The correct answer is:", correct_answer)
    #------------------------

#---------------------------------------




