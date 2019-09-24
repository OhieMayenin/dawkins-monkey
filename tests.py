import dawkins_monkey as dm
s = dm.generate_string(28)


def test_generate_string_length():
    assert len(s) == 28


def test_generate_string_ascii():
    assert all(ord(c) < 128 for c in s)


def test_copy_string():
    assert len(dm.copy_string(s)) == 100


def test_compare():
    test_string = "ACBDE"
    assert dm.compare(test_string, "ABCDE") == 3


def is_ascii():
    return all(ord(c) < 128 for c in s)


    # def generate_string(str_length):
    #     """Generate random 28 char length string"""
    #     letters = string.ascii_uppercase
    #     return ''.join(random.choice(letters) for i in range(str_length))
    #
    # def copy_string(s, copies=100):
    #     """Make 100 copies of input string in a list"""
    #     copied_strings = []
    #     for i in range(copies):
    #         copied_strings.append(s)
    #     return copied_strings
    #
    # def mutate_string(s):
    #     """Replace a given character in a string with 5% probability"""
    #     for i in range(len(s)):
    #         if roll_dice():
    #             s[i] = random.choice(string.ascii_uppercase)
    #     return s
    #
    # def roll_dice():
    #     """Dice returns bool True with 5% probability"""
    #     result = random.randint(1, 101)
    #     if result <= 5:
    #         return True
    #     else:
    #         return False
    #
    # def compare(s, target_string="METHINKSITISLIKEAWEASEL"):
    #     """Compare a given string to the target string"""
    #     score = 0
    #     for i in range(len(target_string)):
    #         if s[i] == target_string[i]:
    #             score += 1
    #     return score
