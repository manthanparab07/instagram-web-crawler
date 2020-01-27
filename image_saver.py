# imported the requests library
import requests
import sys

image_url = str(sys.argv[1])
file_name = str(sys.argv[2])

# image_url = "https://instagram.fnag1-1.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/81242731_121878659312636_5653829913521655556_n.jpg?_nc_ht=instagram.fnag1-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=z-TAuoJBMOUAX_rkGFX&oh=1c5df3aa7f6bff490b86f0d7306d280c&oe=5EBB5183"

# URL of the image to be downloaded is defined as image_url
r = requests.get(image_url)  # create HTTP response object

# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open(file_name + ".jpg", 'wb') as f:

    # Saving received content as a png file in
    # binary format

    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)
