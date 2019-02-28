import itchat
from apscheduler.schedulers.blocking import BlockingScheduler #用于定时
import time

#登陆并保持下次自动登陆
itchat.auto_login(enableCmdQR=True,hotReload=2)

#获取好友列表并显示
def getFriendList():
friend=itchat.get_friends()
    for fd in friend:
        if fd['RemarkName']=='':
            print(fd['NickName'],fd['UserName'])
        else:
            print(fd['RemarkName'],fd['UserName'])

#给指定的人发消息
def sendtofriend():
    Name='django'
    msgs='123'
    UserName=itchat.search_friends(name=Name)[0]['UserName']
    print(UserName)
    itchat.send_msg(msgs,toUserName=UserName)

#给群发消息
def sendtogroup():
    groups=itchat.search_chatrooms(name='电信3')[0]['UserName']
    # print(groups)
    msg='第三组交'
    print(groups)
    itchat.send_msg(msg,toUserName=groups)

def clock():
    scheduler=BlockingScheduler()
    scheduler.add_job(sendtogroup,'cron',day_of_week='0-6',hour=21,minute=54)
    scheduler.start()

if __name__ == "__main__":
    clock()
    #sendtogroup()  
    itchat.run(True)
