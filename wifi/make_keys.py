import itertools as itt
word="qwertyuiopasdfghjklzxcvbnm1234567890"
long=[8]
password=open('keyword.txt', 'a')
for i in long:
    temp=itt.permutations(word,i)

    for j in temp:
        password.write("".join(j))
        password.write("".join("\n"))
