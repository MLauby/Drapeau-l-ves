## pour travailler sur les images nous avons besoin d’une extension de Python (appelée bibliothèque). ##

from PIL import Image

## Création d'un rectangle vert de 300 x 200 ##

img = Image.new("RGB",(300,200),"RGB(0,255,0)")

## Création d'une bande bleue de 100 x 200 ##

for x in range(0,100):
  for y in range (0,200):
    img.putpixel((x,y),(0,0,255))

## A vous de jouer !!! ##





## Enregistrement de l'image ##

img.save('FRANCE.jpg')
img.show()