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
import json

twfy = TWFY.TWFY('PUT_YOUR_API_KEY_HERE')
#Get list of all MPs
#A date between '01/05/1997' and todays date.
mp_list = json.loads(twfy.api.getMPs(output='js',date='01/05/1997'), 'iso-8859-1')
results = {}

#Count the number of MPs for each party.
for mp in mp_list:
    party =  mp['party']
    if party in results.keys():
        results[party] += 1
    else:
        results[party] = 1
        
total_seats = float(sum(results.values()))

#Combine counts for parties with less than 10 seats
other = 0 
parties = set()
for k,v in results.iteritems():
    if v < 10:
        parties.add(k)
        other += v     
        
for party in parties:
    del results[party]
    
results['Other'] = other   

#Print the results.
for k, v in results.iteritems():
    print k, ' = ', (v/total_seats)*100, '%', '(', v, ' seats)'       

#Makes a Google Chart API (http://code.google.com/apis/chart/) URL    
def color_selector(parties):
    results = []
    for party in parties:
        try:
            results.append(colors[party])
        except KeyError:
            results.append(colors['missed'])
    return results

import urllib
colors = {'Labour':'FF0000', 'Conservative':'0000FF', 'Liberal Democrat':'FF9933', 'Other':'333333', 'missed':'CCCCCC'}
CHART_URL = "http://chart.apis.google.com/chart?"
params = {}
params['cht'] = "p"
params['chd'] = "t:"+",".join(str(i) for i in results.values())
params['chs'] = "750x375"
params['chl'] = "|".join(str(i)+" ("+"%.2f" % round((results[i]/total_seats)*100, 2)+"%)" for i in results.keys())
#Need to be a bit cleverer in selecting the colors
params['chco'] = ",".join(color_selector(results.keys()))

params_encoded = urllib.urlencode(params)
print CHART_URL+params_encoded



