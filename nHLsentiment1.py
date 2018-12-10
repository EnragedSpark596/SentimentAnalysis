"""
The purpose of this application is to retrieve text from websites about non-Hodgkins Lymphoma
on which to perform sentiment analysis.

Aim is to gather content from:
1. Main blog body
2. Comments section

"""

import requests
from bs4 import BeautifulSoup
import pandas
import string

#Target list
baseURL_1="https://www.lls.org/blog/my-journey-through-stage-iv-non-hodgkin-lymphoma"

req1=requests.get(baseURL_1)
content1=req1.content
soup1=BeautifulSoup(content1,"html.parser")

# Blog body content grab
all1=soup1.find_all("div",{"class":"article-content x2-top"})
# Blog comments content grab
all2=soup1.find_all("div",{"class":"comments-block x4-top x4"})

# takes content from copy body as list items and cleans out html codes
blogBodyCopy=[]

for item in all1[0].find_all("p"):
    blogBodyCopy.append(item.text.replace("\xa0","").replace("\u200a"," ").replace("\u200b"," "))

# takes content from comments as list items and cleans out html codes
blogCommentsCopy=[]

for item in all2[0].find_all("p"):
    blogCommentsCopy.append(item.text.replace("\n",""))

#removes blanks
blogBodyCopy = list(filter(None, blogBodyCopy))

#merges into one block of copy
blogBodyCopy=" ".join(blogBodyCopy)
blogCommentsCopy=" ".join(blogCommentsCopy)

# removes non-printable / encodable characters
printable = set(string.printable)

blogBodyCopy = ''.join(filter(lambda x: x in printable, blogBodyCopy))
blogCommentsCopy = ''.join(filter(lambda x: x in printable, blogCommentsCopy))

#saves copy as text file
with open("nHLsentiment1.txt", "w+") as file:
    file.write("Source:" + baseURL_1 + "\n" + blogBodyCopy + "\n" + "\n" + blogCommentsCopy)
