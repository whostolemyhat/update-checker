"""
Update Checker

Checks a group of git repositories for any updates

Usage:
    update_checker.py PATH
    update_checker.py (-h | --help)

Options:
    -h --help       Show this message
    -v --version    Show version

"""

from docopt import docopt
import os
import git
from git import GitCommandError

def get_toplevel_dirs(root_dir):
    '''Lists top-level subdirectories in a folder'''
    return [name for name in os.listdir(root_dir)
            if os.path.isdir(os.path.join(root_dir, name))]

def update_progress(progress, total):
    '''Prints progress percentage as #'''
    percent = int(100 / total)

    # this is pretty ugly!
    # 0: <{1} - print var in position 0 and right pad with spaces with
    # var in position 1
    # see http://stackoverflow.com/a/5676884/345078 for full explanation
    print('\r[{0: <{1}}] {2}%'.format(
        '#' * (progress),
        total,
        progress * percent),
          end='')

def check_for_updates(base):
    '''Calls git pull in top-level sub-dirs and prints response'''

    output = '\n'
    dirs = get_toplevel_dirs(base)
    for index, dir_name in enumerate(dirs):
        update_progress(index + 1, len(dirs))

        git_lib = git.cmd.Git(os.path.join(base, dir_name))
        try:
            output += '{}:\n{}\n\n'.format(dir_name, git_lib.pull())
        except GitCommandError as err:
            # if repo is empty you'll get an error
            output += '{}:\n{}\n\n'.format(dir_name, err)

    print(output)


if __name__ == '__main__':
    # check_for_updates()
    arguments = docopt(__doc__, version='Update Checker 1.0')

    if arguments.get('PATH'):
        check_for_updates(arguments.get('PATH'))
