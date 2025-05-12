import qrcode
import qrcode.image.svg
import os

os.makedirs("images/png", exist_ok=True)
os.makedirs("images/svg", exist_ok=True)

urls = {
    "main": "https://game-xpress.xfer.hr/",
    "register": "https://game-xpress.xfer.hr/register",
}

for name, url in urls.items():
    # PNG
    img_png = qrcode.make(url)
    img_png.save(f"images/png/{name}_qrcode.png")

    # SVG
    factory = qrcode.image.svg.SvgImage
    img_svg = qrcode.make(url, image_factory=factory)
    img_svg.save(f"images/svg/{name}_qrcode.svg")
