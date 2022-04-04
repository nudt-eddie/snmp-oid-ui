import tkinter as tk
from tkinter import messagebox
import pysnmp
from pysnmp.entity.rfc3413.oneliner import cmdgen
window = tk.Tk()

entry = tk.Entry(window,width=40)
entry2 = tk.Entry(window,width=40)
entry3 = tk.Entry(window,width=40)
entry.pack()
entry2.pack()
entry3.pack()
def get_ip():
    ip = entry.get()		# 调用get()方法，将Entry中的内容获取出来
    print(ip)
def get_oid():
    oid = entry2.get()		# 调用get()方法，将Entry中的内容获取出来
    print(oid)
def get_value():
    value = entry3.get()		# 调用get()方法，将Entry中的内容获取出来
    print(value)
button = tk.Button(window,text='ip',command=get_ip).pack()
button2 = tk.Button(window,text='oid',command=get_oid).pack()
button3 = tk.Button(window,text='社区',command=get_value).pack()


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
    cmdgen.UdpTransportTarget((ip, 161)),##这是传输的通道，传输到IP 192.168.70.237, 端口 161上(snmp标准默认161 UDP端口)
    oid ##传送的OID,个人认为MIB值
    )
    messagebox.showinfo(title='温馨提示', message=str(varBinds[0][1]))
    print (str(varBinds[0][1])); ##varBinds返回是一个stulp，含有MIB值和获得值
def runit(loop=1):
  for i in range(loop):
    snmpget()
    #print i






window.mainloop()
