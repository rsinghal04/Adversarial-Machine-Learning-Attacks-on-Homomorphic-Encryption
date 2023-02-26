import os
from client import *
import glob

#folder = "D:\PRADA\prada-protecting-against-dnn-model-stealing-attacks\data\F-MNIST"
folder = "D:\PRADA\prada-protecting-against-dnn-model-stealing-attacks\data\lfw\*\*"

#for filename in os.listdir(folder):
 #   run(os.path.join(folder,filename))

for img in glob.glob(folder):
    run(img)