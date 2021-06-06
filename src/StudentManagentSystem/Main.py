from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql

class student:
	def __init__(self, root):
		self.root = root
		blank_space = " "
		self.root.title(200 * blank_space + "Student Database Management System")
		self.root.geometry("1350x600+0+0")

		MainFrame(self.root, bd= 10, width = 1350, height= 700, relief=RIDGE, bg="cadet")