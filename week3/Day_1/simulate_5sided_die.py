import random


def rand7():
    return random.randint(1, 7)


def rand5():

    # Implement rand5() using rand7()
    while True:
        r = rand7()
        print r
        if r < 6:
            return r

    # return 0


print 'Rolling 5-sided die...'
print rand5()