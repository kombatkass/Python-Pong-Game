#1280x720

from tkinter import Tk, Canvas, PhotoImage,Label,Event,Menu,Pack,Entry,StringVar,Button
import time
#Used OOP and instances
class Main_Game():
    def __init__(self):
        self.window = Tk()
        self.window.title("PONG")
        self.canvas = Canvas(self.window, width=1280, height = 720, background = "#000000")
        self.canvas.pack(expand = True, fill = "both")
        self.game_background = PhotoImage(file="background.png")
        self.canvas.create_image(580, 400, image = self.game_background)        #https://www.pexels.com/photo/moon-photography-623147/
       
        
    def start_game(self):        
        self.canvas.delete(self.p1_entry)
        self.canvas.delete(self.p2_entry)
        self.canvas.delete(self.p1_label)      #Removes the text boxes to type in player names
        self.canvas.delete(self.p2_label) 
        self.canvas.delete(self.submit_button)
        self.canvas.delete(self.button_for_load)
        
        self.player1_score = 0 # Resets score
        self.player2_score = 0
        
        #Create the general layout of the game pads, balls lines etc
        self.horizontal_line =  self.canvas.create_line(0, 100, 1280, 100, width=4, fill="#FFFFFF", dash=(4, 8))
        self.horizontal_line2 =  self.canvas.create_line(0, 715, 1290,715, width=4, fill="#FFFFFF", dash=(4, 8))
        self.line =  self.canvas.create_line(660, 100, 660, 800, width=4, fill="#FFFFFF", dash=(4, 8))
        self.paddle_1 = self.canvas.create_rectangle(50, 255, 60, 415, fill = '#FF0000') #Co-ordinates(left x and y, bottom x and y)
        self.paddle_2  = self.canvas.create_rectangle(1190, 255, 1200, 415, fill = '#0000FF')
        self.game_ball = self.canvas.create_oval(630,330,650,350, fill = "#FFFFFF")
        self.score1 =self.canvas.create_text(400,60, fill = "#FF0000", font=('Terminal 50 bold'), text = str(self.player1_name) + ": " + str(self.player1_score))
        self.score2 =self.canvas.create_text(900,60, fill = "#0000FF", font=("Terminal 50 bold"), text = str(self.player2_name) + ": " + str(self.player2_score))
        self.help1 =self.canvas.create_text(90,60, fill = "#FF0000", font=("Terminal 10 bold"), text = "Press q for a hand :)")
        self.help2 =self.canvas.create_text(1210,60, fill = "#0000FF", font=("Terminal 10 bold"), text = "Press o for a hand :)")
        self.save_text =self.canvas.create_text(650,15, fill = "#FFFFFF", font=("Terminal 15 bold"), text = "Press g to save and quit")
        
        #In a way sets the speed of ball movement 
        self.x_coordinate = 0.08
        self.y_coordinate = 0.08
        self.boss = False
        
        self.run_game()
        
        #Loaded game start   NOT WORKING CURRENTLY 
    def loaded_game(self):
    
        self.canvas.delete(self.p1_entry)
        self.canvas.delete(self.p2_entry)
        self.canvas.delete(self.p1_label)      #Removes the text boxes to type in player names
        self.canvas.delete(self.p2_label) 
        self.canvas.delete(self.submit_button)
        self.canvas.delete(self.button_for_load)
        self.canvas.delete(self.image)
        self.canvas.delete(self.opening_Message)
        self.canvas.delete(self.opening_Message_2)
        self.canvas.delete(self.opening_paddle1)
        self.canvas.delete(self.opening_paddle2)
        self.canvas.delete(self.play_message)          
        
        self.save_game1 = open("player1.txt", "r")
        self.save_game2 = open("player2.txt", "r")
        self.save_game3 = open("player1 score.txt", "r")
        self.save_game4 = open("player2 score.txt", "r")
        
        self.player1_name = self.save_game1.read()
        self.player2_name = self.save_game2.read()
        self.player1_score = int(self.save_game3.read())
        self.player2_score = int(self.save_game4.read())
        
        #Create the general layout of the game pads, balls lines etc
        self.horizontal_line =  self.canvas.create_line(0, 100, 1280, 100, width=4, fill="#FFFFFF", dash=(4, 8))
        self.horizontal_line2 =  self.canvas.create_line(0, 715, 1290,715, width=4, fill="#FFFFFF", dash=(4, 8))
        self.line =  self.canvas.create_line(660, 100, 660, 800, width=4, fill="#FFFFFF", dash=(4, 8))
        self.paddle_1 = self.canvas.create_rectangle(50, 255, 60, 415, fill = '#FF0000') #Co-ordinates(left x and y, bottom x and y)
        self.paddle_2  = self.canvas.create_rectangle(1190, 255, 1200, 415, fill = '#0000FF')
        self.game_ball = self.canvas.create_oval(630,330,650,350, fill = "#FFFFFF")
        self.score1 =self.canvas.create_text(400,60, fill = "#FF0000", font=('Terminal 50 bold'), text = str(self.player1_name) + ": " + str(self.player1_score))
        self.score2 =self.canvas.create_text(900,60, fill = "#0000FF", font=("Terminal 50 bold"), text = str(self.player2_name) + ": " + str(self.player2_score))
        self.help1 =self.canvas.create_text(90,60, fill = "#FF0000", font=("Terminal 10 bold"), text = "Press q for a hand :)")
        self.help2 =self.canvas.create_text(1210,60, fill = "#0000FF", font=("Terminal 10 bold"), text = "Press o for a hand :)")
        self.save_text =self.canvas.create_text(650,15, fill = "#FFFFFF", font=("Terminal 15 bold"), text = "Press g to save and quit")
        
        #In a way sets the speed of ball movement 
        self.x_coordinate = 0.08
        self.y_coordinate = 0.08
        self.boss = False
        
        self.run_game()

    #Link to game running
    def run_game(self):
        self.play = True
        
        while self.play:
            self.keybinds()
            self.game_running()
            
                    
     #Keybinds for the game
    def keybinds(self):
            self.canvas.bind_all('<KeyPress-Up>', self.player1_movement)
            self.canvas.bind_all('<KeyPress-Down>', self.player1_movement)
            self.canvas.bind_all('<KeyPress-w>', self.player2_movement)
            self.canvas.bind_all('<KeyPress-s>', self.player2_movement)
            self.canvas.bind_all('<KeyPress-q>', self.player1_cheats)
            self.canvas.bind_all('<KeyPress-o>', self.player2_cheats)
            self.canvas.bind_all('<KeyPress-g>', self.create_save)
            self.canvas.bind_all('<KeyPress-p>', self.pause)
            self.canvas.bind_all('<KeyPress-1>', self.boss_key)
            self.canvas.bind_all('<KeyPress-2>', self.remove_boss_key)
            
     
     #Up and down key assigned to player 2 moving paddle 2       
    def player1_movement(self,event):
        if event.keysym ==  'Up':
            self.canvas.move(self.paddle_2, 0, -30) 
        elif event.keysym == 'Down':
            self.canvas.move(self.paddle_2, 0, 30)
    #Up and down key assigned to player 1 moving paddle 1  
    def player2_movement(self,event):
        if event.keysym ==  'w':
            self.canvas.move(self.paddle_1, 0, -30) 
        elif event.keysym == 's':
           self.canvas.move(self.paddle_1, 0, 30)

    #A cheat included where the player 1 can increment the score manually
    def player1_cheats(self,event):
     self.one_chance = 0
     while self.one_chance != 1:
        if event.keysym == 'q':
            self.player1_score+=1
            self.canvas.delete(self.score1) #Delete the scoreboard and replace with a new  one
            self.score1 = self.canvas.create_text(400,60, fill = "#FF0000", font=("Terminal 50 bold") , text = str(self.player1_name) + ": " + str(self.player1_score))
            self.one_chance = self.one_chance + 1
            break
    
    #A cheat included where the player 1 can increment the score manually
    def player2_cheats(self,event):
     self.one_chance2 = 0
     while self.one_chance2 != 1:
        if event.keysym == 'o':
            self.player2_score+=1
            self.canvas.delete(self.score2) #Delete the scoreboard and replace with a new  one
            self.score2 = self.canvas.create_text(900,60, fill = "#0000FF", font=("Terminal 50 bold"), text = str(self.player2_name) + ": " + str(self.player2_score))
            one_chance2 +=1
            break

    
    #Main running of the game when spacebar is pressed from the start menu
    def game_running(self):
        self.canvas.move(self.game_ball, self.x_coordinate, self.y_coordinate)
        
        self.ball_position = self.canvas.coords(self.game_ball)         #Assigns a variable ball_position to the 4 co-ordinates of the ball
        self.paddle_1_position = self.canvas.coords(self.paddle_1)      #Assigns a variable paddle_posiiton_1 to the 4 co-ordinates of the paddle
        self.paddle_2_position = self.canvas.coords(self.paddle_2)      #Assigns a variable paddle_posiiton_2 to the 4 co-ordinates of the second paddle
        
        #The goal for player 1
        if self.ball_position[2]>=1280:                                 #If the ball hits the right side of the screen
            self.x_coordinate = self.x_coordinate*-1
            self.canvas.coords(self.game_ball,630,330,650,350)          #Puts it back in the middle
            self.player1_score = self.player1_score + 1                 #Increments score
            if self.boss == False:                                      #Deletes and replaces score
                self.canvas.delete(self.score1)
                self.score1 = self.canvas.create_text(400,60, fill = "#FF0000", font=("Terminal 50 bold"), text = str(self.player1_name) + ": " + str(self.player1_score))
            else:
                pass
            time.sleep(1)                                               #Small delay for game smoothness
        
        #The goal for player 2
        if self.ball_position[0]<=0:                                    #If the ball hits the left side of the screen
            self.x_coordinate = self.x_coordinate*-1
            self.canvas.coords(self.game_ball,630,330,650,350)          #same as above
            self.player2_score = self.player2_score + 1
            if self.boss == False:
                self.canvas.delete(self.score2)
                self.score2 = self.canvas.create_text(900,60, fill = "#0000FF", font=("Terminal 50 bold"), text = str(self.player2_name) + ": "+ str(self.player2_score))
            else:
                pass
            time.sleep(1)

        #Paddle 1 if the corners of the ball hit any of the paddle it will bounce off
        if self.ball_position[0] <= self.paddle_1_position[2] and self.ball_position[0]>= self.paddle_1_position[0] and self.x_coordinate< 0:                   #[0][1][2][3] refer to top left x and y and then top right c and y respectively
            if self.ball_position[3]>= self.paddle_1_position[1] and self.ball_position[1]<= self.paddle_1_position[3]:
                self.x_coordinate *= -1

        # Paddle 2 if the corners of the ball hit any of the paddle it will bounce off
        elif self.ball_position[2] >= self.paddle_2_position[0] and self.ball_position[2]<= self.paddle_2_position[2] and self.x_coordinate > 0:
            if self.ball_position[3]>= self.paddle_2_position[1] and self.ball_position[1]<= self.paddle_2_position[3]:
                self.x_coordinate *= -1
   
        if self.ball_position[1] <=100:                 #If the ball hits the bottom bounce off
            self.y_coordinate = self.y_coordinate*-1
            
        if self.ball_position[3] >= 720:
            self.y_coordinate = self.y_coordinate*-1    #If the ball hits the top bounce off
            
        if self.player1_score == 5 or self.player2_score == 5:      #If one person reaches 5 opens text file and writes into it then goes to game over screen
            self.leaderboard = open("Leaderboard.txt","a")
            self.leaderboard.write("\n" + str(self.player1_name) + ": " + str(self.player1_score) + "   -   " + str(self.player2_name) + ": " + str(self.player2_score))
            self.leaderboard.close()
            self.canvas.delete("all")
            self.game_over_screen()
        
        self.window.update()
    
    def start_screen(self):   
        self.red_paddle = PhotoImage(file="PongRed.png")        #3 Images https://images.unsplash.com
        self.blue_paddle = PhotoImage(file="PongBlue.png")
        self.start_image = PhotoImage(file="pongimage.png")
        self.canvas.create_image(580, 400, image = self.game_background)
        
        self.dont_start = True                                      #Boolean to define whether to start or not
        self.canvas.bind_all('<KeyPress-space>', self.jump_to_start)
        
        #Create the visuals for the start screen
        self.opening_Message = self.canvas.create_text(650, 100, fill = '#FFFFFF', font= ('Terminal 50 bold'), text=('Pong Game'))
        self.opening_Message_2 = self.canvas.create_text(650, 200, fill = '#FFFFFF', font= ('Terminal 20 bold'), text=('First to 5 wins!'))
        self.image = self.canvas.create_image(650,370, image = self.start_image)
        self.opening_paddle1 = self.canvas.create_image(400,220, image = self.red_paddle)
        self.opening_paddle2 = self.canvas.create_image(900,220, image = self.blue_paddle)
        
        self.play_message = self.canvas.create_text(650, 600, fill = '#FFFFFF', font= ('Terminal 10 bold'), text=('Press Space to start'))
       
        self.p1_name = StringVar()
        self.p2_name = StringVar()
        
        self.player1_label = Label(self.window, text= "Player 1 Name", font = ("calibre", 10, "bold"))
        self.p1_label =  self.canvas.create_window(500,500, window=self.player1_label)
        self.player1_entry = Entry(self.window, textvariable=self.p1_name, font=('calibre',10,'normal'))
        self.p1_entry = self.canvas.create_window(500,530, window = self.player1_entry)
                                                                                                                    #2 entries so that players can use their names to customise the main game score and the leaderboard score
        self.player2_label = Label(self.window, text= "Player 2 Name", font = ("calibre", 10, "bold"))
        self.p2_label = self.canvas.create_window(800,500, window=self.player2_label)
        self.player2_entry = Entry(self.window, textvariable=self.p2_name, font=('calibre',10,'normal'))
        self.p2_entry = self.canvas.create_window(800,530, window = self.player2_entry)
        
        self.btn=Button(self.window,text = 'Submit', command = self.create_names)
        self.submit_button = self.canvas.create_window(650,540, window = self.btn)
        
        self.load_game_btn=Button(self.window,text = 'Load Last Game', command = self.loaded_game)
        self.button_for_load = self.canvas.create_window(650,660, window = self.load_game_btn)
        #Note game wont work if names aren't submitted 
        
        self.window.update()
        
        while self.dont_start:
            self.window.update()
            
        self.canvas.delete(self.opening_Message)
        self.canvas.delete(self.opening_Message_2)
        self.canvas.delete(self.opening_paddle1)
        self.canvas.delete(self.opening_paddle2)
        self.canvas.delete(self.play_message)
        self.canvas.delete(self.image)   
                  

    def create_names(self):
        self.player1_name = self.p1_name.get()
        self.player2_name = self.p2_name.get()
        

    def create_save(self,event):
        #Essentially if they want to stop mid game it would save their names and scores and continue where they left off
        if event.keysym == 'g':
            
            self.save_game1 = open("player1.txt","w")
            self.save_game1.write(str(self.player1_name))
            self.save_game1.close()
            
            self.save_game2 = open("player2.txt","w")
            self.save_game2.write(str(self.player2_name))
            self.save_game2.close()
            
            self.save_game3 = open("player1 score.txt","w")
            self.save_game3.write(str(self.player1_score))
            self.save_game3.close()
            
            self.save_game4 = open("player2 score.txt","w")
            self.save_game4.write(str(self.player2_score))
            self.save_game4.close()
            
            self.window.destroy()
        
    def game_over_screen(self):
        self.restart_game = True
        
        self.canvas.bind_all('<KeyPress-r>', self.restart)
        self.canvas.bind_all('<KeyPress-Escape>', self.quit)
        self.leaderboard = open("Leaderboard.txt", "r")
        #Create visuaals for game over screen
        self.leaderboard_list = self.canvas.create_text(650, 180, fill = '#FFFFFF', font= ('Terminal 20 bold'), text=('Leaderboard'))
        self.show_leaderboard = self.canvas.create_text(650, 280, fill = '#FFFFFF', font= ('Terminal 20 bold'), text=self.leaderboard.read())
        self.game_over = self.canvas.create_text(650, 100, font='Terminal 50 bold', text='GAME OVER', fill='#FFFFFF')
        self.quit_Message = self.canvas.create_text(650, 700, fill = '#FFFFFF', font= ('Terminal 20 bold'), text=('Press Esc to quit!'))
        self.restart_Message = self.canvas.create_text(650, 650, fill = '#FFFFFF', font= ('Terminal 20 bold'), text=('Press r to restart!'))
        self.window.update()
        
        while self.restart_game:
            self.window.update()
            
        self.canvas.delete(self.restart_Message)
        self.start_screen()
    
    #Attempted pause but didnt manage to unpause
    def pause(self,event):
        if event.keysym == 'p':
            self.pause_text = self.canvas.create_text(650, 350, font='Terminal 30 bold', text="Paused", fill='#FFFFFF')
            self.pause_text1 = self.canvas.create_text(650, 500, font='Terminal 30 bold', text="(Wait 5 seconds cannot unpause)", fill='#FFFFFF')
        
        self.wait()
          
    def wait(self):  
        time.sleep(3)
        self.unpause()
        
    def unpause(self):
        self.canvas.delete(self.pause_text1)
        self.canvas.delete(self.pause_text)    
           
    def boss_key(self,event):
        if event.keysym == '1':
            self.boss = True
            self.b_key = PhotoImage(file="Boss.png")
            self.image_for_boss = self.canvas.create_image(650,500, image = self.b_key)
            
    def remove_boss_key(self,event):
        if event.keysym == '2':
            self.boss = False
            self.canvas.delete(self.image_for_boss)
            #self.score1 = self.canvas.create_text(400,60, fill = "#FF0000", font=("Terminal 50 bold"), text = str(self.player1_name) + ": " + str(self.player1_score))
            #self.score2 = self.canvas.create_text(900,60, fill = "#0000FF", font=("Terminal 50 bold"), text = str(self.player2_name) + ": "+ str(self.player2_score))
            
    def jump_to_start(self, event):
        if event.keysym == 'space': #Function for start  menu
            self.dont_start = False

    def restart(self, event):   
        if event.keysym == 'r':         #Function to restart
            self.canvas.delete("all")
            self.start_screen()
        
        while True:
             self.start_game()
             self.game_over_screen()
                
    def quit(self, event):
        if event.keysym == 'Escape':    #Function to close menu
            
            self.window.destroy()
            

main_game = Main_Game()
main_game.start_screen()

while True:
    main_game.start_game()
    main_game.game_over_screen()
        
  
