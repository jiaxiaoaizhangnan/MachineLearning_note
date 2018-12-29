import os
import datetime  #定时发送，以及日期
import shutil  #文件操作
import smtplib  #邮件模块
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time
# import xlwt  #excel写入

def eSend(sender, receiver, username, password, smtpserver, subject, e_content):
    try:
#邮件头
       message = MIMEMultipart()
       message['From'] = sender#发送
       message['To'] = ";".join(receiver)#收件
       message['Subject'] = Header(subject, 'utf-8')
       message.attach(MIMEText(e_content, 'plain', 'utf-8'))# 邮件正文

# # 构造附件
#        att1 = MIMEText(open(file_path+file_name,'rb').read(), 'base64', 'utf-8')
#        att1["Content-Type"] = 'application/octet-stream'
#        att1["Content-Disposition"] = "attachment;filename="+file_name
#        message.attach(att1)

#执行
       smtp = smtplib.SMTP()
       smtp.connect(smtpserver) #连接服务器
       smtp.login(username, password) #登录
       smtp.sendmail(sender, receiver, message.as_string())  #发送
       smtp.quit()
       print("SEND")
    except:
       print("SEND FAILED")
SEND_ONCE = True
while SEND_ONCE:
#配置
    #__time_____
    ehour=13#定时小时
    emin=50#定时分钟
    esec=0#定时秒
    current_time = time.localtime(time.time())      #当前时间date
    cur_time = time.strftime('%H%M', time.localtime(time.time()))             #当前时间str
    #__mysql_____

    #__email_____
    sender = 'jiaxiao222@126.com'  # 发件人邮箱
    receiver = ['jiaxiao222@126.com']  # 收件人邮箱，可以多个（列表形式）群发
    username = 'jiaxiao222@126.com'  # 发件人姓名
    password = '*******'  # smtp密码，qq是给你分配一串，163是自己设置
    smtpserver = 'smtp.126.com'  # 邮箱服务器

    subject = "工作总结"      #邮件标题
    # e_content = '{0:^27}\n{1:^27}\n{2:^25}\n{3:^25}'.format('i','/   \\','(-----)','(--------)')   #邮件正文
    e_content = 'A. ***\nB. ****'
    #__file_____
    # file_path = "D:/"    #文件位置
    # file_name="shit.xls"    #文件名
    # fLocate = file_path + file_name     #文件路径
    # file_subject='I', 'MISS', 'U' #sheet标题
    # file_sheet='ok'  #sheet名
    # style0=xlwt.XFStyle()
    # style0.num_format_str='YYYY-MM-DD'
#操作
    if ((current_time.tm_hour == ehour) and (current_time.tm_min == emin) and (current_time.tm_sec == esec)):
        print ("START")
        SEND_ONCE = False
        # eWrite(fLocate, file_sheet, file_subject,style0)
        eSend(sender, receiver, username, password, smtpserver, subject, e_content)
        print(cur_time)
    time.sleep(1)
