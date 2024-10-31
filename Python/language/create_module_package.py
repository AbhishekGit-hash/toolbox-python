
'''
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              karaoke.py
              ...
'''

import sound.effects.echo
from sound.effects import echo

