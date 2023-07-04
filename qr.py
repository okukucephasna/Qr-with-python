import qrcode
from reportlab.pdfgen import canvas

def generate_qr_code(message, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(message)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("temp.png")

    c = canvas.Canvas(filename)
    c.drawImage("temp.png", 100, 100)
    c.save()

    print(f"QR code saved as {filename}")

# Example usage
message = input("Enter the message to be embedded in the QR code: ")
filename = input("Enter the filename to save the PDF: ")
generate_qr_code(message, filename)
