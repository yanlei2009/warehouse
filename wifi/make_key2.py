import itertools as itt
lname=['PENG','Peng','peng']
year=[str(i)
      for i in range(1950,2020)]
month=['01','02','03','04','05','06','07','08','09','10','11','12']
data=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
for i in lname:
    for j in year:
        for k in  month:
            for l in data:
                with open('keyword.txt', 'a') as f:
                    f.write(f'\n{i+j+k+l}')

