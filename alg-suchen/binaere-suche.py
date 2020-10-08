import unittest

# Function bineare_suche:
# Parameter:
#   liste: Array aus Elementen
#   wert:  Wert, nach dem in der Liste gesucht wird
# Result:
#   Index des 1. Treffers
#   oder -1, falls kein Treffer


def bineare_suche(liste, wert):  

    links = 0
    rechts = len(liste) -1 
    zaehler = 0

    while links <= rechts:
        zaehler = zaehler + 1
        mitte = (links + rechts) // 2
        print ("Mitte: ", mitte)
        if liste[mitte] == wert:
            print("Zähler: ", zaehler)
            return mitte
        if liste[mitte] < wert:
            links = mitte + 1
        else: 
            rechts = mitte -1
    print("Zähler: ", zaehler)
    return -1
            

        # print (mitte)

        # if wert > range(0, len(liste)


        # for i in range(0, len(liste)):
        #     if liste[i] == wert:
        #         return i
        # return -1


# Testcases


class TestLineareSuche(unittest.TestCase):
    def test_1(self):
        # Arrange
        liste = [1,2,3,4,5,6,7,8]
        wert = 4
        expected = 3

        # Act
        result = bineare_suche(liste, wert)

        # Assert
        self.assertEqual(result, expected)

    def test_2(self):
        # Arrange
        liste = [1,2,3,4,5,6,7,8]
        wert = 9
        expected = -1

        # Act
        result = bineare_suche(liste, wert)

        # Assert
        self.assertEqual(result, expected)

    def test_3(self):
        # Arrange
        liste = [2,3,1,5,8,6,4,8]
        liste.sort()
        wert = 1
        expected = liste.index(wert)

        # Act
        result = bineare_suche(liste, wert)

        # Assert
        self.assertEqual(result, expected)

    def test_4(self):
        # Arrange
        liste = [2,3,1,4,8,6,4,8]
        wert = 4
        expected = 3

        # Act
        result = bineare_suche(liste, wert)

        # Assert
        self.assertEqual(result, expected)

    def test_5(self):
        # Arrange
        liste = range(0, 20000001)
        wert = 20000000
        expected = 20000000

        # Act
        result = bineare_suche(liste, wert)

        # Assert
        self.assertEqual(result, expected)


# Run Tests
if __name__ == "__main__":
    unittest.main()