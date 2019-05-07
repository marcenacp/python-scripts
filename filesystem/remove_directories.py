from shutil import rmtree


def remove_directory(path_to_delete):
    try:
        rmtree(path_to_delete)
        print('Removed directory {}'.format(path_to_delete))
    except OSError as e:
        print('Cannot remove path "{}": {}'.format(path_to_delete, e))
        pass


def remove_directories(list_of_directories):
    for path_to_delete in list_of_directories:
        remove_directory(path_to_delete)
