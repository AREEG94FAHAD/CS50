import sys
from cs50 import get_string


def a():


    if len(sys.argv)!=2:
        print("Usage: python caesar.py")
        sys.exit(1)


    else:


        k = int(sys.argv[1])%26
        massege=get_string("plaintext:")
        print("ciphertext:",end="")
        for s in massege:

            if s>='a' and s<='z':
                n=ord(s)
                w=n+k
                if w>122:
                    s=chr(n-(26-k))
                else:
                    s=chr(n+k)
                print(s,end="")

            elif s>='A' and s<='Z':
                n=ord(s)
                w=n+k
                if w>90:
                    s=chr(n-(26-k))
                else:
                    s=chr(n+k)
                print(s,end="")
            else:
                print(s,end="")

        print()


a()



