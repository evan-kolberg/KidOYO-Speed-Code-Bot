import subprocess

mode = 'HTML'


# Paste the raw coding exercise into this variable
x = '''
'''




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

if '||' in y:
    y = y.replace('||', '|')

subprocess.run('pbcopy', text=True, input=y)
print('Copied to clipboard!')