import sys
import os

def bsh(filename):
    f = open(filename,'r')
    path = None
    for line in f:
        if line.startswith('#!'):
            path = line.replace('#!','').strip()
            mode = 'bash'
            fp = open(path+'/py.py','w')
            fb = open(path+'/bash.sh','w',newline='')
            fv = open(path+'/.bin','w')
            fr = open(path+'/run.sh','w',newline='')
            #run
            fr.write('bash '+path+'/bash.sh'+'\n')
            fr.write('python '+path+'/py.py'+'\n')
            #python
            fr.close()
            fp.write('bsh = {}'+'\n')
            fp.write('def getf(var):'+'\n')
            fp.write('  '+'f = open(".bin","r")'+'\n')
            fp.write('  '+'for line in f:'+'\n')
            fp.write('      '+'line = line.strip()'+'\n')
            fp.write('      '+'if line.startswith(var+"="):'+'\n')
            fp.write('          '+'bsh[var]=line.replace(var+"=","")'+'\n')
            #bash
            fb.write('bshbin=0'+'\n')
            fb.write('function exportf() {'+'\n')
            fb.write('    echo "$1=$bshbin" >> .bin'+'\n')
            fb.write('}'+'\n')
            #parsing
            for line1 in f:
                if line1.startswith('-end'):
                    mode = 'bash'
                elif line1.startswith('-py'):
                    mode = 'python'
                else:
                    if mode == 'bash':
                        fb.write(line1+'\n')
                    elif mode == 'python':
                        fp.write(line1+'\n')
            #run
            os.system('bash '+path+'/run.sh')

if len(sys.argv) ==2:
    bsh(sys.argv[1])
else:
    raise Exception('Invalid amount of arguments')
