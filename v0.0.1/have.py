import urllib2
import urllib
import os
import sys
import cookielib
#import hasit

class HOpener(urllib.FancyURLopener):
    version = "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/6.0"

if "__main__"==__name__:
    hist=raw_input('Enter the width:')
    cj = cookielib.CookieJar()
    hasit = urllib2.build_opener(
        urllib2.HTTPRedirectHandler(),
        urllib2.HTTPHandler(debuglevel=0),
        urllib2.HTTPSHandler(debuglevel=0),
        urllib2.HTTPCookieProcessor(cj)
    )
# pretend we're a web browser and not a python script
    hasit.addheaders = [('User-agent',
        ('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; InfoPath.2; .NET4.0C; .NET4.0E; MSOffice 12)'
         ))
    ]
#    hasit=HOpener()
    url=raw_input()
    #HPA=raw_input('Enter Prefix:')
    HPA='PA'
    url=url.split('&')[0]
    print url
#    dr=raw_input('Enter the folder:')
    dr="."
    try:
        os.chdir(url.split('id=')[1])
    except:
        os.mkdir(url.split('id=')[1])
        os.chdir(url.split('id=')[1])
    y=hasit.open(url+'&printsec=frontcover')
    cj=y.headers['set-cookie']
    popop=open(url.split('id=')[1]+'.txt','w')
    popop.write(cj);
    popop.close()
    print cj
#    y=hasit.open(url+'&printsec=frontcover') 
#    hey=open('ggl.html','w')
    j=""
    for i in y:
#        hey.write(i)
        j+=i
#    hey.close()
    y.close()
#    print url
#    print j
    '''try:
        n=int(j.split(',"num_pages":')[1].split(',')[0])
    except:
        n=input('Enter number of pages:')'''
#    print "%d pages" % n
    if(os.listdir('.').count('frontcover.jpg')==0):
        j=j.split("preloadImg.src = '")[1].split("'")[0][:-3]+hist
        x=hasit.open(j)
        image=open('frontcover.jpg','wb')
        for i in x:
            image.write(i)
        image.close()
        x.close()
#    lilo=open('lilo.txt','w')
#    rast=open("list11.txt","w")
    for hast in range(input('Starting Page:'),input('Total Pages')+1):
#        print hast
        if(os.listdir('.').count('h'+str(10000+hast)+'.png')):
            continue
        flag=1
        j=""
#        lol=open("PA"+str(hast)+".html",'w')
        x=hasit.open(url+'&pg='+HPA+str(hast))
        for i in x:
            j+=i
#            lol.write(i)
        j=j.split("preloadImg.src = '")[1].split("'")[0][:-3]+hist
        x.close()
#        rast.write(j+'\n')
#        print "Link for page {} generated".format(hast)
#        os.system("C:\\Users\\Hasit\\AppData\\Local\\Google\\Chrome SxS\\Application\\chrome.exe "+j)
#        print j
#        lol.close()
#        print j+'&'+'h'+str(10000+hast)+'.png'
        try:
            x=hasit.open(j+'&'+'h'+str(10000+hast)+'.png')
        except:
            flag=0
#            lilo.write(j+'\n')
        if(flag):
            hihihi='h'+str(10000+hast)+'.png'
            image=open(hihihi,'wb')
            for i in x:
                image.write(i)
	    print 'Succesfully Saved Page#{}'.format(hast)
            image.close()
            x.close()
'''            if(os.stat(hihihi).st_size > 20000L):
                print 'Succesfully Saved Page#{}'.format(hast)
            else:
                os.remove(hihihi)'''
#    lilo.close()
#    rast.close()

