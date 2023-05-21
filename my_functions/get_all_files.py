import os

def get_all_files(root_folder: str, files: list, file_ext=None, name_filter=None):
    # collect root_folder content
    folder_content = [os.path.join(root_folder, i) for i in os.listdir(root_folder)]

    # collect files
    # add files to files
    # collect subfolders
    subfolders = []
    found_files = []  # collect all files
    for i in folder_content:
        if os.path.isfile(i):
            found_files.append(i)
        else:
            subfolders.append(i)

    # collect files based on file_ext
    if file_ext:
        found_files_with_ext = []
        for i in found_files:
            file_path, ext = os.path.splitext(i)
            if ext.lower() == file_ext.lower():
                found_files_with_ext.append(i)
        
        found_files = found_files_with_ext

    # collect files based on name filter
    if name_filter:
        found_files_with_name = []
        for i in found_files:
            file_name = os.path.basename(i)
            if name_filter.lower() in file_name.lower():
                found_files_with_name.append(i)

        found_files = found_files_with_name
    
    files += found_files

    for folder in subfolders:
        get_all_files(folder, files, file_ext, name_filter)