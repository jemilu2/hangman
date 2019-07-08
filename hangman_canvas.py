import tkinter as tk
import turtle

SCAFFOLD_HEIGHT = 360
BEAM_LENGTH = 144
ROPE_LENGTH = 18
HEAD_RADIUS = 36
BODY_LENGTH = 144
ARM_OFFSET_FROM_HEAD = 28
UPPER_ARM_LENGTH = 72
LOWER_ARM_LENGTH = 44
HIP_WIDTH = 36
LEG_LENGTH = 108
FOOT_LENGTH = 28


class HangmanCanvas(tk.Frame):
    '''
    Provides the GUI for the hangman game
    '''

    def __init__(self, master=None):
        super().__init__(master,bg="white")
        self.master = master    
        self.master.title("Hangman")
        self.pack()
        self.canvas = tk.Canvas(self,width=500,height=500)
        self.turtle = turtle.RawTurtle(self.canvas)
        self.canvas.pack(side="top")

        self.label_styles = {
            "font":("courier",15,"bold"),
            "padx":10,"pady":10,"justify":tk.LEFT,
            "fg":"black","bg":"white"
        }

        self.secret_label = tk.Label(self,text="------",**self.label_styles)
        self.secret_label.pack(side=tk.BOTTOM,expand=1)

        self.guessed_label = tk.Label(self,text="",**self.label_styles)
        self.guessed_label.pack(side=tk.BOTTOM,expand=1)

        self.num_of_incorrect_guesses = 0

    def note_incorrect_guess(self):
        '''
          Updates the display to correspond to an incorrect guess by the
          user. Calling this method causes the next body part to appear
          on the scaffold and adds the letter to the list of incorrect
          guesses that appears at the bottom of the window.
        '''
        self.num_of_incorrect_guesses += 1
        self.update_ui()

    def update_ui(self):
        if self.num_of_incorrect_guesses == 1:
            self.drawhead()
        elif self.num_of_incorrect_guesses == 2:
            self.drawbody()
        elif self.num_of_incorrect_guesses == 3:
            self.drawleftarm()
        elif self.num_of_incorrect_guesses == 4:
            self.drawrightarm()
        elif self.num_of_incorrect_guesses == 5:
            self.drawhip()
            self.drawleftleg()
        elif self.num_of_incorrect_guesses == 6:
            self.drawrightleg()
        elif self.num_of_incorrect_guesses == 7:
            self.drawleftfoot()
        elif self.num_of_incorrect_guesses == 8:
            self.drawrightfoot()


    def display_words(self,word,guesses):
        '''
        Updates the word on the screen to correspond to the current
        state of the game. The argument strings shows what letters have
        been guessed so far and the letters guessed.
        '''
        self.guessed_label['text'] = guesses
        self.secret_label['text'] = word

    def draw_scaffold(self):
        self.turtle.penup()
        self.turtle.right(90)
        self.turtle.forward(180)
        self.turtle.right(180)
        self.turtle.pendown()
        self.turtle.forward(SCAFFOLD_HEIGHT)
        self.turtle.right(90)
        self.turtle.forward(BEAM_LENGTH)
        self.turtle.right(90)
        self.turtle.forward(ROPE_LENGTH)

    def drawleftarm(self):
        #LEFT ARM
        self.turtle.right(180)
        self.turtle.forward(BODY_LENGTH-ARM_OFFSET_FROM_HEAD)
        self.turtle.left(90)
        self.turtle.forward(UPPER_ARM_LENGTH)
        self.turtle.left(90)
        self.turtle.forward(LOWER_ARM_LENGTH)
        self.turtle.left(180)
        self.turtle.forward(LOWER_ARM_LENGTH)
        self.turtle.right(90)
        self.turtle.forward(UPPER_ARM_LENGTH)
        
    def drawrightarm(self):
        self.turtle.forward(UPPER_ARM_LENGTH)
        self.turtle.right(90)
        self.turtle.forward(LOWER_ARM_LENGTH)
        self.turtle.right(180)
        self.turtle.forward(LOWER_ARM_LENGTH)
        self.turtle.left(90)
        self.turtle.forward(UPPER_ARM_LENGTH)
        self.turtle.left(90) 
        self.turtle.forward(BODY_LENGTH-ARM_OFFSET_FROM_HEAD)       

    def drawbody(self):
        self.turtle.pendown()
        self.turtle.forward(BODY_LENGTH)

    def drawhead(self):
        #CREATE HEAd
        self.turtle.forward(HEAD_RADIUS/2)
        self.turtle.right(90)
        self.turtle.circle(HEAD_RADIUS)
        self.turtle.penup()
        self.turtle.left(90)
        self.turtle.forward(HEAD_RADIUS*2)

    def drawhip(self):
        self.turtle.right(90)
        self.turtle.forward(HIP_WIDTH)
        self.turtle.right(180)
        self.turtle.forward(HIP_WIDTH*2)
        self.turtle.right(90)

    def drawleftleg(self):
        self.turtle.forward(LEG_LENGTH)
        self.turtle.left(180)
        self.turtle.forward(LEG_LENGTH)
        self.turtle.left(90)
        self.turtle.forward(HIP_WIDTH*2)
        self.turtle.left(90)

    def drawrightleg(self):
        self.turtle.forward(LEG_LENGTH)
        self.turtle.right(180)
        self.turtle.forward(LEG_LENGTH)
        self.turtle.right(90)
        self.turtle.forward(HIP_WIDTH*2)
        self.turtle.right(90)
        self.turtle.forward(LEG_LENGTH)
        self.turtle.left(90)

    def drawleftfoot(self):
        self.turtle.forward(FOOT_LENGTH)
        self.turtle.left(180)
        self.turtle.forward(FOOT_LENGTH)
        self.turtle.right(90)
        self.turtle.forward(LEG_LENGTH)
        self.turtle.left(90)
        self.turtle.forward(HIP_WIDTH*2)
        self.turtle.left(90)
        self.turtle.forward(LEG_LENGTH)
        self.turtle.right(90)

    def drawrightfoot(self):
        self.turtle.forward(FOOT_LENGTH)



    


if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanCanvas(master=root)
    app.draw_scaffold()
    app.drawhead()
    app.drawbody()
    app.drawleftarm()
    app.drawrightarm()
    app.drawhip()
    app.drawleftleg()
    app.drawrightleg()
    app.drawleftfoot()
    app.drawrightfoot()
    root.mainloop()