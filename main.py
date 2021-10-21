import random

def manage_type():
    print("What kind of a password do you want?")
    print("Select only one option from below: ")
    print('''    1)Strong, easy to say. No characters and no numbers
    2)Strong, all characters involved but no numbers
    3)Strong, with all characters and numbers
    4)Strong, easy to say but characters involved''')
    option = int(input('Enter an option: '))
    if option in list(range(1, 5)):
        return option
    else:
        return manage_type()


def get_length():
    min_length = int(input('Minimum length you want your password to be: '))
    while min_length > 50:
        print("Minimum length cannot be greater than 50!!")
        min_length = int(input('Minimum length you want your password to be: '))
    return min_length


def generate_password(type, s, special, numbers, letters, uppercase):
    length = random.randrange(s, int(1.8 * s))
    password = ''
    if type == 1:
        for _ in range(length):
            password += random.choice([random.choice(list(letters)), random.choice(list(uppercase))])
    elif type == 2:
        for _ in range(length):
            password += random.choice(
                [random.choice(list(letters)), random.choice(list(uppercase)), random.choice(list(special))])
    elif type == 3:
        for _ in range(length):
            password += random.choice(
                [random.choice(list(letters)), random.choice(list(uppercase)), random.choice(list(special)),
                 random.choice(list(numbers))])
    elif type == 4:
        num_chars = length // 5
        special = set(special).difference(set('!%^()~'))
        special = ''.join(special)
        for _ in range(length):
            if random.random() > 0.5 and num_chars:
                password += random.choice(list(special))
                num_chars -= 1
            else:
                password += random.choice([random.choice(list(letters)), random.choice(list(uppercase))])

    return password 


def check_inconvenience(passwd, selected_choice, asked_length, chars, num_lst, alphas, upper_alpha):
    problem = int(input('''How do you want to change your password
    1)I don't want some special characters in it
    2)Greater number of digits required in it
    3)Nothing needs to be changed\n'''))
    if problem == 1 and selected_choice != 1:
        lst = []
        for val in input('Enter the characters with spacing: '):
            if val != '':
                lst.append(val)
        present = 0
        for val in lst:
            if val in passwd:
                present = 1
                break
        if present == 0:
            print('Characters that you have entered are not present in the password')
            return passwd
        lst = set(lst)
        characters = set(chars)
        chars = characters.difference(lst)
        return generate_password(choice, asked_length, chars, num_lst, alphas, upper_alpha)
    elif problem == 1 and selected_choice == 1:
        print('You have selected an option that does not embed any special characters')
        return passwd
    elif problem == 2:
        digit_req = int(input("Number of digits you want: "))
        for i in range(len(passwd)):
            if passwd[i].isalpha() and random.randint(0, 1) and digit_req:
                passwd = passwd[:i] + random.choice(num_lst) + passwd[i + 1:]
                digit_req -= 1
        return passwd
    elif problem == 3:
        return passwd


def get_input():
    value = int(input('''Do you want to get another?
                    1)Another
                    2)Exit\n'''))
    if value == 1 or value == 2:
        return value
    else:
        print("Enter an option from the given")
        return get_input()


while True:
    chars = '!@_#$%^&*()~|'
    nums = '0123456789'
    alphabets = 'abcdefghijklmopqrstuvwxyz'
    upperalpha = alphabets.upper()
    choice = manage_type()
    min_len = get_length()
    password = generate_password(choice, min_len, chars, nums, alphabets, upperalpha)
    print('Your password:', password)
    inconvenience = int(input('Do you have any inconvenience with password:\n\t1)Yes\n\t2)No\n'))
    if inconvenience == 1:
        new_password = check_inconvenience(password, choice, min_len, chars, nums, alphabets, upperalpha)
        print('Your new password:', new_password)
    s = get_input()
    if s == 2:
        print('Thank you for using our password generator!! Hope you are satisfied!')
        break
