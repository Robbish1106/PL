print('親屬關係圖(親等計算)')
a = ['表兄弟','姑媽','祖父','父親','自己','女兒','外孫女']
b = ['侄子','哥哥','母親','外祖父','姨媽','表姊妹']

def findit(str): #定義findit函數，獲取名稱的索引值
  i = 0 #在迴圈外宣告變數i為0
  if str in a: #判斷名稱在哪一個list中
    for a1 in a:
      i += 1
      if a1 == str:
        break
    return i
  else:
    for b1 in b:
      i += 1
      if b1 == str:
        break
    return i
    
def people1(m,n): #定義函數people1()、people2()，印出相隔親屬名稱
  for l1 in range(m-1,n):
    print(a[l1])

def people2(m,n):
  for l2 in range(m-1,n):
    print(b[l2])

while True:
    x = input('輸入題號(羅馬數字)按6結束:')
    if x == '1':
        q1_1 = findit('姑媽') #宣告變數儲存findit()回傳值，即索引值
        q1_2 = findit('自己')   
        q1 = q1_2 -q1_1 
        print('姑媽與嘟嘟')
        print('旁系 %d親等'%q1)
        people1(q1_1, q1_2)
    elif x == '2':
        q2_1 = findit('祖父')
        q2_2 = findit('外孫女')  
        q2 = q2_2 -q2_1
        print('祖父與外孫女')
        print('直系 %d親等'%q2)
        people1(q2_1, q2_2)
    elif x == '3':
        q3_1 = findit('侄子')
        q3_2 = findit('姨媽')
        q3 = q3_2 -q3_1 
        print('侄子與姨媽')
        print('旁系 %d親等'%q3)
        people2(q3_1, q3_2)
    elif x == '4':
        q4_1 = findit('哥哥')
        q4_2 = findit('表姊妹')
        q4 = q4_2 -q4_1
        print('哥哥與表姊妹')
        print('旁系 %d親等'%q4)
        people2(q4_1, q4_2)
    elif x == '5':
        q5_1 = findit('表兄弟') 
        q5_2 = findit('女兒')
        q5 = q5_2 -q5_1 
        print('表兄弟與女兒')
        print('旁系 %d親等'%q5)
        people1(q5_1, q5_2)
    elif x == '6':
        break
    else:
        print('請重新輸入')
        continue  