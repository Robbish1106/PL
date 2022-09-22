a={"有期徒刑","沒收","罰金"}
b={"無期徒刑","罰金","褫奪公權"}

print(a|b) #聯集(ab總共有)

print(b-a) #差集(b有a無)

print(a&b) #交集(ab共同項)
print("罰金" in a)
print("罰金" in b)