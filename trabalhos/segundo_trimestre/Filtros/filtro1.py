from PIL import Image

#Abrindo imagem
imagem = Image.open('r34.jpg')

#Obtendo as dimensões da imagem
largura, altura = imagem.size
print(largura)
print(altura)

for x in range(altura):
  for y in range(altura):
    pixel=imagem.getpixel((x,y))
    novo_pixel=tuple(255-valor for valor in pixel)
    imagem.putpixel((x,y),novo_pixel)

imagem.save('r34_negativo.jpg')
