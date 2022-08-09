import random
import string
import pyperclip

# --------- CONSTANTS ------------
chars = []
letters_lower = list(string.ascii_lowercase)
letters_upper = list(string.ascii_uppercase)
letters = list(string.ascii_letters)
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special = ["!", "'", '"', "#", "$", "%", "&", "*", "(", ")", "-", "_", "=", "+", "?", "[", "]", "^", "@"]

# ----------------- SETS ------------------------------------------------------------------
nums_set = set(nums)
lett_lower_set = set(letters_lower)
lett_upper_set = set(letters_upper)
special_set = set(special)

# --------------- FULL LIST CHARACTERS ----------------------------------------------------

chars_dict = {"nums": nums, "letters": letters, "special": special}

for key in chars_dict:
    for i in range(len(chars_dict[key])):
        chars.append(chars_dict[key][i])

# -------------- PASSWORD GENERATOR CLASS -------------------------------------------------


class PassGen:

    def __init__(self, size=8):
        self.chars = chars
        self.password = ""
        self.pass_gen(size)

    def pass_gen(self, size=8):

        flag = True
        while flag:
            pass_list = []
            for item in range(size):
                pass_list.append(random.choice(self.chars))
            password = "".join(pass_list)
            pass_set = set(password)

            if len(pass_set & nums_set) == 0:
                pass
            elif len(pass_set & special_set) == 0:
                pass
            elif len(pass_set & lett_upper_set) == 0:
                pass
            elif len(pass_set & lett_lower_set) == 0:
                pass
            else:
                flag = False
                self.password = password
                pyperclip.copy(password)

