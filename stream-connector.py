#!/usr/bin/env python
import sys
import os
from time import sleep
from random import random
from datetime import datetime

if __name__ == "__main__":

    # Do not buffer the output
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

    while True:
            sleep(1.0)
            temperature = random() * 100
            now = datetime.utcnow().isoformat()
            print('{"datapointValue": {"key": "temp", "value": "%s", "dataType": "Float", "tsIso8601": "%sZ"}}' % (temperature, now))
