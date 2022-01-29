###Codes to genrate QR Code
###genrates black and white qrcode
import qrcode as qr
img= qr.make("https://github.com/lokesh29")
img.save("lokesh_git.png")

###genrates codes with desired color an size
import qrcode
import PIL
qr=qrcode.QRCode(version= 1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10, border=4,)
qr.add_data("https://github.com/lokesh29")
qr.make(fit=True)
img=qr.make_image(fill_color="black", back_color="white")
img.save("lokesh_git.png")
