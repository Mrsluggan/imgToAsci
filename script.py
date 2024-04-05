
from PIL import Image, ImageColor

done = False

print("Omvandlar bild till Ascii Art")
print("Detta kommer ta en sekund")
im = Image.open("mona.jpg")
stop = 0
im = im.resize((50,50))
width,height = im.size
gray = im.convert("L")




while not done:
    f = open("text.txt", "w")
    
    
    for x in range(height):
        f.write("\n")
        for y in range(width):
            pixel = gray.getpixel((y, x))
            pixelColor = pixel
            if pixelColor > 0 and pixelColor < 17:
                f.write("@")
            elif pixelColor > 17 and pixelColor < 51:
                f.write("%")
            elif pixelColor > 51 and pixelColor < 87:
                f.write("#")
            elif pixelColor > 87 and pixelColor < 167:
                f.write("*")
            elif pixelColor > 167 and pixelColor < 209:
                f.write("+")
            elif pixelColor > 209 and pixelColor < 255:
                f.write("=")

            
            stop += 1

            if(height == stop):
                done = True
print("klart!")
f.close()

