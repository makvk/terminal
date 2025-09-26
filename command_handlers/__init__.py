from .globals import Command
from .ls import Ls
from .bash import Bash
from .exit import Exit
from .cd import Cd

commands = {"bash": Bash, "ls": Ls, "cd": Cd, "exit": Exit}