#项目介绍
此项目封装了有单微信小程序的部分流程模块，只需要修改一个参数，就可以应用在其他流程、页面与有单一样的项目上。

#环境准备
1、电脑安装好python环境，安装ADB，下载airtest IDE
2、手机通过USB线连接到电脑上，连接可参考：http://airtest.netease.com/docs/docs_AirtestIDE-zh_CN/2_device_connection/1_android_phone_connection.html
airTest IDE可显示手机屏幕就成功了

#安装项目
下载项目到本地，在airTest点击文件->打开脚本，选择下载到本地的脚本 run.py（在run.air 文件夹中） 、WechatTealink.py 、 image.py
项目中有很多图片，不要删除，这些图片都是页面元素，不过脚本中用自定义参数代替了

#文件说明
WechatTealink.py:封装各类函数
image.py ：保存定义好的图片参数,用于在WechatTealink中调用
run.air文件夹中的run.py: 调用WechatTealink中封装好的函数，直接输入函数名即可，不用加文件名，详见示例

#修改参数
1、WechatTealink、run 中的项目路径，需改成你本地的项目路径
![image](https://github.com/sugera/WechatTealink/tree/master/readme/1.jpg)
![image](https://github.com/sugera/WechatTealink/tree/master/readme/2.png)
![image](https://github.com/sugera/WechatTealink/tree/master/readme/6.png)

2、WechatTealink中 修改你要测试的小程序页面元素
![image](https://github.com/sugera/WechatTealink/tree/master/readme/3.png)
![image](https://github.com/sugera/WechatTealink/tree/master/readme/4.png)
![image](https://github.com/sugera/WechatTealink/tree/master/readme/5.png)

#项目准备，部分函数中的元素是写死的，所以需要事先在小程序中创造好条件。

1、后台发放所有商品通用的10元代金券，并进入小程序领取好该卡券，越多越好

2、添加好如图收货地址
![image](https://github.com/sugera/WechatTealink/tree/master/readme/7.png)

3、先打开一下要测试的小程序，确保小程序在最近使用的小程序窗口中

3、测试地点在长虹科技大厦或附近 （涉及切换位置和门店流程）

修改好以上参数就可以在run中调用要使用的模块拼装成你想要的测试脚本啦

#函数说明
#流程类函数，此类函数可以完成某一个流程的函数，函数中包含很多功能类函数
1、getAuth() ：授权函数，用于首次进入小程序，未授权的情况，授权完函数结束。如小程序已经授权，无需再次调用。

2、buyTakeOut()：直线外卖下单流程，在首页进入外卖点单页面->选择商品加入购物车->结算->选择指定收货地址->选择指定优惠券->付款  （如果有配送费，因为代金券不能抵消配送费，脚本运行结束后，手动输入密码付款），可按需在函数中调用其他函数。

3、buyBring():直线堂食下单流程，在首页进入堂食点单页面->选择商品加入购物车->结算->选择指定优惠券->付款 （如商品价格大于10元，脚本运行结束后需手动付款）

4、chanShop()：切换门店，判断有误可配送门店，有则切换至第一个可配送门店，堂食则进入可下单门店

5、changeLocation(): 外卖模式切换当前位置，切换到嘉联大厦


#功能类函数，不含流程
1、click():点击函数，等待某元素出现，执行点击。

2、main(): 点击首页。

3、confirm()：点击确定。

4、isBusiness()： 判断门店营业、配送状态 ，进入门店主页再调用，因为框架无法识别小程序页面元素的层级，只能判断单一门店的状态，所以不在门店列表使用。

5、addGood():商品数量 +5   （该框架input函数无效，所以不支持自定义添加数量）

6、subGood()：商品数量 -4   （该框架input函数无效，所以不支持自定义减少数量）

7、change()：切换配送模式，在门店主页使用


#查看报告
运行完脚本后，框架自动生成一个很漂亮直观的测试报告，点击图中地方即可查看。
![image](https://github.com/sugera/WechatTealink/tree/master/readme/8.png)

注意，该报告只显示最新一次运行的结果，没有历史报告。如需要获取历史报告，每次运行脚本后，在IDE窗口右键点击文件名称，可导出报告，因为报告中包含了静态资源，所以文件有点大。









 







