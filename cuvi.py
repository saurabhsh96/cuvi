import os
import sys
import serial
from threading import Thread
import time
import signal
import subprocess as sp
import random
n=0 #no of threads

#to specify what to be done at the starting up of the program
class startup:

    def __init__(self):
        global n
        try:
            self.port=serial.Serial('/dev/ttyACM0', 9600)
        except:
            self.port=serial.Serial('/dev/ttyACM1', 9600)
        n=1
        self.t=Thread(target=self.func1)
        self.t1=Thread(target=self.func2)
        self.t.setDaemon(True)
        self.t1.setDaemon(True)
        self.t.start()
        self.t1.start()
        self.t.join()
        self.t1.join()

    def func2(self):
        try:
            self.readf=open('/home/saurabh/Desktop/{}.txt'.format(time.localtime()[2]), 'r')
            
        except:
            os.system("espeak 'Tasks are not yet been Scheduled'")
            print "Tasks are not yet been Scheduled"
            

    def func1(self):
        global n
        self.sch=[]
        #global port
        self.y=""
        self.command=""
        self.tasks=[]
        os.system("espeak 'Hello, sir'")
        time.sleep(0.5)
        print("Hello, Sir!")
        x=time.localtime()
        if(x[3]>=0 and x[3]<12):
            os.system("espeak 'It is, {} o clock and {} minutes, Good morning, how can I help you?'".format(x[3], x[4]))
            #time.sleep(1)
            print("It is, {} o'clock and {} minutes, Good morning, how can I help you?".format(x[3], x[4]))
        elif(x[3]>=12 and x[3]<4):
            os.system("espeak 'It is, {} o clock and {} minutes, Good afternoon, how can I help you?'".format(x[3], x[4]))
            #time.sleep(1)
            print("It is, {} o'clock and {} minutes, Good afternoon, how can I help you?".format(x[3], x[4]))
        elif(x[3]>=4 and x[3]<=23):
            os.system("espeak 'It is, {} o clock and {} minutes, Good evening, how can I help you?'".format(x[3], x[4]))
            #time.sleep(1)
            print("It is, {} o'clock and {} minutes, Good evening, how can I help you?".format(x[3], x[4]))

        os.system("espeak 'Please, tell me your choice, sir?'")
        #time.sleep(1)
        print("Please, tell me your choice, sir?")

        os.system("espeak 'Do you want to listen songs?'")
        #time.sleep(1)
        print("Do you want to listen songs?")
        
        os.system("espeak 'Or do you want to watch movies?'")
        #time.sleep(1)
        print("Or do you want to watch movies?")

        os.system("espeak 'We can browse internet too!'")
        #time.sleep(1)
        print("We can browse internet too!")

        os.system("espeak 'If you want to run any other application, please tell'")
        #time.sleep(1)
        print('If you want to run any other application, please tell!')

        os.system("espeak 'Tell me if you have any tasks to schedule!'")
        #time.sleep(1)
        print('Tell me if you have any tasks to schedule!')
        
        os.system("espeak 'If you want I can shut down too, Sir!'")
        #time.sleep(1)
        print('If you want I can shut down too, Sir!')

        while(1):
            self.y=self.port.readline().rstrip() #in coming sentense is stored in y
            #print self.y
            if(self.y>0):
                self.y=self.y[1:] #first and last character of the string is stripped out as It is useless
                self.y=self.y[:-1]
                #print self.y
                os.system("espeak 'You just said, {}!'".format(self.y))
                #time.sleep(1)
                print("You just said, {}".format(self.y))
                self.y=self.y.lower()
                #print self.command

                if(self.y=="volume up"):
                    os.system("espeak 'Tell the percentage, sir!'")
                    #time.sleep(1)
                    print 'Tell the percentage, sir!'
                    x=self.port.readline().rstrip()
                    x=x[1:]
                    x=x[:-1]
                    os.system("amixer -D pulse sset Master {}%+".format(x))

                if(self.y=="volume down"):
                    os.system("espeak 'Tell the percentage, sir!'")
                    #time.sleep(1)
                    print 'Tell the percentage, sir!'
                    x=self.port.readline().rstrip()
                    x=x[1:]
                    x=x[:-1]
                    os.system("amixer -D pulse sset Master {}%-".format(x))

                if(self.y=="mute"):
                    os.system("amixer -D pulse sset Master 100%-")

                if(self.y=="power off" or self.y=="turn off" or self.y=="shut down"):
                    os.system("espeak 'I am turning off the computer, sir! Good bye!'")
                    #time.sleep(1)
                    print 'I am turning off the computer, sir! Good bye!'
                    os.system("echo asdfghjkl | sudo -S poweroff")

                if(self.y=="restart"):
                    os.system("espeak 'I am turning restarting the computer, sir!'")
                    #time.sleep(1)
                    print 'I am turning off the computer, sir!'
                    os.system("echo asdfghjkl | sudo -S reboot")

                if(self.y=="lock"):
                    os.system("espeak 'I am locking up the system!'")
                    #time.sleep(1)
                    print 'I am locking up the system, sir!'
                    os.system("gnome-screensaver-command -l")

                """if(self.y=="unlock"):
                    os.system("espeak 'I am unlcocking the system!'")
                    time.sleep(1)
                    print 'I am unlocking the system!'
                    pwd="asdfghjkl" 
                    os.system("export DISPLAY=:0; sleep 5; xdtool type {}; xdtool key Return".format(pwd))"""
                    
                if(self.y=="what is your name" or self.y=="who are you"):
                    os.system("espeak 'I am Mate! version 1.0, I am coded using pure logic!'")
                    print 'I am Mate! version 1.0, I am coded using pure logic!'
                    #time.sleep(1)
                    os.system("espeak 'I work for Mr Nerkar!, He is the Iron Man!'") # :P
                    print 'I work for Mr Nerkar!, He is the Iron Man!'
                    time.sleep(1)

                if(self.y=="hi" or self.y=="hello"):
                    os.system("espeak 'Hey, hello!'")
                    print "Hey, hello! :P"

                if(self.y=="stop songs" or self.y=="exit songs" or self.y=="exit song" or self.y=="end song" or self.y=="end songs"):
                    os.killpg(self.p_songs.pid, signal.SIGTERM)
                    self.y=""

                if(self.y=="stop movies" or self.y=="exit movies"):
                    os.killpg(self.p_movies.pid, signal.SIGTERM)
                    self.y=""

                if(self.y=="stop browsing" or self.y=="exit browser"):
                    os.killpg(self.p_browse.pid, signal.SIGTERM)
                    self.y=""

                if(self.y=="stop else" or self.y=="exit else"):
                    os.killpg(self.p_else.pid, signal.SIGTERM)
                    self.y=""


                self.command=self.y.split(' ')
                for i in self.command:
                    if(i=="music"):
                        self.tasks.append("music")
                    if(i=="movies"):
                        self.tasks.append("movies")
                    if(i=="browse"):
                        self.tasks.append("browse")
                    if(i=="else"):
                        print "succes"
                        self.tasks.append("other")
                    if(i=="schedule"):
                        self.tasks.append("schedule")
                    if(i=="exit" or i=="bye bye" or i=="bbye" or i=="good bye" or i=="bye"):
                        os.system("espeak 'I am shutting down sir, good bye!'")
                        time.sleep(1)
                        print 'I am shutting down sir, good bye!'
                        sys.exit()
                    if(i=="switch"):
                        os.system("espeak 'Which program, sir?'")
                        time.sleep(0.5)
                        print 'Which program, sir?'
                        temp=self.port.readline().rstrip()
                        temp=temp[1:]
                        temp=temp[:-1]
                        os.system("wmctrl -a {}".format(temp))
                    if(i=="wallpaper"):
                        print "saurabh"
                        setup="/mnt/data1/Photos/DCIM/Camera/"+random.choice(os.listdir("/mnt/data1/Photos/DCIM/Camera"))
                        print setup     
                        os.system("DISPLAY=:0 GSETTINGS_BACKEND=dconf gsettings set org.gnome.background picture-uri 'file://%s'"%(setup))

                    if(i=="file"):
                        os.system("espeak 'Tell the file name.'")
                        print 'Tell the file name.'
                        filename=self.port.readline().rstrip()
                        filename=filename[1:]
                        filename=filename[:-1]
                        fp=open('/home/saurabh/{}.txt'.format(filename), 'w')
                        os.system("espeak 'Narrate the content line by line.'")
                        print 'Narrate the content line by line.'
                        while(self.port.readline().rstrip()!="*finish#"):
                            fp=open('/home/saurabh/{}.txt'.format(filename), 'a')
                            line=self.port.readline().rstrip()
                            line=line[1:]
                            line=line[:-1]
                            print line
                            fp.write(line)
                            fp.close()
                        

                self.command=""

            for i in self.tasks:

                if(i=="music"):
                    #n=n+1
                    self.p_songs=self.songs()
                    
                if(i=="movies"):
                    #n=n+1
                    self.p_movies=self.movies()
                    
                if(i=="browse"):
                    #n=n+1
                    self.p_browse=self.browse()

                if(i=="other"):
                    #n=n+1
                    self.p_other=self.other()
                    
                if(i=="schedule"):
                    #n=n+1
                    self.p_schedule=self.schedule()
                    
            self.tasks[:]=[]
         
    def songs(self):
        p_songs=sp.Popen("xdg-open '/mnt/data1/playlist3.xspf'", stdout=sp.PIPE,
                         shell=True, preexec_fn=os.setsid)
        return p_songs
        
    def movies(self):
        os.chdir('/mnt/data1')
        p_movies=sp.Popen("xdg-open 'movies.xspf'", stdout=sp.PIPE,
                          shell=True, preexec_fn=os.setsid)
        return p_movies
        
    def browse(self):
        os.system("espeak 'Tell me the broswer and website, please!'")
        time.sleep(1)
        print 'Tell me the broswer and website, please!'
        #time.sleep(1)
        x=self.port.readline().rstrip()
        x=x[1:]
        x=x[:-1]
        z=self.port.readline().rstrip()
        z=z[1:]
        z=z[:-1]
        print x, z
        if(x=="Chrome"):
            x="chromium-browser"
        if(x=="Firefox"):
            x="firefox"
        else:
            x="chromium-browser"
        p_browse("{} '{}'".format(x, z), stdout=sp.PIPE,
                 shell=True, preexec_fn=os.setsid)
        return p_browse
        
    def other(self):
        os.system("espeak 'Tell me the application you want to run, please, be precise!'")
        #time.sleep(3)
        print "Tell me the application you want to run, please, be precise"
        #time.sleep(3)
        x=self.port.readline().rstrip()
        x=x[1:]
        x=x[:-1]
        x=x.lower()
        p_else=sp.Popen(x, stdout=sp.PIPE, shell=True, preexec_fn=os.setsid)
        return p_else
        
    def schedule(self):
        os.system("espeak 'How many tasks would you like to be scheduled?'")
        x=self.port.readline().rstrip()
        x=x[1:]
        x=x[:-1]
        temp=[]
        self.fp=open('/home/saurabh/Desktop/{}.txt'.format(time.localtime()[2], 'a'))
        for i in range(int(x)):
            os.system("espeak 'Tell task number {} and its time!'".format(str(i)))
            x=self.port.readline().rstrip()
            x=x[1:]
            x=x[:-1]
            temp.append(x)
            x=self.port.readline().rstrip()
            x=x[1:]
            x=x[:-1]
            temp.append(x)
            self.sch.append(temp)
            temp[:]=[]
        for i in self.sch:
            print>>self.fp, i
            
    
if __name__=="__main__":
    obj1=startup()

        
