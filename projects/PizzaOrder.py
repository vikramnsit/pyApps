print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L:")
pepperoni = input("Do you want pepperoni on your Pizza?: Y or N: ")
extra_cheese = input("Do you want extra cheese on your Pizza?: Y or N: ")

if size == 'S':
    price = 15
    if pepperoni == 'Y':
        price = price + 2
        if extra_cheese == 'Y':
            price = price + 1
elif size == 'M':
    price = 20
    if pepperoni == 'Y':
        price = price + 3
        if extra_cheese == 'Y':
            price = price + 1
elif size == 'L':
    price = 25
    if pepperoni == 'Y':
        price = price + 3
        if extra_cheese == 'Y':
            price = price + 1
else:
    print("Incorrect entries: Please enter S, M or L")

print(f'Total bill:{price}')


