import os, random, sys, time, webbrowser

try:
    from colorama import Fore, Style
    r = Fore.RED
    b = Fore.BLUE
    y = Fore.YELLOW
    g = Fore.GREEN
    bl = Fore.BLACK
    m = Fore.MAGENTA
    c = Fore.CYAN
    res = Style.RESET_ALL
except ImportError:
    print("Colorama Module Not Installed Yet\nWhen Finished Restart this script\nInstalling...")
    l = 'sudo apt install python-colorama'
    w = 'pip install colorama'
    os.system([l,w][os.name == 'nt'])

class brainfuck:
    def __init__(self):
        self.clear()
        self.print_logo()
        self.encode()
    def print_logo(self):
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37]

        x = """

           _______   ________  ________        _______                         _____                        __     
          /       \ /        |/        |      /       \                       /     |                      /  |    
          $$$$$$$  |$$$$$$$$/ $$$$$$$$/       $$$$$$$  | ______    ______     $$$$$ |  ______    _______  _$$ |_   
          $$ |__$$ |$$ |__    $$ |__          $$ |__$$ |/      \  /      \       $$ | /      \  /       |/ $$   |  
          $$    $$< $$    |   $$    |         $$    $$//$$$$$$  |/$$$$$$  | __   $$ |/$$$$$$  |/$$$$$$$/ $$$$$$/   
          $$$$$$$  |$$$$$/    $$$$$/          $$$$$$$/ $$ |  $$/ $$ |  $$ |/  |  $$ |$$    $$ |$$ |        $$ | __ 
          $$ |__$$ |$$ |      $$ |_____       $$ |     $$ |      $$ \__$$ |$$ \__$$ |$$$$$$$$/ $$ \_____   $$ |/  |
          $$    $$/ $$ |      $$       |      $$ |     $$ |      $$    $$/ $$    $$/ $$       |$$       |  $$  $$/ 
          $$$$$$$/  $$/       $$$$$$$$/       $$/      $$/        $$$$$$/   $$$$$$/   $$$$$$$/  $$$$$$$/    $$$$/  
                                                                BrainFuck enCoder v1.0
                                                                Thanks to Ali HalabSaz for Idea <3
                                                                Coded by iWhh                                         
                iraniancoders.ir - iran-cyber.net
                        github.com/iwhh                            
                                                                                                         


        """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" %(random.choice(colors), line, clear))
            time.sleep(0.05)
    def clear(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])
    def encode(self):
        print(m + "---------------------------------")
        inp = input(c + "Enter Your Text " + r + "$ ")    
        bfout = ''
        for encode in inp:
            bfout += ("+" * ord(encode)) + ".>"
        print(m + "---------------------------------")
        print(c + "Result ~>\n" + y + str(bfout))
        webbrowser.open("https://t.me/joinchat/AAAAAERn-oqcxCt82_tEug")
try:
    bf = brainfuck()
except KeyboardInterrupt:
    print(y + "\n[" + r + "<3" + y +"] " + g + "Nice To meet you ")
