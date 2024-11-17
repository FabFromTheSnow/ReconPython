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

webserverS = False
webserver = False

def CheckWeb():
    global webserverS
    global webserver
    print("Check for webserver")

    # Check HTTPS
    try:
        page = urlopen("https://" + urlCTF)
        html_bytes = page.read()
    except:
        print("No https server")
        webserverS = False
    else:
        print("https server detected")
        webserverS = True

    try:
        page = urlopen("http://" + urlCTF)
        html_bytes = page.read()
    except:
        print("No http server")
        webserver = False
    else:
        print("http server detected")
        webserver = True

def robot():
    print("Check for robots")
    url = urlCTF + "/robots.txt"
    if webserverS:
        try:
            page = urlopen("https://" + url)
            html_bytes = page.read()
            robots = html_bytes.decode("utf-8")
        except:
            print("No robots")
        else:
            print(robots)
    elif webserver:       
        try:
            page = urlopen("http://" + url)
            html_bytes = page.read()
            robots = html_bytes.decode("utf-8")
        except:
            print("No robots")
        else:
            print(robots)

def CheckFile():
    url = urlCTF + "/sitemap.xml"
    print("Check for sitemap")
    if webserverS:
        try:
            page = urlopen("https://" + url)
            html_bytes = page.read()
            sitemap = html_bytes.decode("utf-8")
            print(sitemap)
        except:
            print("No sitemap")
    elif webserver:   
        try:
            page = urlopen("http://" + url)
            html_bytes = page.read()
            sitemap = html_bytes.decode("utf-8")
            print(sitemap)
        except:
            print("No sitemap")
    robot()    

        
        


CheckWeb()
CheckFile()

