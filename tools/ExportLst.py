import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import idatool.disassembly

if __name__ == '__main__':
    import logging

    logging.basicConfig(level = logging.DEBUG)
    logger = logging.getLogger(__name__)

    disasm = idatool.disassembly.Disasm()
    
    save_filename = ''
    if len(disasm.Args)>0:
        save_filename = disasm.Args[0]
    else:        
        import idatool.ui

        global form

        title = 'List-Export-UI'
        try:
            form
            form.OnClose(form)
            form = idatool.ui.Form(title)
        except:
            form = idatool.ui.Form(title)

        form.Show()

        save_filename = form.AskSaveFileName("LIST (*.lst)")

    if not save_filename:
        save_filename = disasm.GetFilename()+r'.lst'

    if save_filename:
        print('Save', save_filename)
        disasm.Export(save_filename)
    disasm.Exit()
