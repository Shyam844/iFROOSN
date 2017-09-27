import json
import MySQLdb as mysql


host = 'localhost'
user = 'root'
password = '****'
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
data_file = open('review.json',"r")

connection, cursor = create_connection()
	
for line in data_file:

	
	data=json.loads(line.strip())
	review_id = data['review_id']
	user_id = data['user_id']
	business_id = data['business_id']
	stars = data['stars']
	datex = data['date']
	text = data['text']
	useful = data['useful']
	funny = data['funny']
	cool = data['cool']

	
	try:
		query = ''' INSERT IGNORE INTO review(review_id, user_id, business_id, stars, date, text, useful, funny, cool) VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s)'''
		cursor.execute(query, (review_id, user_id, business_id, stars, datex, text, useful, funny, cool))
	except:
		pass
	

	print(count)
	count += 1 
	if(count == 100000):
		break	

close_connection(cursor, connection)
