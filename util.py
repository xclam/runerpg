import time as t

class _Getch:
    """Gets a single character from standard input.  
    Does not echo to thescreen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()
            
    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys
        
        def __call__(self):
            import sys, tty, termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                return ch
            
class _GetchWindows:
    def __init__(self):
        import msvcrt
        
    def __call__(self):
        import msvcrt
        return msvcrt.getch()
        
getch = _Getch._Getch()

class Schema:
    """ 
    _path
    _point
    """

    def __init__(self, path):
        self._path = path

    def proceed(self):
        point = 0
        print self._path
        start = t.time()
        i = 0
        # compare the path to the input one by one
        while (i < len(self._path)):
            ch = getch()
            if (ch == self._path[i]):
                i += 1
            else:
                point += 100
                print("error")

        exetime = (t.time() - start) * 1000 # msec
        point += exetime

        return point
