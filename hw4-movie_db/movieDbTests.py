#Dev Sethi
#CIT 590 HW 4

from createDb import *
import unittest
createDb()
class TestDb(unittest.TestCase):

    def testDeleteFromDb(self):
        self.assertEquals(deleteFromDb("the fighter"), 1)
        self.assertEquals(deleteFromDb("abcdef"),-1)
        self.assertEquals(deleteFromDb(0),-1)

    def testInsertIntoDb(self):
        self.assertEquals(insertIntoDb(('The Dark Knight', ['Christian Bale', 'Gary Oldman','Heath Ledger'])), 1)
        self.assertEquals(insertIntoDb(('0', ['0', '0','0'])), 1)

    def testSelectMovieInfo(self):
        self.assertRaises(TypeError,selectMovieInfo,0)
        self.assertRaises(TypeError,selectMovieInfo,[1,2,3])

    def testSelectActorInfo(self):
        self.assertRaises(TypeError,selectMovieInfo,0)
        self.assertIsInstance(selectMovieInfo(str()),list)

    

unittest.main()
