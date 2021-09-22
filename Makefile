
build:
	$(MAKE) .targets.mk
	$(MAKE) all

.PHONY: build

-include .targets.mk

all: $(TARGETS)

.targets.mk: gen.py
	python gen.py
