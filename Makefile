TARGETS = K64F

ELFS = $(patsubst %, BUILD/%/GCC_ARM/daplink-validation.elf, $(TARGETS))

all: $(ELFS)

BUILD/%/GCC_ARM/daplink-validation.elf:
	mbed compile -m $*

