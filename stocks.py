stockDict = {
    "GE": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak"
}

purchases = [
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 56 )
]

# for item in purchases:
#     print(item[0], item[1], item[2])

# for stock, name in stockDict.items():
#     print(stock, name)

for purchase in purchases:
    
    print(f"I purchased {stockDict[purchase[0]]} stock for ${purchase[1] * purchase[3]}.")
