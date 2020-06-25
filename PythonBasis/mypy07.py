#训练自己的实际应用能力，可以表示好表格数据
#练习一下for循环及使用len()
r1={'name':'FU','age':18,'salary':20000,'city':'BeiJing'}
r2={'name':'FU2','age':17,'salary':200000,'city':'Shenzhen'}
r3={'name':'FU3','age':16,'salary':2000,'city':'NanCheng'}

tb=[r1,r2,r3]

#获得第二行人的薪资
print(tb[1].get('salary'))

#打印表中所有的薪资
for i in range(len(tb)):
    print(tb[i].get('salary'))

#打印所有数据
for i in range(len(tb)):
     print(tb[i].get('name'),tb[i].get('age'),tb[i].get('salary'),tb[i].get('city'))
