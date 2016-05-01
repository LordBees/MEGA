import os,zipfile

testname = 'File1.txt'
testlen = 3
testdata = ['file1-1','file1-2','file1-3']

hexchars = '1234567890ABCDEF'
class fileobject:
    name = ''
    linelen = 0
    data = []
    def __init__(self,namein,linelenin,datain):
        self.name = namein
        self.linelen = linelenin
        self.data = datain##may need to check if array/forceit
        
    def forcesetdata(self,forcedat):##forces the data of the file to the input specified
        self.data = forcedat
        self.linelen = len(forcedat)
        
    def changename(self,newname):##changes fileobject name
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
def hex2std(m):##adds 0x to hex
    global hexchars
    tempa=[]
    buffer=''
    for x in range(len(m)):
        if (len(buffer))==2:
            tempa.append('0x'  + buffer)
            buffer = ''
            buffer+=m[x]
        else:
            buffer+=m[x]
    tempa.append('0x'  + buffer)
    print(tempa)
    return tempa
##class xor:
##    def __init__ (self):
##        pass
##    def do(self,k,m):
##        pass
##    def de(self,k,m):
##        pass
##    def hexdo
    
def xor(k,m):##normal txt custom
    ##process xor hexify ascii codes then strip 0x and pack
    temp = ''
    temphx = ''##for holding to check
    for x in range(len(m)):
        print('~~~~~~~~//')
        print('Mchar: '+str(m[x]))
        print('Kchar: '+str(k[x%len(k)]))
        print('Msg: '+str(temp))
        print('Result: '+str(ord(m[x])^ord(k[x%len(k)])))
        print(hex(ord(m[x])^ord(k[x%len(k)])).upper())#[2:].upper())
        if len(hex(ord(m[x])^ord(k[x%len(k)]))[2:].upper())<2:
            temp +=hex(ord(m[x])^ord(k[x%len(k)]))[2:].upper()
            temp+='0'
        else:
            temp +=hex(ord(m[x])^ord(k[x%len(k)]))[2:].upper()##ascii values turned into hex and 0x chopped
        #temp += chr((ord(k[(len(str(k))%int(x+1))]))^ord(m[x]))
	#for x in range(len(temp)):
            #temp[x] = chr(temp[x])
    return temp

def xorA(k,m):#arrays
    tempa = []
    for part in m:
        tempa.append(xor(k,part))
    return tempa

def DExor(k,m):
    global hexchars
    tempa=[]##hex
    tempb=[]##ascii codes den
    hbyteb=[0,0]#hexbytebuffer
    buffer=''
    for x in range(len(m)):
        if (len(buffer))==2:
            tempa.append(buffer)
            buffer = ''
            buffer+=m[x]
        else:
            buffer+=m[x]
    tempa.append(buffer)
    print(tempa)
    for x in range(len(tempa)):
        hbyteb[0] = (hexchars.index(tempa[x][0].upper())+1)*16
        hbyteb[1] = (hexchars.index(tempa[x][1].upper())+1)
        tempb.append(int(hbyteb[0])+int(hbyteb[1]))
        print(hbyteb)
    print(tempb)
    for x in range(len(tempb)):#xordec
        #tempb[tempb.index(x)] = chr(str(int(x)^ord(k[x%len(k)])))
        print(chr((int(tempb[x])^ord(k[x%len(k)]))))
    print(tempb)
    return tempb


def DExorA(k,m):#arrays
    tempa = []
    for part in m:
        tempa.append(DExor(k,part))
    return tempa
def Xt():
    k='key'
    m='test'
    DExor(k,xor(k,m))
    
##    print(tempa)
##    tempa=[]
##    buffer=''
##    for x in m:
##        if (len(buffer))==2:
##            tempa.append('0x'  + buffer)
##            buffer = ''
##        else:
##            buffer+=x
##    print(tempa)

##    tempa = []
##    buffer = ''
##    for x in m:##readd the 0x bit
##        if len(buffer) == 2:##hex = 2nums
##            tempa.append('0x' + buffer)
##            buffer = ''
##            print('bc')
##            buffer+=x
##        else:
##            print('add:'+str(x))
##            buffer+=x
##        print(x)
##    print(buffer)
##    print(len(x),';L;',len(m))
##    print(tempa)

            
##def DExor(k,m):##normal txt custom
##    temp = ''
##    buffer = ''
##    for x in range(len(m)):
##        print('#########    ITER:'+str(x))
##        print('Mchar: '+str(m[x]))
##        print('Kchar: '+str(k[x%len(k)]))
##        print('Msg: '+str(temp))
##        print('Result: '+str(ord(m[x])^ord(k[x%len(k)])))
##        if m[x] == ' ':
##            print('@')
##            for letters in range(len(buffer)):#for letters in buffer:
##                temp +=chr(ord(buffer[letters])^ord(k[letters%len(k)]))
##                print(temp,'    ',buffer)
##                buffer = ''
##        else:
##            buffer += m[x]
##        
##        #temp += chr((ord(k[(len(str(k))%int(x+1))]))^ord(m[x]))
##	#for x in range(len(temp)):
##            #temp[x] = chr(temp[x])
##    return temp
##
##def DExorA(k,m):#arrays
##    tempa = []
##    for part in m:
##        tempa.append(DExor(k,part))
##    return tempa

def xtst():
    k = 'key'
    m = 'message'
    c = xor(k,m)
    u = xor(k,c)
    print('========\nkey = '+k+'\nmessage = '+m+'\n')
    print('crypt/uncrypt')
    print('\nc',c,'\nu',u)
    
def XXtst():
    k = 'key'
    m = 'message'
    c = xor(k,m)
    u = DExor(k,c)
    print('========\nkey = '+k+'\nmessage = '+m+'\n')
    print('crypt/uncrypt')
    print('\nc',c,'\nu',u)
    
    


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


def unpackfile_return(fname,mega):##unpacks file then returns array with data and names for use in prgs
    returner = []##name,len,dat
    if '.mega' in mega.lower():
        pass
    else:
        mega+='.mega'
        
    f = open(mega,'r')
    names = csv2array(f.readline())
    lines = csv2array(f.readline())
    pos = names.index(fname)
    MEGA_data = f.readlines()
    FILE_data = []
    filelinetable=[]##all end of datalines use prev endofdatalines to get data

    
    filelinepos = 0##satartline of the line data
    for x in range(names.index(fname)+1):#filepos of data in array 
        filelinepos +=int(lines[x])##gets linepos from adding linelen together
        #print(filelinepos)
        filelinetable.append(filelinepos)
    print(filelinetable)
    print(pos,'/'+str(names)+'/'+str(lines)+'@@@@@@END@@@@@@\n')
    f.close()
    if fname.index(fname) == 0:
        for x in range(0,filelinetable[0]):##case fopr first entry as no previous marker could check for none or neg val instead
            FILE_data.append(MEGA_data[x].strip('\n'))##appends entries to outfile
    else:
        for x in range(filelinetable[pos-1],filelinetable[pos]):
            FILE_data.append(MEGA_data[x].strip('\n'))##ALSO STRIPS\n form lines
            #pass
            #pass#FILE_data = megafile
        
    returner.append(names[pos])
    returner.append(lines[pos])
    returner.append(FILE_data)
    
    return returner


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
    peeker = f.readline()
    f.close()
    return csv2array(peeker)#csv2array(f.readline())

######XOR CRYPTO
def makeMEGAC(megaIn,megac,k = 'key'):##the newlines \n are causing probs crypto works fine but handling of data not
    cwd = os.getcwd()
    os.chdir(cwd)
    os.chdir('test')
    if '.mega' in megaIn.lower():
        pass
    else:
        megaIn+='.mega'

    if '.megac' in megac.lower():
        pass
    else:
        megac+='.megac'
    print('encrypting: '+megaIn+' --> '+megac)
    ##cbit
    f = open(megaIn,'r')
    Mdatin  = f.readlines()
    f.close()
    print(Mdatin)
    input()
    Mdatout = xorA(k,Mdatin)
    print(Mdatout)
    input()
    Mf = open(megac,'w')
    for x in Mdatout:
        Mf.write(x)
    f.close()
    os.chdir(cwd)
    ##end
    
    ##r unmakeMEGAC('TEST','OUT',k = 'key')
def unmakeMEGAC(megacIn,mega,k = 'key'):##may want headers for mega and megac
    cwd = os.getcwd()
    os.chdir(cwd)
    os.chdir('test')
    if '.mega' in mega.lower():
        pass
    else:
        mega+='.mega'

    if '.megac' in megacIn.lower():
        pass
    else:
        megacIn+='.megac'
    print('decrypting: '+megacIn+' --> '+mega)
    ##cbit
    f = open(megacIn,'r')
    Mdatin  = f.readlines()
    f.close()
    print(Mdatin)
    input()
    Mdatout = xorA(k,Mdatin)
    print(Mdatout)
    input()
    Mf = open(mega,'w')
    for x in Mdatout:
        Mf.write(x)
    f.close()
    os.chdir(cwd)
    ##end

def cryptotest():
    makeMEGAC('TESTFILE','ENCRYPTED',k = 'key')
    unmakeMEGAC('ENCRYPTED','DECRYPTED',k = 'key')
    #makeMEGAC('TEST','OUT',k = 'key')
####ENDXOR CRYPTO

####mega zip
def makeMEGAZ(megaIn,megaZ):##megazip
    if '.mega' in megaIn.lower():
        pass
    else:
        megaIn+='.mega'

    if '.megaZ' in megaZ.lower():
        pass
    else:
        megaZ+='.megaZ'
    print('compressing: '+megaIn+' --> '+megac)
    ##zippbit
    ##end
    
    
def unmakeMEGAZ(megazIn,mega):##may want headers for mega and megac
    if '.mega' in mega.lower():
        pass
    else:
        mega+='.mega'

    if '.megaz' in megazIn.lower():
        pass
    else:
        megazIn+='.megaz'
    print('decompressing: '+megazIn+' --> '+mega)
    with zipfile.ZipFile(str(fname)+".megaz") as a:###NOT DONE
        a.extractall()
    print('megaz = '+mega+'\nDONE!')
    
    ##zippbit
    ##end
##END    
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
    
    



