import os

'''
读取文件夹下所有文件的名字并把他们用列表存起来
'''
path = "fileList"
if __name__ == '__main__':
    dirs = os.listdir(path)
    print('type:', type(dirs[0]))
    for dirName in dirs:
        print(dirName)
