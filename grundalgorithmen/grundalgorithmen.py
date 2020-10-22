import unittest

# Function minimum:
# Parameter: unsotiertes Array mit Zahlen
# Result: kleinstes Element des Arrays


def minimum(unsotiert):  

    aktuelles_minimum = unsotiert[0];
    for i in range(1,len(unsotiert)):
        if unsotiert[i] < aktuelles_minimum:
            aktuelles_minimum = unsotiert[i]    
    return aktuelles_minimum
    
            


def maximum(unsotiert):  

    aktuelles_maximum = unsotiert[0];
    for i in range(1,len(unsotiert)):
        if unsotiert[i] > aktuelles_maximum:
            aktuelles_maximum = unsotiert[i]
    return aktuelles_maximum



# Testcases


class TestLineareSuche(unittest.TestCase):
    def test_1(self):
        # Assert
        self.assertEqual(minimum([1,2,3,4,5,6,7,8]),1)

    def test_2(self):
        # Arrange
        unsotiert = [2,3,1,5,8,6,4,8]
        # Assert
        self.assertEqual(minimum([2,3,-1,5,8,6,4,8]),-1)

    def test_3(self):
        # Arrange
        liste = [2,3,1,4,8,6,4,8]
        # Assert
        self.assertEqual(maximum([1,2,3,4,5,6,7,8]),8)

    def test_4(self):
        # Assert
        self.assertEqual(maximum([2,3,1,5,8,6,4,8]),8)


# Run Tests
if __name__ == "__main__":
    unittest.main()