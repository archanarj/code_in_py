import argparse
import textwrap

def justify_text(file, width):
    with open(file) as f:
        line = f.readline()
        width = int(width)
    splitted_width_text = textwrap.fill(line, width)
    splitted_lines = splitted_width_text.splitlines()
    print(splitted_width_text)
    print(splitted_lines)
    for x in range(0, len(splitted_lines)):
        print("Array [",x,"] = ", splitted_lines[x])

if __name__ == '__main__':
    # defined parser to parse
    parser = argparse.ArgumentParser(description='Text justfication')
parser.add_argument('--file','-f',help='text file path',required=True )
parser.add_argument('--width','-w',help='page width', required=True )
args = parser.parse_args()

justify_text(args.file, args.width)
