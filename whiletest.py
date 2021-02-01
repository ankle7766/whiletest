password = 'a123456'
count = 0

while count !=3:
    pwd= input("請輸入密碼:")
    if pwd == password:        #密碼的值，盡量存一次就好
        print("登入成功")
        break
    elif count <2:
        print(f'密碼錯誤! 還有{2-count}次機會')
        count += 1
    else:
        print("密碼錯誤...")
        count +=1
        print("失敗三次，不給玩了")