TARGETS = \
	K64F \
	LPC55S69_NS \
	MAX32630FTHR \
	NRF52_MICROBIT

all: $(patsubst %, dist/%.hex, $(TARGETS))

dist/%.hex: BUILD/%/GCC_ARM-RELEASE/daplink-validation.elf
	@mkdir -p dist
	arm-none-eabi-objcopy -O ihex $< $@
	arm-none-eabi-objcopy -O binary $< $@

dist/%.bin: dist/%.hex

BUILD/%/GCC_ARM-RELEASE/daplink-validation.elf: source/main.cpp mbed_app.json custom_targets.json
	mbed compile -m $* --profile release

.PRECIOUS: BUILD/%/GCC_ARM-RELEASE/daplink-validation.elf
