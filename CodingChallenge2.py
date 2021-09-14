# Part 2
def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("There is a divide by zero error")


# Part 1
def bmicalculator(weight, height):
    results = divide(weight, height)
    return results**2


print(bmicalculator(85, 2))

# Part 3
file = open('demo.txt', 'w')
file.write("this is text")
file.close()

file = open('demo.txt', 'r')
content = file.read()
print(content)
file.close()

file = open('demo.txt', 'a')
file.write(" this is more text")
file.close()


# Part 4
equipment = {
    "socks": "$7.50",
    "shorts": "$15",
    "cleats": "$400",
    "jerseys": "$75",
    "gloves": "$120",
}


def itemlookup(name):
    return equipment.get(name)


print(itemlookup("socks"))

# Part 5
numlist = [x for x in range(100) if x % 2 != 0]
print(numlist)
