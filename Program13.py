h_feet = int(input("Feet "))
h_inch = float(input("Inch "))
h_inch += h_feet*12
h_cm = round(h_inch*2.54, 1)
print("Height is: %d cm" %h_cm)