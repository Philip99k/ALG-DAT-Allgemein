import unittest

# Function minimum:
# Parameter: unsortiertes Array mit Zahlen
# Result: kleinstes Element des Arrays


def merge(sortiert1, sortiert2):  
    finger1 = 0
    finger2 = 0
    laenge1 = len(sortiert1)
    laenge2 = len(sortiert2)
    result = []
    # beide Finger sind noch in der Liste?
    while finger1 < laenge1 and finger2 < laenge2:
        if sortiert1[finger1] < sortiert2<[finger2]:
            result.append(sortiert1[finger1])
            finger1 = finger1 + 1
        else:
            result.append(sortiert2[finger2])
            finger2 = finger2 + 1

    # nur linker finger in der Liste?
    while finger1 < laenge1:
        result.append(sortiert1[finger1])
        finger1 = finger1 + 1

    # nur rechter finger in der Liste?
    while finger2 < laenge2:
        result.append(sortiert2[finger2])
        finger2 = finger2 + 1


    # => kleinerer wert übernehmen
    # => entsprechenden Finger weiterziehen
    
    return result

def mergesort(unsortiert):  
    laenge = len(unsortiert)
    if laenge<= 1:
        # das Array hat null oder ein element und ist daher schon sortiert
        return unsortiert
    else:
        #Array in zwei kleinere Arrays aufteilen
        mitte = laenge // 2
        links = []
        for index in range(0, mitte):
            links.append(unsortiert[index])
        rechts = []
        for index in range(mitte, lange):
            rechts.append(unsortiert[index])

        # beide Teilarrays einzelnd sortieren
        links = mergesort(links)
        rechts = mergesort(rechts)

        return merge(links, rechts)
    
  
# Testcases


class TestMergesort(unittest.TestCase):
    def test_mergesort_1(self):
        unsortiert = [7, 12, 4, 8, 3, 9]
        sortiert = [3, 4, 7, 8, 9, 12]
        self.assertEqual(mergesort(unsortiert),sortiert)

    def test_merge_1(self):
        sortiert1 = [1, 2, 3, 4, 5]
        sortiert2 = [6, 7, 8, 9, 10]
        expectet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(mergesort(sortiert1, sortiert2),expectet)

    def test_merge_2(self):
        sortiert1 = [1, 2, 6, 7, 9]
        sortiert2 = [3, 4, 5, 8, 10]
        expectet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(mergesort(sortiert1, sortiert2),expectet)
    
    def test_merge_3(self):
        sortiert1 = [2]
        sortiert2 = [1]
        expectet = [1, 2]
        self.assertEqual(mergesort(sortiert1, sortiert2),expectet)

    def test_merge_4(self):
        sortiert1 = [1]
        sortiert2 = [2]
        expectet = [1, 2]
        self.assertEqual(mergesort(sortiert1, sortiert2),expectet)


# Run Tests
if __name__ == "__main__":
    unittest.main()