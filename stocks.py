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

    if purchase[0] in report:
        report[purchase[0]].append(purchase)

    else:
        report[purchase[0]] = [purchase]

for report_section in report.items():

    total = 0

    print(f"------ {report_section[0]} ------")
    for report_entry in report_section[1]:
        # print(report_entry, "report entry")
        print(f"{report_entry[1]} shares at {report_entry[3]} dollars on {report_entry[2]}")
        total += report_entry[1] * report_entry[3]
    print()
    print(f"Total value of stock in portfolio: ${total}.")
    print()