# -*- coding: utf-8 -*-
import urllib2, urllib
from bs4 import BeautifulSoup
from marathon.utilities import GetSecsFromTimestring
from marathon import MI_PER_KM

BIB_SEARCH_URL = "http://registration.baa.org/2014/cf/RegAthleteAlert/wnd_iFindBibNumbers.cfm?mode=result"
PROGRESS_SEARCH_URL = "http://registration.baa.org/2013/cf/public/iframe_ResultsSearchDNF.cfm?mode=results"

def search_for_bibs(first, last):
	results = []	

	# set our POST parameters
	values = {
		'FirstName': first,
		'LastName': last }
	
	# URL encode the request & send
	try:
		data = urllib.urlencode(values)
		req = urllib2.Request(BIB_SEARCH_URL, data)
		response = urllib2.urlopen(req)
		result = response.read()
	except Exception as e:
		return []
	
	# parse the html
	# note: yes this is bad, and yes I feel ashamed. hAckAthon WOOT
	soup = BeautifulSoup(result)
	table_text = soup.body.find('tbody').text.encode('utf-8')
	table_text = table_text.replace("\t", "")
	table_text = table_text.replace('\r', '')
	table_text = table_text.replace("\n\n\n\n\n", "|")
	table_text = table_text.replace("\n", "")
	
	# split
	people = table_text.split("|")
	people_dicts = []
	for person in people:
		try:
			"""Examples:
			1297  Russell, Aaron  New Albany  OH  USA  41  M  
			16738  Russell, Alexandra L  Pasadena  CA  USA  28  F  
			13869  Russell, Carl R.  Boone  NC  USA  57  M  
			19648  Russell, Casey R  Denver  CO  USA  41  F 
			"""
			attributes = {}
			fields = [field.strip() for field in person.split(" ") if field != ""]
			
			if len(fields) < 5:
				# invalid
				continue
		
			attributes["bib_number"] = fields[0]
			attributes["last"] = fields[1].replace(",", "")
			attributes["first"] = fields[2]
			
			attributes["city"] = " ".join(fields[3:len(fields) - 4])
			
			attributes["gender"] = fields[-1]
			attributes["age"] = fields[-2]
			attributes["country"] = fields[-3]
			attributes["state"] = fields[-4]
			
			people_dicts.append(attributes)
			
		except Exception as e:
			continue
			
	return people_dicts
	
def search_for_progress(bib):

	progress = {}

	# set our POST parameters
	values = {'BibNumber': bib}
	
	# URL encode the request & send
	try:
		data = urllib.urlencode(values)
		req = urllib2.Request(PROGRESS_SEARCH_URL, data)
		response = urllib2.urlopen(req)
		result = response.read()
	except Exception as e:
		return []
		
	# parse the html
	# note: yes this is bad, and yes I feel ashamed. hAckAthon WOOT
	soup = BeautifulSoup(result)
	split_pace_projectfinish = soup.findChildren('tbody')[0].findChildren('tr')[3].findChildren('td')
	
	# pull out cells
	split_string = split_pace_projectfinish[0].text
	pace_string = split_pace_projectfinish[1].text
	projectfinish_string = split_pace_projectfinish[2].text
	
	# split string
	"""
	Spilt: 35K - 4:19:49
	"""
	arr = split_string.split("-")
	km = arr[0].replace("K", "").strip()
	seconds_since_start = GetSecsFromTimestring(arr[1])
	
	print "KM:", km
	print "Seconds since start:", seconds_since_start
	
	# pace string
	"""
	Pace: 0:11:57
	"""
	seconds_per_mile = GetSecsFromTimestring(pace_string)
	seconds_per_km = float(seconds_per_mile) / float(MI_PER_KM)
	
	print "Seconds per km:", seconds_per_km
	km_per_sec = 1.0 / float(seconds_per_km)
	print "KM per second:", km_per_sec
	
	# projected finish
	"""
	Projected Finish: 5:13:14
	"""
	projected_num_secs_finish = GetSecsFromTimestring(projectfinish_string)
	print "Projected Finish seconds:", projected_num_secs_finish
	
	return {
		"bib" : bib,
		"split_km" : km,
		"secs_since_start" : seconds_since_start,
		"km_per_sec" : km_per_sec,
		"projected_finish_secs" : projected_num_secs_finish
	}
	
	
	
	
	
	
	
		