print "Welcome to the FizzBuzz Game!"

print "Please, select a number between 1 and 100.\nEnter a whole number!"

number = int(raw_input())

for number in range(1, number+1):
    if number % 3 == 0 and number % 5 == 0:
        print 'Fizzbuzz'
    elif number % 3 == 0:
        print 'Fizz'
    elif number % 5 == 0:
        print 'Buzz'
    else:
        print str(number)







