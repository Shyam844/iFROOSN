import json
import MySQLdb as mysql
import matplotlib.pyplot as plt


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


count=0

connection, cursor = create_connection()

cursor.execute("select business_id, review_count from business")
data = cursor.fetchall()

ids = []
counter = []

for idx in data:
	value = str(idx)
	value = value[1:len(value)-1]
	temp = value.split(', ')

	business_id = temp[0][1:len(temp[0]) -1]
	review_count = temp[1][1:len(temp[1]) -1]
	print("count = " + str(count))
	if(int(review_count) >= 3500):
		print(business_id)
		ids.append(business_id)
		counter.append(int(review_count))
		

	if(count == 100002):
		break
	count += 1


print(ids)
print(counter)



for business_id in ids:
	print(business_id)
	dict = {}
	cursor.execute("select r.date from review as r where r.business_id = '" + business_id +"';");
	data = cursor.fetchall()
	cursor.execute("select count(*) from review where business_id = '" + business_id +"';");
	row = cursor.fetchall()
	row_number = 0
	for i in row:
		temp = str(i)
		row_number = int(temp[1:len(temp)-3])
		print(row_number)

	if(row_number > 0):
		minv = 0
		maxv = 2050
		cap = 0
		for time in data:
			date_fetched = str(time)
			date_fetched = date_fetched[2: (len(date_fetched) - 3)]
			print(date_fetched)
			temp = date_fetched.split('-')
			year = int(temp[0])
			month = int(temp[1])
			if(cap == 0):
				minv = year
			cap = 1

			if(year < minv):
				minv = year
			if(year > maxv):
				maxv = year
			rep = 0
			if(month <= 6):
				rep = 1
			else:
				rep = 2
		
			indicator =  str(year) + "_" + str(rep)
			if(indicator in dict):
				dict[indicator] += 1
			else:
				dict[indicator] = 1
		print(dict)
		
		yearly = []
		frequency = []

		for key in dict:
			yearly.append(key)
			frequency.append(dict[key])
		print(yearly)
		print(frequency)

		plt.figure(figsize=(90,60))
		plt.bar(range(len(frequency)), frequency, align ='edge', width = 0.85, edgecolor='black', facecolor ='purple')
		plt.xticks(range(len(yearly)), yearly, rotation = 30)
		plt.xlabel('Year')
		plt.ylabel('Frequency')
		plt.title('Number of reviews of a business vs time')
		plt.show()

	print('\n\n')

close_connection(cursor, connection)

