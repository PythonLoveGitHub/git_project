import numpy as np
import time

count = 1000000000
incount = 0
start_time = time.time()
for i in range(count):
    x = np.random.random()
    y = np.random.random()
    if x*x + y*y <= 1:
        incount+=1
end_time = time.time()
print('Monte_Carlo方法抽取%d次计算出Π的值为%f,消耗时间为%f'% (count,(incount/count)*4,end_time-start_time))

#Monte_Carlo方法抽取10次计算出Π的值为2.800000,消耗时间为0.000000
#Monte_Carlo方法抽取100次计算出Π的值为3.200000,消耗时间为0.000000
#Monte_Carlo方法抽取1000次计算出Π的值为3.160000,消耗时间为0.001021
#Monte_Carlo方法抽取10000次计算出Π的值为3.132000,消耗时间为0.006994
#Monte_Carlo方法抽取100000次计算出Π的值为3.143280,消耗时间为0.084731
#Monte_Carlo方法抽取1000000次计算出Π的值为3.140020,消耗时间为0.828797
#Monte_Carlo方法抽取10000000次计算出Π的值为3.141344,消耗时间为8.181150
#Monte_Carlo方法抽取100000000次计算出Π的值为3.141316,消耗时间为86.440756
