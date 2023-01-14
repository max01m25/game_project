import time
def read_file(name):
    f = open(name,"r")
    lines = f.readlines()
    for line in lines:
        print(line)
        time.sleep(3)
        
    f.close()