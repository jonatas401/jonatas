from PIL import Image, ImageDraw

# Abrir a imagem
img = Image.open("profile.jpg").convert("RGBA")

# Tamanho mínimo para o recorte
size = min(img.size)

# Coordenadas para o corte quadrado central
x = (img.width - size) // 2
y = (img.height - size) // 2
img_cropped = img.crop((x, y, x + size, y + size))

# Criar máscara circular
mask = Image.new('L', (size, size), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, size, size), fill=255)

# Aplicar máscara
final_img = Image.new("RGBA", (size, size))
final_img.paste(img_cropped, (0, 0), mask=mask)

# Salvar imagem circular
final_img.save("profile_circular.png")
