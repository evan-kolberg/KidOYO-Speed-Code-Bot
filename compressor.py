import re
import subprocess

# used this method from Markus Jarderot to expunge comments
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
                y += 'ᨆ'

    return y


x = """

public class LeapYear {
    public static void main(String[] args) {
        int year = 2104;
        // if the year is divisible by 4, it is probably a leap year
        boolean c1 = (year % 4 == 0);
        // except if it is divisible by 100
        boolean c2 = (year % 100 != 0);
        // but if it is also divisible by 400 then it is a leap year
        boolean c3 = (year % 100 == 0 && year % 400 == 0);
        
        // if the year is divisible by 4 and it is either (not divisible by 100) or (divisible by 400)
        // then it is a leap year
        if (c1 && (c2 || c3)) {
            System.out.println(year + " is a leap year");
        }
        else {
            System.out.println(year + " is not a leap year");
        }
    }
}


"""



subprocess.run('pbcopy', text=True, input=comment_remover(x))
print('Copied to clipboard!')

