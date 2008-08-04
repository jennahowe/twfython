'''
testTWFY.py v.0.1
Author: dorzey@gmail.com

A library that provides a python binding to the TWFY API(http://www.theyworkforyou.com/api/)

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
'''
import datetime
import time
import urllib

class TWFY():
    apiKey=""
    errors={'function':'Invalid function', 'output':'Invalid output supplied', 'date':'Invalid date',\
             'type':'Invalid type provided'}
    functions=['convertURL', 'getConstituency', 'getConstituencies', 'getMP', 'getMPInfo', 'getMPs', \
                   'getLord', 'getLords', 'getMLAs', 'getMSP', 'getMSPs', 'getGeometry', 'getCommittee'\
                   'getDebates', 'getWrans', 'getWMS', 'getHansard', 'getComments']        
    outputs=['xml', 'php', 'js', 'rabx']
    types=['commons', 'westminsterhall', 'lords']


    def __init__(self, apiKey):
        self.apiKey = apiKey

    def isValidDate(self, date):
        if date == '':
            return True
        else:
            try:
                c = time.strptime(date, "%d/%m/%Y")
                if datetime.datetime(*c[:6]).date() <= datetime.datetime.today().date():
                    return True
                else:
                    return False
            except (ValueError, TypeError):
                return False

    def twfy(self, function, output, params={}):
        """
        Generic function to call the api.
        Modified from MPFight(telnet://seagrass.goatchurch.org.uk:646/)
        """
        if output in self.outputs:
            if function in self.functions:
                params_encoded = urllib.urlencode(params)
                url = "http://www.theyworkforyou.com/api/%s?key=%s&output=%s&%s" \
                % (function, self.apiKey, output, params_encoded);
                return urllib.urlopen(url).read()
            else:
                return self.errors.get('function')
        else:
           return self.errors.get('output')

    def convertURL(self, output, url):
        """
        Converts a parliament.uk Hansard URL into a TheyWorkForYou one, if possible
        """
        return self.twfy('convertURL', output, {'url':url})

    def getConstituency(self, output, postcode):
        """
        Searches for a constituency
        """
        return self.twfy('getConstituency', output, {'postcode':postcode})

    def getConstituencies(self, output, date="", search="", latitude="", longitude="", distance=""):
        """
        Returns list of constituencies
        """
        if isValidDate(self, date):
            return self.twfy('getConstituencies', output, \
                             {'date':date, 'search':search, \
                                  'latitude':latitude, 'longitude':longitude, 'distance':distance})
        else:
            return 'Invalid date'

    def getMP(self, output, postcode="", constituency="", id="", always_return=""):
        """
        Returns main details for an MP
        """
        return self.twfy('getMP', output, {'postcode':postcode, 'constituency':constituency, \
                                             'id':id, 'always_return':always_return})

    def getMPInfo(self, output, id):
        """
        Returns extra information for a person
        """
        return self.twfy('getMPInfo', output, {'id':id})

    def getMPs(self, output, date="", party="", search=""):
        """
        Returns list of MPs
        """
        if self.isValidDate(date):
            return self.twfy('getMPs', output, {'date':date, 'party':party, 'search':search})
        else:
            return self.errors.get('date')

    def getLord(self, output, id):
        """
        Returns details for a Lord
        """
        return self.twfy('getLord', output, {'id':id})

    def getLords(self, output, date="", party="", search=""):
        """
        Returns list of Lords
        """
        if self.isValidDate(date):
            return self.twfy('getLords', output, {'date':date, 'party':party, 'search':search})
        else:
            return self.errors.get('date')

    def getMLAs(self, output, date="", party="", search=""):
        """
        Returns list of MLAs
        """
        if self.isValidDate(date):
            return self.twfy('getMLAs', output, {'date':date, 'party':party, 'search':search})
        else:
            return self.errors.get('date')

    def getMSP(self, output, postcode="", constituency="", id=""):
        """
        Returns details for an MSP
        """
        return self.twfy('getMSP', output, {'postcode':postcode, 'constituency':constituency, 'id':id})

    def getMSPs(self, output, date="", party="", search=""):
        """
        Returns list of MSPs
        """
        if self.isValidDate(date):
            return self.twfy('getMSPs', output, {'date':date, 'party':party, 'search':search})
        else:
            return self.errors.get('date')

    def getGeometry(self, output, name=""):
        """
        Returns centre, bounding box of constituencies
        """
        return self.twfy('getGeometry', output, {'name':name})

    def getCommittee(self, output, name, date=""):
        """
        Returns members of Select Committee
        """
        if self.isValidDate(date):
            return self.twfy('getCommittee', output, {'name':name, 'date':date})
        else:
            return self.errors.get('date')

    def getDebates(self, output, type, date="", search="", person="", gid="", order="", page="", num=""):
        """
        Returns Debates (either Commons, Westminhall Hall, or Lords).This includes Oral Questions.
        """
        if type in types:
            if self.isValidDate(date):
                return self.twfy('getDebates', output, {'type':type, 'date':date, 'search':search, 'person':person, \
                                                  'gid':gid, 'order':order, 'page':page, 'num':num})
            else:
                return self.errors.get('date')
        else:
            return self.errors.get('type')

    def getWrans(self, output, date="", search="", person="", gid="", order="", page="", num=""):
        """
        Returns Written Answers
        """
        if self.isValidDate(date):
            return self.twfy('getWrans', output, {'date':date, 'search':search, 'person':person, 'gid':gid, \
                                                  'order':order, 'page':page, 'num':num})
        else:
            return self.errors.get('date')

    def getWMS(self, output, date="", search="", person="", gid="", order="", page="", num=""):
        """
        Returns Written Ministerial Statements
        """
        if self.isValidDate(date):
            return self.twfy('getWMS', output, {'date':date, 'search':search, 'person':person, 'gid':gid, \
                                                  'order':order, 'page':page, 'num':num})
        else:
            return self.errors.get('date')

    def getHansard(self, output, search="", person="", order="", page="", num=""):
        """
        Returns any of the above(Debates,Wrans,WMS)
        """
        return self.twfy('getHansard', output, {'search':search, 'person':person, 'order':order, \
                                                  'page':page, 'num':num})

    def getComments(self, output, date="", search="", user_id="", pid="", page="", num=""):
        """
        Returns comments. With no arguments, returns most recent comments in reverse date order.
        """
        if self.isValidDate(date):
            return self.twfy('getComments', output, {'date':date, 'search':search, 'user_id':user_id, 'pid':pid, \
                                                  'page':page, 'num':num})
        else:
            return self.errors.get('date')
