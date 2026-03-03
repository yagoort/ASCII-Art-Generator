from easy_ascii import EasyAscii

# file path
file_name = "test.jpg"
# New EasyAscii object
my_ascii_generator = EasyAscii(file_name)

# Now let's create two different ascii .txt files
my_ascii_generator.genGaussianBlur("img_blurred_reversed", True)
my_ascii_generator.genGaussianBlur("img_weighted_reversed", True)
