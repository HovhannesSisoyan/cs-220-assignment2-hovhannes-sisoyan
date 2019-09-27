import os

pathFrom = '/home/hovhannes/mFrom/'
pathTo = '/home/hovhannes/mTo/'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(pathFrom):
    for file in f:
        files.append(os.path.join(r, file))
        os.system('dd if={} of={}'.format(os.path.join(r, file), pathTo+r+file))
for f in files:
    print(f)


