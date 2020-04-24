#封装脚本
# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

#指定项目路径
ST.PROJECT_ROOT = "F:/project/AirTest"
#使用image文件
using("image.py")
from image import *

 

auto_setup(__file__)

#打开微信
start_app("com.tencent.mm")

#下拉微信主页，显示最近使用的小程序
poco("com.tencent.mm:id/b6u").swipe([0.0896, 0.7762])

#打开有单微信小程序
click(tealink)

#点击函数
def click(img):
    wait(img)
    touch(img)
    return print("click" + str(img))

#查看是否在首页，不是则点击首页
def main():
    if exists(index_img):
        touch(index_img)
    return print("进入首页")

#购物车增加商品数量,+5个
def addGood(): 
    for i in range(10):
        while i <5:
            click(addBtn)
            break
    return
            
 #购物车减少商品数量，-4个
def subGood():
    for i in range(10):
        while i <4:
            click(lessBtn)
            break  
    return

#点击确定按钮
#因为有不同样式的确定按钮，不清楚哪些场景下出现哪些按钮，所以遍历，出现的是哪个就点哪个
def confirm():
    for i in confirmBtn:
        if exists(i):
            click(i)
    return

#授权（如果未授权过，需引用）
def getAuth():
    if exists(auth_toast):
        click(auth_agree)
        click(allow_get_user)
    click(allow_get_user)
    return print("授权成功")

#判断门店营业、配送状态 ，进入门店主页再调用
#因为框架无法识别小程序页面元素的层级，只能判断单一门店的状态，所以不在门店列表使用
def isBusiness():
    if exists(notDistri):
        print("门店不在配送时间")
    elif exists(shopRelax):
        print("门店休息中")
    else:
        print("门店正常营业")
    return print("判断完毕")

#切换位置
def changeLocation():
    click(setLocation)
    click(JiaLian)
    return print("成功切换位置")

#切换门店
def chanShop():
    click(setNearShop)
    if exists(noNearShop):
        print("没有可配送门店")
    elif exists(goBuy):
        click(goBuy)
        print("成功切换门店")
    else:
        print("没有可下单的门店")
    return 


#切换配送模式
def change():
    if exists(noTakeOut):  #切换到外卖
        click(noTakeOut)
        print("当前为堂食模式，切换为外卖模式") 
    elif exists(noBring):  #切换到堂食
        click(noBring)
        print("当前为外卖模式，切换为堂食模式")
    return
   
    
#主流程外卖点单
#不含切换地址、切换门店操作
def buyTakeOut():
    click(takeOutOrder)
    getAuth()
    click(chooseSpe)
    click(addShoppingCar)
    click(settlement)
    if exists(allow_get_user):
        click(allow_get_user)
        pass
    click(shippingAdress)   
    click(chooseAddress)
    click(hadCoupon)
    if exists(chooseCoupon):
        click(chooseCoupon)
        confirm()
        pass
    else:
        click(back)
    click(pay)
    click(allow_get_user)
    confirm()
    return print("外卖模式下单")

#主流程堂食点单
def buyBring():
    click(inHereOrder)
    if exists(chooseShop):
        click(goBuy)
        pass
    click(chooseSpe)
    click(addShoppingCar)
    click(settlement)
    if exists(allow_get_user):
        click(allow_get_user)
        pass
    click(hadCoupon)
    if exists(chooseCoupon):  #如果有可用优惠券，点击
        click(chooseCoupon)
        confirm()
        pass
    else:
        click(back)
    click(pay)
    click(allow_get_user)
    confirm()
    return print("堂食模式下单")


