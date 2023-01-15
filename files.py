import time

from PIL import Image

def read_img(name):
    im = Image.open(name, "r")
    im.show()



def read_file(name):
    f = open(name,"r")
    lines = f.readlines()
    for line in lines:
        print(line)
        time.sleep(3)
        
    f.close()