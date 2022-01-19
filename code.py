import pyqrcode
import png
from pyqrcode import QRCode
#here tap your own url 
#I choose url of my account GitHub :)
s="https://github.com/ChaimaeBougattaya"
url=pyqrcode.create(s)
#generate a png and svg files
url.svg("myqr.svg",scale=8)
url.png("myqr.png",scale=6)