import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

import matplotlib.style as psl
import matplotlib

# 收入多少  --每个月净收入模型构建
# 支持多少  --每月开始模型构建
# 是否吃土  --使用花呗的不同情况下，看看偿还额度的变化

# 设置字体
font_set = FontProperties(fname=r"c:\windows\fonts\MSYHL.TTC", size=12)
matplotlib.matplotlib_fname()
psl.use('seaborn-colorblind')
# 设置一个图标风格
# % matplotlib inline
# 魔法函数，IDE中不需要
print('导入完成')


# 构建税费计算函数
def tax(salary_sum):
    # 扣除五险一金后的工资，按照上海市标准 养老8% 医疗2% 失业0.5% 公积金7%
    if salary_sum <= 5000:
        return salary_sum
    elif salary_sum <= 8000:
        return (salary_sum - 5000)*0.03
    elif salary_sum <= 17000:
        return (salary_sum - 5000) * 0.1 - 210
    elif salary_sum <= 30000:
        return (salary_sum - 5000) * 0.2 - 1410
    elif salary_sum <= 40000:
        return (salary_sum - 5000) * 0.25 - 2660
    elif salary_sum <= 60000:
        return (salary_sum - 5000) * 0.3 - 4410
    elif salary_sum <= 85000:
        return (salary_sum - 5000) * 0.35 - 7160
    else:
        return (salary_sum - 5000) * 0.45 - 15160


test = 16000
print('函数构建完成，当月薪为%.1f元时，需要缴纳%.2f元' % (test, tax(test)))

# 创建奖金随机函数


def bonus(b_avg):
    # 预设10年的奖金，生成120个随机量
    return pd.Series(np.random.normal(loc=b_avg, scale=200, size=120))


print('函数构建完成，当奖金均值为1500时，随机数组为：')
print(bonus(1500)[:120])

plt.title('奖金随机函数-数据分布直方图', fontproperties=font_set)
plt.hist(bonus(1500), bins=30)
plt.grid()
# plt.show()
# 绘制直方图


# 构建五险一金函数
def insurance(salary):
    if salary <= 21396:
        return salary*0.175
    else:
        return 3744.58


test = 15000
print('函数构建完成，当月薪为%.1f时，需要缴纳五险一金%.2f' % (test, insurance(test)))


# 构建每月净收入函数
def final_income(s, b_avg):
    df_i = pd.DataFrame({
           '月薪': [s for i in range(120)],    # 月薪基数
           '五险一金': [insurance(s) for j  in range(120)], # 计算五险一金，
           '奖金': bonus(b_avg)
         })
    df_i['计税部分'] = df_i['月薪'] + df_i['奖金']
    df_i['个人所得税'] = df_i['计税部分'].apply(lambda x: tax(x))
    df_i['月净收入'] = df_i['月薪'] + df_i['奖金'] - df_i['个人所得税'] - df_i['五险一金']
    return df_i


result = final_income(10000, 1500)

# 测试结果：当月收入1W，平均奖金1500元时的月净收入情况
result['月净收入'].iloc[:12].plot(kind='bar', figsize=(12, 4), color='Green')
plt.title('月净收入情况 - 前12月')
plt.grid()
# plt.show()
print(result.head(5))

# 基本生活支出
general_expense = pd.Series(np.random.randint(3000, 3501, size=120))

# histogram  直方图又称柱状图

plt.title('基本生活支出', fontproperties=font_set)
plt.hist(general_expense, bins=30)
plt.grid()
# plt.show()
# print(general_expense)

shopping = pd.Series(np.random.normal(400, 1200, size=120))
plt.title('购物支出', fontproperties=font_set)
plt.hist(shopping, bins=30)
plt.grid()
# plt.show()

# 娱乐支出
happy = pd.Series(np.random.randint(400, 1200, size=120))
plt.title('娱乐支出', fontproperties=font_set)
plt.hist(shopping, bins=30)
plt.grid()


# 学习支出
study = pd.Series(np.random.randint(100, 500, size=120))
plt.title('学习支出', fontproperties=font_set)
plt.hist(study, bins=30)
plt.grid()

# 其它支出
other = pd.Series(np.random.randint(100, 500, size=120))
plt.title('其它支出', fontproperties=font_set)
plt.hist(other, bins=30)
plt.grid()


# 构建每月开支函数
def final_expense():
    df_i = pd.DataFrame({'基本生活支出': np.random.randint(3000, 3500, size=120),
                         '购物支出': np.random.normal(loc=5000, scale=500, size=120),
                         '娱乐指出': np.random.randint(400, 1200, size=120),
                         '学习支出': np.random.randint(100, 500, size=120),
                         '其它支出': np.random.normal(loc=500, scale=40, size=120)
                         })
    df_i['月总支出'] = df_i['基本生活支出']+df_i['购物支出']+df_i['娱乐指出']+df_i['学习支出']+df_i['其它支出']
    return df_i


result = final_expense()
plt.legend(prop=font_set)
result[['基本生活支出', '购物支出', '娱乐指出', '学习支出', '其它支出', '月总支出']].iloc[:12].plot(kind='bar',
                                                                          figsize=(12, 4),
                                                                          stacked=True,
                                                                          colormap='Reds_r')
plt.title('月总支出情况 - 前十二个月')
plt.grid()
print('#########')
print(result.head(7))
# plt.show()

# 是否吃土，使用花呗还款情况模拟
# 整理几个约束条件
# 每月先还贷款，在消费
# 每月的支出除还款外，都可以使用花呗头指
# 当这个月的收入小于等于需要还款的金额，代表你要吃土
# 花呗信用总额度为1.5万
# 当月需要借贷花呗的金额 = 月初余额 + 月收入 - 本月需要还花呗 > 15000

# 创建120个月每月的收入、支出、月初余额、本月需要还花呗

income = final_income(10000, 1500)['月净收入'].tolist()
expense = final_expense()['月总支出'].tolist()
saving = [0 for i in range(120)]
debt = [0 for i in range(120)]

print('前6个月的月收入，月支出，月初余额（未计算），本月需要还花呗（为计算）数据分别为：\n')
print(income[:6])
print(expense[:6])
print(saving[:6])
print(debt[:6])

# 第二个月推导
if income[0] >= expense[0]:
    '''
    第一个月收入大于等于支出：
    第二个月月初余额= 第一个月收入 - 第一个月支出
    第二个月需要还花呗 = 0
    '''
    saving[1] = income[0] - expense[0]
    debt[1] = 0
else:
    '''
    第一个月收入小于支出：
    第二个月月初余额= 0
    第二个月需要还花呗 = 第一个月收入 - 第一个月支出
    '''
    saving[1] = 0
    debt[1] = expense[0] - income[0]

print(income[:2])
print(expense[:2])
print(saving[:2])
print(debt[:2])

# 构建函数模拟
income = final_income(10000, 1500)['月净收入'].tolist()
expense = final_expense()['月总支出'].tolist()
saving = [0 for i in range(120)]
debt = [0 for i in range(120)]


def case_a():
    month = []
    data = []
    for i in range(120):
        money = saving[i] + income[i] - expense[i] - debt[i]
        if -money > 15000:
            # 当月还需借花呗金额大于15000  破产
            print('第%i个月花呗救不了我了，要破产了,欠钱%i！\n' % (i+1, money))
            break
        else:
            # 当月还需借花呗金额小于15000  继续浪
            if money > 0:
                # 有结余
                saving[i+1] = money
            else:
                # 有负债
                debt[i+1] = -money
        month.append(i+1)
        data.append([income[i], expense[i], debt[i], saving[i+1], debt[i+1]])
    result_a = pd.DataFrame(data, columns=['月收入', '月支出', '本月需要还花呗', '本月余钱', '欠债'], index=month)
    result_a.index.name = '月份'
    # 将数据放入dataframe中返回
    return result_a


# case_a()
# 第一回合，不使用分期情况下， 进行1万次模拟，查看破产月份

month_case_a = []
for i in range(10): # 10为模拟次数
    print('正在进行第%i次模拟' % (i+1))
    income = final_income(10000, 1500)['月净收入'].tolist()
    expense = final_expense()['月总支出'].tolist()
    saving = [0 for i in range(120)]
    debt = [0 for i in range(120)]
    result_a = case_a().index.max()
    month_case_a.append(result_a)
result_last = pd.Series(month_case_a)

# 几月10000次模拟的破查月份， 制作直方图
plt.figure(figsize=(12, 4))
result_last.hist(bins=15)
plt.title('第一回合，不可分期模拟结果')
#plt.show()


# 第二回合模拟分期
# 需要计算花呗得利息，分期得基本都在10%左右年化
income = final_income(10000, 1500)['月净收入'].tolist()
expense = final_expense()['月总支出'].tolist()
saving = [0 for i in range(120)]
debt = [0 for i in range(120)]

# 构建函数模拟--分期三个月
def case_b():
    month = []
    data = []
    for i in range(120):
        money = saving[i] + income[i] - expense[i] - debt[i]
        if -money > 15000:
            # 当月还需借花呗金额大于15000  破产
            print('第%i个月花呗救不了我了，要破产了,欠钱%i！\n' % (i+1, money))
            break
        else:
            # 当月还需借花呗金额小于15000  继续浪
            if money > 0:
                # 有结余
                saving[i+1] = money
            else:
                # 有负债
                money_per = abs(money)*(1+0.025)/3  # 分期三个月
                debt[i+1] = debt[i+1] + money_per
                debt[i+2] = debt[i+2] + money_per
                debt[i+3] = debt[i+3] + money_per
        month.append(i+1)
        data.append([income[i], expense[i], debt[i], saving[i+1], debt[i+1]])
    result_b = pd.DataFrame(data, columns=['月收入', '月支出', '本月需要还花呗', '本月余钱', '欠债'], index=month)
    result_b.index.name = '月份'
    # 将数据放入dataframe中返回
    return result_b

month_case_b = []

# 几月10000次模拟的破查月份， 制作直方图
for i in range(1000): # 10为模拟次数
    print('正在进行第%i次模拟' % (i+1))
    income = final_income(10000, 1500)['月净收入'].tolist()
    expense = final_expense()['月总支出'].tolist()
    saving = [0 for i in range(120)]
    debt = [0 for i in range(120)]
    result_b = case_a().index.max()
    month_case_b.append(result_b)
result_last_b = pd.Series(month_case_b)


plt.figure(figsize=(12, 4))
result_last_b.hist(bins=15)
plt.title('第二回合，分期三次模拟结果')
plt.show()
