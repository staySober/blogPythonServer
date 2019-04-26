import datetime
# 1.把datetime转成字符串
def datetime_toString(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")

# 2.把字符串转成datetime
def string_toDatetime(st):
    datetime.datetime.strptime(st, "%Y-%m-%d %H:%M:%S")