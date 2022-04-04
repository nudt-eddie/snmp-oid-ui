import tkinter as tk
from tkinter import messagebox
import pysnmp
from pysnmp.entity.rfc3413.oneliner import cmdgen
window = tk.Tk()
window.title('SNMP')
entry = tk.Entry(window,width=40)
entry2 = tk.Entry(window,width=40)
entry3 = tk.Entry(window,width=40)
def get_ip():
    ip = entry.get()		# 调用get()方法，将Entry中的内容获取出来
    print(ip)
def get_oid():
    oid = entry2.get()		# 调用get()方法，将Entry中的内容获取出来
    print(oid)
def get_value():
    value = entry3.get()		# 调用get()方法，将Entry中的内容获取出来
    print(value)
entry.pack()
button = tk.Button(window,text='ip',command=get_ip).pack()
entry2.pack()
button2 = tk.Button(window,text='oid',command=get_oid).pack()
entry3.pack()
button3 = tk.Button(window,text='社区',command=get_value).pack()
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
entry4 = tk.Entry(window,width=40)
def get_child_oid():
    child_oid = entry4.get()		# 调用get()方法，将Entry中的内容获取出来
    print(child_oid)
entry4.pack()
button4 = tk.Button(window,text='child_oid',command=get_child_oid).pack()
def click_button_2():
    # 使用消息对话框控件，showinfo()表示温馨提示
    runit_2(loop=1)
button = tk.Button(window,text="get_children_value",command=click_button_2).pack()
def snmpget_all():
    ip = entry.get()
    child_oid = entry4.get()  
    com = entry3.get()
    #########
    errorIndication, errorStatus, errorIndex, varBindTable = cmdgen.CommandGenerator().nextCmd(
    cmdgen.CommunityData('test-agent', com , 1), ##社区信息，my-agent ,public 表示社区名,1表示snmp v2c版本，0为v1版本
    cmdgen.UdpTransportTarget((ip, 161)),##端口 161上(snmp标准默认161 UDP端口)
    child_oid ##传送的OID
    #(1,3,6,1,2,1,1)#1.3.6.1.2.1.1.1.0
    )

    if errorIndication:
        messagebox.showinfo(title='温馨提示', message=str('%s = %s' % errorIndication))
        print (errorIndication)
    else:
        if errorStatus:
            print ('%s at %s\n' % (
                errorStatus.prettyPrint(),
                errorIndex and varBindTable[-1][int(errorIndex)-1] or '?'
                ))
        else:
            for varBindTableRow in varBindTable:
                for name, val in varBindTableRow:
                    print ('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                    messagebox.showinfo(title=str('%s' % child_oid + '所有子节点'), message=str('%s = %s' % (name.prettyPrint(), val.prettyPrint())))
def runit_2(loop=1):
  for i in range(loop):
    snmpget_all()


#########################################################################################################


# 当按钮被点击的时候执行click_button()函数
def click_button():
    # 使用消息对话框控件，showinfo()表示温馨提示
    runit(loop=1)
# 创建图片对象
# 通过image参数传递图片对象
button = tk.Button(window,text="get_value",command=click_button).pack()


def snmpget():
    ip = entry.get()
    oid = entry2.get()  
    com = entry3.get()
    cg = cmdgen.CommandGenerator() ##获得CommandGenerator对象
    errorIndication, errorStatus, errorIndex, varBinds = cg.getCmd(
     #0代表v1,1代表v2c 
    cmdgen.CommunityData('my-agent', com , 1), ##社区信息，my-agent ,public 表示社区名,1表示snmp v2c版本，0为v1版本
    cmdgen.UdpTransportTarget((ip, 161)),##这是传输的通道，传输到IP, 端口 161上(snmp标准默认161 UDP端口)
    oid ##传送的OID,个人认为MIB值
    )
    messagebox.showinfo(title=str('%s' % oid), message=str('%s = %s' % (varBinds[0][0],varBinds[0][1])))
    print (str(varBinds[0][1])); ##varBinds返回是一个stulp，含有MIB值和获得值
def runit(loop=1):
  for i in range(loop):
    snmpget()
    #print i

window.mainloop()
