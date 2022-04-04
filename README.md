# snmp-oid-ui
通过pysnmp+twinter实现简单ui界面
输入ip（第一行）oid（第二行） community（第三行）可读取设备信息 
Start the SNMP service and create Community before using it.

python3 demo-snmp.py

add in finaldemo：
#########################增加获取oid子树的所有值的功能###########################################

##在get_child——oid下输入.1.3.6.1.2.1.1则输出值为
'''
Value:
[1.3.6.1.2.1.1.1.0] = Hardware: AMD64 Family 23 Model 96 Stepping 1 AT/AT COMPATIBLE - Software: Windows Version 6.3 (Build 19044 Multiprocessor Free)
[1.3.6.1.2.1.1.2.0] = 1 0 0 768 3 0 0 1536 6 0 0 256 
[1.3.6.1.2.1.1.3.0] = 29935365
[1.3.6.1.2.1.1.4.0] = 
[1.3.6.1.2.1.1.5.0] = DESKTOP-EAAO1V0
[1.3.6.1.2.1.1.6.0] = 
[1.3.6.1.2.1.1.7.0] = 76
'''
################################################################################################
