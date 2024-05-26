import termcolor
from termcolor import colored

def print_heart(colors):
    heart_shape = [
        '  @@@   @@@  ', 
        ' @@@@@ @@@@@ ', 
        '@@@@@@@@@@@@@', 
        '@@@@@@@@@@@@@', 
        ' @@@@@@@@@@@ ', 
        '  @@@@@@@@@  ', 
        '   @@@@@@@   ', 
        '    @@@@@    ', 
        '     @@@     ', 
        '      @      '
    ]
    
    for line in heart_shape:
        colored_line = ""
        for idx, char in enumerate(line):
            if char == "@":
                color = colors[idx % len(colors)]
                colored_line += colored(char, color)
            else:
                colored_line += char
        print(colored_line)

def main():
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    print_heart(colors)

if __name__ == "__main__":
    main()
