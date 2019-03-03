import itchat
from apscheduler.schedulers.blocking import BlockingScheduler #用于定时

from msg import *  #记录回复文本的模块

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
    print('@'+Name+':'+msgs)

#给群发消息
def sendtogroup():
    name='电信3'
    msg=schedule()    
    groups=itchat.search_chatrooms(name=name)[0]['UserName']
    itchat.send_msg(msg,toUserName=groups)
    print('@'+name+':'+msg)

def send_greetins():
    name = '电信3'


#定时任务
def time_task():
    print('定时任务：running...')
    scheduler=BlockingScheduler()
    scheduler.add_job(sendtogroup,'cron',day_of_week='0-6',hour=8,minute=50)
    scheduler.start()
    
def init():
    itchat.send_msg("task running...",toUserName='filehelper')

if __name__ == "__main__":
    init()
    time_task()
    #sendtogroup()  
    #sendtofriend()
    itchat.run(True)
