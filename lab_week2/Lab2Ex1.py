books = {"python": 50, "web": 30, "c": 20, "java": 40}

price_from = int(input("Enter price from: "))
price_to = int(input("Enter price to: "))

canbuylist = []

for k, v in books.items():
    if (v >= price_from and v <= price_to):
        canbuylist.append(k)

print("You can purchase: ", canbuylist)

books = {"python": 50, "web": 30, "c": 20, "java": 40}

price_from = int(input("Enter price from: "))
price_to = int(input("Enter price to: "))

canbuylist = []

for k, v in books.items():
    if (v >= price_from and v <= price_to):
        canbuylist.append(k)

print("You can purchase: ", canbuylist)

