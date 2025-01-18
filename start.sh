#!/bin/zsh

python3 -m venv .venv
source .venv/bin/activate
source .venv/Scripts/activate

pip3 install poetry
poetry  install
