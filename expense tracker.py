import csv
import os
expenses = []
with open("expenses.csv", "a",newline="") as file:
    writer = csv.writer(file)

    if os.path.getsize("expenses.csv") == 0:
        writer.writerow(["date", "expense", "amount"])
#for loop
    while True:
        date = input("what is the date: ")
        if date == "done": break
        expense = input("what did you spend your money on?: ")
        amount = float(input("how much did it cost?: "))
        expense = {"date": date, "expense": expense, "amount": amount}
        expenses.append(expense)
        writer.writerow([expense["date"], 
                         expense["expense"], 
                         expense["amount"]])
#user puts the required information
print("Expense:", expense["expense"])
print("amount:", expense["amount"])
print("Date:", expense["date"])
print("Expense saved!")




