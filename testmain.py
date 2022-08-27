import unittest
import main

class TestProgram(unittest.TestCase):
    def testStatusCode(self):

        self.assertEqual(main.r.status_code, 200) #test if status code is 200

if __name__ == '__main__':
    unittest.main()