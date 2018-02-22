def valid_password(p):
    if (len(p) < 6 or len(p) > 16):
        print("The password length should be in range 6-16 characters")
        return False
    
    hasDigit = False
    for ch in p:
        if ch.isdigit():
            hasDigit = True
    if (not hasDigit):
        print("The password should have at least one number")
        return False

    hasSpecial = False
    for ch in p:
        for test in "$@!*":
            if ch == test:
                hasSpecial = True
    if (not hasSpecial):
        print("The password should have at least one speical character in [$@!*]")
        return False

    hasUpper = False
    hasLower = False
    for ch in p:
        if ch.islower():
            hasLower = True
        if ch.isupper():
            hasUpper = True;
    if (not hasUpper or not hasLower):
        print("The password should have at least one lowercase and at least one uppercase letter")
        return False
    
    print("Password is valid")
    return True

valid_password(input("Enter password:" ))
