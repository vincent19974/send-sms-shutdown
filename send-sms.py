#!/usr/bin/python

import os, time
import sys
from twilio.rest import Client
#print("Enter Number of Seconds to Shutdown System: ")
#sec = int(input())

def shutdown():
    count = 0
    client = Client("AC5a1c6180888f1935bc9db7f3ff854f51", "9753aa7db0a12e5d3a90f95d2a78b1e2")
    # the following line needs your Twilio Account SID and Auth Token
    print("Are you sure you want to reboot? Yes/no")
    sec1 = str(input())
    while sec1 != 'Yes':
        count +=1;
        print("What do you want me to do?")
        sec1 = str(input())
        if sec1 == "Sleep":
            print("Your PC is about to sleep")
            for i in reversed(range(1, 6)):
                time.sleep(1)
                print("%s\r" %i)
            client.messages.create(to="+639361439068",
                    from_="+17242432231",
                    body="Hey Mr.NAMBATAC your pc is about to sleep")
            os.system("sudo systemctl suspend")

    

        if count == 5:
            print("Please Try Again Later!")
            client.messages.create(to="+639361439068",
                    from_="+17242432231",
                    body="Hey Mr.NAMBATAC, Someone attempted to shutdown your PC" + " " + str(count) + " " + "times, do you know about this?")
            break

    else:
        print("Shutting Down ..")
        os.system("sudo reboot")

shutdown()
    
