from string import ascii_uppercase, ascii_lowercase, digits

passwords = list(input("Enter comma separated passwords: ").split(","))
def min_length(password):
    return len(password) >= 6

def max_length(password):
    return len(password) <= 12

def has_lower(password):
    lower_count = 0
    for letter in password:
        if letter in ascii_lowercase:
            lower_count += 1

    return lower_count > 0

def has_upper(password):
    upper_count = 0
    for letter in password:
        if letter in ascii_uppercase:
            upper_count += 1
    return upper_count > 0

def has_digit(password):
    digit_count = 0
    for i in password:
        if i in digits:
            digit_count += 1

    return digit_count > 0

def has_char(password):
    char_count = 0
    char_list = ["$", "#", "@"]
    for i in password:
        if i in char_list:
            char_count += 1
    
    return char_count > 0 

def password_validate(passwords):
    good_passwords = []
    for password in passwords:
        if min_length(password) and max_length(password) and has_char(password) and has_digit(password) and has_lower(password) and has_upper(password):
            good_passwords.append(password)

    return good_passwords

for password in password_validate(passwords):
    print(password)




