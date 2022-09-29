print('觸犯道路交通管理處罰條例人員名單')
person1 = {'name':'阿程',
           'age':34,
           '罪責':{
               '第16條':'裝置高音量喇叭或其他產生噪音器物',
               '第17條':'汽車不依限期參加定期檢驗或臨時檢驗',
               '第62條':'汽車駕駛人駕駛汽車肇事',
               '第21條':'未領有駕駛執照駕駛小型車或機車'
           },
           '罰鍰':{
               '第16條':1600,
               '第17條':1500,
               '第62條':2500,
               '第21條':10500
           }}

person2 = {'name':'阿力',
           'age':29,
           '罪責':{
               '第12條':'汽車使用吊銷、註銷之牌照'
           },
           
           '罰鍰':{
               '第12條':5000
           }}

person3 = {'name':'阿瑤',
           'age':58,
           '罪責':{
               '第82條':'未經許可在道路擺設攤位',
               '第56條':'在禁止臨時停車處所停車'
           },
           '罰鍰':{
               '第82條':2000,
               '第56條':1000
           }}

#定義guilt()函數，計算罪責數和處存罪責內容
def guilt(dict_name): 
    number = len(dict_name['罪責']) 
    #len()函式用來計算dict罪責共有幾個key
    content = []
    for i in dict_name['罪責']: #for crime in dict_name['罪責'].items:
        crime = (i,dict_name['罪責'][i]) #用 .items 這行就可以不用
        content.append(crime)
    return number, content
#定義money()函數，計算總金額和處存罰鍰內容
def money(dict_name): 
    sum = 0
    content = []
    for i in dict_name['罰鍰']: #for key, value in dict_name['罰鍰'].items:
        crime = (i,dict_name['罰鍰'][i]) #crime = (key, value)
        content.append(crime)
        sum += dict_name['罰鍰'][i] #sum += value
    return sum, content

'''犯罪次數排名'''
person1_guilt_num, person1_guilt_content = guilt(person1) #宣告讀取函數回傳值 (罪責數, 罪責內容)
person2_guilt_num, person2_guilt_content = guilt(person2)
person3_guilt_num, person3_guilt_content = guilt(person3)
ranking_g = [
    person1_guilt_num,
    person2_guilt_num,
    person3_guilt_num
]
#設定原始位置
ranking_g_enumerate = enumerate(ranking_g, start = 1) # >>>[(1,person1_guilt_num),(2,person2_guilt_num),(3,person3_guilt_num)]
#enumerate()賦予編號 start設定起始值 預設從0開始

#進行排名
ranking_g_enumerate_sorted = sorted(ranking_g_enumerate, key = lambda s: s[1]) 
#sorted( ,reverse = False) 由小到大(預設)

#lambda 參數列表 : 運算式
#lam = lambda s:s[1]
#ranking_g_enumerate_sorted = sorted(ranking_g_enumerate, key = lam) 

'''罰錢金額排名'''
person1_money_sum, person1_money_content = money(person1) #宣告讀取函數回傳值 (總金額, 罰鍰內容)
person2_money_sum, person2_money_content = money(person2)
person3_money_sum, person3_money_content = money(person3)
ranking_m = [
    person1_money_sum,
    person2_money_sum,
    person3_money_sum
]
#設定原始位置
ranking_m_enumerate = enumerate(ranking_m, start = 1) 
#進行排名
ranking_m_enumerate_sorted = sorted(ranking_m_enumerate, key = lambda s: s[1]) 

def getit(list_name): #定義getit()函數執行for-loop
    for i in list_name:
        print(i) #直接行為不需要return回傳值
'''罰錢金額排名'''
person1_money_sum, person1_money_content = money(person1) #宣告讀取函數回傳值 (總金額, 罰鍰內容)
person2_money_sum, person2_money_content = money(person2)
person3_money_sum, person3_money_content = money(person3)
ranking_m = [
    person1_money_sum,
    person2_money_sum,
    person3_money_sum
]
#設定原始位置
ranking_m_enumerate = enumerate(ranking_m, start = 1) 
#進行排名
ranking_m_enumerate_sorted = sorted(ranking_m_enumerate, key = lambda s: s[1]) 

def getit(list_name): #定義getit()函數執行for-loop
    for i in list_name:
        print(i) #直接行為不需要return回傳值

while True: #開始題目要求之迴圈
    options = input('請輸入: 1.查看阿程 2.查看阿力 3.查看阿瑤 4.犯罪數排名 5.累積罰金&罰鍰數排名 6.結束程式:')
    if options == '1':
        print('Name:',person1['name'],'\nAge:',person1['age']) #\n分行
        print('共觸犯(條):',person1_guilt_num)
        print('條例內容:') 
        getit(person1_guilt_content) #呼叫函數用for-loop印出person1_guilt_content各項 
        print('罰鍰總額(元):',person1_money_sum)
        print('詳細內容:')
        getit(person1_money_content)
    elif options == '2':
        print('Name:',person2['name'],'\nAge:',person2['age'])
        print('共觸犯(條):',person2_guilt_num)
        print('條例內容:')
        getit(person2_guilt_content)
        print('罰鍰總額(元):',person2_money_sum)
        print('詳細內容:')
        getit(person2_money_content)
    elif options == '3':
        print('Name:',person3['name'],'\nAge:',person3['age'])
        print('共觸犯(條):',person3_guilt_num)
        print('條例內容:')
        getit(person3_guilt_content)
        print('罰鍰總額(元):',person3_money_sum)
        print('詳細內容:')
        getit(person3_money_content)
    elif options == '4':
        print('甲為1，乙為2，丙為3')
        print('(人,犯罪次數)(少->多）')
        print(ranking_g_enumerate_sorted)
    elif options == '5':
        print('甲為1，乙為2，丙為3')
        print('(人,金額)(少->多）')
        print(ranking_m_enumerate_sorted)
    elif options == '6':
        print('Bye bye~~~')
        break
    else:
        print('輸入錯誤，請重新輸入')
        continue