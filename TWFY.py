'''
A library that provides a python interface to the TWFY API(http://www.theyworkforyou.com/api/)

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

__author__ = 'dorzey@googlemail.com'
__version__ = '0.1'

import datetime
import time
import urllib

class TWFY():
    apiKey=""
    outputs=['xml','php','js','rabx']
    functions=['convertURL','getConstituency','getConstituencies','getMP','getMPInfo','getMPs',\
                   'getLord','getLords','getMLAs','getMSP','getMSPs','getGeometry','getCommittee'\
                   'getDebates','getWrans','getWMS','getHansard','getComments']
    types=['commons','westminsterhall','lords']

    def __init__(self, apiKey):
        self.apiKey = apiKey

    def isValidDate(self, date):
        if date == '':
            return True
        else:
            try:
                c = time.strptime(date,"%d/%m/%Y")
                #print time.strftime("%Y %m %d",c)
                if datetime.datetime(*c[:6]).date() <= datetime.datetime.today().date():
                    return True
                else:
                    return False
            except ValueError:
                return False

    def twfy(self,function, output, params={}):
        """
        Generic function to call the api.
        Modified from MPFight(telnet://seagrass.goatchurch.org.uk:646/)
        """
        if output in self.outputs and function in self.functions:
            params_encoded = urllib.urlencode(params)
            url = "http://www.theyworkforyou.com/api/%s?key=%s&output=%s&%s" \
                % (function, self.apiKey, output,params_encoded);
            print url
            return urllib.urlopen(url).read()
        else:
            print 'Invalid out/function supplied'

    def convertURL(self, output, url):
        """
        Converts a parliament.uk Hansard URL into a TheyWorkForYou one, if possible
        """
        return self.twfy('convertURL',output,{'url':url})

    def getConstituency(self, output, postcode):
        """
        Searches for a constituency
        """
        return self.twfy('getConstituency',output,{'postcode':postcode})

    def getConstituencies(self,output,date="",search="",latitude="",longitude="",distance=""):
        """
        Returns list of constituencies
        """
        if isValidDate(self,date):
            return self.twfy('getConstituencies',output,\
                             {'date':date,'search':search,\
                                  'latitude':latitude,'longitude':longitude,'distance':distance})
        else:
            print 'Invalid date'

    def getMP(self, output,postcode="",constituency="",id="",always_return=""):
        """
        Returns main details for an MP
        """
        return self.twfy('getMP',output,{'postcode':postcode,'constituency':constituency,\
                                             'id':id,'always_return':always_return})

    def getMPInfo(self, output,id):
        """
        Returns extra information for a person
        """
        return self.twfy('getMPInfo',output,{'id':id})

    def getMPs(self, output,date="",party="",search=""):
        """
        Returns list of MPs
        """
        if isValidDate(self,date):
            return self.twfy('getMps',output,{'date':date,'party':party,'search':search})
        else:
            print 'Invalid date'

    def getLord(self, output,id):
        """
        Returns details for a Lord
        """
        return self.twfy('getLord',output,{'id':id})

    def getLords(self, output,date="",party="",search=""):
        """
        Returns list of Lords
        """
        if isValidDate(self,date):
            return self.twfy('getLords',output,{'date':date,'party':party,'search':search})
        else:
            print 'Invalid date'

    def getMLAs(self, output, date="",party="",search=""):
        """
        Returns list of MLAs
        """
        if isValidDate(self,date):
            return self.twfy('getMLAs',output,{'date':date,'party':party,'search':search})
        else:
            print 'Invalid date'

    def getMSP(self, output,postcode="",constituency="",id=""):
        """
        Returns details for an MSP
        """
        return self.twfy('getMSP',output,{'postcode':postcode,'constituency':constituency,'id':id})

    def getMSPs(self, output,date="",party="",search=""):
        """
        Returns list of MSPs
        """
        if isValidDate(self,date):
            return self.twfy('getMSPs',output,{'date':date,'party':party,'search':search})
        else:
            print 'Invalid date'

    def getGeometry(self, output,name=""):
        """
        Returns centre, bounding box of constituencies
        """
        return self.twfy('getGeometry',output,{'name':name})

    def getCommittee(self, output,name,date=""):
        """
        Returns members of Select Committee
        """
        if isValidDate(self,date):
            return self.twfy('getCommittee',output,{'name':name,'date':date})
        else:
            print 'Invalid date'

    def getDebates(self, output,type,date="",search="",person="",gid="",order="",page="",num=""):
        """
        Returns Debates (either Commons, Westminhall Hall, or Lords).This includes Oral Questions.
        """
        if type in types and isValidDate(self,date):
            return self.twfy('getDebates',output,{'type':type,'date':date,'search':search,'person':person,\
                                                  'gid':gid,'order':order,'page':page,'num':num})
        else:
            print 'Invalid type/date provided'

    def getWrans(self, output,date="",search="",person="",gid="",order="",page="",num=""):
        """
        Returns Written Answers
        """
        if isValidDate(self,date):
            return self.twfy('getWrans',output,{'date':date,'search':search,'person':person,'gid':gid,\
                                                  'order':order,'page':page,'num':num})
        else:
            print 'Invalid date'

    def getWMS(self, output,date="",search="",person="",gid="",order="",page="",num=""):
        """
        Returns Written Ministerial Statements
        """
        if isValidDate(self,date):
            return self.twfy('getWMS',output,{'date':date,'search':search,'person':person,'gid':gid,\
                                                  'order':order,'page':page,'num':num})
        else:
            print 'Invalid date'

    def getHansard(self, output,search="",person="",order="",page="",num=""):
        """
        Returns any of the above(Debates,Wrans,WMS)
        """
        return self.twfy('getHansard',output,{'search':search,'person':person,'order':order,\
                                                  'page':page,'num':num})

    def getComments(self, output,date="",search="",user_id="",pid="",page="",num=""):
        """
        Returns comments. With no arguments, returns most recent comments in reverse date order.
        """
        if isValidDate(self,date):
            return self.twfy('getComments',output,{'date':date,'search':search,'user_id':user_id,'pid':pid,\
                                                  'page':page,'num':num})
        else:
            print 'Invalid date'
