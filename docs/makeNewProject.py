#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from os import listdir
from os.path import isfile, join
import time, datetime
import re
import sys

import shutil
import glob
from pathlib import Path
import json


# # Function

# In[2]:


def createSidebar(projectName):
    newProject = projectName
    
    cwd = os.getcwd()
    templateSidebar = cwd + '\\_template\\template_sidebar.yml'
    dstFile = templateSidebar.replace('\\_template\\','\\_data\\sidebars\\').replace('template',newProject)
    
    srcFile = templateSidebar
    dstFile = templateSidebar.replace('\\_template\\','\\_data\\sidebars\\').replace('template',newProject)
    shutil.copy(srcFile, dstFile)
    
    with open(srcFile,'r', encoding="utf8") as src:
        with open(dstFile,'w', encoding="utf8") as dst:

            line = src.readline()

            while line:
                if 'template' in line:
                    line = line.replace('template',newProject)

                dst.write(line)    
                line = src.readline()
    
    print('Finished creating sidebar')


# In[3]:


def createPosts(projectName):
    newProject = projectName
    
    cwd = os.getcwd()
    
    src = cwd + '\\_template\\templatePost\\'
    dst = cwd + '\\_posts\\'+newProject
    
    shutil.copytree(src, dst)  
    
    print('Finished creating posts')


# In[4]:


def createPages(projectName):
    newProject = projectName
    
    cwd = os.getcwd()
    
    srcFolder = cwd + '\\_template\\templatePages\\'
    dstFolder = cwd + '\\pages\\'+newProject + '\\'
    os.mkdir(dstFolder)
    
    onlyfiles = [f for f in listdir(srcFolder) if isfile(join(srcFolder, f))]
    
    for fileName in onlyfiles:
        with open(srcFolder+fileName,'r', encoding="utf8") as src:
            with open(dstFolder+fileName.replace('template',newProject),'w', encoding="utf8") as dst:
                line = src.readline()

                while line:
                    if 'template' in line:
                        line = line.replace('template',newProject)

                    dst.write(line)    
                    line = src.readline()            
    
    print('Finished creating pages')


# In[5]:


def addToNav(projectName):
    newProject = projectName
    
    cwd = os.getcwd()
    
    navFile = cwd + '\\_data\\topnav.yml'

    with open(navFile,'a', encoding="utf8") as nav:
        nav.write('\n')
        nav.write(f"        - title: {newProject}\n")
        nav.write(f"          url: /{newProject}_intro.html")
        
    print('Finished adding to topnav.html')


# In[6]:


def main(projectName):
    createSidebar(projectName)
    createPosts(projectName)
    createPages(projectName)
    addToNav(projectName)    


# # Main

# In[7]:


#newProject = 'newProject'


# In[8]:


#main(newProject)


# In[ ]:


if __name__ == '__main__':
    argList = list(sys.argv)
    main(argList[1])

