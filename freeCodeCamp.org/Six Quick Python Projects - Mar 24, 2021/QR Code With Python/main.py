# pip install qrcode Pillow pyzbar
# 1.
# import qrcode

# data = 'Don\'t forget to subscribe'

# img = qrcode.make(data)

# img.save('C:/Users/BOSS/Documents/QR_Code_with_Python/myqrcode.png')

# 2.
# import qrcode

# data = 'Don\'t forget to subscribe'

# qr = qrcode.QRCode(version = 1, box_size=10, border=5)

# qr.add_data(data)

# qr.make(fit=True)
# img = qr.make_image(fill_color = 'red', back_color='white')

# img.save('C:/Users/BOSS/Documents/QR_Code_with_Python/myqrcode1.png')

# 3.
from ctypes import cdll
cdll.LoadLibrary("full/path/to/libzbar-64.dll")
from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/BOSS/Documents/QR_Code_with_Python/myqrcode.png')

result = decode(img)

print(result)