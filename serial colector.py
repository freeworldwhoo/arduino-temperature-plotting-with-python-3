from serial import Serial
import time
'''set the serial to connect to the arduino (you should change the port)'''
ser =Serial(
    port='COM8',
    baudrate = 115200,
    timeout=None)
def adddata(data):
    '''a function to add the data to the text file'''
    date=time.time()
    h=str(data)+','+str(date)+'\n'
    fh = open('example.txt', 'a')
    fh.write(h) 
    fh.close 
while 1:
    ''' infinit loop'''
    while(ser.inWaiting()==0):
        '''wait for the data from serial'''
        pass
    a=float(ser.readline().decode('utf-8'))
    '''read and decode the data'''
    adddata(a)
    '''add the data to the txt file'''
