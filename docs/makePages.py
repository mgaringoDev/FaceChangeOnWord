#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[1]:


# Imports
import os
from os import listdir
from os.path import isfile, join
import time, datetime
from pathlib import Path
import sys


# # Functions

# In[2]:


def myHelp():
    projects = ['migraine', 'fibro', 'lieDection']
    pageType = ['notes', 'reporting']
    
    strOut = """
        python makePages.py <project> <pageType>
        
        <project>
            - covid
            - fifmaps
            - medHolo
            - stravaMaps
        
        <pageType>
            - notes
            - reporting
        
        EXAMPLE:
            python makePages.py migraine notes
            
            python makePages.py migraine reporting 1EtDIPsZCLa-zPJWRKR6qOZM044n-BLSD
            
        NOTES:
            If you are using reporting you have to add the user ID            
    """
    
    print(strOut)


# In[3]:


def writeOut(project,pageType,frontMatter):
        
    cwd = os.getcwd()
    dirOut = cwd+'\\_posts\\'+project+'\\'+pageType+'\\'
    fileOut = datetime.date.today().isoformat() + '-ADD_TITLE.md'

    with open(dirOut+fileOut,'w+',encoding="utf8") as newNote:
        newNote.writelines(frontMatter)
    
    os.system("subl " + dirOut+fileOut)


# In[4]:


def writeFrontMatter(param):

    if len(param) == 2:
        project = param["projectType"]
        pageType = param["pageType"]
        
        frontMatter = getFrontMatter(projectType = project,
                       pageType = pageType)
        
    elif len(param) == 3:
        project = param["projectType"]
        pageType = param["pageType"]
        gID = param["gID"]
        
        frontMatter = getFrontMatter(projectType = project,
                                     pageType = pageType,
                                     gID=gID)
    else:
        print('Something went wrong\nRUN python makePages.py help for more detail')
        return 0
        
    writeOut(project,pageType,frontMatter)
        


# In[5]:


def myCheck(argList):
    print(argList[1])
    if len(argList)==2:
        if argList[1] == 'help':
            myHelp()
        else:
            print('Something went wrong\nRUN python makePages.py help for more detail')
        return 0
    
    try:
        if len(argList)==3:
            param = {
                "projectType":argList[1],
                "pageType":argList[2]
            }

            writeFrontMatter(param)
        elif len(argList)==4:
            param = {
                "projectType":argList[1],
                "pageType":argList[2],
                "gID":argList[3]
            }
            
            writeFrontMatter(param)
        else:
            print('Something went wrong\nRUN python makePages.py help for more detail')
        
    except Exception as e:
        print('Something went wrong\nRUN python makePages.py help for more detail')


# In[6]:


def getFrontMatter(projectType = 'migraine', 
                   pageType = 'notes',
                   gID= "1EtDIPsZCLa-zPJWRKR6qOZM044n-BLSD"):
    
    if projectType=='migraine':
        projectTypeCat = 'migraineHSI'
    else:
        projectTypeCat = projectType        
        
    
    if pageType == 'reporting':
        print("Creating a new reporting page")
        strOut = f"""---
title:      ____ADD__TITLE
author:     Mario Garingo
keywords:   ____ADD__KEYWORDS
summary:    ____ADD__SUMMARY
category:   {projectTypeCat}
type:       {pageType}
gDrivePDFile: {gID}
sidebar:    {projectType}_sidebar 
---"""
        
    else:
        print("Creating a new note page")
        strOut = f"""---
title:      ____ADD__TITLE
author:     Mario Garingo
keywords:   ____ADD__KEYWORDS
summary:    ____ADD__SUMMARY
category:   {projectTypeCat}
type:       {pageType}
sidebar:    {projectType}_sidebar 
---"""
    
    return strOut


def main(argList):
    for a in argList:
        print(a)
    myCheck(argList)


# # Main

# In[ ]:


if __name__ == "__main__":    
    main(list(sys.argv))

