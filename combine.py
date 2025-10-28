from PIL import Image

# Open images
img1 = Image.open("ER model GDP.jpg")
img2 = Image.open("ER model Olympics.jpg")
img3 = Image.open("ER model inflation.jpg")

# Find the maximum width and total height
width = max(img1.width, img2.width, img3.width)
height = img1.height + img2.height + img3.height

# Create a new blank image with a white background
combined = Image.new("RGB", (width, height), (255, 255, 255))

# Paste images one by one
y_offset = 0
for img in [img1, img2, img3]:
    combined.paste(img, (0, y_offset))
    y_offset += img.height

# Save as PNG
combined.save("teamX_ERmodel.png")
print("Combined image saved as combined.png")