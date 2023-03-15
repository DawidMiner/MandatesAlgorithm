import unittest
from mandates import Mandates


class TestMyAlgorithm(unittest.TestCase):
    def testDHondtMethod(self):
        self.mandates = Mandates()
        self.mandates.table_of_votes = [[24000], [18000], [12000], [9000], [6000], [3000]]
        self.mandates.DivideSumsOfVotes(1, 1, 12)
        self.mandates.ChooseMandates(12)
        result = self.mandates.AddMandatesToList(1)
        self.assertEqual(result, [5, 3, 2, 1, 1, 0])

    def testSainteLagueMethod(self):
        self.mandates = Mandates()
        self.mandates.table_of_votes = [[24000], [18000], [12000], [9000], [6000], [3000]]
        self.mandates.DivideSumsOfVotes(3, 2, 12)
        self.mandates.ChooseMandates(12)
        result = self.mandates.AddMandatesToList(2)
        self.assertEqual(result, [4, 3, 2, 2, 1, 0])

    def testHareNiemeyerMethod(self):
        self.mandates = Mandates()
        self.mandates.table_of_votes = [[24000], [18000], [12000], [9000], [6000], [3000]]
        self.mandates.MandatesWithHareNiemeyera(12)
        result = self.mandates.AddMandatesToList(3)
        self.assertEqual(result, [4, 3, 2, 1, 1, 1])

    def testDHondtMethodAnotherExample(self):
        self.mandates = Mandates()
        self.mandates.table_of_votes = [[100000], [70000], [19000], [11000]]
        self.mandates.DivideSumsOfVotes(1, 1, 12)
        self.mandates.ChooseMandates(10)
        result = self.mandates.AddMandatesToList(1)
        self.assertEqual(result, [5, 4, 1, 0])

    def testSainteLagueMethodAnotherExample(self):
        self.mandates = Mandates()
        self.mandates.table_of_votes = [[100000], [70000], [19000], [11000]]
        self.mandates.DivideSumsOfVotes(3, 2, 12)
        self.mandates.ChooseMandates(10)
        result = self.mandates.AddMandatesToList(2)
        self.assertEqual(result, [5, 4, 1, 0])

    def testHareNiemeyerMethodAnotherExample(self):
        self.mandates = Mandates()
        self.mandates.table_of_votes = [[100000], [70000], [19000], [11000]]
        self.mandates.MandatesWithHareNiemeyera(10)
        result = self.mandates.AddMandatesToList(3)
        self.assertEqual(result, [5, 3, 2, 0])


if __name__ == '__main__':
    unittest.main()




2 * 2 * 2 * 2 * 2

a = 2
n = 5
