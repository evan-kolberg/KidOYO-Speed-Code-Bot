import subprocess

mode = 'C++'


# Paste the raw coding exercise into this variable
x = '''#include <iostream>

int main() {
    std::cout << "Comments in C++" << std::endl;
    // Comments are solely intended to be used as notes 
    // by the humans that read the source code
    std::cout << "Use // to comment single line" << std::endl;
    /*
     This is multi-line comments
     Use slash-star to begin, and star-slash to end
    */
    std::cout << "Use /* ... */ to comment multi lines" << std::endl;
    
    return 0;
}'''


comment = False
force_all = True
y = ''

if mode == 'HTML':
    for i in x.split('\n'):
        if comment == True:
            if i.strip()[-3:] == '-->' or i.strip()[-2:] == '*/':
                comment = False
                continue
            else:
                continue

        if i.strip()[:4] == '<!--' or i.strip()[:2] == '/*':
            if i.strip()[-3:] == '-->' or i.strip()[-2:] == '*/':
                continue
            else:
                comment = True
                continue

        y += i.strip()
        if i != x.split()[-1]:
            y += '|'



# ABANDONED THIS METHOD OF EXPUNGING COMMENTS
if mode == 'C++':
    for i in x.split('\n'):

        if '"' in i.strip():
            for j in i.strip():
                if j == '"':
                    y += j
                    continue
        else:

            if comment == True:
                if '*/' in i.strip():
                    comment = False
                    continue
                else:
                    continue

            if '/*' in i.strip() and '*/' in i.strip():
                continue
            elif '/*' in i.strip() and not '*/' in i.strip():
                comment = True
                continue


            if  '//' in i.strip():
                if i.strip()[:2] == '//':
                    continue
                else:
                    y += i.strip()[:i.find('/')-4]
                    continue
            y += i.strip()
            if i != x.split()[-1]:
                y += '|'



for i in range(2):
    if '||' in y:
        y = y.replace('||', '|')

subprocess.run('pbcopy', text=True, input=y)
print('Copied to clipboard!')