from cs50 import SQL
db = SQL("sqlite:///finance.db")
b=db.execute("select symbol , sum(shares)  as sara from buied where userid=:userid group by symbol having shares >=1",userid=6)

for n in b:

    print (n)
