# coding: utf-8
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    # 连接数据库
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='qidong70824.',
        charset="utf8",
        db='university',
    )
def dep():
    datas = []
    lists = []
    with open('/home/kynton/下载/MySQL上课文件/作业/university/department.txt', 'r') as f:
        for lines in f.readlines():
            result = lines.decode('utf-8').strip().split(" ")
            for line in result:
                lists.append(line)
            datas.append(lists)
            lists = []
    cur = conn.cursor()
    for d in datas:
        sql_query = "insert into department(dept_name, building, budget) values('%s', '%s', '%s')" %(d[0], d[1], d[2])
        cur.execute(sql_query)
        conn.commit()
def exm():
    datas = []
    lists = []
    with open('/home/kynton/下载/MySQL上课文件/作业/university/exam.txt', 'r') as f:
        for lines in f.readlines():
            result = lines.decode('utf-8').strip().split(" ")
            result[0] = int(result[0])
            for line in result:
                lists.append(line)
            datas.append(lists)
            lists = []
    cur = conn.cursor()
    for d in datas:
        sql_query = "insert into exam(student_ID, exam_name, grade) values(%d, '%s', '%s')" % (d[0], d[1], d[2])
        cur.execute(sql_query)
        conn.commit()
def stu():
    datas = []
    lists = []
    with open('/home/kynton/下载/MySQL上课文件/作业/university/student.txt', 'r') as f:
        for lines in f.readlines():
            result = lines.decode('utf-8').strip().split(" ")
            result[0] = int(result[0])
            result[3] = int(result[3])
            for line in result:
                lists.append(line)
            datas.append(lists)
            lists = []
    cur = conn.cursor()
    for d in datas:
        sql_query = "insert into student(ID, name, sex, age, emotion_state, dept_name) values(%d, '%s', '%s', %d, '%s', '%s')" % (d[0], d[1], d[2], d[3], d[4], d[5])
        cur.execute(sql_query)
        conn.commit()
dep()
stu()
exm()
