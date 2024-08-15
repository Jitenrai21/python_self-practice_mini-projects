import qrcode 
from PIL import Image
# img = qr.make('https://jitenrai.com.np/')
# img.save("JitenRai_Portfolio.png")

# The above commented code creates and saves a qr in the file containing folder for the given url.

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data("https://jitenrai.com.np/")
qr.make(fit=True)

img = qr.make_image(fill_color="brown", back_color="white")

img.save('qrcode.png')