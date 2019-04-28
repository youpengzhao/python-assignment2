import sqlite3
from crawler2 import request


class Result():
    def __init__(self):
        super().__init__()
        self.year = []                # 存放数据的四个list
        self.totalincome = []
        self.totalout = []
        self.one = []
        self.two = []
        self.three = []
        self.ave = []
        self.conn = sqlite3.connect('value.db')              # 与数据库文件建立链接

    def getvalue(self):
        res = request()                    # 爬取数据
        for i in range(20):                  # 从爬到的数据中获取需要的
            self.year.append(2018-i)
            self.totalincome.append(res['returndata']['datanodes'][i]['data']['data'])
            self.totalout.append(res['returndata']['datanodes'][i+20]['data']['data'])
            self.one.append(res['returndata']['datanodes'][i+40]['data']['data'])
            self.two.append(res['returndata']['datanodes'][i + 60]['data']['data'])
            self.three.append(res['returndata']['datanodes'][i + 80]['data']['data'])
            self.ave.append(res['returndata']['datanodes'][i + 100]['data']['data'])

    def database(self):
        cursor = self.conn.cursor()                     # 建立游标
        try:                        # 建立表格并插入数据，如果已存在则提示，表格中数据已存在则提示
            cursor.execute('create table value(year int PRIMARY KEY,totalincome float,totalout float\
            ,one float,two float,three float,ave float)')
            for j in range(20):                       # 以年份为主值，将数据插入表格
                spl = 'insert into value(year,totalincome,totalout,one,two,three,ave) values(%d,%f,%f,%f,%f,%f,\
                %f)'% (self.year[j], self.totalincome[j], self.totalout[j],self.one[j],self.two[j],self.three[j]\
                ,self.ave[j])
                cursor.execute(spl)
            self.conn.commit()
        except Exception as OperationalError:
            print("表格已存在\n")
        except Exception as IntegrityError:
            print("数据已存在于表格中\n")
        finally:              # 将表格中数据显示出来
            cursor.execute('select * from value')
            print(cursor.fetchall())
            self.conn.close()

    def deletedata(self):                # 删除表格，如不存在，则提示
        try:
            self.conn.execute('drop table value')
        except Exception as OperationalError:
            print('表格不存在\n')


def main():
    result = Result()
    a = int(input('直接利用数据库数据绘图输入1，重新爬取数据并绘图输入2：'))
    if a is 2:
        result.deletedata()
        result.getvalue()
        result.database()
    else:
        result.database()


if __name__ == '__main__':
    main()
