import sqlite3
from Crawler import request


class Result():
    def __init__(self):
        super().__init__()
        self.year = []                # 存放数据的四个list
        self.total = []
        self.male = []
        self.female = []
        self.conn = sqlite3.connect('popularity.db')              # 与数据库文件建立链接

    def getvalue(self):
        res = request()                    # 爬取数据
        for i in range(20):                  # 从爬到的数据中获取需要的
            self.year.append(2018-i)
            self.total.append(res['returndata']['datanodes'][i]['data']['data'])
            self.male.append(res['returndata']['datanodes'][i+20]['data']['data'])
            self.female.append(res['returndata']['datanodes'][i+40]['data']['data'])

        self.male[8] = int(self.male[8]+0.5)              # 男女人口中有两个数据是浮点型，但网站上是整型，这里将其转化为整型
        self.male[9] = int(self.male[9]+0.5)
        self.female[8] = int(self.female[8] + 0.5)
        self.female[9] = int(self.female[9] + 0.5)

    def database(self):
        cursor = self.conn.cursor()                     # 建立游标
        try:                        # 建立表格并插入数据，如果已存在则提示，表格中数据已存在则提示
            cursor.execute('create table popularity(year int PRIMARY KEY,total int,male int,female int)')
            for j in range(20):                       # 以年份为主值，将数据插入表格
                spl = 'insert into popularity(year,total,male,female) values(%d,%d,%d,%d)' % (
                self.year[j], self.total[j], \
                self.male[j], self.female[j])
                cursor.execute(spl)
            self.conn.commit()
        except Exception as OperationalError:
            print("表格已存在\n")
        except Exception as IntegrityError:
            print("数据已存在于表格中\n")
        finally:              # 将表格中数据显示出来
            cursor.execute('select * from popularity')
            print(cursor.fetchall())
            self.conn.close()

    def deletedata(self):                # 删除表格，如不存在，则提示
        try:
            self.conn.execute('drop table popularity')
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

