ROWS, COLUMNS = 20, 10

GRID_WIDTH = 300
GRID_HEIGHT = 2*GRID_WIDTH

WIDTH = GRID_WIDTH + 300
HEIGHT = GRID_HEIGHT

FONT_SIZE = 30

BUTTON_WIDTH = 150
BUTTON_HEIGHT = 70
BUTTON_X = int(1/2*GRID_WIDTH) + int(1/2*WIDTH) - int(1/2*BUTTON_WIDTH)
SCORE_Y = 100
LEVEL_Y = 50
START_BUTTON_Y = 100 + SCORE_Y
RESTART_BUTTON_Y = 100 + START_BUTTON_Y
QUIT_BUTTON_Y = 100 + RESTART_BUTTON_Y

BLOCK_SIZE = int(GRID_WIDTH / COLUMNS)

BACKGROUND = (0, 0, 0)

GRID_COLOR = (105, 105, 105)

INTERVAL = 1000

O = [['00.',
      '00.',
      '...']]

I = [['.0..',
      '.0..',
      '.0..',
      '.0..',
      '.....'],
     [#'.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

L = [['..0.',
      '000.',
      '....',
      '....'],
     [#'....',
      '.0..',
      '.0..',
      '.00.',
      '....'],
     [#'....',
      #'....',
      '000.',
      '0...',
      '....'],
     [#'....',
      '00..',
      '.0..',
      '.0..',
      '....']]


J = [['0...',
      '000.',
      '....',
      '....'],
     [#'....',
      '.00.',
      '.0..',
      '.0..',
      '....'],
     [#'....',
      #'....',
      '000.',
      '..0.',
      '....'],
     [#'....',
      '.0..',
      '.0..',
      '00..',
      '....']]

S = [['.00..',
      '00...',
      '....'],
     ['.0..',
      '.00.',
      '..0.',
      '....']]


Z = [['00..',
      '.00.',
      '....'],
     ['.0..',
      '00..',
      '0...',
      '....']]

T = [['.0..',
      '000.',
      '....',
      '....'],
     ['.0..',
      '.00.',
      '.0..',
      '....'],
     ['000.',
      '.0..',
      '....'],
     ['.0..',
      '00..',
      '.0..',
      '....']]

PIECES = [O, I, L, J, S, Z, T]

COLORS = [(255, 255, 0), 
          (0, 255, 255), 
          (255, 127, 0), 
          (0, 0, 255), 
          (0, 255, 0), 
          (255, 0, 0), 
          (128, 0, 128)]

