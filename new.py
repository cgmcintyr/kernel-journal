#!/usr/bin/env python
# Script for creating new journal entry
from __future__ import print_function
import datetime
import os
import subprocess
import sys

now = datetime.datetime.now()
fname = now.strftime('%Y-%m-%d_entry')
fname += '.md'

# Create file if doesn't exist
open(fname, 'a').close()

# Open file with default editor
if sys.platform.startswith('darwin'):
    subprocess.call(('open', fname))
elif os.name == 'nt':
    os.startfile(fname)
elif os.name == 'posix':
    editor = os.getenv('EDITOR')
    if editor:
        os.system('%s %s' % (editor, fname))
    else:
        subprocess.call(('xdg-open', fname))
