
x = 2
y = 3

print("x =", x)

print('value of', x, '+', x, 'is', (x + x))

print('x =')

print((x + y), '=', (y + x))



print("                   ")





rating = int(input('Enter an integer rating between 1 and 10:'))

for numbers in range(1, 11):

	print(numbers)



print("                   ")





27.5
2

print('The value of', 27.5, '+', 2, '=', (27.5 + 2))

print('The value of', 27.5, '-', 2, '=', (27.5 - 2))

print('The value of', 27.5, '*', 2, '=', (27.5 * 2))

print('The value of', 27.5, '/', 2, '=', (27.5 / 2))

print('The value of', 27.5, '//', 2, '=', (27.5 // 2))

print('The value of', 27.5, '**', 2, '=', (27.5 ** 2))


print("                   ")




radius = 2
pi = 3.14159

print('diameter', 'formula', 'is', '2 * radius')

print('diameter', '=', (2 * radius))

print('circumference', 'formula', 'is', '2 * pi * radius')

print('circumference', '=', (2 * pi * radius))

print('area', 'formula', 'is', 'pi * radius ** 2')

print('area', '=', (pi * radius ** 2))



print("                   ")




integer = int(input('Enter an integer: '))

if integer % 2 == 0:
	print('Even')
else:
	print('odd')

print("                   ")



if 1024 % 4 == 0:
	print("1024 is a multiple of 4")
else:
	print("1024 is not a multiple of 4")

if 2 % 10 == 0:
	print("2 is a muliple of 10")
else:
	print("2 is not a multiplke of 10")


print("                   ")



print('number', '  ', 'square', '      ', 'cube', '    ')

for number in range(1, 6):
	square = number * number
	cube = number * number * number

	print(number, '             ', square, '        ', cube)




print("                   ")


char  = input('char: ')
integer_value = ord(char)


print(f"The integer representation of {char} is {integer_value}.")


print("                   ")



figure3 = int(input('Enter a number: '))
figure2 = int(input('Enter a number: '))
figure1 = int(input('Enter a number: '))

sum = figure1 + figure2 + figure3
print("Sum is ", sum)
average = (figure1 + figure2 + figure3) / 3
print("Average is ", average)
product = figure1 * figure2 * figure3
print("Product is ", product)
Smallest = min(figure1, figure2, figure3)
print("Smallest is ", Smallest)

Largest = max(figure1, figure2, figure3)
print("Largest is ",Largest)


print("                   ")



fivedigits = int(input("Enter a five digit Integer: "))

fifthMod = fivedigits % 10
fourdigits = fivedigits // 10
fourthMod = fourdigits % 10
threedigits = fourdigits // 10
thirdMod = threedigits % 10
twodigits = threedigits // 10
secondMod = twodigits % 10
onedigit = twodigits // 10
print(onedigit, '   ', secondMod, '   ', thirdMod, '   ', fourthMod, '   ', fifthMod)




print("                   ")



principal = 1000
r = 0.07
n = (10, 20 ,30)


amount = principal * (1 + 0.07) ** 10
print(amount, "in 10 years")

amount = principal * (1 + 0.07) ** 20
print(amount, "in 20 years")

amount = principal * (1 + 0.07) ** 30
print(amount, "in 30 years")








