import os
import shutil
import random

def func(output_folder,images,obj_train_data,test_ratio):

    ##make folders for train - (image,txt) AND test - (image,txt)
    os.makedirs(os.path.join(output_folder, 'train','images'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'train','txt'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'test','txt'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'test','images'), exist_ok=True)


    image_list = [file for file in os.listdir(images) if os.path.isfile(os.path.join(images, file))]
    txt_list = [file for file in os.listdir(obj_train_data) if os.path.isfile(os.path.join(obj_train_data, file))]

    common_files = list(set([os.path.splitext(file)[0] for file in image_list]) & set([os.path.splitext(file)[0] for file in txt_list]))


    num_files_to_test = int(len(common_files) * test_ratio)

    random.shuffle(common_files)

    for i, file_name in enumerate(common_files):
        source_file1 = os.path.join(images, file_name + '.png')
        source_file2 = os.path.join(obj_train_data, file_name + os.path.splitext(txt_list[0])[1])

        if i < num_files_to_test:
            destination_folder_images = os.path.join(output_folder, 'test','images')
            destination_folder_txt = os.path.join(output_folder, 'test','txt')
        else:
            destination_folder_images = os.path.join(output_folder, 'train','images')
            destination_folder_txt = os.path.join(output_folder, 'train','txt')

        try:
            shutil.copy(source_file1, os.path.join(destination_folder_images, os.path.basename(source_file1)))
            shutil.copy(source_file2, os.path.join(destination_folder_txt, os.path.basename(source_file2)))
        except FileNotFoundError:
            try:
                source_file1 = os.path.join('images', file_name + '.jpeg')
                shutil.copy(source_file1, os.path.join(destination_folder_images, os.path.basename(source_file1)))
                shutil.copy(source_file2, os.path.join(destination_folder_txt, os.path.basename(source_file2)))
            except FileNotFoundError:
                source_file1 = os.path.join('images', file_name + '.jpg')
                shutil.copy(source_file1, os.path.join(destination_folder_images, os.path.basename(source_file1)))
                shutil.copy(source_file2, os.path.join(destination_folder_txt, os.path.basename(source_file2)))
            except:
                print('error')
        except:
            print('error')

