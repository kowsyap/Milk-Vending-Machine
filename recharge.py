import pandas as pd
import RPi.GPIO as g
from mfrc522 import SimpleMFRC522

g.setmode(g.BCM)
g.setup(2, g.IN)

global count
count = 0
global bal
bal = 0
global cost
global flag
flag = 0
x = 0

def increaserev(channel):
    global count
    count += 1
    if count == 4:
        count = 0
        global bal
        bal = bal + 1
        print("Balance is " + str(bal))        
g.add_event_detect(2, g.RISING, callback=increaserev)

def RFID():
    reader =SimpleMFRC522()
    try:
        id,_=reader.read()
        print(id)
        df =pd.read_csv('data.csv')
        for i in range(len(df)):
            if(df['id'][i]==id):
                l = [df['name'][i],df['balance'][i]]
                return ([1,l])
        return 0
    finally:
        g.cleanup()

def recharge():
    flag = RFID()
    if flag==0:
        print("Error Looks like you have not registered yet:)")
       # tmsg.showinfo("Error", "Looks like you have not registered yet:)")
       # top.destroy()
    else:
        name = flag[1][0]
        balance_amount = flag[1][1]
        if(x==1): #x is ok button
            dff = pd.read_csv('data.csv')
            for i in range(len(dff)):
                if(dff['name'][i]==name):
                    global bal
                    balance_amount = int(balance_amount)+bal        
                    dff.set_value(i,'balance',balance_amount)
                    dff.to_csv('data.csv', index=False)

def bal_update():
    global amount
    global flag
    name = flag[1][0]
    balance_amount = flag[1][1]
    dfff = pd.read_csv('data.csv')
    for i in range(len(dfff)):
        if(dfff['name'][i]==name):
            balance_amount = int(balance_amount)-amount       
            dfff.set_value(i,'balance',balance_amount)
            dfff.to_csv('data.csv', index=False)

        
        
        

    