import requests
import time

bot = "5007640887:AAH5eiFbpasf4XpEQ91evPxhDV4M1YA6JDk"
url = "https://api.telegram.org"
chatId = "-483158329"
urlFinal = url+"/bot"+bot+"/sendMessage?chat_id="+chatId+"&text="


img_url = "https://persianencrypter.github.io/frame/20220723_032154_0000.jpg"
req = requests.get(img_url)
file = open("ok.jpg", "wb")
file.write(req.content)
file.close()
file = open("ok.jpg", "rb")
data = file.read()
data = {"realImg": data}
file.close()
urlphp = "https://coldphp.herokuapp.com/"
requests.post(urlphp, data=data)
requests.get(urlFinal+"start download")
time.sleep(5)
reqq = requests.get(urlphp)
newF = open("final.jpg", "wb")
newF.write(reqq.content)
newF.close()
ok = open("final.jpg", "rb")
requests.get(urlFinal+"start sending")
urlForImag = url+"/bot"+bot+"/sendPhoto"
chatDict = {"chat_id":chatId}
fileDict = {"photo":ok}
reqqq = requests.post(urlForImag, data=chatDict, files=fileDict)
requests.get(urlFinal+str(reqqq.text))



