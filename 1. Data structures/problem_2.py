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


path1 = '/home/vasilis/Dropbox/Development/Udacity - Data Strctures and Algorithms/Section2Submissions'
print(find_files('.py', path1))

"""
Returns:

['/home/vasilis/Dropbox/Development/Udacity - Data Strctures and Algorithms/Section2Submissions/problem_4.py',
 '/home/vasilis/Dropbox/Development/Udacity - Data Strctures and Algorithms/Section2Submissions/problem_1.py',
 '/home/vasilis/Dropbox/Development/Udacity - Data Strctures and Algorithms/Section2Submissions/problem_2_directory/pythontest1.py',
 '/home/vasilis/Dropbox/Development/Udacity - Data Strctures and Algorithms/Section2Submissions/problem_2_directory/problem_2_subdirectory/pythonsubtest2.py',
 '/home/vasilis/Dropbox/Development/Udacity - Data Strctures and Algorithms/Section2Submissions/problem_2_directory/problem_2_subdirectory/pythonsubtest1.py',
 '/home/vasilis/Dropbox/Development/Udacity - Data Strctures and Algorithms/Section2Submissions/problem_2_directory/pythontest2.py',
 '/home/vasilis/Dropbox/Development/Udacity - Data Strctures and Algorithms/Section2Submissions/problem_6.py',
 '/home/vasilis/Dropbox/Development/Udacity - Data Strctures and Algorithms/Section2Submissions/problem_5.py',
 '/home/vasilis/Dropbox/Development/Udacity - Data Strctures and Algorithms/Section2Submissions/problem_3.py',
 '/home/vasilis/Dropbox/Development/Udacity - Data Strctures and Algorithms/Section2Submissions/problem_2.py']
"""

path2 = 'C:\\Users\\vasileios.tsakalos\\OneDrive - Education First\\Projects\\DataScienceCollab\\data structures_algorithms\\latestSubmission\\testdir'
print(find_files('.c', path2))

"""
Returns:

['C:\\Users\\vasileios.tsakalos\\OneDrive - Education First\\Projects\\DataScienceCollab\\data structures_algorithms\\latestSubmission\\testdir\\subdir1\\a.c',
 'C:\\Users\\vasileios.tsakalos\\OneDrive - Education First\\Projects\\DataScienceCollab\\data structures_algorithms\\latestSubmission\\testdir\\subdir3\\subsubdir1\\b.c',
 'C:\\Users\\vasileios.tsakalos\\OneDrive - Education First\\Projects\\DataScienceCollab\\data structures_algorithms\\latestSubmission\\testdir\\subdir5\\a.c',
 'C:\\Users\\vasileios.tsakalos\\OneDrive - Education First\\Projects\\DataScienceCollab\\data structures_algorithms\\latestSubmission\\testdir\\t1.c']
"""
path1 = '/home/vasilis/Dropbox/Development/Udacity - Data Strctures and Algorithms/Section2Submissions'
print(find_files('.csv', path1))

"""
Returns:

[]
"""
