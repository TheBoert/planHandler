import unittest

from layutils.plan import *
from layutils.point import phPoint


class PlanTester(unittest.TestCase):
    #create PlanLayout for testing without any margins
    testMargins = phPageMargins(0,0,0,0)
    testPage = phPageLayout(20, 10,testMargins,0)
    testPoint = phPoint(0,0)
    testPlan = phPlanLayout(testPage, 1000, 0, testPoint)

    def testWorldViewHeight(self):
        result = self.testPlan.worldViewHeight,
        expected = 10,
        self.assertEqual(result, 
                         expected, 
                         "\nphPlan.worldViewHeight returns unexpected length." 
                         + f"\nExpected: \"{expected}\" but got: \"{result}\"")
        
    def testWorldViewWidth(self):
        result = self.testPlan.worldViewWidth,
        expected = 20,
        self.assertEqual(result, 
                         expected, 
                         "\nphPlan.worldViewHeight returns unexpected length." 
                         + f"\nExpected: \"{expected}\" but got: \"{result}\"") 

    def test_lowerleft(self):
        result = self.testPlan.worldViewLowerLeft
        expected = self.testPoint
        self.assertEqual(result, 
                         expected, 
                         "\nphPlan.worldViewLowerLeft returns unexpected phPoint." 
                         + f"\nExpected: \"{expected}\" but got: \"{result}\"")

    def test_lowerright(self):
        result = self.testPlan.worldViewLowerRight
        expected = phPoint(20,0)
        self.assertEqual(result, 
                         expected, 
                         "\nphPlan.worldViewLowerRight returns unexpected phPoint." 
                         + f"\nExpected: \"{expected}\" but got: \"{result}\"")

    def test_upperleft(self):
        result = self.testPlan.worldViewUpperLeft
        expected = phPoint(0,10)
        self.assertEqual(result, 
                         expected, 
                         "\nphPlan.worldViewUpperLeft returns unexpected phPoint." 
                         + f"\nExpected: \"{expected}\" but got: \"{result}\"")

    def test_upperright(self):
        result = self.testPlan.worldViewUpperRight
        expected = phPoint(20,10)
        self.assertEqual(result,
                         expected, 
                         "phPlan.worldViewUpperRight returns unexpected phPoint." 
                         + f"\nExpected: \"{expected}\" but got: \"{result}\"")
    
if __name__ == '__main__':
    unittest.main(verbosity=2)