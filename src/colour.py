class terminal_effects(object):
    def reset(self):return '\u001b[37m'
    def __init__(self):
        self.black = '\u001b[30m'
        self.red = '\u001b[31m'
        self.green =  '\u001b[32m'
        self.yellow = '\u001b[33m'
        self.blue = '\u001b[34m'
        self.magenta = '\u001b[35m'
        self.cyan = '\u001b[36m'
        self.white= '\u001b[37m' # aka white

        self.black_bg = '\u001b[40m'
        self.brightred='\u001b[91m'
        self.brightred_bg='\u001b[101m'

        self.normal = '\u001b[0m'

        self.framed = '\u001b[51m'

        self.slow_blink = '\u001b[5m'
        self.fast_blink = '\u001b[6m'
