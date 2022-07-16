#!/usr/bin/env python
"""
This is my interpreter for tab.
:Author: benni347@github.com
"""
import os.path
import random as rnd
import re  # for regex
import math
from datetime import datetime


class Interpreter:
	def __init__(self):
		self.code: str = ""

	def set_code(self, code):
		"""
		Sets the code to be used in the program.
		:param code: a str
		:return: None
		"""
		self.code = code

	def get_code(self):
		"""
		Returns the code.
		:return: a str
		"""
		return self.code

	def ask_user(self):
		"""
		Ask the user if he wants to writer the code in the terminal or to load from a file
		:return:
		"""
		print("Do you want to write the code in the terminal or load from a file?")
		print("1. Write in the terminal")
		print("2. Load from a file")
		choice = input("Choice: ")
		if choice == "1":
			self.write_code()
		elif choice == "2":
			self.load_code()
		else:
			print("Invalid choice")
			self.ask_user()

	def write_code(self):
		"""
		Write the code in the terminal.
		:return: None
		"""
		print("Write the code in the terminal")
		self.code = input("Code: ")
		sequence = self.interpreter(self.get_code())
		self._print(sequence)

	def load_code(self):
		"""
		Load the code from a file.
		:return: None
		"""
		print("Load the code from a file")
		file = input("File: ")
		with open(file, "r") as f:
			self.code = f.read()
		sequence = self.interpreter(self.get_code())
		self._print(sequence)

	@staticmethod
	def interpreter(code):
		"""
		Finds the sequence of the code.
		:param code: a str
		:return: a str
		"""
		output = ''
		char_code = 0
		for char in code:
			if char_code >= 255:
				char_code = 0
			if char == ' ':
				char_code = char_code + 1
			if char == '	':
				output += chr(char_code)
		return output

	def _print(self, sequence):
		"""
		Prints the sequence.
		:param sequence: a str
		:return: None
		"""
		print(sequence)


class Compiler:
	"""
	This will convert text to tab code.
	:return:
	"""

	def __init__(self):
		self.text: str = ""
		self.file_name: str = ""
		self.path: str = ""

	def set_path(self, path):
		"""
		Sets the path.
		:param path: a str
		:return: None
		"""
		self.path = os.path.join(path, self.get_file_name()+".tab")

	def get_path(self):
		"""
		Returns the path.
		:return: a str
		"""
		return self.path


	def get_file_name(self):
		"""
		Returns the file name.
		:return: a str
		"""
		return self.file_name

	def set_file_name(self, file_name):
		"""
		Sets the file name.
		:param file_name: a str
		:return: None
		"""
		self.file_name = file_name

	def set_text(self, text):
		"""
		Sets the text to be used in the program.
		:param text: a str
		:return: None
		"""
		self.text = text

	def get_text(self):
		"""
		Returns the text.
		:return: a str
		"""
		return self.text

	def ask_user(self):
		"""
		Ask the user if he wants to writer the code in the terminal or to load from a file
		:return:
		"""
		print("Do you want to write the code in the terminal or load from a file?")
		print("1. Write in the terminal")
		print("2. Load from a file")
		self.set_file_name(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
		choice = input("Choice: ")
		if choice == "1":
			self.write_text()
		elif choice == "2":
			self.load_text()
		else:
			print("Invalid choice")
			self.ask_user()

	def write_text(self):
		"""
		Write the text in the terminal.
		:return: None
		"""
		print("Write the text in the terminal")
		self.text = input("Text: ")
		sequence = self.compiler(self.get_text())
		self.save_to_file(sequence)

	def load_text(self):
		"""
		Load the text from a file.
		:return: None
		"""
		print("Load the text from a file")
		file = input("File: ")
		with open(file, "r") as f:
			self.text = f.read()
		sequence = self.compiler(self.get_text())
		self.save_to_file(self.get_file_name(), sequence)

	@staticmethod
	def compiler(string):
		"""
		Finds the sequence of the text.
		:param string: a str
		:return: a str
		"""
		letters = []
		lastCode = 0
		for char in string:
			code = ord(char)
			compiledLetter = ''
			if code - lastCode < 0:
				for i in range(255 - lastCode):
					compiledLetter += ' '
				compiledLetter += '#'
				for i in range(code):
					compiledLetter += ' '
			else:
				for i in range(code - lastCode):
					compiledLetter += ' '
			compiledLetter += '	'
			lastCode = code
			letters.append(compiledLetter)
		return ''.join(letters)

	def save_to_file(self, code):
		"""
		Saves the text to a file.
		:param code: a str
		:return: None
		"""
		self.set_path(os.getcwd() + "/" + "output/")
		# create a dir named output
		if not os.path.exists(os.getcwd() + "/" + "output/"):
			os.makedirs(os.getcwd() + "/" + "output/")
		with open(self.get_path(), "w") as f:
			f.write(self.get_text() + "\n" + code)




if __name__ == "__main__":
	# ask the user if he wants to convert text to tab or tab to text
	print("Do you want to convert text to tab or tab to text?")
	print("1. Text to tab")
	print("2. Tab to text")
	choice = input("Choice: ")
	if choice == "1":
		compiler = Compiler()
		compiler.ask_user()
	elif choice == "2":
		interpreter = Interpreter()
		interpreter.ask_user()
