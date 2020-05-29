# SPDX-License-Identifer: MPL-2.0
# Copyright © 2020 Andreas Stenberg


import nox


@nox.session(python=["2.7", "3.5", "3.6", "3.7", "3.8"])
def tests(session):
    session.install("pytest")
    session.run("pytest")


@nox.session
def format(session):
    session.install("black")
    session.run("black", "noxfile.py", "raptorstr/", "tests/", "--check")


@nox.session
def lint(session):
    session.install("flake8")
    session.run(
        "flake8", "noxfile.py", "raptorstr/", "tests/",
    )


@nox.session
def lint_tests(session):
    session.install("flake8")
    session.run("flake8", "tests/")
