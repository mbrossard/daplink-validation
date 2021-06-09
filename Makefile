TARGETS = \
	ARCH_BLE \
	BLACKPILL BLUEPILL_F103C8 \
	K64F \
	LPC55S69_NS \
	MAX32630FTHR \
	NRF51822 \
	NRF51_DK NRF51_MICROBIT \
	NRF52_DK NRF52_MICROBIT \
	NRF52833_DK NRF52840_DK

all: $(patsubst %, dist/%.hex, $(TARGETS))

dist/%.hex: BUILD/%/GCC_ARM-RELEASE/daplink-validation.elf
	@mkdir -p dist
	arm-none-eabi-objcopy -O ihex $< $@
	arm-none-eabi-objcopy -O binary $< dist/$*.bin

dist/%.bin: dist/%.hex

BUILD/%/GCC_ARM-RELEASE/daplink-validation.elf: source/main.cpp mbed_app.json custom_targets.json
	mbed compile -m $* --profile release

.PRECIOUS: BUILD/%/GCC_ARM-RELEASE/daplink-validation.elf
