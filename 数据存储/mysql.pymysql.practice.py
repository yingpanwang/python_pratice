import pymysql
import random

dbName = 'python_practice'


def create_db(cursor):
    cursor.execute(f'create database if not exists {dbName}')
    cursor.execute(f'use {dbName}')


def create_table(cursor):
    sql = '''
    create table if not exists students(
        id int not null,
        name varchar(10) not null,
        age int not null,
        primary key (id)
    )
    '''
    cursor.execute(sql)


def insert(db):

    id = random.randint(0, 9999)
    name = f'www+{random.randint(0, 9999)}'
    age = random.randint(1, 99)

    sql = f'insert into students (id,name,age) values({id},\'{name}\',{age});'
    try:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


def update(db):

    sql = 'update students set name = %s where id = %s'
    try:
        cursor = db.cursor()
        cursor.execute(sql, ('我是更新的数据', 1))
        db.commit()
    except BaseException as e:
        print(e)
        db.rollback()


def query(db):

    sql = 'select * from students;'
    cursor = db.cursor()
    cursor.execute(sql)
    print('查询到 {rowcount} 条数据'.format(rowcount=cursor.rowcount))
    data = cursor.fetchall()
    for row in data:
        print(row)


# 建立连接
db = pymysql.connect(host='localhost', user='root',
                     password='root', port=3306)

# 获取游标
cursor = db.cursor()
# # 执行sql
# cursor.execute('select Version()')
# # 获取数据
# data = cursor.fetchone()
# print(data)

create_db(cursor)

create_table(cursor)

for i in range(99):
    insert(db)

update(db)

query(db)

db.close()
