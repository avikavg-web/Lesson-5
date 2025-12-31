boughtcost = int(input("What was the cost of the object when you bought it?"))
sellcost = int(input("What was the cost of the object when you sold it?"))

profitandloss = sellcost - boughtcost


if boughtcost > sellcost:
    print("You had a loss of", profitandloss)


if sellcost > boughtcost:
    print("You had a profit of", profitandloss)