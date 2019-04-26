from flask import Flask, jsonify, request, make_response
import pymysql
import json
from app import createApp, mysql
import util

# 创建app
app = createApp()

# 拉取所有博客
@app.route('/fetchBlog', methods=["GET","POST"])
def fetchBlog():
    db = mysql.connect()
    # 使用 cursor() 方法创建一个游标对象 cursor
    sql = "select * from blog"
    cursor = db.cursor()
    cursor.execute(sql)

    # 遍历结果集
    result = cursor.fetchall()

    finalResult = []
    for row in result:
        blog = {}
        blog['id'] = row[0]
        blog['title'] = row[1]
        blog['content'] = row[2]
        finalResult.append(blog)
    
    resp =  make_response(jsonify(finalResult))
    resp.status = "200"
    resp.headers["Content-type"] = "application/json"   #  通过字典的形式设置响应头
    return resp


# 根据ID拉去博客内容
@app.route('/fetchBlogById', methods=["POST"])
def fetchBlogById():
    # 获取请求中的参数ID
    data = request.get_json()
    id = data['id']

    db = mysql.connect()
    # 使用 cursor() 方法创建一个游标对象 cursor
    sql = "select * from blog where id = '{}'".format(id)
    cursor = db.cursor()
    cursor.execute(sql)

    # 遍历结果集
    result = cursor.fetchone()

    blog = {}
    blog['id'] = result[0]
    blog['title'] = result[1]
    blog['content'] = result[2]
    blog['createTime'] = result[4]
    blog['type'] = result[3]
    blog['updateTime'] = result[5]
   
    
    resp =  make_response(jsonify(blog))
    resp.status = "200"
    resp.headers["Content-type"] = "application/json"   #  通过字典的形式设置响应头
    return resp

# 获取文章类型
@app.route('/getBlogType', methods=['GET','POST'])
def getBlogType():
    db = mysql.connect()
    sql = "select distinct type from blog"
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    finalResult = []
    for row in result:
        #finalResult.append(row[0])
        titles = getBlogTitleByType2(row[0])

        titleObj ={}
        titleObj['name'] = row[0]
        titleObj['subTtile'] = titles
        finalResult.append(titleObj)

    resp =  make_response(jsonify(finalResult))
    resp.status = "200"
    resp.headers["Content-type"] = "application/json"   #  通过字典的形式设置响应头
    return resp

def getBlogTitleByType2(type):
    db = mysql.connect()
    sql = "select id, title from blog where type = '{}' ".format(type)
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    finalResult = []
    for row in result:
        data = {}
        data['id'] = row[0]
        data['title'] = row[1]
        finalResult.append(data)
    return finalResult

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)