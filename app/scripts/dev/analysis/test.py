import json
#import MySQLdb as mysql

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

'''
count=0
user_location = []
business_location = []
distance_value = []
'''
#connection, cursor = create_connection()

business_idArr = []
'''
crop = 0 
flag = 0
'''
id1 = ''

idx = raw_input()
business_idArr.append(idx)

for businessID in business_idArr:
	id1 = businessID

	json_str = json.dumps(
		{

		"variation" : [
				{"2008" : 6}, 
				{"2009": 6}, 
				{"2010" : 6}, 
				{"2011" : 6}, 
				{"2012" : 6}, 
				{"2013" : 6}, 
				{"2014" : 6}, 
				{"2015" : 5}, 
				{"2016": 4}, 
				{"2017" : 6}
			]
		})

	print(json_str)

	break

	'''cursor.execute("select r.date, r.stars from review as r where r.business_id = '" + businessID + "'")
	row = cursor.fetchall()


	data08 = []
	data09 = []
	data10 = []
	data11 = []
	data12 = []
	data13 = []
	data14 = []
	data15 = []
	data16 = []
	data17 = []
	
	dataRating08 = []
	dataRating09 = []
	dataRating10 = []
	dataRating11 = []
	dataRating12 = []
	dataRating13 = []
	dataRating14 = []
	dataRating15 = []
	dataRating16 = []
	dataRating17 = []

	dict = {}
	dict_total_rating = {}

	


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
	if(crop == 0):
		crop = 1
		if('2008' in dict):
			data08.append(dict['2008'])
		else:
			data08.append(0)

		if('2009' in dict):
			data09.append(dict['2009'])
		else:
			data09.append(0)


		if('2010' in dict):
			data10.append(dict['2010'])
		else:
			data10.append(0)


		if('2011' in dict):
			data11.append(dict['2011'])
		else:
			data11.append(0)


		if('2012' in dict):
			data12.append(dict['2012'])
		else:
			data12.append(0)

		if('2013' in dict):
			data13.append(dict['2013'])
		else:
			data13.append(0)



		if('2014' in dict):
			data14.append(dict['2014'])
		else:
			data14.append(0)


		if('2015' in dict):
			data15.append(dict['2015'])
		else:
			data15.append(0)


		if('2016' in dict):
			data16.append(dict['2016'])
		else:
			data16.append(0)


		if('2017' in dict):
			data17.append(dict['2017'])
		else:
			data17.append(0)


	#################################################################

		if('2008' in dict_total_rating):
			dataRating08.append(dict_total_rating['2008'])
		else:
			dataRating08.append(0)

		if('2009' in dict_total_rating):
			dataRating09.append(dict_total_rating['2009'])
		else:
			dataRating09.append(0)


		if('2010' in dict_total_rating):
			dataRating10.append(dict_total_rating['2010'])
		else:
			dataRating10.append(0)


		if('2011' in dict_total_rating):
			dataRating11.append(dict_total_rating['2011'])
		else:
			dataRating11.append(0)


		if('2012' in dict_total_rating):
			dataRating12.append(dict_total_rating['2012'])
		else:
			dataRating12.append(0)

		if('2013' in dict_total_rating):
			dataRating13.append(dict_total_rating['2013'])
		else:
			dataRating13.append(0)



		if('2014' in dict_total_rating):
			dataRating14.append(dict_total_rating['2014'])
		else:
			dataRating14.append(0)


		if('2015' in dict_total_rating):
			dataRating15.append(dict_total_rating['2015'])
		else:
			dataRating15.append(0)


		if('2016' in dict_total_rating):
			dataRating16.append(dict_total_rating['2016'])
		else:
			dataRating16.append(0)


		if('2017' in dict_total_rating):
			dataRating17.append(dict_total_rating['2017'])
		else:
			dataRating17.append(0)

#######################################################################################3
		for i in range(0, len(data08)):
			total_reviews = float(data08[i])
			if(total_reviews != 0):
				dataRating08[i] = dataRating08[i]/total_reviews

		for i in range(0, len(data09)):
			total_reviews = float(data09[i])
			if(total_reviews != 0):
				dataRating09[i] = dataRating09[i]/total_reviews
	
		for i in range(0, len(data10)):
			total_reviews = float(data10[i])
			if(total_reviews != 0):
				dataRating10[i] = dataRating10[i]/total_reviews
	
		for i in range(0, len(data11)):
			total_reviews = float(data11[i])
			if(total_reviews != 0):
				dataRating11[i] = dataRating11[i]/total_reviews
	
		for i in range(0, len(data12)):
			total_reviews = float(data12[i])
			if(total_reviews != 0):
				dataRating12[i] = dataRating12[i]/total_reviews
	
		for i in range(0, len(data13)):
			total_reviews = float(data13[i])
			if(total_reviews != 0):
				dataRating13[i] = dataRating13[i]/total_reviews
	
		for i in range(0, len(data14)):
			total_reviews = float(data14[i])
			if(total_reviews != 0):
				dataRating14[i] = dataRating14[i]/total_reviews
	
		for i in range(0, len(data15)):
			total_reviews = float(data15[i])
			if(total_reviews != 0):
				dataRating15[i] = dataRating15[i]/total_reviews
	
		for i in range(0, len(data16)):
			total_reviews = float(data16[i])
			if(total_reviews != 0):
				dataRating16[i] = dataRating16[i]/total_reviews
	
		for i in range(0, len(data17)):
			total_reviews = float(data17[i])
			if(total_reviews != 0):
				dataRating17[i] = dataRating17[i]/total_reviews

		output_array = []
		output_array.append(dataRating08[0])
		output_array.append(dataRating09[0])
		output_array.append(dataRating10[0])
		output_array.append(dataRating11[0])
		output_array.append(dataRating12[0])
		output_array.append(dataRating13[0])
		output_array.append(dataRating14[0])
		output_array.append(dataRating15[0])
		output_array.append(dataRating16[0])
		output_array.append(dataRating17[0])
'''		

		

#close_connection(cursor, connection)
