from fbs_runtime.application_context.PyQt5 import ApplicationContext

from ggapp import GGApp

import sys

if __name__ == '__main__':

    appctxt = ApplicationContext()
    
    app = GGApp(appctxt)
    app.show()

    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)