import os


def create_directory(path_to_create):
    try:
        os.mkdir(path_to_create)
        print('Created directory {}'.format(path_to_create))
    except FileExistsError as e:
        print('Directory {} already exists: {}'.format(path_to_create, e))
        pass


def create_directories(list_of_directories):
    for path_to_create in list_of_directories:
        create_directory(path_to_create)
