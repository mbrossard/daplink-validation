
build: .targets.mk
	$(MAKE) all

-include .targets.mk

all: $(TARGETS)

.targets.mk: gen.py
	python gen.py
