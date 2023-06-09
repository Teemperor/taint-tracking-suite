#!/usr/bin/env python3

import argparse
import os
import subprocess as sp
import tempfile
import shutil
import os.path as path
import sys
from pathlib import Path

tests = []

script_dir = os.path.dirname(os.path.realpath(__file__))

class Color:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    END = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    PASS = BOLD + GREEN
    WARN = BOLD + YELLOW
    FAIL = BOLD + RED


parser = argparse.ArgumentParser(prog=sys.argv[0], description="Runs taint tests")
parser.add_argument("--target", dest="target", help="Target directory", required=True)
parser.add_argument("--verbose", action="store_true", dest="verbose", help="Enbles verbose output")
parser.add_argument("-f", "--filter", action="store", dest="filter", default="", help="Filter tests")
args = parser.parse_args()

target_path = path.realpath(args.target)
run_script = path.join(args.target, "run.sh")

driver_source = path.join(script_dir, "infrastructure", "driver.c")

def run_test(test_source):
    env = os.environ.copy()
    env["SOURCE"] = test_source
    env["OUTPUT"] = test_source + ".bin"
    env["TARGET_DIR"] = target_path
    env["CFLAGS"] = "-I " + path.join(script_dir, "infrastructure") + " " + driver_source

    retcode = sp.call([run_script], env=env, stdout=sp.DEVNULL, stderr=sp.DEVNULL)
    return retcode == 0

def get_test_display_name(test_dir, test_source):
    separator = "."

    name = path.relpath(test_source, test_dir)
    name = name.replace(os.path.sep, separator)
    return name

with tempfile.TemporaryDirectory() as tmpdir:
    test_dir = path.join(tmpdir, "test")
    shutil.copytree(path.join(script_dir, "tests"), test_dir)

    tests = []
    if len(tests) == 0:
        for p in Path(test_dir).rglob("**/*.c"):
            tests.append(str(p))

    for test in tests:
        test_name = get_test_display_name(test_dir, test) + " "
        sys.stdout.write("• " + test_name.ljust(80, "┄") + " ")
        sys.stdout.flush()
        if run_test(test):
            print("[" + Color.PASS + " OK " + Color.END + "]")
        else:
            print("[" + Color.FAIL + "FAIL" + Color.END + "]")

    sys.exit(0)

def run_test(directory):
    with tempfile.TemporaryDirectory() as tmpdir:
        test_dir = path.join(tmpdir, "test")
        shutil.copytree(directory, test_dir)
        output = sp.check_output(
            [path.join(test_dir, "check.py"), plugin_path], cwd=test_dir
        )
        if args.verbose and output:
            print(output)


print("Running {num} tests".format(num=len(tests)))
had_error = False
for test in tests:
    test_name = str(Path(test).relative_to(script_dir))
    fancy_test_name = test_name.replace("/", separator)
    sys.stdout.write("• ")
    sys.stdout.write(fancy_test_name + " ")
    sys.stdout.flush()


    status = ""
    if args.filter in test_name:
        try:
            run_test(test)
        except sp.CalledProcessError as e:
            had_error = True
            print(Color.FAIL + "FAIL" + Color.END)
            if e.stdout:
                print(e.stdout.decode("utf-8"))
            if e.stderr:
                print(e.stderr.decode("utf-8"))
            continue
        status = Color.PASS + " ✔" + status + Color.END
    else:
        status = Color.WARN + " Skipped" + Color.END
    max_test_len_name = 50
    sys.stdout.write((max_test_len_name - len(test_name)) * "┄")
    print(status)

if had_error:
    sys.exit(1)