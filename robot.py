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
    url_list = ['http://openapi.tuling123.com/openapi/api/v2',"http://idc.emotibot.com/api/ApiKey/openapi.php"]
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
    chat_data = eval('{"cmd": "chat", "appid": apiKey[2], "userid": "qiao", "text": "哈哈", "location": ""}')

    #图灵聊天机器人
    @classmethod
    def tu_reply(cls,msg):
        djson=eval(cls.data_json%(msg,cls.apiKey[0]))
        resp = requests.post(cls.url_list[0],json=djson)
        return resp.json()['results'][0]['values']['text']

    #emotibot聊天机器人
    @classmethod
    def et_reply(cls,msg):
        res = requests.post(cls.url_list[1],params=cls.chat_data)
        return res.json()['data'][0]['value']

    #有消息windou声音提示
    @classmethod
    def alarm(cls):
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)

#监听别人发给我的消息,个人聊天
@itchat.msg_register(itchat.content.TEXT)
def single_reply(msg):
    print(msg.text)
    if msg['ToUserName'] == myself:
        res = Robot.tu_reply(msg.text)
        # res = Robot.et_reply(msg.text)
        msg.user.send(res)
        print('I response:',res)
    Robot.alarm()

#监听群聊中@我的消息，群聊
@itchat.msg_register(TEXT, isGroupChat=True)
def group_reply(msg):
    if '@%s'%mynickname in msg.text:
        print('%s send me: %s'%(msg.actualNickName, msg.text))
        res = Robot.tu_reply(msg.text)
        # res = Robot.et_reply(msg.text)
        msg.user.send('@%s %s'%(msg.actualNickName,res))
        print('I response:',res)
    else:
        print('%s:'%msg.actualNickName,msg.text)
    Robot.alarm()


itchat.run()









