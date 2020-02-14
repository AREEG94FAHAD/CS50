from cs50 import get_int

    # for second number
mod=0
    # for second value
div=0
    # for first number and so on
mod2=0
    # for the third
c=0
    # for the for
dii=0
    # for the five
ok=0
    # for the last
n=get_int("Number:")



if (349999999999999//n)>=1 and (n//340000000000000)>=1 or (379999999999999//n)>=1 and (n//370000000000000)>=1:
    while n!=0:

        mod+=n%10
        # # print(mod)
        n=n//10
        print(n)
        c=n%10
        # print(n)
        if c>4:
             c=c*2
             dii=c%10
             c=c//10
             mod2=mod2+dii+c
             n=n//10
             print(mod2,"okkkk")

        else:

            mod2=mod2+(n%10)*2
            n=n//10
            # mod2=mod2*2
    modtotal=mod+(mod2)

    if modtotal%10==0:
        print("AMEX\n")
    else:
       print("INVALID\n")

elif 5599999999999999//n>=1 and n//5100000000000000>=1:
    while n!=0:
        mod+=n%10
        n=n//10
        c=n%10
        if c>4:
            # printf("%iln",c);
              c=c*2
# //                  printf("%iln",c);
              dii=c%10
# //                  printf("%iln",dii);
              c=c//10
              mod2+=dii+c
# //                  printf("%iln",mod2);
              n=n//10


        else:
            mod2+=(n%10)*2
            n=n//10






    modtotal=mod+(mod2)
        # ceck if the sum equal 0
    if modtotal%10==0:

        print("MASTERCARD\n")

    else:


        #   {
        print("INVALID\n")
        #   }


elif (4999999999999999/n)>=1and (n/4000000000000000)>=1or(4999999999999/n)>=1and(n/4000000000000)>=1:

    while(n!=0):
        mod+=n%10
        n=n//10

        c=n%10
        if(c>4):
            # printf("%iln",c);
            c=c*2
# //                  printf("%iln",c);
            dii=c%10
# //                  printf("%iln",dii);
            c=c//10
            mod2+=dii+c
# //                  printf("%iln",mod2);
            n=n//10

            # }
        else:


            mod2+=(n%10)*2
            n=n//10

            mod+=n%10
            n=n//10

            c=n%10
            if(c>4):


# //                 printf("%iln",c);
               c=c*2
# //                  printf("%iln",c);
               dii=c%10
# //                  printf("%iln",dii);
               c=c//10
               mod2+=dii+c
# //                  printf("%iln",mod2);
               n=n//10


            else:
                mod2+=(n%10)*2
                n=n//10




    modtotal=mod+(mod2)+ok


    if((modtotal%10==0)):
        print("VISA\n")

    else:
        print("INVALID\n")

else:


        print("INVALID\n")









