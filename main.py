import qrcode

qr = qrcode.make("www.google.com")
qr.save("google.png")

qr1 = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=20,
                    border=2)
qr1.add_data("www.google.com")
qr1.make(fit=True)

qr1.make_image(fill_color="black", back_color="white")
qr.save("advance.png")