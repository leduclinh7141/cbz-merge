# -*- coding: utf-8 -*-
# @author: Peter Lamut

import argparse
import os
import shutil

N = 10  # the number of files in seach subfolder folder


def move_files(abs_dirname):
    """Move files into subdirectories."""

    files = [os.path.join(abs_dirname, f) for f in os.listdir(abs_dirname)]

    i = 0
    curr_subdir = None
    folder = os.path.basename(os.path.normpath(abs_dirname))
    for f in files:
        # create new subdir if necessary
        if i % N == 0:
            countName = '{0:1f}'.format(i / N + 1)
            subdir_name = os.path.join(abs_dirname, folder + " " + countName)
            os.mkdir(subdir_name)
            curr_subdir = subdir_name

        # move file to current dir
        f_base = os.path.basename(f)
        shutil.move(f, os.path.join(subdir_name, f_base))
        i += 1


def parse_args():
    """Parse command line arguments passed to script invocation."""
    parser = argparse.ArgumentParser(
        description='Split files into multiple subfolders.')

    parser.add_argument('src_dir', help='source directory')

    return parser.parse_args()


def main():
    """Module's main entry point (zopectl.command)."""
    args = parse_args()
    src_dir = args.src_dir

    if not os.path.exists(src_dir):
        raise Exception('Directory does not exist ({0}).'.format(src_dir))

    child_folders = os.listdir(os.path.abspath(src_dir))
    for child_folder in child_folders:
        folder = os.path.join(os.path.abspath(src_dir), child_folder)
        move_files(folder)
        sub_folders = os.listdir(os.path.abspath(folder))
        for sub_folder in sub_folders:
            dir_to_move = os.path.join(os.path.abspath(folder), sub_folder)
            shutil.move(dir_to_move, os.path.abspath(src_dir))
        os.rmdir(os.path.abspath(folder))
        
if __name__ == '__main__':
    main()