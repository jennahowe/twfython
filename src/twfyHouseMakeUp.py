'''
An example that uses the python interface to the TWFY API(http://www.theyworkforyou.com/api/)

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
from twfy import TWFY
from xml.dom import minidom

y = TWFY.TWFY('PUT_YOUR_API_KEY_HERE')
#Get list of all MPs
#A date between '01/05/1997' and todays date.
x = minidom.parseString(y.twfy.getMPs(output='xml',date='01/08/2008'))
#Just get the XML elements that are 'party'
results = x.getElementsByTagName('party')
partylist=[]    #List of party names
partySet = set()#Set of part names

for party in results:
    xml = party.toxml()
    xml = xml[7:-8]
    partylist.append(xml)
    partySet.add(xml)#Duplicate elements will not be added

finalResults={}
for ele in partySet:
    finalResults[ele]=partylist.count(ele)

totalSeats =0
for k,v in finalResults.iteritems():
    totalSeats = totalSeats + v

percentResults={}   
floatTotalSeats = float(totalSeats) #To stop division returning an integer 
for k,v in finalResults.iteritems():
    percentResults[k]= (v/floatTotalSeats )*100
    
for k,v in percentResults.iteritems():
    print str(k)+' = '+str(v)+'%'