import matplotlib.pyplot as plt
import numpy as np
from config import peoples
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

def count(dic):
    namedic=dic
    n = []
    keys = namedic.keys()
    long = len(keys)
    for i in keys:
        print(f'{i}代表{namedic[i]}')
    while True:
        print('请输入您的投票人代号(输入0表示停止)')
        num=input('>>>')
        try:
            num = int(num)
            if num == 0:
                print('投票结束')
                break
            elif num > long:
                print('错误,不在范围内')
            else:
                n.append(num)
        except:
            print('错误，非数字！')
    if len(n)<long:
        print('\n\n\n')
        print('---'*24)
        print('请重新输入')
        count(namedic)
    return n

def draw(namedic):
    labels = [i for i in namedic.values()]
    n = count(namedic)
    key_long = len(namedic.keys())
    l = np.zeros(key_long, dtype=int)
    for i in range(key_long):
        l[i] = n.count(i + 1)
    l_all = l.sum()
    data = [(l[n] / l_all) * 100
            for n in range(key_long)]
    fig, ax = plt.subplots()
    ax.pie(data, labels=labels, autopct='%1.1f%%')
    plt.title('投票结果')
    plt.show()

if __name__ == '__main__':
    draw(peoples)