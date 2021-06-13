#!/usr/bin/env python
targets = {
    "FRDM-K64F":                 "K64F",
    "LPCXpresso55S69":           "LPC55S69_NS",
}

header = r"""# Generated file do not edit

"""

footer = r"""
dist/%.bin: dist/%.hex

BUILD/%/GCC_ARM-RELEASE/daplink-validation.elf: source/main.cpp mbed_app.json custom_targets.json
	mbed compile -m $* --profile release

.PRECIOUS: BUILD/%/GCC_ARM-RELEASE/daplink-validation.elf

"""

with open('.targets.mk', 'w') as f:
    f.write(header)
    f.write("TARGETS := \\\n\t%s\n\n" % (" \\\n\t".join([ "dist/%s.hex" % i for i in targets.keys() ])))

    for k, v in targets.items():
        f.write(r"""dist/%s.hex: BUILD/%s/GCC_ARM-RELEASE/daplink-validation.elf
	@mkdir -p dist
	arm-none-eabi-objcopy -O ihex $< $@
	arm-none-eabi-objcopy -O binary $< dist/%s.bin

""" % (k, v, k))
    f.write(footer)

