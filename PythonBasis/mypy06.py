#训练嵌套循环打印，注意空格，了解二维列表的存储结构

a=[
    ['Xiao3',18,20000,'Beijing'],
    ['ErGouzi',21,120000,'Beijing'],
    ['wife1',20,40000,'Beijing'],
    ]

for m in range(3):
    for n in range (4):
        print(a[m][n],end='\t')
    print()#打印完一行换行
   
#注意空格缩进使得最后一个print（）与range(3)这里的循环对应
