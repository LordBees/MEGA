#ziplib

##def unzip(source_filename, dest_dir):
##    with zipfile.ZipFile(source_filename) as zf:
##        for member in zf.infolist():
##            zf.extract(member, dest_dir)

##def unzip(source_filename, dest_dir):
##    with zipfile.ZipFile(source_filename) as zf:
##        zf.extractall(dest_dir)

##import zipfile
##with zipfile.ZipFile("ds_dphs_csv.zip") as a:
##        a.extractall()
import zipfile,os
def ext2dir(fname,dname):##filename , dirname
    cwd = os.getcwd()
    zipfl = zipfile.ZipFile(os.getcwd()+'\\'+fname+".zip")
    os.mkdir(str(dname))
    os.chdir(str(dname))
#    with  as a:
    zipfl.extractall()
    os.chdir(cwd)
    
def extract_all(fname):
    with zipfile.ZipFile(str(fname)+".zip") as a:
        a.extractall()
##testing push system
def walkforzip():
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            #break
            print(os.path.join(root, name))
        for name in dirs:
            #break
            print(os.path.join(root, name))
            
