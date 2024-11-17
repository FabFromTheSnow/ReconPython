#!/usr/bin/pythonb3
from urllib.request import urlopen
import subprocess

print("CTF recon")
ctf_platform_acronym = "." + input("What extension is use for your platform url(example : HTB, THM)")
ctf_platform_acronym.lower()

ctf_Name = input("What is the name of this ctf ?")
urlCTF = ctf_Name + ctf_platform_acronym
ctf_IP = input("What is the ip of the initial target ?")

hostfileD = ctf_IP + "  " +  urlCTF
#subprocess.call(['sudo', 'echo', hostfileD, "> /etc/hosts"])  to be tested on linux

def robottxt():
    print(hostfileD)
    url = urlCTF + "/robots.txt"
    print(url)
    try:
        page = urlopen("https://" + url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        print(html)
        return(url)
    except:
        pass
    try:
        page = urlopen("http://" + url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        print(html)
        return(url)
    except:
        print("there is no robots.txt")

def sitemapXML():
    print(hostfileD)
    url = urlCTF + "/sitemap.xml"
    print(url)
    try:
        page = urlopen("https://" + url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        print(html)
        return(url)
    except:
        pass
    try:
        page = urlopen("http://" + url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        print(html)
        return(url)
    except:
        print("there is no sitemap")


robottxt()
sitemapXML()
