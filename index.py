import requests

img_url = "https://persianencrypter.github.io/frame/20220723_032154_0000.jpg"
req = requests.get(img_url)
file = open("ok.jpg", "wb")
file.write(req.content)
file.close()
file = open("ok.jpg", "rb")
data = file.read()
data = {"realImg": data}
urlphp = ""
requests.post(urlphp, data=data)




