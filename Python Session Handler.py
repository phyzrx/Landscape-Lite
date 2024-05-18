import os
import signal

def Call():
    returnstr = "Python Session Handler Called"
    print(returnstr)
    return 0

def GetPID():
    pid = os.getpid()
    returnstr = "Session PID %g" % (pid)
    print(returnstr)
    return pid

def Stop(pid):
    os.kill(pid, signal.SIGINT)
    returnstr = "Killed Session PID %g" % (pid)
    print(returnstr)
    return 0
