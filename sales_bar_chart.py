#Matthew Cires
#CMP 131
#Week 8
#Lab 1
#Sale bar chart
print("-----------------------------------")
print("Sales Bar Chart for Five Stores")
print("-----------------------------------")

Ast = ""

for i in range(1, 6):

    sales = float(input("Enter today's sales for Store " + str(i) + ": "))

    while sales < 0:
        print("Error: Sales cannot be negative.")
        sales = float(input("Please retype the sales amount: "))

    stars = int(sales / 100)

    Ast = Ast + "Store " + str(i) + ": "

    for j in range(stars):
        Ast = Ast + "*"

    Ast = Ast + "\n"

print("-----------------------------------")
print("SALES BAR CHART")
print("Each * represents $100")
print("-----------------------------------")
print(Ast)