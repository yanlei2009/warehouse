'''
I/O API函数

读取              写入
read_csv         to_csv
read_excel       to_excel
read_hdf         to_hdf
read_sql         to_sql
read_json        to_json
read_html        to_html
read_stata       to_stata
read_clipboard   to_clipboard
read_pickle      to_pickle
read_msgpack     to_msgpack
read_gbq         to_gbq
'''
import pandas as pd


csv=pd.read_csv('hello.csv',sep=',')
print(csv)
