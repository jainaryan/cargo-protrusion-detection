import os
import shutil
path_to_names =  'data/annotated data/temp/annotations'
folder_to_look = 'data/annotated data/temp/images'
output_folder = 'data/annotated data/temp/new-images'

def copy_files_from_list(path_to_names, folder_to_look, output_folder):
    # Get a list of .txt filenames in path_to_names
    txt_filenames = [f for f in os.listdir(path_to_names) if f.lower().endswith('.txt')]

    # Iterate through .txt files and copy matching image files
    for txt_filename in txt_filenames:
        # Remove the extension to get the base filename
        base_filename = os.path.splitext(txt_filename)[0]

        # Check for image files with matching names in folder_to_look
        for image_extension in ['.jpg', '.jpeg', '.png']:
            image_filename = base_filename + image_extension
            source_path = os.path.join(folder_to_look, image_filename)
            destination_path = os.path.join(output_folder, image_filename)

            if os.path.exists(source_path):
                shutil.copy(source_path, destination_path)
                print(f"Copied: {image_filename}")
                break  # Stop checking other extensions if a match is found
            else:
                print(f"File not found: {image_filename}")

copy_files_from_list(path_to_names, folder_to_look, output_folder)

'''
import os
import shutil
path_to_test_data = 'data/annotated data/temp/images'
path_to_annotations = '.\\data\\annotated data\\temp\\annotations'
output_path = 'data/annotated data/temp/test-annotations'
def copy_and_delete_matching_files(path_to_test_data, path_to_annotations, output_folder):
    # Get a list of filenames in path_to_test_data
    test_data_filenames = [f for f in os.listdir(path_to_test_data) if f.endswith('.jpg')]

    # Get a list of filenames in path_to_annotations
    annotation_filenames = [f for f in os.listdir(path_to_annotations) if f.endswith('.txt')]

    # Ensure the output folder exists; create if not
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through files in path_to_test_data, copy matching ones, and delete from path_to_annotations
    for test_filename in test_data_filenames:
        # Assuming that the corresponding annotation file has the same name but with a .txt extension
        annotation_filename = test_filename[:-4] + '.txt'

        if annotation_filename in annotation_filenames:
            source_path = os.path.join(path_to_annotations, annotation_filename)
            destination_path = os.path.join(output_folder, annotation_filename)

            # Copy the file
            shutil.copy(source_path, destination_path)
            print(f"Copied: {annotation_filename}")

            # Delete the file from path_to_annotations
            os.remove(source_path)
            print(f"Deleted: {annotation_filename}")


copy_and_delete_matching_files(path_to_test_data, path_to_annotations, output_path)



'''