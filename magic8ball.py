"""

Program: magic8ball.py
Author: Eric Gerson 
Date : 4/1/19

Magic 8-Ball Program 


GUI based python program that simulates Magic 8-Ball toy. Input will be to ask the user to type a question. For output, The program will randomly choose one of a pre-set list of responses.

"""

from breezypythongui import EasyFrame
from tkinter.font import Font
from PIL import ImageTk, Image 
import random


class Magic8Ball(EasyFrame):
	"""Generates and displays a random response message from the user's input"""
	
	def __init__(self):
		"""Sets up the window, widgets and data."""
		EasyFrame.__init__(self, title = "Magic 8-Ball", background = "Royal Blue" ,resizable = False)
		
		#Label for the title of the application / also sets font styling
		titleFont = Font(family = "Copperplate Gothic Bold" , size = 40)
		self.title = self.addLabel(text = "Magic 8-Ball", row = 0 , column = 0, columnspan = 2, font = titleFont, sticky = "NSEW", background = "Royal Blue", foreground ="white")
		
		
		# Loads the image and associates it with the image label.
		imageFont = Font(family = "Helvetica" , size = 20, weight = "bold")
		self.imageLabel = self.addLabel(text = "", row = 1,  column = 0, sticky = "NSEW", background = "Royal Blue")
		
		#Import image to the image label
		self.ballImage = ImageTk.PhotoImage(Image.open("magic8ball.jpg"))
		self.imageLabel["image"] = self.ballImage
		
		#font styles for the question label
		questionFont = Font(family = "Arial" , size = 25)
		
		#Panel for the question fields/ labels
		questionPanel = self.addPanel(row = 2, column = 0,  background = "Cadet Blue")
		questionPanel.addLabel(text = "Ask your question", row = 0, column = 0,  columnspan = 2, font= questionFont, sticky = "NSEW", background = "Cadet Blue")
		
		#font size for the button and input field
		submitBtnFont = Font(size = 15)
		
		#input field for the question
		self.questionField = questionPanel.addTextField(text = "", row = 1 , column = 0 ,sticky = "NSEW", width = 42)
		self.questionField["font"] = submitBtnFont
		
		#The command button for the question panel 
		self.questionButton= questionPanel.addButton(text = "Submit Question" , row =1 , column = 1, columnspan = 2,command =self.response, state = "normal")
		self.questionButton["font"] = submitBtnFont
		self.questionButton["borderwidth"] = 3
		self.questionButton["relief"] = "raised"
		
		self.questionButton.bind("<Return>", lambda event: self.response())
		
		#font style for the response label
		responseFont = Font(family = "Arial" , size = 25)
		
		#font style for the output of the response labels
		ansFont = Font(family = "Helvetica", size = 20)
		
		#Panel for the response fields and labels
		responsePanel = self.addPanel(row = 3, column = 0, background = "Light Steel Blue")
		
		#Will display output for the what the user entered as their question(input)
		responsePanel.addLabel(text = "You asked", row = 0, column = 0, font= responseFont, background = "Light Steel Blue")
		self.questMsg = responsePanel.addLabel(text = "", row = 0, column = 2, font = ansFont , columnspan = 3 , background = "Navy", foreground ="White")
		self.questMsg["width"] = 30
		
		#Will display output for the reply from the random response of the magic 8 ball
		responsePanel.addLabel(text = "Your reply", row = 2 , column = 0, font= responseFont, background = "Light Steel Blue")
		self.responseMsg = responsePanel.addLabel(text = "", row = 2, column = 2, columnspan = 3, font = ansFont , sticky = "NSEW", background = "Navy" , foreground = "white")
		
	#The event handling method for the button	
	def response(self):
			
		#Accesor method retrieving the text from input field
		result = self.questionField.getText()
		
		#Special characters 
		special=("!", "@", "#", "%", "^", "&", "*", "(", ")", "[", "]", "{" ,"}",":", ";", "/", "<" ,">", ".", "?", "`","~", "+", "=","-", "_", "|")
		
		#Decision(if...else) statement
		if result == "" or result.startswith(special):
			self.questMsg["text"] = ""
			self.responseMsg["text"] = "Enter a Valid Question"
		else:
			answers = ["As I see it, yes", "Concentrate and ask again", "Don't count on it.","Yes - definitely.", "Better not tell you now.","Signs point to yes.","Cannot predict now.","Outlook not so good.", "My reply is no.","It is certain.","It is decidedly so.","Without a doubt."]
			reply = random.choice(answers)
			self.questMsg["text"] = result
			self.responseMsg["text"] = reply
			self.questionField.setText("")

def main():
	Magic8Ball().mainloop()
	
main()