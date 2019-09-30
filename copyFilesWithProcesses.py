from concurrent.futures import ProcessPoolExecutor
import os

def createFile(root, file, pathT):
    os.system('dd if={} of={}  count=1024000 bs=1024'.format(os.path.join(root, file), os.path.join(pathT, file)))


pathFrom = '/home/hovhannes/copyFrom/'
pathTo = '/home/hovhannes/copyTo/'

# r=root, d=directories, f = files
executor = ProcessPoolExecutor(max_workers=8);
for r, d, f in os.walk(pathFrom):
    for file in f:
        executor.submit(createFile(r, file, pathTo))

