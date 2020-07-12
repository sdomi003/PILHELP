from PIL import Image
from PIL import ImageDraw

# First, get the image you want on the left side
im1 = Image.open('/Users/samueldominguez/Downloads/pct.jpg')

# Next, create a new blank white image to write over.
im2 = Image.new('RGB', (im1.width, im1.height), color = 'white')

# This part is to write words on the blank white image
d = ImageDraw.Draw(im2)
d.text((10,100), "Hello World", fill = (0, 0, 0))

# Now we create a new image which will be a composite of the two images above
newImage = Image.new('RGB', (im1.width + im2.width, im2.height))
# as you can see, we left enough width to paste both images side by side

# now past the two images side by side.
newImage.paste(im1, (0,0))
newImage.paste(im2, (im1.width, 0))

# finally, save the new image that is a composite of both images
newImage.save('/Users/samueldominguez/Downloads/newImage.jpg')
