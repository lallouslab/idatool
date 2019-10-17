import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import pprint
import logging
import json

import idatool.disassembly

logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    disasm = idatool.disassembly.Disasm()
    
    if len(disasm.Args) == 0:
        import ui

        global form

        title = 'Breakpoints-UI'
        try:
            form
            form.OnClose(form)
            form = ui.Form(title)
        except:
            form = ui.Form(title)

        form.Show()

        filename = form.AskOpenFileName("DB (*.db)")

    if not filename:
        filename = 'InstructioNotations.db'

    if filename:
        print 'Loading file:', filename
        disasm.LoadNotations(filename, hash_types = [])
    disasm.Exit()
