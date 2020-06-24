

from tkinter import Tk
import serial
def main():
	root=Tk()
	botonON=Button(root,text="ON",command=on)
	botonOFF=Button(root,text="OFF")
	botonON.pack()
	botonOFF.pack()
	root.mainloop()
def ON():
	ser=serial.Serial("/dev/ttyACM0",9600)
	time.sleep(10)
	ser.write('1')
main()

