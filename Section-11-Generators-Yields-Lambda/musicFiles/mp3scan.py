import os
import fnmatch


def complete_filename(root, ext):
    for path, directories, _ in os.walk(root, topdown=True):
        for directory in directories:
            subdir = os.path.join(path, directory)
            for artist_name, album, files in os.walk(subdir):
                if files:
                    complete_path = os.path.join(artist_name)
                    for file in files:
                        if file.endswith(ext):
                            yield os.path.abspath(os.path.join(complete_path, file))


def find_music(root, ext):
    for path, directories, files in os.walk(root, topdown=True):
        for file in fnmatch.filter(files, "*.{}".format(ext)):
            yield os.path.abspath(os.path.join(path, file))


relative_path = find_music("music", "emp3")

for s in relative_path:
    print(s)
