GITHUB_REMOTE	=	origin
GITHUB_PUSH_BRANCHS	=	master
TESTS_DIR = pydsalg/tests/
TESTS_FP_PREFIX = test_*

.PHONY: help

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  test         Run unit tests"

test:
	python -m unittest discover -v -s $(TESTS_DIR) -p $(TESTS_FP_PREFIX)

push:
	git push $(GITHUB_REMOTE) $(GITHUB_PUSH_BRANCHS)