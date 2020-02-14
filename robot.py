import itchat,time,requests

#登录微信
itchat.auto_login(hotReload = True)

#获取自己的session
myself = itchat.get_friends()[0]['UserName']

class Robot:
#key,请求url
# apiKey = '98402a996a1f41b7b75aa427ca1b7902'
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    data_json = '''{
        "reqType":0,
        "perception": {
            "inputText": {
                "text": '%s'
            }
    
        },
        "userInfo": {
            "apiKey": '98402a996a1f41b7b75aa427ca1b7902',
            "userId": "qiao"
        }
    }'''

    @classmethod
    def auto_reply(cls,msg):
        djson=eval(cls.data_json%msg)
        resp = requests.post(cls.url,json=djson)
        return resp.json()['results'][0]['values']['text']

#监听别人发给我的消息
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    # print(msg.text)
    if msg['ToUserName'] == myself:
        # print(Robot.auto_reply(msg.text))
        itchat.send(Robot.auto_reply(msg.text),toUserName=msg['FromUserName'])

itchat.run()









