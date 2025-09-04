name = "Ana M"
age = 20
height = 5.7
favorite_color = "Blue"

# part 1 Q 1
print(name)
print(age)
print(height)
print(favorite_color)
# part Q 2
print(name, age, height, favorite_color)
# part 1 Q 2 S 2 : Yes, it adds a space

# part 1 @ 3
print(f"Hello: {name} my favorite color {favorite_color} is {age} years old.")
print(f"My name is: {name} my favorite color {favorite_color} my age is {age} years old {height: .1f} my height is")
print(f"My name is: {name} my favorite color {favorite_color} my age is {age} years old {height:^10.1f} my height is")

# part 1 Q 2 P4
my_multi_line_str_ = f"""
my name is {name}
my age is {age:d}
my height is {height:.1f}
my favorite color is {favorite_color}!
"""
print(my_multi_line_str_)

# part 1 Q 3 P1
radius = 5

from math import pi

area_circle = pi* radius**2
print(round(area_circle, 1))
print(f"{area_circle:.1f}")
# part 2 Q 1 & 2
from math import sqrt
print(f"{sqrt(area_circle):.2f}")


# part 2 Q 3
from math import sin, cos

print(sin(height))
print(cos(height))

# The sum of age and 5.
print(age +5)
# The difference between height and 4.
print(f"{height - 4:.1f}")
# The product of age and height.
print(age*height)
# The quotient of height and 2.
print(height/2)
# The remainder of age divided by 3.
print(age%3)
# age raised to the power of 2.
print(age**2)


# part 4 Q 1
f_deg = float(input("Please enter degrees in Fahrenheit: "))
#  print(f_deg, type(f_deg))
celsius = (f_deg  - 32) * 0.55555555555556
print(f"{f_deg:.2f}F in celsius is: {celsius:.2f}°C")
