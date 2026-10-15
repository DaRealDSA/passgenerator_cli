import random
import string
from colorama import Fore

"""

Password generator CLI

"""


# default char length to 25 if isn't entered
# default amount generated to 5 if isn't entered
def PassGenerator(char_length=25, amount_generated=5):
    result = ""
    genered_pass_list = []
    # ASCII characters
    chars = string.printable

    # Loops amount of generated passwords
    for _ in range(amount_generated):
        # Returns the result
        result = ""
        # Loops character length and adds random character to result list
        for _ in range(char_length):
            result += chars[random.randint(0, len(chars) - 1)].strip()
        # Loops finishes so the generated password is added to the genered_pass_list
        genered_pass_list.append(result)

    # Finally, returns the generated passwords to the function
    return genered_pass_list


try:

    # Prompting input from the user
    char_length = int(input("Char length: "))
    amount_generated = int(input("Amount of pass generated?: "))

    # Checks if both are valid numbers
    if char_length and amount_generated:
        pass_generate = PassGenerator(char_length, amount_generated)
        print(f"{Fore.YELLOW}DO NOT share these password with anybody.{Fore.RESET}")
        # prints the generated password list
        for index, item in enumerate(pass_generate):
            print(f"{index}. {item}")
    else:
        print(f"{Fore.RED}Failed to generated password.{Fore.RESET}")
except ValueError:
    print(f"{Fore.RED}Please enter numbers only!{Fore.RESET}")
