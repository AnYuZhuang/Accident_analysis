import requests
import json
import matplotlib.pyplot as plt

url='http://210.69.35.216/od/data/api/88C78BC3-DF8F-4FC6-9E22-F65648B6CFD1?$format=json'
response=requests.get(url)
my_file=json.loads(response.text)
#print(my_file)
#print(len(my_file))
data_list1=[]
data_list2=[]

data_list3=[]
data_list4=[97,98,99,100,101,102,103,104,105,106]

for i in range(1,11):
    B=int(my_file[i]['dead'])
    A=int(my_file[i]['A1-count'])     #創建list存每個x的值,才不會被覆蓋!
    C=int(my_file[i]['A2-count'])

    data_list1.append(A)
    data_list2.append(B)

    data_list3.append(C)

def plotdata1(plt,data1):
    for k in range(10):
        row=data_list1[k]
        col=data_list2[k]
        plt.xlabel('A1-count')
        plt.ylabel('dead')
        plt.scatter(row,col,c = 'red',marker = 'o')
def plotdata2(plt,data2):
    for l in range(10):
        row=data_list1[l]
        col=data_list3[l]
        plt.xlabel('A1-count')
        plt.ylabel('A2-count')
        #pic=plt.figure().add_subplot()
        plt.scatter(row,col,c = 'blue',marker = 'o')
def plotdata3(plt,data3):
    for h in range(10):
        row=data_list4[h]
        col=data_list2[h]
        plt.xlabel('year')
        plt.ylabel('dead')
        plt.scatter(row,col,c = 'green',marker = 'o')

plt.figure(figsize=(10,5))  
plotdata1(plt,data_list1)
plotdata1(plt,data_list2)

plt.figure(figsize=(10,6))
plotdata2(plt,data_list1)
plotdata2(plt,data_list3)

plt.figure(figsize=(10,6))
plt.title('fatal casualty & year')
plotdata3(plt,data_list4)
plotdata3(plt,data_list2)

plt.show()