#!/usr/bin/env python3
import paramiko
import warnings 
import time
from git import Repo
from git import db
from datetime import date

output_file = 'paramiko.org' 
warnings.filterwarnings(action='ignore',module='.*paramiko.*')
def paramiko_GKG(hostname, command):
    #print('running')
    try:
        port = '22'
         
        # created client using paramiko
        client = paramiko.SSHClient()
         
        # here we are loading the system 
        # host keys
        client.load_system_host_keys()
         
        # connecting paramiko using host 
        # name and password
        client.connect(hostname, port=22, username='dell',
                       password='dell')
         
        # below line command will actually 
        # execute in your remote machine
        (stdin, stdout, stderr) = client.exec_command(command,timeout=10)
        exit_status = stdout.channel.recv_exit_status()          # Blocking call
         
        # redirecting all the output in cmd_output 
        # variable
        linenum=0
        for line in stdout.readlines():
                linenum = linenum+1
                if(linenum == 2):
                        out = line.strip()
                        print(out)
             
        # we are returning the output
        return out
    finally:
        client.close()
 
#cmd ="Get-Counter -Counter '\Processor(_Total)\% Processor Time'"
psCmd = "wmic cpu get loadpercentage"
f = open("cpu_usage.txt", "w")

# GIT Settings
full_local_path = "/home/jinu/Documents/JINU/gitRepo/githubio/jinujayachandran.github.io"
username = "jinujayachandran"
password = "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"
remote = f"git@github.com:jinujayachandran/jinujayachandran/jinujayachandran.github.io.git"
repo = Repo(full_local_path,odbt=db.GitDB)

#f.write("   IP Address            CPU Load    ")
#f.write("------------------    ---------------")
while(1):
        t = time.localtime()
        today = date.today()
        d1 = today.strftime("%d-%m-%Y")
        current_time = time.strftime("%H:%M:%S", t)
        f.seek(0)

        usage = paramiko_GKG('10.208.67.109', psCmd)
        fstr ="10.208.67.109      "+(usage)+"%\n"
        print(fstr)
        f.write(fstr)

        #usage =paramiko_GKG('10.208.67.26', psCmd)
        #fstr ="10.208.67.26       "+(usage)+"%\n"
        #print(fstr)
        #f.write(fstr)

        usage = paramiko_GKG('10.208.67.247', psCmd)
        fstr ="10.208.67.247      "+(usage)+"%\n"
        print(fstr)
        f.write(fstr)

        usage = paramiko_GKG('10.208.66.95', psCmd)
        fstr ="10.208.66.95       "+(usage)+"%\n"
        print(fstr)
        f.write(fstr)

        usage = paramiko_GKG('10.208.66.217', psCmd)
        fstr ="10.208.66.217      "+(usage)+"%\n"
        print(fstr)
        f.write(fstr)

        time.sleep(5)

        f.write("\n\n\n")
        timeStr="Updated On "+current_time+"  "+d1
        f.write(timeStr)
        f.truncate()
        
        #Commit and push to GIT.
        commitStr = "CPU Load Update"
        origin = repo.remote(name="origin")
        existing_branch = repo.heads['main'] 
        existing_branch.checkout() 
        repo.index.add(['cpu_usage.txt'])
        repo.index.commit(commitStr)
        origin.push()



