import random


def pwd_gen():
    # password will be randomized
    # it will be of variable length (at least 10, at most 18)
    ln = random.randint(10, 18)
    psswrd = "*" * ln
    print("Generating password: %s" % psswrd)

    for ch in psswrd:
        # use ascii values compatible with a standard U.S. keyboard
        num = random.randint(33, 126)
        pwdchr = chr(num)
        psswrd = psswrd[1:] + pwdchr
    return psswrd


def main():
    new_pwd = pwd_gen()
    print("Your newly generated password is: " + new_pwd)


if __name__ == "__main__":
    main()