import subprocess

mode = 'HTML'


# Paste the raw coding exercise into this variable
x = '''<!DOCTYPE html>
<html>
    <head>
        <title>CSS in style tag</title>
        <style>
            /* Everything between the style tags are written in another language: CSS. 
               Start by choosing a selector to modify, such as a HTML element, followed 
               by a set of curly braces. 
            */
            
            /* CSS comment: In CSS, you start a comment with a forward slash 
               followed by an asterisk and end it with an asterisk followed by 
               a forward slash. Comments do not affect your code in any way. 
               They are for the coder's reference only. You should comment so 
               others know what you are trying to do but also for yourself so 
               you remember what you were trying to do in the future. 
            */
            
            body {
                /* A CSS declarartion follow a "property: value" format. 
                   The property changes an element of a selector and the 
                   value changes to what you want to change the property to. 
                */
                background-color: green;
            }
            h1 {
                color: pink;
            }
            p {
                color: white;
            }
        </style>
    </head>
    <body>
        <h1>CSS in style tag</h1>
        <p>Text inside the p tag becomes white because of the defined CSS above.</p>
    </body>
</html>'''




if mode == 'HTML':
    comment = False
    y = ''

    for i in x.split('\n'):
        if comment == True:
            if i.strip()[-3:] == '-->' or i.strip()[-2:] == '*/':
                comment = False
                continue
            else:
                continue

        if i.strip()[0:4] == '<!--' or i.strip()[0:2] == '/*':
            if i.strip()[-3:] == '-->' or i.strip()[-2:] == '*/':
                continue
            else:
                comment = True
                continue

        y += i.strip()
        if i != x.split()[-1]:
            y += '|'

for i in range(2):
    if '||' in y:
        y = y.replace('||', '|')

subprocess.run('pbcopy', text=True, input=y)
print('Copied to clipboard!')