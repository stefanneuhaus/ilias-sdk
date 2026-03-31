#!/usr/bin/env python3
import os
import sys

from ilias_service import IliasService

ILIAS_CONFIGURATION_FILENAME = os.getenv("ILIAS_CONFIGURATION_FILENAME")

if ILIAS_CONFIGURATION_FILENAME == None:
    print("ERROR: environment variable 'ILIAS_CONFIGURATION_FILENAME' is not set.")
    exit(2)
if len(sys.argv) == 1:
    print("ERROR: no tasks files given.")
    print("  Usage: %s <TASKS_FILES>" % sys.argv[0])
    exit(1)
tasks_filenames = sys.argv[1:]

service = None
try:
    service = IliasService(ILIAS_CONFIGURATION_FILENAME)
    service.login()
    for tasks_filename in tasks_filenames:
        service.process_tasks(tasks_filename)

finally:
    if service is not None:
        service.logout()
