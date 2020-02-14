from cs50 import get_string
from sys import argv


def main():

    if len(argv) !=2:
        print("Usage: python bleep.py dictionary")
        sys.exit(1)


    else:
        massege=get_string("What message would you like to censor?\n")

        m=[i for j in massege.split() for i in (j, ' ')][:-1]

        # print(m)
        word=[]
        wok=[]
        f = open(argv[1],"r")

        for i in f :
            i=i.rstrip('\n')
            word.append(i)
            i.upper()
            wok.append(i.upper())

        # for i in

        word=word+wok
        # print(word)

        d=""
        for i in m:
            for j in word:
                if(i==j):
                    for x in range(len(i)):
                        d+= "*"
                    d+=" "

            d+=i
        # ///////////////////////////////////////////////////print(d)

        b=[i for j in d.split() for i in (j, ' ')][:-1]
        # ///////////////////////////////////////////////////print(b)

        for i in b:
            for j in word:
                if i==j:
                    b.remove(i)

        # print(b)


        for i in b:
            if i ==' ':
                b.remove(i)

        # ////////////////////////////////////////////////////////print (b)

        # print(b)
        for i in b[:len(b)]:
            if b.index(i)==(len(b)-1):
                print(i,end="")
            elif i==" ":
                continue
            else:
                print(i,end=" ")

        #/////////////// for i in b[len(b)-1:]:
        #///////////////     print(i,end="")

    print()

if __name__ == "__main__":
    main()
