def listDivide(numbers, divide=2):
    amt = 0
    for num in numbers:
        if(num % divide == 0):
            amt += 1
    return amt

class ListDivideException(Exception):
    pass
def testListDivide():
    print("calling listDivide")
    def listDivide(numbers, divide=2):
        amt = 0
        for num in numbers:
            if(num % divide == 0):
                amt += 1
        return amt
print(listDivide([1,2,3,4,5]))
print(listDivide([2,4,6,8,10]))
print(listDivide([30, 54, 63,98,100],10))
print(listDivide([]))
print(listDivide([1,2,3,4,5],1))