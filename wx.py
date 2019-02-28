import itchat
from apscheduler.schedulers.blocking import BlockingScheduler #用于定时
import datetime

def schedule():
    time=datetime.datetime.now()
    day=time.weekday()
    print(day)
    if day == 4:
        msgs="""[耶]早上好~
[太阳][太阳][太阳]周五课表[太阳][太阳][太阳]
[强]1-2节：概率论与数理统计 
             10#二合堂"""
    elif day == 1:
        msgs="""[耶]早上好~
[太阳][太阳][太阳]周二课表[太阳][太阳][太阳]
[强]1-2节：信号与系统
             11#403
[强]3-4节：概率论与数理统计 
             10#二合堂
[强]7-8节：中国近代史纲要
             10#一合堂"""
    elif day == 2:
        msgs="""[耶]早上好~
[太阳][太阳][太阳]周三课表[太阳][太阳][太阳]
[强]1-2节：数字电路 
             1#516"""
    elif day == 3:
        msgs="""[耶]早上好~
[太阳][太阳][太阳]周四课表[太阳][太阳][太阳]
[强]1-2节：大学英语
             1#703
[强]3-4节：信号与系统
             1#516
[强]5-6节：体育"""
    elif day == 0:
        msgs="""[耶]早上好~
[太阳][太阳][太阳]周一课表[太阳][太阳][太阳]
[强]1-2节：数字电路 
             1#709
[强]5-6节：信号与系统实验
             3#501
             """
    else:
        msgs=' '
    return(msgs)

#登陆并保持下次自动登陆
itchat.auto_login(enableCmdQR=2,hotReload=True)

#获取好友列表并显示
def getFriendList():
    friends=itchat.get_friends()
    for fd in friends:
        if fd['RemarkName']=='':
            print(fd['NickName'],fd['UserName'])
        else:
            print(fd['RemarkName'],fd['UserName'])

#给指定的人发消息
def sendtofriend():
    Name='杨卓'
    msgs=schedule()
    UserName=itchat.search_friends(name=Name)[0]['UserName']
    #print(UserName)
    itchat.send_msg(msgs,toUserName=UserName)
    #print({}Name{}msg.format('@',':'))

#给群发消息
def sendtogroup():
    name='电信3'
    msg=schedule()    
    groups=itchat.search_chatrooms(name=name)[0]['UserName']
    itchat.send_msg(msg,toUserName=groups)
    #print({}name{}msg.format('@',':'))

def time_task():
    print('定时任务：running...')
    scheduler=BlockingScheduler()
    scheduler.add_job(sendtogroup,'cron',day_of_week='1-5',hour=8,minute=50)
    scheduler.start()
    



if __name__ == "__main__":
    time_task()
    #sendtogroup()  
    #sendtofriend()
    itchat.run(True)
