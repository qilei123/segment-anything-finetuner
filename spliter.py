import glob
import os

data_root = 'segment-anything/DATA/TN-SCUI2020/segmentation/augtrain'

img_list = sorted(glob.glob(os.path.join(data_root,"image/*.bmp")))

train_num = int(len(img_list)/10*6)

train_files =open(os.path.join(data_root,'train.txt'), "w")
val_files = open(os.path.join(data_root,'val.txt'), "w")

for file_dir in img_list[:train_num]:
    file_name = os.path.split(file_dir)[1]
    train_files.write( os.path.splitext(file_name)[0]+ "\n")
    
for file_dir in img_list[train_num:]:
    file_name = os.path.split(file_dir)[1]
    val_files.write( os.path.splitext(file_name)[0]+ "\n")
    