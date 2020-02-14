import crypt
import sys
from cs50 import get_string

def a():



    if len(sys.argv)!=2:
        print("Usage: ./crack hash\n")
        sys.exit(1)
    hashcode = sys.argv[1];
    salt = hashcode[0:2]
    letters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for f in letters:
        for fo in letters:
            for t in letters:
                for tw in letters:
                    for o in letters:
                        candidate = f"{f}{fo}{t}{tw}{o}".strip()

                        if crypt.crypt(candidate, salt) == hashcode:
                            print(candidate)
                            sys.exit(0)
a()





















