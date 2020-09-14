import os
import re

from classes.factories import FileFactory
from classes.files import VideoFile


def get_all_video_files(root_path, reg_exp=None):
    video_files = []

    for (root, dirs, files) in os.walk(root_path, topdown=True):
        for filename in files:
            file_obj = FileFactory.create_file(filename)
            if isinstance(file_obj, VideoFile):
                video_file = {
                    'root': root,
                    'filename': filename,
                    'has_to_be_moved': root != root_path,
                }
                if reg_exp:
                    m = re.search(reg_exp, filename)
                    if not m:
                        video_file["has_to_be_renamed"] = False
                    else:
                        video_file["has_to_be_renamed"] = True
                        video_file["season_indexes"] = m.regs[1]
                        video_file["episode_indexes"] = m.regs[2]
                        video_file["episode"] = m.group(2)
                        video_file["season"] = m.group(1)
                video_files.append(video_file)
    return video_files
