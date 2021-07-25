
try1 = input('What is your first 333 attempt? ')
try2 = input('What is your second 333 attempt? ')
try3 = input('What is your third 333 attempt? ')

def compare(try1 , try2 , try3):
    if try1 < try2 and try1 < try3:
        return try1
    elif try2 < try1 and try2 < try3:
        return try2
    else:
        return try3

print('Your best 333 attempt was ' + compare(try1, try2, try3))

best333 = float(compare(try1, try2, try3))
print()

try1 = input('What is your first 363 attempt? ')
try2 = input('What is your second 363 attempt? ')
try3 = input('What is your third 363 attempt? ')


compare(try1, try2, try3)
print('Your best 363 attempt was ' + compare(try1, try2, try3))

best363 = float(compare(try1, try2, try3))
print()

try1 = input('What is your first cycle attempt? ')
try2 = input('What is your second cycle attempt? ')
try3 = input('What is your third cycle attempt? ')

compare(try1, try2, try3)

print('Your best cycle attempt was ' + compare(try1, try2, try3))
print()

bestcycle = float(compare(try1, try2, try3))

print('Your best overall time is ' + str(best333 + best363 + bestcycle))