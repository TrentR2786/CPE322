def sumOfSquares(numbers):
        sum = 0
        for number in numbers:
                sum += number ** 2
        return sum

print(sumOfSquares([1,2,3]))
print(sumOfSquares([2,3,4,5]))

def fullName(firstName, middleInitial, lastName):
	return firstName + " " + middleInitial + ". " + lastName

name = fullName("Trent", "A", "Reichenbach")
print("My full name is %s." % name)

