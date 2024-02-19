import qrcode
from datetime import datetime


class MyQR:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(version=1, box_size=size, border=padding)

    def create_qr(self, foreground: str, background: str):
        user_input = input("Enter a text: ")
        try:
            self.qr.add_data(user_input)
            self.qr.make(fit=True)
            # Usar un timestamp en el nombre del archivo para hacerlo único
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            file_name = f'qr_code_{timestamp}.jpg'
            qr_image = self.qr.make_image(fill_color=foreground, back_color=background)
            qr_image.save(file_name)
            print(f'Creado correctamente! {file_name}')
        except Exception as e:
            print(f'Error: {e}')


def main():
    qr = MyQR(size=10, padding=2)
    qr.create_qr(foreground='black', background='white')


if __name__ == '__main__':
    main()
