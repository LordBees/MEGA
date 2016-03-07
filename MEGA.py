import os

def makeresident():
    cwd = os.getcwd()
    os.mkdir('DATA')#dat4mega conv##put in seperate folder
    os.mkdir('MEGA')#megacreatedfromdat
    os.mkdir('MEGA2DATA')#expanding
    os.mkdir('MEGAC')#2MEGA')#compressed
    os.chdir('MEGA2DATA')#changes to for subdir
    os.mkdir('DATA')
    os.chdir(cwd)

    
##compact
##get names of files
##csv names
##read each set of data in each file into array
##get length and store in length array
##write names,length,data

def compact():##could write len for each block in table rather then at beginning
    cwd = os.getcwd()##could maybe put at start of file dunno if lib will work or create funct to chdir from cwd to file
    os.chdir('DATA')
    names = os.listdir()
    csvnames = ''
    linelen = []#may have to be length in chars
    csvlinelen = ''
    filecontent = []
    
    ##csv names
    for fn in names:
        #if'.mega' in fn:
        #    pass
        #else:
        #    csvnames += fn+','
        csvnames +=fn+','
    csvnames+=','##eof
        
    ##reading and linelen
    for files in names:
        with open(files) as f:
            content = f.readlines()
        f.close()
        filecontent.append(content)
        linelen.append(len(content))
        print(len(content))
        
    ##csv linelen
    for fl in linelen:
        print(fl)
        csvlinelen += str(fl)+','
    csvlinelen+=','
            
    ##write data
    os.chdir('..')
    os.chdir('MEGA')
    print('writing')
    cfile =  open('OUT.mega','w')
    print(csvnames)
    print(csvlinelen)
    cfile.write(csvnames+'\n')
    cfile.write(csvlinelen+'\n')
    for lines in filecontent:
        #print(lines)
        for x in lines:
            cfile.write(x.strip('\n')+'\n')
    cfile.close()

    os.chdir(cwd)


##expand
##get namescsv of files
##uncsv names = arrayified
##get lengthcsv of files
##uncsvlength and store in length array
##read each set of data in each file into array
##get length and store in length array
##write names,length,data foreachfile

    
    
def expand(fname):
    names = []
    csvnames = ''
    linelen = []#may have to be length in chars
    csvlinelen = ''
    filecontent = []##maynotneed
    
    cwd = os.getcwd()
    os.chdir('MEGA2DATA')
    ##namecheck
    if '.mega' in fname.lower():
        pass
    else:
        fname+='.mega'

    ##uncsvnamesandlength        
    f = open(str(fname),'r')

    csvnames = f.readline()
    csvlinelen = f.readline()
    ##print('._.'+csvnames+'._.')
    ##print(csvlinelen)
    temp = ''
    flag = False
    for x in csvnames:#range(len(csvnames)):
        if flag and (x==','):
            break
        if x ==',':
            names.append(temp)
            temp = ''
            flag = True
        else:
            temp+=x
            flag = False


    temp = ''
    flag = False
    for x in csvlinelen:#range(len(csvnames)):
        if flag and (x==','):
            break
        if x ==',':
            linelen.append(int(temp))##note conv2int
            temp = ''
            flag = True
        else:
            temp+=x
            flag = False##could funct as str2array
    print(names)
    print(linelen)

    ##filewriting
    os.chdir('DATA')
    for files in names:
        filex = open(files,'w')
        for x in range(int(linelen[names.index(files)])):
            print('x'+str(x),files)
            filex.write(f.readline())
        filex.close()

    f.close()
    os.chdir(cwd)

def lzma_compressMEGA(data):##add as a switch
    pass
    ##megac as extension
    ##has switch for returning contents as array insteadrather than turning into .mega from .MEGAC
    ##mega c compressed variant
def lzma_decomressMEGA(data):
    pass

def make_MEGA():##sudocode
    compact()
    lzma_compress_MEGA()
def unmake_MEGA(data):#sudocode
    lzma_decomressMEGA(data)
    expand(data)
    
##        with open(files,'w') as filex:
##            for x in linelen:
##                print('linelenx:'+str(x))
##                for y in range(x):
##                    print('y'+str(y))
##                    print(str(x)+'.'+str(y),files)
##                    filex.write(f.readline())
##        filex.close()

    
##    for files in names:
##        with open(files,'w') as filex:
##            for x in linelen:
##                for y in range(x):
##                    filex.write(f.readline())
##        filex.close()
    
    



