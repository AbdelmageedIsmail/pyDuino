try:
	import tkinter as tk
	from tkinter import ttk
except ImportError:
	# Python 2
	import Tkinter as tk
	import ttk

import parser
import base64
import serial
import Tkinter as tk

#ser = serial.Serial('COM3', baudrate=9600, timeout=1)

class TkGUI(tk.Tk):
	FONT_LARGE = ("Calibri", 32)  	# selects the font of the text inside buttons
	FONT_MED = ("Calibri", 32)

	# Max rows and columns in the GUI
	MAX_ROW = 3 
	MAX_COLUMN = 8
	i = 0
	NEW_OPERATION = False
	BINARY_CODE = 0
	BTN1_ACTIVE = False
	BTN2_ACTIVE = False
	BTN3_ACTIVE = False
	BTN4_ACTIVE = False
	BTN5_ACTIVE = False
	BTN6_ACTIVE = False
	BTN7_ACTIVE = False
	BTN8_ACTIVE = False

	

	def __init__(self):
		try:
			super(TkGUI, self).__init__()
		except TypeError:
			# Python 2
			tk.Tk.__init__(self)

		self.title('Leds Controller By Abdelmageed Ismail')
		self.resizable(width=True, height=True)

		for row in range(self.MAX_ROW):
			self.columnconfigure(row,pad=1)

		for column in range(self.MAX_COLUMN):
			self.rowconfigure(column,pad=1)

		self.display = tk.Entry(self, font=("Calibri", 48),justify='center')
		self.display.grid(row=1, columnspan=8, sticky=tk.W + tk.E)

                self._init_ui()
            

	def _init_ui(self):
                global photo_off
                photo_off=tk.PhotoImage(file="off.gif")

                global photo_on
                photo_on=tk.PhotoImage(file="on.gif")
                
		global one
		one = tk.Button(
			self, text="1-OFF", command=lambda: self.get_variables1(1), font=self.FONT_LARGE)
		one.grid(row=2, column=7)
                one.config(image=photo_off)
                one.image = photo_off
                

		global two
		two = tk.Button(
			self, text="2-OFF", command=lambda: self.get_variables2(2), font=self.FONT_LARGE)
		two.grid(row=2, column=6)
		two.config(image=photo_off)
                two.image = photo_off

		global three
		three = tk.Button(
			self, text="3-OFF", command=lambda: self.get_variables3(4), font=self.FONT_LARGE)
		three.grid(row=2, column=5)
		three.config(image=photo_off)
                three.image = photo_off

                global four
		four = tk.Button(
			self, text="4-OFF", command=lambda: self.get_variables4(8), font=self.FONT_LARGE)
		four.grid(row=2, column=4)
		four.config(image=photo_off)
                four.image = photo_off

		global five
		five = tk.Button(
			self, text="5-OFF", command=lambda: self.get_variables5(16), font=self.FONT_LARGE)
		five.grid(row=2, column=3)
		five.config(image=photo_off)
                five.image = photo_off

		global six
		six = tk.Button(
			self, text="6-OFF", command=lambda: self.get_variables6(32), font=self.FONT_LARGE)
		six.grid(row=2, column=2)
		six.config(image=photo_off)
                six.image = photo_off

                global seven
		seven = tk.Button(
			self, text="7-OFF", command=lambda: self.get_variables7(64), font=self.FONT_LARGE)
		seven.grid(row=2, column=1)
		seven.config(image=photo_off)
                seven.image = photo_off

		global eight
		eight = tk.Button(
			self, text="8-OFF", command=lambda: self.get_variables8(128), font=self.FONT_LARGE)
		eight.grid(row=2, column=0)
		eight.config(image=photo_off)
                eight.image = photo_off

		#b=Button(self,justify = LEFT)
                
                #one.config(image=photo,width="10",height="10")
                #b.pack(side=LEFT)


	def clear_all(self, new_operation=True):
		"""clears all the content in the Entry widget."""
		self.display.delete(0, tk.END)
		self.NEW_OPERATION = new_operation

	def get_variables1(self, num):
                if self.BTN1_ACTIVE:
                        self.BTN1_ACTIVE = False
                        self.BINARY_CODE = self.BINARY_CODE - num
                        one.config(text='1-OFF')
                        one.config(image=photo_off)
                        one.image = photo_off
                else:
                        self.BTN1_ACTIVE = True
                        self.BINARY_CODE = self.BINARY_CODE + num
                        one.config(text='1- ON')
                        one.config(image=photo_on)
                        one.image = photo_on
                
                self.disp_binary(self.BINARY_CODE)

        def get_variables2(self, num):
                if self.BTN2_ACTIVE:
                        self.BTN2_ACTIVE = False
                        self.BINARY_CODE = self.BINARY_CODE - num
                        two.config(text='2-OFF')
                        two.config(image=photo_off)
                        two.image = photo_off
                else:
                        self.BTN2_ACTIVE = True
                        self.BINARY_CODE = self.BINARY_CODE + num
                        two.config(text='2- ON')
                        two.config(image=photo_on)
                        two.image = photo_on
                        
                self.disp_binary(self.BINARY_CODE)

        def get_variables3(self, num):
                if self.BTN3_ACTIVE:
                        self.BTN3_ACTIVE = False
                        self.BINARY_CODE = self.BINARY_CODE - num
                        three.config(text='3-OFF')
                        three.config(image=photo_off)
                        three.image = photo_off                        
                else:
                        self.BTN3_ACTIVE = True
                        self.BINARY_CODE = self.BINARY_CODE + num
                        three.config(text='3- ON')
                        three.config(image=photo_on)
                        three.image = photo_on
                        
                self.disp_binary(self.BINARY_CODE)

                
        def get_variables4(self, num):
                if self.BTN4_ACTIVE:
                        self.BTN4_ACTIVE = False
                        self.BINARY_CODE = self.BINARY_CODE - num
                        four.config(text='4-OFF')
                        four.config(image=photo_off)
                        four.image = photo_off        
                else:
                        self.BTN4_ACTIVE = True
                        self.BINARY_CODE = self.BINARY_CODE + num
                        four.config(text='4- ON')
                        four.config(image=photo_on)
                        four.image = photo_on

                        
                self.disp_binary(self.BINARY_CODE)

        def get_variables5(self, num):
                if self.BTN5_ACTIVE:
                        self.BTN5_ACTIVE = False
                        self.BINARY_CODE = self.BINARY_CODE - num
                        five.config(text='5-OFF')
                        five.config(image=photo_off)
                        five.image = photo_off
                        
                else:
                        self.BTN5_ACTIVE = True
                        self.BINARY_CODE = self.BINARY_CODE + num
                        five.config(text='5- ON')
                        five.config(image=photo_on)
                        five.image = photo_on

                        
                self.disp_binary(self.BINARY_CODE)

        def get_variables6(self, num):
                if self.BTN6_ACTIVE:
                        self.BTN6_ACTIVE = False
                        self.BINARY_CODE = self.BINARY_CODE - num
                        six.config(text='6-OFF')
                        six.config(image=photo_off)
                        six.image = photo_off
                        
                else:
                        self.BTN6_ACTIVE = True
                        self.BINARY_CODE = self.BINARY_CODE + num
                        six.config(text='6- ON')
                        six.config(image=photo_on)
                        six.image = photo_on
                        
                self.disp_binary(self.BINARY_CODE)

        def get_variables7(self, num):
                if self.BTN7_ACTIVE:
                        self.BTN7_ACTIVE = False
                        self.BINARY_CODE = self.BINARY_CODE - num
                        seven.config(text='7-OFF')
                        seven.config(image=photo_off)
                        seven.image = photo_off
                        
                else:
                        self.BTN7_ACTIVE = True
                        self.BINARY_CODE = self.BINARY_CODE + num
                        seven.config(text='7- ON')
                        seven.config(image=photo_on)
                        seven.image = photo_on
                        
                self.disp_binary(self.BINARY_CODE)

        def get_variables8(self, num):
                if self.BTN8_ACTIVE:
                        self.BTN8_ACTIVE = False
                        self.BINARY_CODE = self.BINARY_CODE - num
                        eight.config(text='8-OFF')
                        eight.config(image=photo_off)
                        eight.image = photo_off
                        
                else:
                        self.BTN8_ACTIVE = True
                        self.BINARY_CODE = self.BINARY_CODE + num
                        eight.config(text='8- ON')
                        eight.config(image=photo_on)
                        eight.image = photo_on
                        
                        
                self.disp_binary(self.BINARY_CODE)
               

        def disp_binary(self,num):
                self.clear_all()
		self.display.insert(0, bin(num)[2:].zfill(8) )
		#self.display.insert(14, num )
		print bin(num)[2:].zfill(8)
		self.i += 1
		ser.write(chr(num))
        


	def run(self):
		self.mainloop()
