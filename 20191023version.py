#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchFrameException
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime
from get_newid import get_CID

import sys 
#sys.path.append('vcode_vertify\vcode_predict.py')

sys.path.append("vcode_vertify")

from vcode_predict import get_vcode_ByNN


# In[2]:



driver = webdriver.Chrome(".\chromedriver.exe")



CName = "假名字"
CTel = "0999999999"
#ChkCode = "1111"

#身份證字號最多六筆
CId = get_CID()
print("")
print("")
print("自動為您產生 Fake ID is "+str(CId))
print("")
print("")
#----------------------------------------------------

driver.maximize_window()
driver.get("https://www.ebus.com.tw/NetOrder/payOrder/addOrder.aspx")
driver.implicitly_wait(10)

#----------------------------------------------------


# In[3]:



addOrder_options = []
addOrder_inputs = []

addOrder_select1 = []
addOrder_select2 = []
addOrder_select3 = []
addOrder_select4 = []
addOrder_select5 = []

#----------------------------------------------------

#查詢各站資料：
addOrder_options.append(driver.find_element_by_id("SelectAddr"))
#訂購者姓名：
addOrder_options.append(driver.find_element_by_id("txtCName"))
#身分證字號：
addOrder_options.append(driver.find_element_by_id("txtCId"))
#行動電話：
addOrder_options.append(driver.find_element_by_id("txtCTel"))
#上車地點：
addOrder_options.append(driver.find_element_by_id("listGsStationId"))
#下車地點：
addOrder_options.append(driver.find_element_by_id("listGeStationId"))
#乘車日期：
addOrder_options.append(driver.find_element_by_id("listGDate"))
#乘車時段：
addOrder_options.append(driver.find_element_by_id("listGTime"))
#驗證碼：
addOrder_options.append(driver.find_element_by_id("txtChkCode"))


    


    


#----------------------------------------------------
    
def print_space():
    print("")
    print("")
    print("#---------------------------------------------------------------------------------------#")
    print("#---------------------------------------------------------------------------------------#")
    print("#---------------------------------------------------------------------------------------#")
    print("")
    print("")

options = Select(addOrder_options[0]).options
for i in options:
    addOrder_select1.append(i.text)


ct=1

for i in range(len(addOrder_select1)):
    print(str(i)+". "+addOrder_select1[i], end='     ')
    for j in range(20-len(addOrder_select1[i])):
        print(" ",end='')
    if(ct%4==0):
        print("  ")
    ct+=1

print("")
print("")
input_1 = input("請輸入起始站名編號 : ") 

print_space()

options = Select(addOrder_options[4]).options
for i in options:
    addOrder_select2.append(i.text)


ct=1

for i in range(len(addOrder_select2)):
    print(str(i)+". "+addOrder_select2[i], end='     ')
    for j in range(20-len(addOrder_select2[i])):
        print(" ",end='')
    if(ct%4==0):
        print("  ")
    ct+=1

print("")
print("")
input_2 = input("請輸入上車地點 : ") 

print_space()

Select(driver.find_element_by_id("listGsStationId")).select_by_index(int(input_2))

options = Select(addOrder_options[5]).options
for i in options:
    addOrder_select3.append(i.text)

ct=1

for i in range(len(addOrder_select3)):
    print(str(i)+". "+addOrder_select3[i], end='     ')
    for j in range(20-len(addOrder_select3[i])):
        print(" ",end='')
    if(ct%4==0):
        print("  ")
    ct+=1

print("")
print("")
input_3 = int(input("請輸入下車地點 : "))

print_space()


'''

ct=1

for i in range(len(addOrder_select4)):
    print(str(i)+". "+addOrder_select4[i], end='     ')
    for j in range(20-len(addOrder_select4[i])):
        print(" ",end='')
    if(ct%4==0):
        print("  ")
    ct+=1

print("")
print("")
input_4 = input("請輸入乘車日期 : ") 

print_space()

'''

options = Select(addOrder_options[6]).options
for i in options:
    addOrder_select4.append(i.text)

options = Select(addOrder_options[7]).options
for i in options:
    addOrder_select5.append(i.text)

ct=1

for i in range(len(addOrder_select5)):
    print(str(i)+". "+addOrder_select5[i], end='     ')
    for j in range(20-len(addOrder_select5[i])):
        print(" ",end='')
    if(ct%4==0):
        print("  ")
    ct+=1


print("")
print("")
input_5 = input("請輸入乘車時間 : ")

print_space()

full_ticket = input("需要幾個全票座位嗎(1/2/3/4/5/6) ? ")
half_ticket = input("需要幾個半票座位嗎(1/2/3/4/5/6) ? ")
#love_seat = input("需要博愛座嗎(0/1) ? ")
prefer = input("有沒有偏好幾號座位 ? ")




ct=1

for i in range(len(addOrder_select4)):
    print(str(i)+". "+addOrder_select4[i], end='     ')
    for j in range(20-len(addOrder_select4[i])):
        print(" ",end='')
    if(ct%4==0):
        print("  ")
    ct+=1

print("")
print(" 非代號、請以EX : 2019/10/23 , 2019/10/24 ... 等等日期形式輸入，可以輸入尚未出現日期讓程式自動掛票，或輸入現有日期完成自動訂票")
print("")
input_4 = input("請輸入想掛的乘車日期 : ") 

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True



xpath='//option[@value=\''+input_4+'\']'
#print(xpath)
loop=1
while(check_exists_by_xpath(xpath)==0):
    print("找不到您要訂票之日期，自動掛票系統運作中 ... ")
    driver.refresh()


# In[4]:



def sc_code():
    driver.save_screenshot('test.png')
    vcode = driver.find_element_by_id('imgChkCode')

    left = vcode.location['x']
    right = vcode.location['x'] + vcode.size['width']
    top = vcode.location['y']
    bottom = vcode.location['y'] + vcode.size['height']

    #----------------------------------------------------

    left, right, top, bottom

    from PIL import Image
    img = Image.open('test.png')

    img = img.crop((left, top, right, bottom))

    #img.show()

    img.save('captua.png')

    tmp = get_vcode_ByNN('captua.png')

    
    ChkCode = ""

    for i in range(4):
        if not (int(tmp[i])<9 and int(tmp[i])>0):
            ChkCode+=(chr(int(tmp[i])+55))
    
    return ChkCode


# In[5]:


#print(tmp[0])

ChkCode = sc_code()

print(ChkCode)


# In[6]:


#----------------------------------------------------

#各站資料：
Select(driver.find_element_by_id("SelectAddr")).select_by_index(input_1)
#訂購者姓名：
driver.find_element_by_id("txtCName").send_keys(CName)
#身分證字號：
driver.find_element_by_id("txtCId").send_keys(CId)
#行動電話：
driver.find_element_by_id("txtCTel").send_keys(CTel)
#上車地點：
Select(driver.find_element_by_id("listGsStationId")).select_by_index(int(input_2))
#下車地點：
Select(driver.find_element_by_id("listGeStationId")).select_by_index(input_3)
#乘車日期：
driver.find_element_by_xpath(xpath).click()
#乘車時段：
Select(driver.find_element_by_id("listGTime")).select_by_index(input_5)
#驗證碼：
driver.find_element_by_id("txtChkCode").send_keys(ChkCode)


# In[7]:



#----------------------------------------------------

driver.find_element_by_id("butgBusTimeList").click()

#----------------------------------------------------


# In[8]:


while(1==1):
    
    xpath='//*[@id="label_gTravelData"]/font'
    ChkCode = ""

    data = driver.find_element_by_xpath(xpath).get_attribute("innerText")

    if(data=='驗證碼錯誤！'):

        xpath='//*[@id="link_gTravelData"]'

        driver.find_element_by_xpath(xpath).click()

        ChkCode = sc_code()

        print("嘗試破解驗證碼中... 本次猜測之結果為 : "+">>> "+ChkCode+" <<<")
        driver.find_element_by_id("txtChkCode").clear()
        driver.find_element_by_id("txtChkCode").send_keys(ChkCode)


        driver.find_element_by_id("butgBusTimeList").click()
    
    else :
        print("破解驗證碼成功 !!")
        break


# In[9]:


try:
    driver.find_element_by_link_text(u"單程").click()
except:
    print("此時段全部皆已客滿，請重新購票 T.T")
    time.sleep(5)
    exit()


# In[11]:



def book_PS(prefer,l):
    if(l==0):
        return
    
    for i in range(1,15):
        try:
            driver.find_element_by_id("chkBox_gSeatB_"+"%02d"%i).click()
            alert = driver.switch_to_alert()
            time.sleep(1)
            print (alert.text)
            alert.accept()
            print("選擇博愛座位成功 ! ")
            break
            
        except:
            print("find priority seat_"+"%02d"%i+ " failed !")
            
       
def book_SS(prefer,l,max_seat):
    
    seat_type='A'
    print("---嘗試選擇偏好座位---")
    try:
        driver.find_element_by_id("chkBox_gSeat"+seat_type+"_"+"%02d"%prefer).click()
        l-=1
    except:
        print("選擇偏好座位"+seat_type+"區"+"%02d"%prefer+"失敗") 
        try:
            seat_type='B'
            driver.find_element_by_id("chkBox_gSeat"+seat_type+"_"+"%02d"%prefer).click()
            l-=1
        except:
            print("選擇偏好座位"+seat_type+"區"+"%02d"%prefer+"失敗") 
            try:
                seat_type='C'
                driver.find_element_by_id("chkBox_gSeat"+seat_type+"_"+"%02d"%prefer).click()
                l-=1
            except:
                print("選擇偏好座位"+seat_type+"區"+"%02d"%prefer+"失敗") 
    print("---選擇完畢---")
    
    
    
    

   # print(l)
    for i in range(1,int(max_seat)):
        if(i!=prefer):
            if(l==0):
                break
            seat_type='A'
            try:
                driver.find_element_by_id("chkBox_gSeat"+seat_type+"_"+"%02d"%i).click()
                l-=1
            except:
                print("find simple seat_"+seat_type+"%02d"%i+" failed ! ")
                
            seat_type='B'
            try:
                driver.find_element_by_id("chkBox_gSeat"+seat_type+"_"+"%02d"%i).click()
                l-=1
            except:
                print("find simple seat_"+seat_type+"%02d"%i+" failed ! ")
                
            seat_type='C'
            try:
                driver.find_element_by_id("chkBox_gSeat"+seat_type+"_"+"%02d"%i).click()
                l-=1
            except:
                print("find simple seat_"+seat_type+"%02d"%i+" failed ! ")


      
def seat_A(n):
    #print("tk_A_"+str(n))
    driver.find_element_by_id("tk_A_"+str(n)).click()
    
def seat_H(n):
    driver.find_element_by_id("tk_H_"+str(n)).click()

#----------------------------------------------------

tmp=int(full_ticket)+int(half_ticket)
print("---你要的清單---")
print("全票張數 : "+full_ticket)
print("半票張數 : "+half_ticket)
#print("博愛座張數 : "+love_seat)
print("偏好座位 : "+str(prefer))
print("總張數 : " +str(tmp))
print("---你要的清單---")
try:
    seat_A(full_ticket)
    seat_H(half_ticket)
except:
    print("你訂太多票了啦，座位不夠，請重新訂票 T.T")


#book_PS(prefer,love_seat)

print("---正在查詢最大座位數量---")

xpath1='//*[@id="Row_0Seat"]/td[1]/table/tbody/tr['
xpath2=']/td[2]'
max_seat = ""
ct=10
while(len(max_seat)==0):
    try:
        xpath=xpath1+str(ct)+xpath2
        print(xpath)
        for i in range(len(driver.find_element_by_xpath(xpath).get_attribute("innerText"))):
            if(driver.find_element_by_xpath(xpath).get_attribute("innerText")[i].isdigit()):
                max_seat+=driver.find_element_by_xpath(xpath).get_attribute("innerText")[i]
        
        
    except:
        ct-=1
        print("查詢最大座位中...請稍後"+"  tr = "+str(ct))

print("max seat = "+max_seat)

print("---查詢最大座位數量完畢---")

book_SS(int(prefer),tmp,max_seat)

print("---選擇座位完畢，進入購買環節---")
time.sleep(3)


# In[5]:


#----------------------------------------------------

try:
    xpath='//*[@id="butOrderSeat"]'
    driver.find_element_by_xpath(xpath).click()
except:
    print("你訂太多票了啦，座位不夠，請重新訂票 T.T")

#----------------------------------------------------

driver.save_screenshot('buy_page1.png')
time.sleep(1)
xpath='//*[@id="butCreditCard"]'

driver.find_element_by_xpath(xpath).click()

driver.save_screenshot('buy_page2.png')
time.sleep(1)
xpath='//*[@id="butChkFare"]'

driver.find_element_by_xpath(xpath).click()

xpath='//*[@id="butGoAuth"]'

driver.find_element_by_xpath(xpath).click()

#----------------------------------------------------

print("---刷卡中請稍後---")

master_card_ID='5203191517620713'
cvc2='568'
expireM='7'
expireY='2022'

xpath='//*[@id="pan_no1"]'
driver.find_element_by_xpath(xpath).send_keys(master_card_ID)

xpath='//*[@id="cvc2"]'
driver.find_element_by_xpath(xpath).send_keys(cvc2)

xpath='//*[@id="Expire_Month"]'
driver.find_element_by_xpath(xpath).send_keys(expireM)

xpath='//*[@id="Expire_Year"]'
driver.find_element_by_xpath(xpath).send_keys(expireY)
time.sleep(3)
driver.save_screenshot('card.png')

#----------------------------------------------------

xpath='//*[@id="but_chkCardData"]'

driver.find_element_by_xpath(xpath).click()

print("---刷卡完畢---")

#----------------------------------------------------


# In[4]:


import cv2

img1 = cv2.imread('buy_page1.png')
img2 = cv2.imread('buy_page2.png')
img3 = cv2.imread('card.png')

# 顯示圖片
cv2.imshow('購買資訊1', img1)
cv2.imshow('購買資訊2', img2)
cv2.imshow('信用卡資訊', img3)
print("觀看圖片後，按下任意鍵結束~~~~~爬蟲結束囉~~~")
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




