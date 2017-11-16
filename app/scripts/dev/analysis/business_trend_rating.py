import json
import MySQLdb as mysql

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


connection, cursor = create_connection()




idx = raw_input()


cursor.execute("select date, stars from review where business_id = '" + idx + "';")
row = cursor.fetchall()

dict = {}
dict_total_rating = {}
data = []
dataRating = []

for rating in row:
	cursor_row = str(rating)
	temp = cursor_row.split(", ")

	time = str(temp[0])
	time = time[2:len(time) - 1]
	yr = time.split("-")[0]
	star = int(temp[1][1:len(temp[1]) - 2])
	#print(yr +"   " +str(star))
	if(yr in dict):
		dict[yr] += 1
	else:
		dict[yr] = 1

	if(yr in dict_total_rating):
		dict_total_rating[yr] += star
	else:
		dict_total_rating[yr] = star

	###############################################################################################
if('2008' in dict):
	data.append(dict['2008'])
else:
	data.append(0)

if('2009' in dict):
	data.append(dict['2009'])
else:
	data.append(0)


if('2010' in dict):
	data.append(dict['2010'])
else:
	data.append(0)


if('2011' in dict):
	data.append(dict['2011'])
else:
	data.append(0)


if('2012' in dict):
	data.append(dict['2012'])
else:
	data.append(0)

if('2013' in dict):
	data.append(dict['2013'])
else:
	data.append(0)


if('2014' in dict):
	data.append(dict['2014'])
else:
	data.append(0)


if('2015' in dict):
	data.append(dict['2015'])
else:
	data.append(0)


if('2016' in dict):
	data.append(dict['2016'])
else:
	data.append(0)


if('2017' in dict):
	data.append(dict['2017'])
else:
	data.append(0)


#################################################################

if('2008' in dict_total_rating):
	dataRating.append(dict_total_rating['2008'])
else:
	dataRating.append(0)

if('2009' in dict_total_rating):
	dataRating.append(dict_total_rating['2009'])
else:
	dataRating.append(0)


if('2010' in dict_total_rating):
	dataRating.append(dict_total_rating['2010'])
else:
	dataRating.append(0)


if('2011' in dict_total_rating):
	dataRating.append(dict_total_rating['2011'])
else:
	dataRating.append(0)


if('2012' in dict_total_rating):
	dataRating.append(dict_total_rating['2012'])
else:
	dataRating.append(0)

if('2013' in dict_total_rating):
	dataRating.append(dict_total_rating['2013'])
else:
	dataRating.append(0)


if('2014' in dict_total_rating):
	dataRating.append(dict_total_rating['2014'])
else:
	dataRating.append(0)


if('2015' in dict_total_rating):
	dataRating.append(dict_total_rating['2015'])
else:
	dataRating.append(0)


if('2016' in dict_total_rating):
	dataRating.append(dict_total_rating['2016'])
else:
	dataRating.append(0)


if('2017' in dict_total_rating):
	dataRating.append(dict_total_rating['2017'])
else:
	dataRating.append(0)

#######################################################################################3

for i in range(0, len(data)):
	total_reviews = float(data[i])
	if(total_reviews != 0):
		dataRating[i] = dataRating[i]/total_reviews



close_connection(cursor, connection)



string = "{\"total_reviews\" : ["

string+= "{\"2008\" : "+str(data[0])+"}, "
string+= "{\"2009\" : "+str(data[1])+"}, "
string+= "{\"2010\" : "+str(data[2])+"}, "
string+= "{\"2011\" : "+str(data[3])+"}, "
string+= "{\"2012\" : "+str(data[4])+"}, "
string+= "{\"2013\" : "+str(data[5])+"}, "
string+= "{\"2014\" : "+str(data[6])+"}, "
string+= "{\"2015\" : "+str(data[7])+"}, "
string+= "{\"2016\" : "+str(data[8])+"}, "
string+= "{\"2017\" : "+str(data[9])+"} "

string+= "], "
string += "\"avg_rating_review\" : ["

string+= "{\"2008\" : "+str(dataRating[0])+"}, "
string+= "{\"2009\" : "+str(dataRating[1])+"}, "
string+= "{\"2010\" : "+str(dataRating[2])+"}, "
string+= "{\"2011\" : "+str(dataRating[3])+"}, "
string+= "{\"2012\" : "+str(dataRating[4])+"}, "
string+= "{\"2013\" : "+str(dataRating[5])+"}, "
string+= "{\"2014\" : "+str(dataRating[6])+"}, "
string+= "{\"2015\" : "+str(dataRating[7])+"}, "
string+= "{\"2016\" : "+str(dataRating[8])+"}, "
string+= "{\"2017\" : "+str(dataRating[9])+"} "

string += "]}"


temp = json.loads(string)

print(temp)