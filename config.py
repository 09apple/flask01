import pymysql.cursors
from werkzeug.security import generate_password_hash, check_password_hash


connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='demo',
    charset='utf8'
)

def sreach():
    cursor = connect.cursor()
    str = '阿斯顿'
    #sql = "INSERT INTO users (username) VALUES ( '阿斯顿' )"
    #sql = "alter table users add COLUMN password varchar(64)"
    sql = "select * from users where id =3"
    cursor.execute(sql)
    #for row in cursor.fetchall():
     #   print(row)

    #connect.commit()
    #print('成功插入', cursor.rowcount, '条数据')
    return cursor.fetchall()


def setpass():
    password_hash = generate_password_hash('123123')

    cursor = connect.cursor()
    sql = "UPDATE users SET pwd = \'{}' WHERE id = 3 ".format(password_hash)
    cursor.execute(sql)
    print("!!!", cursor.rowcount)


setpass()

something = input("输入密码:")

for i in sreach():
    print('！！！')
    if check_password_hash(i[3], something):
        print('正确！！！')
        break

    print('错误！！！')

