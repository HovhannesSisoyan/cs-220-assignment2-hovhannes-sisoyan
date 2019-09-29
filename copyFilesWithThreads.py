from concurrent.futures import ThreadPoolExecutor
import os

def createFile(root, file, pathT):
    os.system('dd if={} of={}'.format(os.path.join(root, file), os.path.join(pathT, file)))


pathFrom = '/home/hovhannes/copyFrom/'
pathTo = '/home/hovhannes/copyTo/'

# r=root, d=directories, f = files

for r, d, f in os.walk(pathFrom):
    for file in f:
        executor = ThreadPoolExecutor(100);
        feature = executor.submit(createFile(r, file, pathTo))

