# Poor-man's ILIAS SDK

*Tired of clicking through the ILIAS GUI over and over again to accomplish your repetitive tasks like updating uploaded files?*

This project utilizes ILIAS' SOAP Webservice interface. Though not aiming for building an actual SDK I decided to provide at least some level of abstraction to facilitate reuse.

## Limitations
- designed for ILIAS 5.4.20
- only a very limited amount of [API concepts](https://test54.ilias.de/webservice/soap/server.php) is supported

## Installation
- `pip install zeep` -- see [python-zeep](https://github.com/mvantellingen/python-zeep)

## Configuration
- change `ILIAS_CONFIGURATION_FILENAME` to your personal configuration file (see [example_ilias-config.json](./example_ilias-config.json))
- provide your personal tasks file(s) -- see [example_tasks.json](./example_tasks.json)

## Run
- `process_tasks.py <TASK_FILES>`
