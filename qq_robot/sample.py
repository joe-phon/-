import json
import requests
import re
# 插件加载方法： 
# 先在命令行运行 qqbot ，
# 启动成功后，在另一个命令行窗口输入： qq plug qqbot.plugins.sample
def answerMessage(ask_message):
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    body = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": ""
            }
        },
        "userInfo": {
            "apiKey": "6c293e88435c4ef99b86f8d15ed25a3f",
            "userId": "qiao"
        }
    }
    body['perception']['inputText']['text'] = ask_message
    data = json.dumps(body)
    
    response = requests.post(url, data = data)
    retext = response.text
    
    answ_text = re.findall((re.compile('{.*?results":.*?values.*?text":"(.*?)"}', re.S)), retext)
    text = str(answ_text[0])
    try:
        answ_shows = re.findall((re.compile('{.*?showtext":"(.*?)",', re.S)), retext)
        return str(answ_shows[0])
    except IndexError:
        answ_names = re.findall((re.compile('{.*?name":"(.*?)",', re.S)), retext)
        answ_urls = re.findall((re.compile('{.*?detailurl":"(.*?)"}', re.S)), retext)
        try:
            for index in range(3):
                text = text+"\n原标题"+str(index+1)+":"+str(answ_names[index])+"\n链接地址："+str(answ_urls[index])
            return (text)
        except IndexError:
            return (str(answ_text[0]))
                
def onQQMessage(bot, contact, member, content):
        answer = answerMessage(content)
        bot.SendTo(contact, answer)
