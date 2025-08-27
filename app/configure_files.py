import os

def initialize_files():
    app_data_path = os.getenv('APPDATA')
    folder_path = app_data_path + r"\StudyManager"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        return folder_path
    else:
        return folder_path

