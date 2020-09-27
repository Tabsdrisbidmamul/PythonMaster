import os
import fnmatch

import id3reader_p3 as id3reader


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
error_list = []

for s in relative_path:
    try:
        id3r = id3reader.Reader(s)
        print("Artist: {}, Album: {}, Track: {}, Song: {}".format(
            id3r.get_value('performer'),
            id3r.get_value('album'),
            id3r.get_value('track'),
            id3r.get_value('title')
        ))
    except:
        # print("Error in this file: {}".format(s))
        error_list.append(s)

for e in error_list:
    print(e)
