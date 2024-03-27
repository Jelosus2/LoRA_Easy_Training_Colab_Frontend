import json
from pathlib import Path
import sys
import subprocess
import os


def check_version_and_platform() -> bool:
    version = sys.version_info
    if not (
        False
        if version.major != 3 and version.minor < 10
        else sys.platform in ["win32", "linux"]
    ):
        print("ERROR: you have too old of a python version")
        return False
    return True


def check_git_install() -> None:
    try:
        subprocess.check_call(
            "git --version",
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            shell=sys.platform == "linux",
        )
    except FileNotFoundError:
        print("ERROR: git is not installed, please install git")
        return False
    return True


def main():
    if not check_version_and_platform():
        return
    if not check_git_install():
        return
    python = sys.executable
    subprocess.check_call(f"{python} -m venv venv", shell=sys.platform == "linux")
    venv_path = Path(
        "venv/Scripts/pip.exe" if sys.platform == "win32" else "venv/bin/pip"
    )
    subprocess.check_call(
        f"{venv_path} install -U -r requirements.txt", shell=sys.platform == "linux"
    )

    config = Path("config.json")
    config_dict = json.loads(config.read_text()) if config.exists() else {}

    config_dict["run_local"] = False
    config_dict["colab"] = True
    config.write_text(json.dumps(config_dict, indent=2))

if __name__ == "__main__":
    main()
