import qrcode

data = 'https://www.leunghoyin.hk'

img = qrcode.make(data)

img.save('qr.png')