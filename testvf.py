# unitesting module used to test programme

import unittest
import verify_funcs as vf 

class TestClass(unittest.TestCase):
    """Used for unitesting"""

    def test_isInteger(self):
        self.assertTrue(vf.isInteger(5))
        self.assertTrue(vf.isInteger(0))
        self.assertFalse(vf.isInteger("antelope"))
        
    def test_isValidName(self):
        self.assertEqual(vf.isValidName('Jim', 0, 10), True)
        self.assertEqual(vf.isValidName('King Arthur the Third', 0, 10), False)
        
    def test_isValidTeamSize(self):
        self.assertTrue(vf.isValidTeamSize(5, 0, 10))
        self.assertFalse(vf.isValidTeamSize(15, 0, 10))
         
    def test_voteInput(self):
        self.assertEqual(vf.voteInput(5), 5)
        
    def test_voteCheck(self):
        self.assertTrue(vf.voteCheck(5))
        self.assertFalse(vf.voteCheck(-10))
        self.assertFalse(vf.voteCheck(101))        

if __name__ == '__main__':
    unittest.main()
