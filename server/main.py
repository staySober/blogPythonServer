from flask import Flask, jsonify, request, make_response
import pymysql
import json
from app import createApp, db

# 创建app
app = createApp('developement')

# 拉去所有博客
@app.route('/getInfo', methods=["GET","POST"])
def fetchBlog():
    # 使用 cursor() 方法创建一个游标对象 cursor
    sql = "select * from blog"
    cursor = db.cursor()
    cursor.execute(sql)

    # 遍历结果集
    result = cursor.fetchall()
    for row in result:
        for i in row:
            print(i)
        print(row)
    
    resp =  make_response(jsonify(result))
    resp.status = "200"
    resp.headers["Content-type"] = "application/json"   #  通过字典的形式设置响应头
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)