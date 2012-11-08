# convenience makefile to boostrap & run buildout
# use `make options=-v` to run buildout with extra options

pep8_ignores = E501
options = -N -q -t 3

.PHONY: help prerequisites install test

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo " prerequisites    Install requisites"
	@echo "       install    Install"
	@echo "         tests    Run all testes"

prerequisites:
	sudo apt-get install -qq pep8 pyflakes
	mkdir -p buildout-cache/downloads

install: prerequisites
	python bootstrap.py -c travis.cfg
	bin/buildout -c travis.cfg $(options)

tests:
	bin/test
	pyflakes plonesocial/
	pep8 --ignore=$(pep8_ignores) plonesocial/
