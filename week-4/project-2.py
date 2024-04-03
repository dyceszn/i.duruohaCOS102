print('Welcome to Izifin Technologies')

staffName = input('Enter your name:')
staffYoe = int(input('Enter your year of experience:'))
staffAge = int(input('Enter your age:'))

if staffYoe > 25 and staffAge >= 55:
    print('Your annual tax revenue is N5600000')

elif staffYoe > 20 and staffAge >= 45:
    print('Your annual tax revenue is N4480000')

elif staffYoe > 10 and staffAge >= 35:
    print('Your annual tax revenue is N1500000')

elif staffYoe < 10 and staffAge < 35:
    print('Your annual tax revenue is N550000')

else:
    print('No money for you')
