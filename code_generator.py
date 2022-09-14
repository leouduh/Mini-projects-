import random
import string


key_length = 0
new_list_of_characters = ""
random_character = ""
y = True


def split_ascii_chars():
    global new_list_of_characters
    new_list_of_characters = string.ascii_letters + string.digits + string.punctuation
    return new_list_of_characters


def receive_password_length():
    global key_length
    try:
        key_length = int(input("Please enter length of code: "))
    except Exception:
        print("Please make a valid entry ")
        receive_password_length()
    else:
        return key_length


# receive_password_length()
def generate_key(key_len, charc_options):
    global random_character
    random_character = ""
    for i in range(1, key_len + 1):
        random_character += random.choice(charc_options)
    return random_character


def exit_pane():
    exit_prompt = input("would you like to quit? (y)es or (n)o").casefold()
    if exit_prompt not in ["y", "n"]:
        print("enter 'y' to continue 'n' to terminate")
        exit_pane()
    elif exit_prompt == 'y':
        return False
    elif exit_prompt == 'n':
        return True


while y is True:
    receive_password_length()
    split_ascii_chars()
    generate_key(key_length, new_list_of_characters)
    print("your generated code is ", random_character)
    y = exit_pane()
    if y is True or y is False:
        continue
else:
    print("Thanks for running this program")




