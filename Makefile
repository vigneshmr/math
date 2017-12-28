.DEFAULT_GOAL := math

env:
	virtualenv env
	$@/bin/pip install -r requirements.txt

.PHONY: math
math: | env
	$|/bin/python math/main.py

.PHONY: nuke
nuke:
	rm -rf env
