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
data_file = open('user.json',"r")

connection, cursor = create_connection()
	
for line in data_file:

	
	data=json.loads(line.strip())
	user_id = data['user_id']
	name = data['name']
	review_count = data['review_count']
	yelping_since = data['yelping_since']
	useful = data['useful']
	funny = data['funny']
	cool = data['cool']
	fans = data['fans']
	elite_count = len(data['elite'])
	average_stars = data['average_stars']
	compliment_profile = data['compliment_profile']
	compliment_writer = data['compliment_writer']
	
	try:
		query = ''' INSERT IGNORE INTO user(user_id, name, review_count, yelping_since, useful, funny, cool, fans, elite_count, average_stars, compliment_profile, compliment_writer) VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)'''
		cursor.execute(query, (user_id, name, review_count, yelping_since, useful, funny, cool, fans, elite_count, average_stars, compliment_profile, compliment_writer))
		cursor.execute("select count(*) from user")
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
