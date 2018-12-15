readfile = open('Osakdata.txt')
file = open('Osakchat.txt','a+')
for line in readfile:
    item = line.strip().split(',')
    lenth = len(item)
    file.write(item[0]+','+item[-1]+','+str(len(item))+'\n')
    newline = ','.join(item[1:lenth-1])+'\n'
    file.write(newline)
readfile.close()
file.close()