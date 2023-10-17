def read_level(filename):
    level_list = []
    with open(filename, 'r') as f:
        lines=f.readlines()
        for line in lines:
            l=[]
            for string in line:
                  if string != '\n':
                    l.append(string)
    return lines
def mapping(listname,dictname):
    for i in range(10):
        for j in range(10):
            index=listname[i][j]
            listname[i][j]=dictname[index]
name_dict={
    'w':'wall',
    '=': 'floor',
    '@':'music_player_v1.0_commad_line',
    '!':'door'
}

if __name__ == '__main__':
    print(mapping(read_level('level/level_1.txt'), name_dict))