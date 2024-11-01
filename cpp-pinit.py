#!/usr/bin/env python

from pathlib import Path
import shutil

PNAME = ""
PPATH = Path()
SUBDIRS = ["tests", "benchmarks", "security"]
CONFIG = {}
LOCAL_CONFIG_FNAME = "cpp-pinit.yml"


def set_project_path(project_path_str: str):
    global PPATH
    PPATH = Path(project_path_str)


def set_project_name():
    global PNAME
    PNAME = PPATH.name
    SUBDIRS.insert(0, PNAME)


def load_config(fname: str = ""):
    import yaml

    with open("cpp-pinit-global.yml") as f:
        CONFIG.update(yaml.load(f, Loader=yaml.SafeLoader))

    if fname:
        with open(fname) as f:
            CONFIG.update(yaml.load(f, Loader=yaml.SafeLoader))

    local_config_path = PPATH.joinpath(LOCAL_CONFIG_FNAME)
    if local_config_path.is_file():
        with local_config_path.open() as f:
            CONFIG.update(yaml.load(f, Loader=yaml.SafeLoader))


def subdir_filter_cond(subdir: str):
    return subdir == PNAME or CONFIG["enable_" + subdir]


def create_dirs(force=False):
    from sys import exit
    from os import listdir
    from shutil import rmtree

    PPATH.mkdir(parents=True, exist_ok=True)

    if force:
        for item in listdir(PPATH):
            if item == LOCAL_CONFIG_FNAME:
                continue

            path = PPATH.joinpath(item)

            if path.is_file():
                path.unlink()
                continue

            if path.is_dir():
                rmtree(path)

    ls = listdir(PPATH)
    if (not ls) or (len(ls) == 1 and LOCAL_CONFIG_FNAME in ls):
        pass
    else:
        print("Failed: directory is not empty. Use option -f to remove old version.")
        exit(1)

    for subdir in SUBDIRS:
        if not subdir_filter_cond(subdir):
            continue
        PPATH.joinpath(subdir).joinpath("include").mkdir(parents=True)
        PPATH.joinpath(subdir).joinpath("src").mkdir(parents=True)


def create_cmakelists(**kwargs):
    from samples.cmake import main, target, tests, benchmarks, security

    vars = CONFIG
    vars.update(kwargs)

    for subdir, template in zip(
        SUBDIRS,
        [
            target.template,
            tests.template,
            benchmarks.template,
            security.template,
        ],
    ):
        if not subdir_filter_cond(subdir):
            continue
        with PPATH.joinpath(subdir).joinpath("CMakeLists.txt").open("w") as f:
            f.write(template.format(project_name=PPATH.name, **vars))

    with PPATH.joinpath("CMakeLists.txt").open("w") as f:
        f.write(main.template.format(project_name=PPATH.name, **vars))


def create_ide():
    from samples.ide import clang_format

    with PPATH.joinpath(".clang-format").open("w") as f:
        f.write(clang_format.const)


def create_git():
    from samples.git import gitignore

    with PPATH.joinpath(".gitignore").open("w") as f:
        f.write(gitignore.const)


if __name__ == "__main__":
    set_project_path("/home/void/Projects/cpp-pinit/myproj")
    set_project_name()
    load_config("cpp-pinit-global.yml")
    create_dirs()
    create_cmakelists()
    create_ide()
    create_git()
