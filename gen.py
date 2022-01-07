#!/usr/bin/env python
targets = {
    "EA-LPC4088":                "LPC4088",
    "FRDM-K22F":                 "K22F",
    "FRDM-K64F":                 "K64F",
    "FRDM-K66F":                 "K66F",
    "FRDM-K82F":                 "K82F",
    "LPCXpresso4367":            "LPC4330_M4",
    "LPCXpresso54608":           "LPC546XX",
    "LPCXpresso55S69":           "LPC55S69_NS",
    "MAX32620":                  "MAX32620FTHR",
    "MAX32625":                  "MAX32625MBED",
    "MAX32630":                  "MAX32630FTHR",
    "MIMXRT1050":                "MIMXRT1050_EVK",
    "Microbit":                  "NRF51_MICROBIT",
    "Microbitv2":                "NRF52_MICROBIT",
    "Nordic-nRF51822":           "NRF51822",
    "Nordic-nRF51-DK":           "NRF51_DK",
    "Nordic-nRF52-DK":           "NRF52_DK",
    "Nordic-nRF52840-DK":        "NRF52840_DK",
    "Seeed-Arch-BLE":            "ARCH_BLE",
    "Seeed-Arch-Link":           "ARCH_LINK",
    "ST-Nucleo-F401RE":          "NUCLEO_F401RE",
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
	arm-none-eabi-objcopy -O binary --gap-fill=0xff $< dist/%s.bin

""" % (k, v, k))
    f.write(footer)

