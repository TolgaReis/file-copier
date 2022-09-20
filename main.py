import shutil
import sys

try:
    src = sys.argv[1:][0]
    dst = sys.argv[1:][1]
    shutil.copyfile(src, dst)
except IndexError:
    print("Source or destination argument does not exist!")
except FileNotFoundError:
    print("File not found in directory!")
