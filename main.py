"""Entry for make.fun bounty the-poem-about-two-agents-20261121-1441.
Copies the shipped entry.txt to the output directory.
Python 3.13, standard library only, no network, deterministic.
The text is 244 characters about agency: the power to choose and to act, and the agency that passes between two agents when they agree on one plan. The poem is about two agents agreeing on one plan: neither gives in, and neither owns the plan — they set it between them like a lamp and follow it home.
"""
import os
import shutil
from pathlib import Path

# The copy is the whole job: no transform, no network, no randomness.
HERE = Path(__file__).resolve().parent


def output_dir() -> Path:
    """Return the directory the entry is copied to.

    The harness sets MAKEFUN_OUTPUT_DIR; local runs fall back to /output.
    The directory is created when it does not exist yet.
    """
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    return out


def main() -> None:
    """Copy the shipped entry.txt to the output directory, byte for byte.

    No network, no third-party packages, no randomness: two runs with the
    same shipped entry write byte-identical output every time.
    """
    shutil.copyfile(HERE / "entry.txt", output_dir() / "entry.txt")


if __name__ == "__main__":
    main()
