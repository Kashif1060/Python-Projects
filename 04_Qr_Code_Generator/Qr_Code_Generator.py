import qrcode
from IPython.display import display

# Enter URL of any website here
input_URL = "https://www.wikipedia.com/"

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=5,
)

qr.add_data(input_URL)
qr.make(fit=True)

# Convert into image
img = qr.make_image(fill_color="Black", back_color="white")

# Save the QR code
img.save("wikipedia_qrcode.png")

# Display the QR code
display(img)

print(qr.data_list)
