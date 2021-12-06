import sqlite3

monday={"my home" : 'is here'}
tuesday={'is here' : 'all my life'}
wednesday = {}
thursday = {}
friday = {}
saturday = {}
sunday = {}

print(monday)
print(monday == '' or tuesday == '')

def test():
    global monday, tuesday, wednesday, thursday, friday, saturday, sunday
    if monday=='' or tuesday=='' or wednesday=='' or thursday=='' or friday=='' or saturday=='' or sunday=='':
        print('they are empty!')
    else:
        print('they are not empty!')

test()



lesson = {'lessons' : ['22:00', '22:40']}

print(lesson['lessons'][1])

connect = sqlite3.connect('tests.db')
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS test(
    id INTEGER,
    date VARCHAR,
    start VARCHAR,
    end VARCHAR    
)""")

usersid = 222
weekday = 'monday'
starts = '11:00'
ends = '11:40'
cursor.execute("INSERT INTO test VALUES (?, ?, ?, ?);", (usersid, weekday, starts, ends))
connect.commit()

usersid = 220
weekday = 'monday'
starts = '11:30'
ends = '12:10'
cursor.execute("INSERT INTO test VALUES (?, ?, ?, ?);", (usersid, weekday, starts, ends))
connect.commit()


cursor.execute(f"SELECT * FROM test")
data = cursor.fetchall()
print(data)