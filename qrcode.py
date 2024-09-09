import qrcode

imagem = qrcode.make("www.insira-o-link.com.br")
imagem.save("qrcode.png")
