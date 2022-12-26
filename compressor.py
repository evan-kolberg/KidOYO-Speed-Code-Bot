import re
import subprocess

# used this method from Markus Jarderot to expunge comments
# https://stackoverflow.com/a/241506/13793957

# problem: when there is a \t or \n in the code, 
# it is seem as an escape character in python
# you have to manually fix it by adding a "\\"
def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " " # note: a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    y = ''
    for i in re.sub(pattern, replacer, text).split('\n'):
        if i.strip() == '':
            continue
        else:
            y += i.strip()
            if i != x.split()[-1]:
                y += '⭔'

    return y


x = """




"""



subprocess.run('pbcopy', text=True, input=comment_remover(x))
print('Copied to clipboard!')

