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
flag = 0
connection, cursor = create_connection()

for line in data_file:

	
	data=json.loads(line.strip())
	user_id = data['user_id']

	friends = data['friends']
	for friend in friends:

		try:
			query = ''' INSERT IGNORE INTO friend(user_id, friend_id) VALUES (%s, %s)'''
			cursor.execute(query, (user_id, friend))
			cursor.execute("select count(*) from friend")
			row = cursor.fetchall()
			for row_count in row:
				row_count = str(row_count)[1:len(row_count)-4]
				row_count = int(row_count)
				count = row_count
			print(count)
	
			if(count >= 100000):
				flag  =1
				break
		except:
			pass
		print('flag == ' + str(flag))
	if(flag == 1):
		break

	

			

close_connection(cursor, connection)
