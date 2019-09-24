import string
import random


def generate_string(str_length):
    """Generate random string of given length"""
    letters = string.ascii_uppercase + ' '
    return ''.join(random.choice(letters) for i in range(str_length))


def copy_string(s, copies=100):
    """Make 100 copies of input string in a list"""
    copied_strings = []
    for i in range(copies):
        copied_strings.append(s)
    return copied_strings


def mutate_string(s):
    """Replace a given character in a string with 5% probability"""
    new_s = ''
    letters = string.ascii_uppercase + ' '
    s = list(s)
    for i in range(len(s)):
        if roll_dice():
            new_s = new_s + random.choice(letters)
        else:
            new_s = new_s + s[i]
    return new_s


def roll_dice():
    """Dice returns bool True with 5% probability"""
    result = random.randint(1, 101)
    if result <= 5:
        return True
    else:
        return False


def compare(s, target_string="METHINKS IT IS LIKE A WEASEL"):
    """Compare a given string to the target string"""
    score = 0
    for i in range(len(s)):
        if s[i] == target_string[i]:
            score += 1
    return score


def find_best_candidate(s_array):
    """Finds highest scoring string in a mutated array"""
    best_string = ''
    max_val = 0
    for s in s_array:
        score = compare(s)
        if score > max_val:
            max_val = score
            best_string = s
    return best_string


def dawkins_algorithm(strlen=28):
    """Runs the dawkins algorithm until perfect score is attained"""
    copies = copy_string(generate_string(strlen))
    new_score = 0

    while new_score < 28:
        for index, s in enumerate(copies):
            current_score = compare(s)
            mutated_string = mutate_string(s)
            new_score = compare(mutated_string)
            if new_score > current_score:
                copies[index] = mutated_string
                print(mutated_string)

                if new_score == strlen:
                    break

        copies = copy_string(find_best_candidate(copies))

    return print("Done")


dawkins_algorithm()