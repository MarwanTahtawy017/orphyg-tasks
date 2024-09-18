SlabShapes = ["Square", "Rectangular", "Round"]

Amount = int(input("Enter the amount of slabs you want: "))
while Amount < 20 or Amount > 100:
    Amount = int(input("The amount must be between 20 and 100 inclusive: "))

Remainder = Amount % 20
Number = 40
while Remainder != 0 and Amount != Number:
    if Number < Amount:
        Number += 20
    else:
        print("Amount rounded up to:", Number)
        Amount = Number

Colour = input("Enter the colour of slab: ")

Depth = int(input("Enter the depth of the slab, 38 or 45: "))
while Depth != 38 and Depth != 45:
    Depth = int(input("Please input either 38 or 45: "))

Shape = input("Enter the shape of the slab: ")
while Shape not in SlabShapes:
    Shape = input("The shape must be either a square, rectangle, or round: ")

if Shape == "Round":
    Diametre = int(input("Enter the diametre, 300 or 450:"))
    while Diametre != 300 and Diametre != 450:
        Diametre = int(input("Please enter either 300 or 450: "))

    Radius = Diametre/2
    Volume = 3.14 * Radius**2 * Depth

elif Shape == "Square":
    Dimension = int(input("Enter a the length of the dimensions, 600 or 450: "))
    while Dimension != 600 and Dimension != 450:
        Dimension = int(input("Please enter either 600 or 450: "))

    Volume = Dimension**2 * Depth

else:
    Length = int(input("Enter the length, 700 or 450:"))
    while Length != 700 and Length != 450:
        Length = int(input("Please enter either 700 or 450: "))

    Volume = Length * 600 * Depth

Price = (Volume * 0.05)/100000
if Colour != "Grey":
    if Colour == "Red" or Colour == "Green":
        Price = Price * 1.1
    else:
        Price = (Price * 1.15) + 5

print("Slab Details- Colour:", Colour, "Depth:", Depth, "Shape:", Shape, "Price of one slab in $:", int(Price))
print("Price of batch of", Amount, "slabs in $:", int(Price * Amount))
