from .globals import Command
from .ls import Ls
from .exit import Exit
from .cd import Cd
from .echo import Echo
from .uniq import Uniq
from .whoami import Whoami

commands = {"ls": Ls, "cd": Cd, "exit": Exit, "echo": Echo, "uniq": Uniq, "whoami": Whoami}