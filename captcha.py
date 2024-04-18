# importing the required libraries
from captcha.image import ImageCaptcha
# specify dimensions
image = ImageCaptcha(width = 100, height = 100)
# enter the text to create its captcha
captcha_text = input("Please enter text: ")
# generate the text-based captcha
data = image.generate(captcha_text)
# save the captcha image file
image.write(captcha_text, (captcha_text) + ".png")