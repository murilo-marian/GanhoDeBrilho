

def readImage(filepath):
    with open(filepath, "r") as image:
        imageType = image.readline().strip()
        assert imageType == "P2", "Não é P2"
        
        line = image.readline().strip()
        
        width, height = map(int, line.split())
        grayscaleBits = int(image.readline().strip())
        
        pixels = []
        for _ in range(height):
            row = []
            row.extend(image.readline().split())
            pixels.append(row)
        
    return pixels, grayscaleBits, width, height

def aumentarBrilho(pixels, bits, width, height):
    convertedPixels = []
    for y in range(height):
        newRow = []
        for x in range(width):
            chosenPixel = pixels[y][x]
            if (int(chosenPixel) * 1.2 <= bits):
                newValue =  round(int(chosenPixel) * 1.2)
            else:
                newValue = bits
            newRow.append(newValue)
        convertedPixels.append(newRow)
    
    return convertedPixels


def saveIMG(filename, pixels, width, height, bits):
    with open(filename, "w") as newImage:
        newImage.write("P2\n")
        newImage.write(str(width) + " " + str(height) + "\n")
        newImage.write(str(bits) + "\n")
        
        for row in pixels:
            newImage.write(" ".join(map(str, row)) + "\n")
            
            
originalIMG = "newIMG720p.pgm"

pixels, bits, width, height = readImage(originalIMG)
convertedPixels = aumentarBrilho(pixels, bits, width, height)

output = "newIMGBrilho.pgm"
saveIMG(output, convertedPixels, width, height, bits)