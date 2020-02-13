import itchat,time,requests

#key
KEY = '98402a996a1f41b7b75aa427ca1b7902'

#登录微信
itchat.auto_login(hotReload = True)

#获取自己的session
myself = itchat.get_friends()[0]['UserName']

#监听别人发给我的消息
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    if msg['ToUserName'] == myself:
        itchat.send(msg['Text'],toUserName='FromUserName')




itchat.run()








