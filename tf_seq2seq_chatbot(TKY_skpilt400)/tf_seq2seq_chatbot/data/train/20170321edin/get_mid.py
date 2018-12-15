readfile = open('/home/marlboro/wht/tf_seq2seq_chatbot(edin)/tf_seq2seq_chatbot/data/train/20170321edin/Edindata.txt')
file = open('/home/marlboro/wht/tf_seq2seq_chatbot(edin)/tf_seq2seq_chatbot/data/train/20170321edin/Edinchat1.txt','a+')
for line in readfile:
    item = line.strip().split(',')
    lenth = len(item)
    file.write(item[0]+','+item[-1]+','+str(len(item))+'\n')
    newline = ','.join(item[1:lenth-1])+'\n'
    file.write(newline)
readfile.close()
file.close()