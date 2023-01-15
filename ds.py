import os ;
def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    subfile=[f.path for f in os.scandir(dirname) if f.is_dir()==False]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    subfolders=subfolders+subfile
    return subfolders
def Cloning(li1):
    li_copy = li1[:]
    return li_copy
li2=Cloning(fast_scandir("/home/revan/rw"))
print(li2)