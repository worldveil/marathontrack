# -*- coding: utf-8 -*-
import urllib2, urllib
from bs4 import BeautifulSoup

SEARCH_URL = "http://registration.baa.org/2014/cf/RegAthleteAlert/wnd_iFindBibNumbers.cfm?mode=result"

def get_name_matches(first, last):
	results = []	

	# set our POST parameters
	values = {
		'FirstName': first,
		'LastName': last }
	
	# URL encode the request & send
	try:
		data = urllib.urlencode(values)
		req = urllib2.Request(SEARCH_URL, data)
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