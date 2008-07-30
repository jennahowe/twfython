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

import urllib

class TWFY():
    """B6DKutCjm8AqEXnFsFE2U4er"""
    BASE_URL="http://www.theyworkforyou.com/api/%(function)s?key=%(key)s&output=%(output)s&(args)s"
    apiKey=""
    outputs=['xml','php','js','rabx']
    functions=['convertURL','getConstituency','getConstituencies','getMP','getMPInfo','getMPs',\
                   'getLord','getLords','getMLAs','getMSP','getMSPs','getGeometry','getCommittee'\
                   'getDebates','getWrans','getWMS','getHansard','getComments']
    types=['commons','westminsterhall','lords']

    def __init__(self, apiKey):
        self.apiKey = apiKey

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
            print 'Invalid out supplied'

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
        return self.twfy('getConstituencies',output,\
                             {'date':date,'search':search,\
                                  'latitude':latitude,'longitude':longitude,'distance':distance})

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
        return self.twfy('getMps',output,{'date':date,'party':party,'search':search})

    def getLord(self, output,id):
        """
        Returns details for a Lord
        """
        return self.twfy('getLord',output,{'id':id})

    def getLords(self, output,date="",party="",search=""):
        """
        Returns list of Lords
        """
        return self.twfy('getLords',output,{'date':date,'party':party,'search':search})

    def getMLAs(self, output):
        """
        Returns list of MLAs
        """
        return self.twfy('getMLAs',output,{'date':date,'party':party,'search':search})

    def getMSP(self, output,postcode="",constituency="",id=""):
        """
        Returns details for an MSP
        """
        return self.twfy('getMSP',output,{'postcode':postcode,'constituency':constituency,'id':id})

    def getMSPs(self, output,date="",party="",search=""):
        """
        Returns list of MSPs
        """
        return self.twfy('getMSPs',output,{'date':date,'party':party,'search':search})

    def getGeometry(self, output,name=""):
        """
        Returns centre, bounding box of constituencies
        """
        return self.twfy('getGeometry',output,{'name':name})

    def getCommittee(self, output,name,date=""):
        """
        Returns members of Select Committee
        """
        return self.twfy('getCommittee',output,{'name':name,'date':date})

    def getDebates(self, output,type,date="",search="",person="",gid="",order="",page="",num=""):
        """
        Returns Debates (either Commons, Westminhall Hall, or Lords).This includes Oral Questions.
        """
        if type in types:
            return self.twfy('getDebates',output,{'type':type,'date':date,'search':search,'person':person,\
                                                  'gid':gid,'order':order,'page':page,'num':num})
        else:
            print 'Invalid type provided'

    def getWrans(self, output,date="",search="",person="",gid="",order="",page="",num=""):
        """
        Returns Written Answers
        """
        return self.twfy('getWrans',output,{'date':date,'search':search,'person':person,'gid':gid,\
                                                  'order':order,'page':page,'num':num})

    def getWMS(self, output,date="",search="",person="",gid="",order="",page="",num=""):
        """
        Returns Written Ministerial Statements
        """
        return self.twfy('getWMS',output,{'date':date,'search':search,'person':person,'gid':gid,\
                                                  'order':order,'page':page,'num':num})

    def getHansard(self, output,search="",person="",order="",page="",num=""):
        """
        Returns any of the above(Debates,Wrans,WMS)
        """
        return self.twfy('getHansard',output,{'date':date,'search':search,'person':person,'order':order,\
                                                  'page':page,'num':num})

    def getComments(self, output,date="",search="",user_id="",pid="",page="",num=""):
        """
        Returns comments. With no arguments, returns most recent comments in reverse date order.
        """
        return self.twfy('getComments',output,{'date':date,'search':search,'user_id':user_id,'pid':pid,\
                                                  'page':page,'num':num})