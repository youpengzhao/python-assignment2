import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from sqlite_1 import Result
import sqlite3


def paint():
    conn = sqlite3.connect('popularity.db')                   # 与数据库文件建立链接
    cursor = conn.cursor()
    cursor.execute('select * from popularity')
    value = cursor.fetchall()                   # 读取出文件中表格的数据
    year = []
    male = []
    female = []
    total = []
    for j in range(1, 21):                       # 这里按年份升序排列，故而在四个list从上面value中读取数据时就对顺序进行调整
        year.append(value[20-j][0])
        total.append(value[20-j][1])
        male.append(value[20-j][2])
        female.append(value[20-j][3])
    for i in range(20):                          # 将男性和女性人口处理成占总人口的百分数，保留两位小数
        male[i] = round((male[i]/total[i])*100, 2)
        female[i] = round((female[i]/total[i])*100, 2)

    plt.rcParams['font.sans-serif'] = ['SimHei']                # 用来正常显示中文标签
    fig = plt.figure(num=1, figsize=(12, 6), facecolor=(0.75, 1, 0.75))            # 设置界面的一些属性
    fmt = '%.2f%%'
    yticks = mtick.FormatStrFormatter(fmt)  # 设置百分比形式的坐标轴
    ax1 = fig.add_subplot(111)                                              # 绘制男女人口百分比的折线图
    ax1.plot(range(20), male, 'or-', label=u'男性人口占比')
    ax1.yaxis.set_major_formatter(yticks)
    ax1.plot(range(20), female, 'or-', label=u'女性人口占比', color='green')
    for x, y in enumerate(male):
        plt.text(x, y+0.1, '%s' % round(y, 2), ha='center', color='black', fontsize=10)  # 将百分比数值显示在图形上
    for x, y in enumerate(female):
        plt.text(x, y+0.1, '%s' % round(y, 2), ha='center', color='black', fontsize=10)  # 将百分比数值显示在图形上
    ax1.legend(loc=1)                         # 图例显示的位置
    ax1.set_ylim([48, 51.8])               # 折线轴的范围
    ax1.set_ylabel('男女人口占比（%）', fontproperties="STKaiti", fontsize=16)            # 折线轴的文字显示

    ax2 = ax1.twinx()                      # 将总人口条形图绘制在一起
    plt.bar(range(20), total, align='center', color='steelblue', alpha=0.3)        # 设置条形图的属性
    plt.ylabel('总人口（万）', fontproperties="STKaiti",fontsize=16)          # 条形图轴的文字显示
    plt.title('1999-2018年度人口情况', fontproperties='SimHei', fontsize=16)     # 图像标题的文字显示
    plt.xticks(range(20), year, fontproperties="YouYuan")       # 图像的横轴
    ax2.set_ylim([120000, 145000])            # 条形轴的范围
    for x, y in enumerate(total):               # 数组显示在条形上
        plt.text(x, y + 100, '%s' % round(y, 1), ha='center')
    plt.show()

def main():
    result = Result()
    a = int(input('直接利用数据库数据绘图输入1，重新爬取数据并绘图输入2：'))      # 供选择，是直接利用数据库现成表格绘图还是重新爬取，存入数据库，读取并绘图
    if a is 2:
        result.deletedata()
        result.getvalue()
        result.database()
        paint()

    else:
        result.database()
        paint()


if __name__ == '__main__':
    main()

