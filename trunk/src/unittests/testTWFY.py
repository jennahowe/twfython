"""
testTWFY.py v.0.1
Author: dorzey@gmail.com

   This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.       
"""
import unittest
from twfy import TWFY
 
class testTWFY(unittest.TestCase):
    """
    *WARNING*The unit tests cause a lot of calls to the API, so test sparingly*WARNING*
    A Test class for the TWFY module.
    """
    def setUp(self):
        """
        set up data used in the tests.
        """
        self.twfy = TWFY.TWFY('PUT_YOUR_API_KEY_HERE')
    
    def testisValidDate(self):
        self.assertTrue(self.twfy.isValidDate('08/08/1908'))
        self.assertFalse(self.twfy.isValidDate('08/XX/1908'))
        self.assertFalse(self.twfy.isValidDate('sdksldksldks'))
        self.assertFalse(self.twfy.isValidDate(20081983))
        self.assertFalse(self.twfy.isValidDate(20081983.0))
        self.assertFalse(self.twfy.isValidDate(['08','08','1908']))
        self.assertFalse(self.twfy.isValidDate({'day':'08','month':'08','year':'1908'}))
        
    def testtwfy(self):
        for function in self.twfy.functions:
            self.failIfEqual(self.twfy.twfy(function, 'anOutput'), None) 
            for output in self.twfy.outputs:
                self.failIfEqual(self.twfy.twfy(function, output), 'Invalid function')
                self.failIfEqual(self.twfy.twfy(function, output), 'Invalid output supplied')
                self.failIfEqual(self.twfy.twfy('afunction', output), None) 
                                        
                        
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(testTWFY))
        return suite
    
if __name__ == '__main__':
    unittest.main()

    
