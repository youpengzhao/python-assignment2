import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from sqlite_2 import Result
import sqlite3
import numpy as np

def paint():
    conn = sqlite3.connect('value.db')                   # 与数据库文件建立链接
    cursor = conn.cursor()
    cursor.execute('select * from value')
    value = cursor.fetchall()    # 读取出文件中表格的数据
    pie = []
    year = []
    year1 = []
    one = []
    two = []
    three = []
    totalincome = []
    totalout = []
    ave = []
    for i in range(3, 6):                 # 将表格中数据写入数组并适当处理
        pie.append(value[0][i]/value[0][2])
    for i in range(3):
        pie[i] = round(pie[i], 3)
    for i in range(1, 21):
        year.append(value[20-i][0])
        one.append(value[20-i][3])
        two.append(value[20 - i][4])
        three.append(value[20 - i][5])
    for i in range(10, 20):
        totalincome.append(value[20-i][1]/10)
        totalout.append(value[20-i][2]/10)
        ave.append(value[20-i][6])
        year1.append(1998+i)

    fig = plt.figure(figsize=(12, 8))                # 设置图像参数，这里设置出三张子图
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,1,2)
    plt.rcParams['font.sans-serif'] = ['SimHei']

    labels1 = ['第一产业', '第二产业', '第三产业']              # 第一张饼状图，绘制2018年数据
    colors = ['red', 'yellow', 'pink']
    ax1.axis(aspect='equal')
    ax1.pie(pie, labels=labels1, colors=colors, radius=1.2, labeldistance=0.4, pctdistance=0.8, autopct='%.3f%%')
    ax1.set_title('2018年三类产业增加值占国内生产总值百分比（%）')

    ax2.plot(year1, totalincome, 'or-', label=u'国民总收入')                # 2008-2018年的数据，用折线图
    ax2.plot(year1, totalout, 'or-', label=u'国内生产总值', color='blue')
    ax2.plot(year1, ave, 'or-', label=u'人均国内生产总值',color='green')
    ax2.grid(color='y', linestyle='--', linewidth=1, alpha=0.3)                 # 设置网格，增强美观效果
    ax2.legend()
    ax2.set_ylabel('国民总收入和GDP（十亿元)人均生产总值(元)',fontproperties="STKaiti")
    ax2.set_title('2008-2018年国民总收入，GDP和人均生产总值')
    plt.ylim([30000,85000])

    ax3.bar(np.arange(20), one, label='第一产业', color='steelblue', alpha=0.8, width=0.3)         # 绘制条形图
    ax3.bar(np.arange(20) + 0.3, two, label='第二产业', color='indianred', alpha=0.8, width=0.3)    # 每个横坐标有三样数据，依次平移
    ax3.bar(np.arange(20)+0.6, three, label='第三产业', color='green', alpha=0.8, width=0.3)
    plt.ylabel('三类产业增加值（亿元）')
    plt.title('1999-2018年度国内三类产业增加值', fontproperties="YouYuan")
    plt.xticks(np.arange(20)+0.3, year)
    plt.ylim([10000, 485000])
    for x, y in enumerate(one):               # 数组显示在条形上
        plt.text(x, y + 100, '%s' % int(y), ha='center', fontsize=7)
    for x, y in enumerate(two):               # 数组显示在条形上
        plt.text(x+0.3, y + 10000, '%s' % int(y), ha='center', fontsize=7,weight='bold')
    for x, y in enumerate(three):               # 数组显示在条形上
        plt.text(x+0.6, y + 100, '%s' % int(y), ha='center', fontsize=7)
    plt.legend(loc='upper left')

    plt.show()


if __name__ == '__main__':
    paint()
