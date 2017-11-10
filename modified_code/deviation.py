import json
import MySQLdb as mysql
import matplotlib.pyplot as plt
import math
from highcharts import Highchart
from geotext import GeoText
import requests

import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver

key = 'AIzaSyBGPODmFudGHu3ab1HLw8QaWYcPArE03cI'

def cord(place):
	temp = place.split(" ")
	location = ''
	for i in range(0, len(temp)-1):
		if(temp[i][len(temp[i]) -1] == ","):
			string = temp[i][0:len(temp[i])-1]
			location += string
		else:
			location += temp[i]
	
		if(i!= len(temp) -1):
			location += '+' 
	url = "https://maps.googleapis.com/maps/api/geocode/json?address="+location+"&key="+key


	data = requests.get(url)
	rep = json.loads(data.text)

	loc = (rep['results'][0])
	loc = loc['geometry']
	loc = loc['location']
	return(loc['lat'], loc['lng'])

def hav(long1, lat1, long2,lat2):

	lat1 *= math.pi/180
	lat2 *= math.pi/180

	long1 *= math.pi/180
	long2 *= math.pi/180

	dlong = (long2- long1)
	dlat = (lat2 - lat1)

	R = 6371
	a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(lat1) * math.cos(lat2) * math.sin(dlong/2)*math.sin(dlong/2)
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
	d = R*c
	return d




host = 'localhost'
user = 'root'
password = '34185'
db = 'yelp_db'


def create_connection():
	connection = mysql.connect(host, user, password, db)
	cursor = connection.cursor()
	return connection, cursor

def close_connection(cursor, connection):
	cursor.close()
	connection.commit()
	connection.close()


distance_value = []
user_id_arr = []


business_id = raw_input()
connection, cursor = create_connection()
cursor.execute("select city, state from business where business_id = '" + business_id + "'")
area = cursor.fetchall()
city = ""
state = ""
for ar in area:
	city = ar[0]
	state = ar[1]
location_business = city + str(" ") + state
(long1, lat1) = cord(location_business)


cursor.execute("select user_id from review where business_id = '" + business_id +"';");
data = cursor.fetchall();


for row in data:
	
	user_id = row[0]
	user_id_arr.append(user_id)

	url="https://www.yelp.com/user_details?userid="+str(user_id)
	response=urllib2.urlopen(url)
	html=response.read()
	soup=BeautifulSoup(html,"html.parser")
	location=soup.find('h3',{"class":"user-location alternate"})
	area = location.getText()	
	print(area)
		
	(long2, lat2) = cord(area)

	dist = hav(long1, lat1, long2, lat2)
	distance_value.append(dist)
		

close_connection(cursor, connection)

string = "{\"dist_var\" : ["
for i in range(0, len(user_id_arr)):
	string += "{"+str(user_id_arr[i])+" : "+str(distance_value[i])+" }"
	if(i != len(user_id_arr) - 1):
		string += ","

string+= "]}"


temp = json.loads(string)

print(temp)




