from cs50 import get_float

conies=get_float("Change owed:")

while conies < 0:

    coines = get_float("Change owed:")
count = 0

conies = round(conies*100)


while conies != 0:
    if conies // 25 != 0:
       conies =conies-25
       count=count+1
    elif conies // 10 != 0:
       conies =conies-10
       count=count+1

    elif conies // 5 != 0:
       conies =conies-5
       count=count+1
    else:
        conies =conies-1
        count=count+1
print(count)



















# elif conies / 10 !=0:
    #      conies =conies-10
    #      count+1
    # elif conies / 5 !=0:
    #      conies =conies-5
    #      count+1
    # elif conies / 1 !=0:
    #      conies =conies-1
    #      count+1