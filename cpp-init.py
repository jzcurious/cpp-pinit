#!/usr/bin/env python

# import argparse
from pathlib import Path


SUBDIRS = ["tests", "benchmarks", "security"]


def set_project_name(project_path: Path):
    pname = project_path.name
    SUBDIRS.insert(0, pname)


def create_dirs(project_path: Path):
    pname = project_path.name

    project_path.mkdir(parents=True, exist_ok=True)

    if any(project_path.iterdir()):
        print("Fail: directory is not empty")
        return

    for subdir in SUBDIRS:
        project_path.joinpath(subdir).joinpath("include").mkdir(parents=True)
        project_path.joinpath(subdir).joinpath("src").mkdir(parents=True)


def create_cmakelists(project_path: Path, **kwargs):
    from samples.cmake import main, target, tests, benchmarks, security, config

    vars = config.vars
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
    set_project_name(project_path)
    create_dirs(project_path)
    create_cmakelists(project_path)
    create_ide(project_path)
    create_git(project_path)
