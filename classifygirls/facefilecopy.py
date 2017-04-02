import os
from shutil import copyfile

label_dict = {
    'aoyama': 0, 'jissen': 1, 'keio': 2, 'phoenix': 3, 'rika': 4,
    'rikkyo': 5, 'seikei': 6, 'sophia': 7, 'todai': 8, 'tonjo': 9
}

def main():
    for srcpath, _, files in os.walk('faces'):
        if len(_):
            continue
        dstpath = 'modeldata'
        foldername = ''
        for label in label_dict:
            if label in srcpath:
                if '2015' in srcpath:
                    foldername = '{}/{}/{}/'.format(dstpath, 'test', label)
                else:
                    for year in range(2007, 2015):
                        dstpath = dstpath.replace('{}{}'.format(label, year), '')

                    foldername = '{}/{}/{}/'.format(dstpath, 'train', label)
                break
        if foldername != '':
            if not os.path.exists(foldername):
                os.makedirs(foldername)
            for filename in files:
                if filename.startswith('.'):
                    continue
                copyfile('{}/{}'.format(srcpath, filename), '{}/{}'.format(foldername, filename))




if __name__ == '__main__':
    main()
    # for year in range(2007, 2015):
    #     print(year)