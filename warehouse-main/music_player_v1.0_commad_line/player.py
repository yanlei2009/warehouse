'''
版本：'1.0.0'
作者：'yan_lei  -QQ 234909594'
'''
import playsound
from multiprocessing import Process
import time
import os


music_name_list = os.listdir('mp3')
music_name_set  = tuple(x for x in range(len(music_name_list)))
music_name_dict = dict(zip(music_name_set, music_name_list))

def reputation():
    version='1.0.0'
    author='yan_lei  -QQ 234909594'
    print('欢迎使用音乐播放器命令行版')
    print(f'作者：{author}')
    print(f'版本：{version}')


def play_sound(music_name):
    print(f'正在播放{music_name}......')
    playsound.playsound('mp3/'+music_name)
    print('播放结束')

class Player:
    def run(self, music_name):
        global  p
        p = Process(target=play_sound, args=(music_name,),name='playing_music')
        p.start()
        return p.pid



if __name__ == '__main__':
    p=Player()
    while True:
        print('当前拥有以下音乐：')
        print(f'编号           音乐名')
        for k,v in music_name_dict.items():
            print(f'{k}           {v}')
        num=input('请输入要播放的音乐的编号（输入/stop关闭程序）>>>')
        if num == '/stop':
            print('感谢使用')
            time.sleep(1)
            break
        yn=input(f'您要播放的音乐是：{music_name_dict[int(num)]}吗？输入y以确认>>>')
        while True:
            if yn=='y' or yn=='Y':
                pid=p.run(music_name_dict[int(num)])
                time.sleep(1)
                io = input('输入stop以停止播放当前音乐>>>')
                if io == 'stop':
                    os.kill(pid,9)
                    break
            elif yn=='n' or yn=='N':
                print('已为您退出选择')
                time.sleep(1.5)
                print('\n'*3)
                print('-'*50)
                break
            else:
                print('错误，只能输入y或者n')