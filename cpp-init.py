#!/usr/bin/env python

from pathlib import Path
from sys import exit
import yaml


PNAME = ""
SUBDIRS = ["tests", "benchmarks", "security"]
CONFIG = {}


def set_project_name(project_path: Path):
    global PNAME
    PNAME = project_path.name
    SUBDIRS.insert(0, PNAME)


def load_config(fname: str):
    with open(fname) as f:
        CONFIG.update(yaml.load(f, Loader=yaml.SafeLoader))
        print(CONFIG)


def _subdir_filter_cond(subdir: str):
    return subdir == PNAME or CONFIG["enable_" + subdir]


def create_dirs(project_path: Path):
    project_path.mkdir(parents=True, exist_ok=True)

    if any(project_path.iterdir()):
        print("Failed: directory is not empty")
        exit(1)

    for subdir in SUBDIRS:
        if not _subdir_filter_cond(subdir):
            continue
        project_path.joinpath(subdir).joinpath("include").mkdir(parents=True)
        project_path.joinpath(subdir).joinpath("src").mkdir(parents=True)


def create_cmakelists(project_path: Path, **kwargs):
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
        if not _subdir_filter_cond(subdir):
            continue
        with project_path.joinpath(subdir).joinpath("CMakeLists.txt").open("w") as f:
            f.write(template.format(project_name=project_path.name, **vars))

    with project_path.joinpath("CMakeLists.txt").open("w") as f:
        f.write(main.template.format(project_name=project_path.name, **vars))


def create_ide(project_path: Path):
    from samples.ide import clang_format

    with project_path.joinpath(".clang-format").open("w") as f:
        f.write(clang_format.const)


def create_git(project_path: Path):
    from samples.git import gitignore

    with project_path.joinpath(".gitignore").open("w") as f:
        f.write(gitignore.const)


if __name__ == "__main__":
    project_path = Path("/home/void/Projects/cpp-pinit/myproj")
    load_config("init-config.yml")
    set_project_name(project_path)
    create_dirs(project_path)
    create_cmakelists(project_path)
    create_ide(project_path)
    create_git(project_path)
