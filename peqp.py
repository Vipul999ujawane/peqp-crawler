import requests
import re
import os
import datetime
#url = "http://10.18.24.22/peqp/"
#response=requests.get(url)

def logging(data):
    log=open("peqp.log","a")
    print(data)
    log.write(str(datetime.datetime.now())+" :: "+data+"\n")
    log.close()

def crawl(url,host):
    to_crawl=[]
    to_crawl.append(url)
    while to_crawl:
        current_url=to_crawl.pop(0)
        logging("current: " + current_url)
        dir_path='C:\\Users\\hp\\Desktop\\GRU_All'
        r=requests.get(current_url)
        if(current_url.endswith(".pdf")):
            fname=os.path.join(dir_path,str((current_url.replace(host,"")).replace("/","\\"))[1:])
            fname = re.sub('[\']', '', fname)  
            try: 
                file = open(fname, "w+")
            except:
                logging("ERROR ERROR : MOVING ON")
                continue
            file.write(str(r.content))
            file.close()
            logging("File Written Successfully")
        for link in re.findall('<A HREF="([^"]+)">', str(r.content)):
           # print(link)
            if(len(link)==1):
                continue
            if(link[0]=='/'):
                if(link.endswith(".pdf")==False):
                    #print(dir_path)
                    dir2=os.path.join(dir_path,(link.replace('/',"\\"))[1:])
                    logging(dir2)
                    if(os.path.isdir(dir2)==False):
                        os.mkdir(dir2)
                    logging("Directory Made: "+str(dir2))
                link=host + link
            to_crawl.append(link)
    return True

print(crawl("http://10.18.24.22/peqp/","http://10.18.24.22"))