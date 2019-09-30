import os

def createFile(root, file, pathT):
    os.system('dd if={} of={} count=1024000 bs=1024'.format(os.path.join(root, file), os.path.join(pathT, file)))


pathFrom = "/home/hovhannes/copyFrom/"
pathTo = "/home/hovhannes/copyTo/"

# r=root, d=directories, f = files

for r, d, f in os.walk(pathFrom):
    for file in f:
        createFile(r, file, pathTo)

