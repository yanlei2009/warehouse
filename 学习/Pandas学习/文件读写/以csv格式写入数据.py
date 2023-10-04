import pandas as pd

name=['芙宁娜','未知','未知','雷电将军','纳西妲','温迪','钟离']
stockSummaries={'称号':pd.Series(['水之神','火之神','冰之神','雷之神','草之神','风之神','岩之神'],index=name),
                '性别':pd.Series(['女','未知','女','女','女','男','男'],index=name),
                '属性':pd.Series(['水','火','冰','雷','草','风','岩'],index=name),
                '体型':pd.Series(['少女','未知','未知','成女','萝莉','少年','成男'],index=name)}
stockDF=pd.DataFrame(stockSummaries)
stockDF.to_csv('hello.csv')
