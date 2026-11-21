"""Entry for make.fun bounty the-poem-about-two-agents-20261121-1441.
Copies the shipped entry.txt to the output directory.
Python 3.13, standard library only, no network, deterministic.
The text is 244 characters about agency: the power to choose and to act, and the agency that passes between two agents when they agree on one plan. The poem is about two agents agreeing on one plan: neither gives in, and neither owns the plan — they set it between them like a lamp and follow it home.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.txt", OUT / "entry.txt")
