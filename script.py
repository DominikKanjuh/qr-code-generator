import qrcode
import os

os.makedirs("images", exist_ok=True)

urls = {
    "main": "https://game-xpress.xfer.hr/",
    "register": "https://game-xpress.xfer.hr/register",
}

for name, url in urls.items():
    img = qrcode.make(url)
    img.save(f"images/{name}_qrcode.png")
