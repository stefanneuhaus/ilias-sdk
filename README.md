# Poor-man's ILIAS SDK

*Tired of clicking through the ILIAS GUI over and over again to accomplish your repetitive tasks like updating uploaded files?* :shrug:

This project utilizes ILIAS' SOAP Webservice interface. Though not aiming for building an actual SDK I decided to provide at least some level of abstraction to facilitate reuse.

## Limitations
- (Originally) designed for ILIAS 5.4 (not maintained anymore)
- Only a very limited amount of [API concepts](https://test9.ilias.de/webservice/soap/server.php) is supported

## Installation
- `pip install .`

## Configuration
- Create personal configuration file (see [example_ilias-config.json](./example_ilias-config.json))
- Set environment variable `ILIAS_CONFIGURATION_FILENAME` to hold the config file's path
- Provide your personal tasks file(s) (see [example_tasks.json](./example_tasks.json))

## Run
- `process_tasks.py <TASK_FILES>`
