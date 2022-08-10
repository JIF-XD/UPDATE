import os,time,rich
from rich.panel import Panel as nel
from rich import print as cetak
 
__alvino__ganteng__ = '\t[yellow]•[white] [green]WELCOME[white] TO JIF TOOL[yellow] •[white]'
cetak(nel(__alvino__ganteng__));time.sleep(1)
 
if __name__ == "__main__":
        try:
                __import__("JIF").()
        except Exception as e:
                exit(str(e))
