NRIC = input("Input NRIC here ")
if NRIC.startswith('S'):
     year=1900
else:
     year = 2000
year = int(NRIC[1:3]) + year
age = 2020 - year
print('Your age is ' + str(age))
