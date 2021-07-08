'''
Developed by: Zaahier Adams
https://github.com/ZaahierAdams
'''

import os
import shutil
import time
import sys

##RootDir1 =      r'C:\1\2'
##TargetFolder =  r'C:\1\2'
##File_type=      '.txt'

print('-'*80+'\n[About]: Moves specified files from a source directory to a target directory.')
print('\t Does not handle identical file names.\n'+'-'*80)
while True:
        RootDir1 = input('\n(1)Input Source Directory: ')
        TargetFolder = input('(2)Input Target Directory: ')
        File_type =input('(3)Input File type: ')
        print('\n')

        Folders_searched,Files_inspected,Valid_File=0,0,0
        loading = 0
        start = time.time()

        for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):

                if loading > 7:
                        loading = 0
        ##        sys.stdout.write('\r'+'Searching for ('+File_type+') files'+'.'*loading+' '*7)
                loading += 1
                
                sys.stdout.write('\r'+'Folders ['+str(Folders_searched)+'], Files ['+str(Files_inspected)+'], Moved ['+str(Valid_File)+'] '+'.'*loading+' '*7)
                
                Folders_searched+=1     
                for name in files:
                    Files_inspected+=1
                    if name.endswith(File_type):
        ##                if Valid_File == 0:
        ##                    print('\nFiles found:')
        ##                print('>> '+name.replace(File_type,''))
                        Valid_File+=1
                        SourceFolder = os.path.join(root,name)
                        shutil.move(SourceFolder, TargetFolder)
        end = time.time()
        sys.stdout.write('\r'+'\tSearch Completed'+' '*30)
        print('\n'+'-'*35)

        print('Search took',str(round(end-start))+'seconds')
        print('\n['+str(Folders_searched)+']\tFolders Searched')
        print('['+str(Files_inspected)+']\tFiles inspected')
        print('['+str(Valid_File)+']\tFiles moved !!!')

        ##print('>'*3,str(Folders_searched),'folder(s) searched')
        ##print('>'*3,str(Files_inspected),'file(s) inspected')
        ##if Valid_File !=0:
        ##    print('>'*3,str(Valid_File),'('+File_type+') file(s) were moved, over',str(round(end-start,0))+'seconds.')
        ##
        ##else:
        ##    print('>'*3+' No ('+File_type+') files were found !!!')

        print('-'*35)
        restart = input('Restart(y/n)').lower()
        if restart == 'y':
                pass
        else:
                break







