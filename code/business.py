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
data_file = open('business.json',"r")

connection, cursor = create_connection()
	
for line in data_file:

	
	data=json.loads(line.strip())
	
	business_id = data['business_id']
	name = data['name']
	address = data['address']
	city = data['city']
	state = data['state']
	stars = data['stars']
	review_count = data['review_count']	

	
	try:
		query = ''' INSERT IGNORE INTO business(business_id, name, address, city, state, stars, review_count) VALUES (%s, %s, %s, %s, %s, %s,%s)'''
		cursor.execute(query, (business_id, name, address, city, state, stars, review_count))
		cursor.execute("select count(*) from business")
		row = cursor.fetchall()
		for row_count in row:
			row_count = str(row_count)[1:len(row_count)-4]
			row_count = int(row_count)
			count = row_count

	except:
		pass
	

	print(count)
	
	if(count == 100000):
		break	

close_connection(cursor, connection)
