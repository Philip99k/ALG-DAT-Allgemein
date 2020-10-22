import unittest

# Function summe:
# Parameter: unsotiertes Array mit Zahlen
# Result: Summe aller zahlen


def summe(unsotiert):  

    aktuelle_summe = 0
    for zahl in unsotiert:
        aktuelle_summe = aktuelle_summe + zahl
    return aktuelle_summe

# Function durchschnitt:
# Parameter: unsotiertes Array mit Zahlen
# Result: arithmetisches Mittel aller zahlen

def durchschnitt(unsotiert):  
    return summe(unsotiert)/len(unsotiert)

# Testcases


class TestSummeDurchschnitt(unittest.TestCase):
    def test_1(self):
        # Assert
        self.assertEqual(summe([7,8,12,4,3,9]),43)

    def test_2(self):
        # Assert
        self.assertEqual(summe([2,3,5,8,6,4,8]),36)

    def test_3(self):
        # Assert
        self.assertEqual(durchschnitt([7,8,12,4,3,9]),7.166666666666667)

    def test_4(self):
        # Assert
        self.assertEqual(durchschnitt([2,3,5,8,6,4,8]),5.142857142857143)

# Run Tests
if __name__ == "__main__":
    unittest.main()