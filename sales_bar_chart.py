#Matthew Cires
#CMP 131
#Week 8
#Lab 1
#Sales bar chart
#10/28/26

print("-----------------------------------")
print("Sales Bar Chart for Five Stores")
print("-----------------------------------")

store_1 = float(input("Please type the sales for your first store: "))
while(store_1 < 0):
    store_1 = float(input("Error please retype a different value: "))

store_2 = float(input("Please type the sales for your second store: "))
while(store_2 < 0):
    store_2 = float(input("Error please retype a different value: "))

store_3 = float(input("Please type the sales for your third store: "))
while(store_3 < 0):
    store_3 = float(input("Error please retype a different value: "))

store_4 = float(input("Please type the sales for your fourth store: "))
while(store_4 < 0):
    store_4 = float(input("Error please retype a different value: "))

store_5 = float(input("Please type the sales for your fifth store: "))
while(store_5 < 0):
    store_5 = float(input("Error please retype a different value: "))

# Calculate the number of stars
stars_1 = int(store_1 / 100)
stars_2 = int(store_2 / 100)
stars_3 = int(store_3 / 100)
stars_4 = int(store_4 / 100)
stars_5 = int(store_5 / 100)

# Display the sales chart
print("-----------------------------------")
print("SALES BAR CHART")
print("Each * represents $100")
print("-----------------------------------")

