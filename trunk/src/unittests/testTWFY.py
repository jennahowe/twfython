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
from sys import argv
from twfy import TWFY

API_KEY = "YOUR API KEY"
CONSTITUENCY = "Aberdeen North"
ERRORLIST = ("\"error\"" ,"T5:error" ,"<error>")
LORDID = "13375"
MPID = "10186"
NAME = "Home Affairs Committee"
POSTCODE = "L69 3BX"
SEARCH = "python"
URL = "http://www.publications.parliament.uk/pa/cm200708/cmhansrd/cm080421/debtext/80421-0007.htm#0804216000685"


def contains(string, errors):
    to_return = False
    for err in errors:
        if err in string:
            to_return = "True"
    return to_return
 
class TWFYTestCase(unittest.TestCase):
    """
    *WARNING*The unit tests cause a lot of calls to the API, so test sparingly*WARNING*
    A Test class for the TWFY module.
    """
    def setUp(self):
        """
        set up data used in the tests.
        """
        self.twfy = TWFY.TWFY(API_KEY)
        
    
    def test_is_valid_date(self):
        """Tests is_valid_date is wokring"""
        self.assertTrue(TWFY.is_valid_date('08/08/1908'))
        self.assertFalse(TWFY.is_valid_date('08/XX/1908'))
        self.assertFalse(TWFY.is_valid_date('sdksldksldks'))
        self.assertFalse(TWFY.is_valid_date(20081983))
        self.assertFalse(TWFY.is_valid_date(20081983.0))
        self.assertFalse(TWFY.is_valid_date(['08', '08', '1908']))
        self.assertFalse(TWFY.is_valid_date({'day':'08', 'month':'08', 'year':'1908'}))
        
    def test_twfy_calls(self):
        """Tests that all possible (not all param variations) calls can be made."""
        i = 0
        for k, v in TWFY.API['twfy'].iteritems():
            params = {}
            params['method'] = k
            for value in v[0]:
                params[value] = ''
            if k == "getCommittee":
                params['name'] = NAME
            if k == "getHansard" or k == "getWMS" or k == "getWrans":
                params['search'] = SEARCH 
            if k == "getMSP":
                params['constituency'] = CONSTITUENCY
            if k == "convertURL":
                params['url'] = URL
            if k == "getConstituency":
                params['postcode'] = POSTCODE
            if k == "getMPsInfo" or k == "getMPInfo" or k == "getMP":
                params['id'] = MPID
            if k == "getDebates":
                params['type'] = TWFY.TYPES[0]
                params['search'] = SEARCH 
            if k == "getLord":
                params['id'] = LORDID
            for out in TWFY.OUTPUTS:
                params['output'] = out
                self.assertFalse(contains(self.twfy.get(**params), ERRORLIST))
                i += 1
        self.assertEqual(i, len(TWFY.OUTPUTS) * len(TWFY.API['twfy']))
    
if __name__ == '__main__':
    unittest.main()

    
