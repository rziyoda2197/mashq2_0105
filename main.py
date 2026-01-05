from sana import yosh_top


from datetime import datetime
hozirgi_yil = datetime.now().year

tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting: "))


natija = yosh_top(hozirgi_yil, tugilgan_yil)
print(natija)
