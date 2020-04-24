#调用WechatTeaklink中的函数就行
# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

#指定项目路径
ST.PROJECT_ROOT = "F:/project/AirTest"
#使用image文件
using("WechatTealink.air")
from WechatTealink import *

#例：调用切换门店   输入：change()   

