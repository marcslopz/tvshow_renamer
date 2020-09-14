import os
import re

from classes import factories
from classes import files
from classes.directories import get_all_video_files

if __name__ == '__main__':
    # reg_exp = re.compile(r".Cap\.(3)(\d\d).")
    root_path = "D:\\video\\tvshows\\The Good Doctor\\Season 3"
    video_files = get_all_video_files(root_path, r"Cap\.(3)(\d\d)")
    for video_file in video_files:
        old_filename = video_file["filename"]
        old_root_path = video_file["root"]
        has_to_be_renamed = video_file.get("has_to_be_renamed", False)
        if has_to_be_renamed:
            season_start_index = video_file["season_indexes"][0]
            season_end_index = video_file["season_indexes"][1]
            season = video_file["season"]
            episode_start_index = video_file["episode_indexes"][0]
            episode_end_index = video_file["episode_indexes"][1]
            episode = video_file["episode"]
            new_filename = \
                old_filename[:season_start_index] + \
                "s" + season.zfill(2) + \
                old_filename[season_end_index:episode_start_index] + \
                "e" + episode + \
                old_filename[episode_end_index:]
            # print(f"Renaming {old_filename} by {new_filename}")
        else:
            # print(f"Filename {old_filename} does not need to be renamed")
            new_filename = old_filename

        has_to_be_moved = video_file.get("has_to_be_moved", False)

        if has_to_be_moved or has_to_be_renamed:
            new_abs_filename = os.path.join(root_path, new_filename)
            old_abs_filename = os.path.join(old_root_path, old_filename)
            answer = input(f"File {old_abs_filename} -> {new_abs_filename}? (y/n): ")
            if answer == "y":
                os.rename(old_abs_filename, new_abs_filename)
                print("File renamed OK.")
        else:
            print(f"File {old_abs_filename} is already correct")



