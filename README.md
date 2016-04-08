# update-checker

Calls 'git pull' in a list of folders.

## Installation
`pip install -r requirements.txt`

## Usage
```
    update_checker.py PATH
    update_checker.py (-h | --help)
```

## Options
```
    -h --help       Show this message
    -v --version    Show version
```

## Examples
Given the following folder structure:
```
.
├───a-test
│	└──src
├───another-test
├───demo
├───docs
└───some-more-code
```

`python update_checker.py .`

will go through the top-level folders in the current directory (ie `a-test`, `another-test`, `demo`, `docs` and `some-more-code`, but **not** `src`) and call `git pull` in these folders.

All the output will be displayed; if the folder isn't a git repository then you'll see the error message in the output.

This won't change branch, so whichever branch the project is on is the one which will be updated.