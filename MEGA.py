import os,zipfile

testname = 'File1.txt'
testlen = 3
testdata = ['file1-1','file1-2','file1-3']
class fileobject:
    name = ''
    linelen = 0
    data = []
    def __init__(self,namein,linelenin,datain):
        self.name = namein
        self.linelen = linelenin
        self.data = datain##may need to check if array/forceit
        
    def forcesetdata(self,forcedat):
        self.data = forcedat
        self.linelen = len(forcedat)
        
    def changename(self,newname):
        self.name = newname
    def getdata(self):
        return self.data
    def getdatalineseg(self,startl,endl):
        datseg = []
        for x in range(startl,endl+1):
            datseg.append(self.data[x])
        return datseg
    
    def getname(self):
        return self.name
    def getlinelen(self):
        return self.linelen

def makeresident():
    cwd = os.getcwd()
    os.mkdir('DATA2MEGA')
    os.chdir('DATA2MEGA')
    os.mkdir('DATA')#dat4mega conv##put in seperate folder
    os.mkdir('MEGA')#megacreatedfromdat
    os.chdir(cwd)
    os.mkdir('MEGA2DATA')#expanding
    os.chdir('MEGA2DATA')#changes to for subdir
    os.mkdir('DATA')
    os.chdir(cwd)
    os.mkdir('MEGAC')#2MEGA')#compressed

    
##compact
##get names of files
##csv names
##read each set of data in each file into array
##get length and store in length array
##write names,length,data

def compact(mega = 'OUT'):##could write len for each block in table rather then at beginning
    cwd = os.getcwd()##could maybe put at start of file dunno if lib will work or create funct to chdir from cwd to file
    os.chdir('DATA2MEGA')
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
    cfile =  open(mega+'.mega','w')
    print(csvnames)
    print(csvlinelen)
    cfile.write(csvnames+'\n')
    cfile.write(csvlinelen+'\n')
    for lines in filecontent:
        #print(lines)
        for x in lines:
            cfile.write((x.strip('\n'))+'\n')
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


def unpack_name(fname,mega):
    if '.mega' in mega.lower():
        pass
    else:
        mega+='.mega'
        
    f = open(mega,'r')
    names = csv2array(f.readline())
    lines = csv2array(f.readline())
    pos = names.index(fname)
    temp = 0
    for x in range(names.index(fname)+1):
        temp +=int(lines[x])
        print(temp)
    print(pos,'/'+str(names)+'/'+str(lines))
    f.close()


def add_name(fname,mega):#add_name('file4.txt','out')
    names = []
    csvnames = ''
    linelen = []#may have to be length in chars
    csvlinelen = ''
    filecontent = []##maynotneed
    
    cwd = os.getcwd()
    #os.chdir('MEGA2DATA')
    
    ##namecheck
    if '.mega' in mega.lower():
        pass
    else:
        mega+='.mega'

    ##uncsvnamesandlength        
    fa = open(str(mega),'r')
    names = csv2array(fa.readline())
    linelen = csv2array(fa.readline())
    f_MEGAcontent = fa.readlines()
    fa.close()
    ##print('._.'+csvnames+'._.')
    ##print(csvlinelen)
    print('Pre MEGA data')
    print('filenames: ',names)
    print('linelengths: ',linelen)
    print('MEGADATA: ',f_MEGAcontent)
    print('########END########')
    
    ##add new content
    with open(fname) as f:
        newcontent = f.readlines()##could just use seek to write to end of file instead of repacking perhaps
    f.close()
    for contentline in newcontent:
        f_MEGAcontent.append(contentline)
    linelen.append(len(newcontent))
    names.append(fname)
    print('file contents to add:\n',newcontent,'\nlinelen:',len(newcontent),'\nname of file: '+fname)
    ####csvnamesandlength
    ##csv names
    csvnames = array2csv(names)##can probably replace names with this content instead of creating a new var
    ##csv linelen
    csvlinelen = array2csv(linelen)
    ####
    
    
    ##filewriting
    print('Writing MEGA data')
    print('filenames: ',csvnames)
    print('linelengths: ',csvlinelen)
    print('MEGADATA: ',f_MEGAcontent)
    print('########END########')
    newmega = open(mega,'w')
    newmega.write(csvnames+'\n')
    newmega.write(csvlinelen+'\n')
    for x in f_MEGAcontent:
        newmega.write(x.strip('\n')+'\n')
        print(x)
    newmega.close()
    print('Done!')
    os.chdir(cwd)

    
def csv2array(csvstr):##may need os.isfile() or whatever it is to check file is in dir before declaring eofsame for array2csv
    arrayreturn = []
    temp = ''
    flag = False
    for x in csvstr:#range(len(csvnames)):
        if flag and (x==','):## ,, delimiter
            break
        if x ==',':
            arrayreturn.append(temp)
            temp = ''
            flag = True
        else:
            temp+=x
            flag = False
    return arrayreturn


def array2csv(array):
    temp = ''
    for fl in array:
        print(fl)
        temp += str(fl)+','
    temp+=','
    return temp


def peek(mega):##peek files in mega
    if '.mega' in mega.lower():
        pass
    else:
        mega+='.mega'
    f = open(mega)
    return csv2array(f.readline())


def makeMEGAC(megaIn,megac):
    if '.mega' in megaIn.lower():
        pass
    else:
        megaIn+='.mega'

    if '.megac' in megac.lower():
        pass
    else:
        megac+='.megac'
    print('compressing: '+megaIn+' --> '+megac)
    ##zippbit
    ##end
    
    
def unmakeMEGAC(megacIn,mega):##may want headers for mega and megac
    if '.mega' in mega.lower():
        pass
    else:
        mega+='.mega'

    if '.megac' in megacIn.lower():
        pass
    else:
        megacIn+='.megac'
    print('decompressing: '+megacIn+' --> '+mega)
    ##zippbit
    ##end


#def cryptMEGAheader(megax):##old def
##def cryptMega(mega,compressed = False,cryptinfo = ['','','']):#megafile|compression enabled|cryptinfo[type,key,iteration]    ####.megax for crypted output
##    if compressed:##may do different things to compressed to mk secure
##        pass
##    else:
##        pass


##def decryptMEGA(megax,cryptinfo = ['','',''])
##    pass## getheader crypted which has been encrypted in a different way
##    decrypt chunk will tell if compressed or not
##    if compressed:
##        pass
##    else:
##        pass


##def scramblelinedata(mega):  scrambles lines of data and stores linenums as tuple either next to filename or in linenumsas array[]denote cryptedlinesfor preceeding array or in separate line(line3)
##def unscramblelinedata(mega):

##def lzma_compressMEGA(data):##add as a switch
##    pass
##    ##megac as extension
##    ##has switch for returning contents as array insteadrather than turning into .mega from .MEGAC
##    ##mega c compressed variant
##def lzma_decompressMEGA(data):
##    pass
##
##def make_MEGAC():##sudocode
##    compact()
##    lzma_compress_MEGA()
##def unmake_MEGAC(data):#sudocode
##    lzma_decompressMEGA(data)
##    expand(data)
    
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
    
    



