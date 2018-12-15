from sklearn.cross_validation import train_test_split

loadfile = open('Osakchat.txt','r')
ratio = 0.1
savefiletrain = open('Osakchat_train.txt','a+')
savefiletest = open('Osakchat_test.txt','a+')
random_num=5

X = []
y = []
i = 1
for line in loadfile:
    if i%2 == 1:
        X.append(line)
    else:
        y.append(line)
    i += 1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=ratio,random_state=random_num)

j = 0
for x in X_train:
    savefiletrain.write(x+y_train[j])
    j += 1

j = 0
for x in X_test:
    savefiletest.write(x+y_test[j])
    j += 1