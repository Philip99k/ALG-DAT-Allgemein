import unittest

# Function bineare_suche:
# Parameter:
#   liste: Array aus Elementen
#   wert:  Wert, nach dem in der Liste gesucht wird
# Result:
#   Index des 1. Treffers
#   oder -1, falls kein Treffer


def pi(n):  

    pi = 0
    zaeler = 4
    nenner = 1
    vorzeichen = 1

    for _ in range(0,n):
        pi = pi + vorzeichen*zaeler/nenner
        vorzeichen = -vorzeichen
        nenner = nenner + 2
    return pi

for i in range(1, 10000000):
    print(pi(i))

def pi_ausrechnen2():  

    # pi = 4/1 - 4/3 + 4/5
    # print('Hier ist pi: ', pi)

    x = 4/1
    y = 3
    z = (4/y)
    toggle = 0

    while y <= 200:
        z = (4/y)
        if toggle == 0:
            a = x - z
            x = a
            toggle = 1
        else: 
            a = x + z
            x = a
            toggle = 0

        # a = x - (-1)*z
        # x = a
        y = y + 2
        # print('Hier ist pi: ', a)
        # print('zwischenstand: ', x)
        # print('y laufwert: ', y)
    print('Hier ist das Endergebniss 2 von pi: ', a)


# Testcases

# pi_ausrechnen()
pi_ausrechnen2()
# Run Tests
if __name__ == "__main__":
    unittest.main()