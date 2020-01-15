stockDict = {
    "GE": "General Motors",
    "CAT": "Caterpillar",
    "EK": "Eastman Kodak"
}

purchases = [
    ('GE', 100, '10-sep-2001', 48),
    ('CAT', 100, '1-apr-1999', 24),
    ('GE', 200, '1-jul-1998', 56)
]

# for item in purchases:
#     print(item[0], item[1], item[2])

# for stock, name in stockDict.items():
#     print(stock, name)

# for purchase in purchases:

#     print(f"I purchased {stockDict[purchase[0]]} stock for ${purchase[1] * purchase[3]}.")


report = {}

for purchase in purchases:
 
    stock_symbol = purchase[0] 

    if purchase[0] in report:
        report[stock_symbol].append(purchase)

    else:
        report[stock_symbol] = [purchase]

for report_section in report.items():

    total = 0

    print(f"------ {report_section[0]} ------")
    for report_entry in report_section[1]:
        #Set variables for indexes of tup
        num_shares = report_entry[1]
        purchase_price = report_entry[3]
        purchase_date = report_entry[2]

        print(f"{num_shares} shares at {purchase_price} dollars on {purchase_date}")
        total += num_shares * purchase_price
    print()
    print(f"Total value of stock in portfolio: ${total}.")
    print()