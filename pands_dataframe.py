import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.random.randn(4,4), index=list('ABCD'), columns=list('ABCD'))
print(df1)

df100 = pd.DataFrame(np.random.randn(3,4), index=list('ABC'), columns=list('ABCD'))
print(df100)
print(df100.shape[0])
print(df100.shape[1])

print(df100.sum(0))
print(df100.cumsum(1))



dic1={'name':['小明','小红','狗蛋','铁柱'],'age':[17,20,5,40],'gender':['男','女','女','男']}
df3=pd.DataFrame(dic1)

print(df3)

#print(df3.dtypes)
#print('###############')
#print(df3.head(0))
#print('###############')
#print(df3.head(1))
#print(df3.head(2))
print('###############')
print(df3.tail(1))
print('###############')
print(df1.index)
print(df1.columns)
print(df1)
#print(df1.values)
#print('###############')
#print(df1.loc['B'])
#print(df1.iloc[0])
#print('###############')
#print(df1['A'])
#print('###############')
#print(df3.shape[0])
#print(df3.shape[1])
#print(df1.T)
#print(df3)
#print(df3.sum())
#print(df3.sum(1))

df1['E'] = [999,999,999,999]
print(df1)
df4 = pd.DataFrame([777,777,777,777],index = list('ABCD'),columns=list('M'))

df7 = pd.DataFrame([666,666,666,666],index = list('ABCH'),columns=list('Z'))


df1.insert(0,'F',[888,888,888,888])
print(df1)
print(df4)
df5 = df1.join(df4)
print(df5)
df8 = df1.join(df7,how='outer')
print(df8)


df10=pd.DataFrame([1,2,3,4],index=list('ABCD'),columns=['a'])
df11=pd.DataFrame([10,20,30,40],index=list('ABCD'),columns=['b'])
df12=pd.DataFrame([100,200,300,400],index=list('ABCD'),columns=['c'])
#list1=[df10.T, df11.T, df12.T]
list1=[df10, df11, df12]
df13=pd.concat(list1, sort=False)
print(df13)
df14=pd.concat(list1, sort=False)
print(df14)

# 第三次更新