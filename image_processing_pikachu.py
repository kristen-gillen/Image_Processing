from PIL import Image, ImageFilter
img = Image.open('./pikachu_images/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png', 'png')
gray_img = img.convert('L')
# gray_img.save('gray.png', 'png')
# gray_img.show()
#crop image
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save('cropped.png','png')
# region.show()
#unsplash is good place for images
#Thumbnail method is useful to keep aspect ratio
img.thumbnail((400,400)) #400 is max
img.save('pikachu_thumb.jpg')