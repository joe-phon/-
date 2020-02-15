import itchat,time,requests,random
from itchat.content import TEXT
import winsound

#登录微信
itchat.auto_login(hotReload = True)

#获取自己的session
myself = itchat.get_friends()[0]['UserName']
mynickname = itchat.get_friends()[0]['NickName']
class Robot:
#key,请求url
    apiKey = ['98402a996a1f41b7b75aa427ca1b7902','6c293e88435c4ef99b86f8d15ed25a3f','87a7dad6235e0537377e2bb05188f88e']
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    data_json = '''{
        "reqType":0,
        "perception": {
            "inputText": {
                "text": '%s'
            }
        },
        "userInfo": {
            "apiKey": '%s',
            "userId": "qiao"
        }
    }'''

    @classmethod
    def auto_reply(cls,msg):
        djson=eval(cls.data_json%(msg,random.choice(cls.apiKey)))
        resp = requests.post(cls.url,json=djson)
        return resp.json()['results'][0]['values']['text']
    @classmethod
    def alarm(cls):
    # Windows嗡鸣声
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)

#监听别人发给我的消息,单个人聊天
@itchat.msg_register(itchat.content.TEXT)
def single_reply(msg):
    print(msg.text)
    if msg['ToUserName'] == myself:
        res = Robot.auto_reply(msg.text)
        msg.user.send(res)
        print('I response:',res)
    Robot.alarm()

@itchat.msg_register(TEXT, isGroupChat=True)
def group_reply(msg):
    if '@%s'%mynickname in msg.text:
        print('%s send me: %s'%(msg.actualNickName, msg.text))
        res = Robot.auto_reply(msg.text)
        msg.user.send('@%s %s'%(msg.actualNickName,res))
        print('I response:',res)
    else:
        print('%s:'%msg.actualNickName,msg.text)
    Robot.alarm()


itchat.run()









