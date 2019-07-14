import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of pathswhats
    """

    list_of_paths = []
    try:
        path_objects = os.listdir(path)
    except:
        print("The path you have selected is not valid / there is no file in your folder")
        return None
    for object in path_objects:
        if object.endswith(suffix) and os.path.isfile(os.path.join(path, object)):
            list_of_paths.append(os.path.join(path, object))
        else:
            try:
                if len(find_files(suffix,os.path.join(path, object))) > 0:
                    list_of_paths += find_files(suffix,os.path.join(path, object))
            except:
                continue

    return list_of_paths
