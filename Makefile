SHELL = /bin/bash

DEFAULT_GOAL := help
PIPX = $(shell which pipx)
ifeq (${PIPX},)
	$(error "pipx is not installed")
endif
PIPENV_SETUP = $(shell which pipenv-setup)
ifeq (${PIPENV_SETUP},)
	PIPENV_SETUP = pipx run pipenv-setup
endif



.PHONY: help

help:
	@echo "Usage: make [target]"
	@echo
	@echo "Targets:"
	@echo "  help        Show this help message"
	@echo "  setup       Update setup.py with Pipfile.lock contents"
	@echo "  install     Install via pipx"
	@echo

setup:
	${PIPENV_SETUP} check || ${PIPENV_SETUP} sync

install: setup
	${PIPX} install --force --pip-args="--no-cache-dir" --editable .[dev]

_temp_pipenv_setup:
	pipx run pipenv-setup check || pipx run pipenv-setup sync
