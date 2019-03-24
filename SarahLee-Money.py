print("Hello, this is a money calculator that calculates how much your money will increase in how many years if an interest percentage is some amount.") 

def CalcCurrYearMoney(money,percentage):
    i=percentage/100
    i = i+1
    money = money*i
    return money 

def main():
    x = int(input("please insert initial money in digit(s) (ex:1000)"))
    y = int(input("please insert interest percentage in digit(s) (ex:2)"))
    z = int(input("please insert the number of years that will pass (ex:5)"))

    j = z
    i = x

    while z>0:
        x=CalcCurrYearMoney(x,y)
        z = z-1
        return print("after", j, "years, your money",i, "will increase to", x)

print(main())
        
