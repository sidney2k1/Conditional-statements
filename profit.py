actualcost=int(input("enter the cost of the item:"))
sellingcost=int(input("enter the selling price of the item:"))
if(sellingcost>actualcost):
    amount=sellingcost-actualcost
    print("total profit={0}".format(amount))
else:
    print("No profit")