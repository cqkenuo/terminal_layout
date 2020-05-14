class Key:
    ENTER = '\x0d'
    BACKSPACE = '\x7f'
    ESC = '\x1b'

    # cursors
    UP = '\x1b\x5b\x41'
    DOWN = '\x1b\x5b\x42'
    LEFT = '\x1b\x5b\x44'
    RIGHT = '\x1b\x5b\x43'

    # CTRL
    CTRL_A = '\x01'
    CTRL_B = '\x02'
    CTRL_C = '\x03'
    CTRL_D = '\x04'
    CTRL_E = '\x05'
    CTRL_F = '\x06'
    CTRL_Z = '\x1a'

    # ALT
    ALT_A = '\x1b\x61'


ALLOW_KEY = {Key.ENTER, Key.ESC, Key.UP, Key.DOWN, Key.LEFT, Key.RIGHT}
