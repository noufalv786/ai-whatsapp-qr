import qrcode
import json

base_url = "https://noufalv786.github.io/ai-whatsapp-qr/index.html?tool="

with open("tools.json", "r") as f:
    tools = json.load(f)

for key, description in tools.items():
    url = f"{base_url}{key}"
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    filename = f"qr_{key}.png"
    img.save(filename)
    print(f"QR code for {key} saved as {filename}")
