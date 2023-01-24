import pymysql
from flask import Flask
import json
# เชื่อมต่อกับฐานข้อมูล MySQL
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='test'
)
# เรียก Flask มาใช้
app = Flask(__name__)
# สร้าง cursor เพื่อใช้ในการเรียกข้อมูลจากฐานข้อมูล โดยขอข้อมูลเป็น Dictionary
# ใช้ข้อมูล JSON
# get
@app.route('/get')
def index():
  conn.connect()
  cursor = conn.cursor(pymysql.cursors.DictCursor) 
  sql = "SELECT * FROM user"
  cursor.execute(sql)
  data = cursor.fetchall()
  j = []
  for d in data:
    j.append(d) 
  conn.close()
  return j
#insert
@app.route('/insert')
def insert():
  conn.connect()
  cursor = conn.cursor(pymysql.cursors.DictCursor) 
  json_d = {"test":"insert data json","name":"test"}
  sql = f"INSERT INTO `user`(`data`) VALUES ('{json.dumps(json_d)}')"
  cursor.execute(sql)
  conn.commit()
  conn.close()
  return f"insert {json_d} success"
#update
@app.route('/update')
def update():
  conn.connect()
  cursor = conn.cursor(pymysql.cursors.DictCursor) 
  json_update = {"update":"update test data json","name":"update"}
  id = 3
  sql = f"UPDATE `user` SET `data`='{json.dumps(json_update)}' WHERE `u_id` = {id}"
  cursor.execute(sql)
  conn.commit()
  conn.close()
  return f"update {id} sucess"
#delete
@app.route('/delete')
def delete():
  conn.connect()
  cursor = conn.cursor(pymysql.cursors.DictCursor) 
  id = 3
  sql = f"DELETE FROM `user` WHERE `u_id` = {id}"
  cursor.execute(sql)
  conn.commit()
  conn.close()
  return f"delete id : {id} success"




if __name__=="__main__":
  app.run(port=2000,debug=True)
# ปิดการเชื่อมต่อ
