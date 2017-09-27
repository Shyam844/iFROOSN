import json
import MySQLdb as mysql
import matplotlib.pyplot as plt

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

connection, cursor = create_connection()

cursor.execute("select review_id, user_id, stars, useful from review")
data = cursor.fetchall()
arr = []
deviation_arr = []
for idx in data:
	value = str(idx)
	value = value[1:len(value)-1]
	temp = value.split(', ')
	review_id = temp[0][1:len(temp[0])-1]
	user_id = temp[1][1:len(temp[1]) - 1]
	stars = temp[2][1:len(temp[2]) - 1]
	useful = temp[3][1:len(temp[3]) - 1]
	#print(stars)

	cursor.execute("select average_stars from user where user_id = '" + user_id + "'")
	rows = cursor.fetchall()
	post = 0
	for row in rows:
		post = 1
		row = str(row)
		average_stars = row[2:len(row) - 3]
		#print(average_stars)

	if(post == 1):
		deviation = int(stars) - float(average_stars)
		if(deviation < 0):
			deviation = -(deviation)
		#print(deviation)
		#print('\n\n')
	
	if(deviation >= 3.2):
		print(deviation)
		print(user_id)
		deviation_arr.append(deviation)
		arr.append(useful)

	if(count == 10000):
		break
	count += 1
	
close_connection(cursor, connection)

print(deviation_arr)
print(arr)


plt.figure(figsize=(120,80))
plt.bar(range(len(arr)), arr, align ='edge', width = 0.55, edgecolor='black', facecolor ='green')
plt.xticks(range(len(deviation_arr)), deviation_arr, rotation = 30)
plt.xlabel('Deviation')
plt.ylabel('Frequency')
plt.title('Variation of useful feature with deviation')
plt.show()
