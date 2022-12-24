import re
import subprocess

# used this expunging method from Markus Jarderot
# https://stackoverflow.com/a/241506/13793957

# problem: when there is a \t in the code, 
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
                y += '|'

    return y


x = """public class PrintStatement {
    // the main method is required for any code to run in Java
    public static void main(String[] args) {
        // This will print Hello World and then move to the next line
        System.out.println("Hello World");
        
        // This will print Good morning and then move to the next line
        System.out.println("Good morning!");
        
        // This will print 'The T-rex has the PIE' and will NOT move to the next line
        System.out.print("The T-rex has the PIE!");
    }
}"""



subprocess.run('pbcopy', text=True, input=comment_remover(x))
print('Copied to clipboard!')