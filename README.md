# Template for MicroPython development

This repo is a Template Repository you can use to initialize a MicroPython project. 

# Setup

## Dependencies

Run `make install_deps` to install the dependencies.

## Prepare the Raspberry Pi Pico

You will need to [install the MicroPython firmware](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#drag-and-drop-micropython) on your Raspberry Pi Pico.

# Usage

Run `make` when you are ready to upload and run your code. This will upload every `*.py` file to the Pico and connect to the serial console. From here you can press `^D` to soft reboot and run your code.

## make help

Use `make help` to see the available commands:

```
Usage: make [command]

Commands for the Raspberry Pi Pico:

    make              - Runs make upload followed by make console
    make console      - Opens the serial console for the RPi Pico
    make ls           - List all files on the RPi Pico
    make reset        - Soft reboot the RPi Pico and run main.py
    make rm-rf        - Removes all files from the Raspberry Pi Pico
    make upload       - Upload user code from the current directory
    make upload_mods  - Upload 3rd party modules installed with make upip

Commands for the Local Machine:

    make install_deps - Install dependencies needed for development
    make upip         - Install a 3rd party micropython library
    make help         - This output

Detailed help for upip:

    This command will install a 3rd party package and upload it to your RPi Pico.
    You must pass PACKAGE=<package_name> to the command. If you don't want to
    install it to your RPi Pico just yet you can also pass NOUPLOAD=true.

    make upip PACKAGE=<package_name> [NOUPLOAD=true]
```
