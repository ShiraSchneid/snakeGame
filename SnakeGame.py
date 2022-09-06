#"I hereby certify that this program is solely the result of my own work and 
#is in compliance with the Academic Integrity policy of the course syllabus.”
import Draw 
import random 
snakeSize = 12
score = 0 

#sets up the canvas 
Draw.setCanvasSize(500,500)
Draw.setBackground(Draw.BLACK)  

#this makes a grid to see the 2D list 
def grid():
    for row in range(20):
        for col in range(20):
            Draw.setColor(Draw.BLACK)
            Draw.rect(row*25,col*25,25,25)
   
#this function picks a random spot for the apple 
def makeApple(): 
    Draw.setColor(Draw.YELLOW) 
    z = random.randint(1,18)*25
    y = random.randint(1,18)*25
    Draw.filledRect(z,y,25,25) 
    return (z,y)

#if the position of the apple is equal to the head of the snake 
def eatApple(snakeX,snakeY, appleX, appleY):  
    if (snakeX,snakeY)==(appleX,appleY): return True 

#this function changes the list to coordinates 
def makeSnake(segments): 
    ans = []
    for i in range(snakeSize):  
        x = segments[i][0] *25
        y = segments[i][1] *25
        ans.append([x,y])
    return ans

#this moves the snake 
def moveSnake(s, dx, dy):
    head = s[0]   #the first segment of the snake 
    newS = [[head[0] + dx, head[1]+dy]] + s[0:-1] #the head with the new position + everything except the last segment 
    return newS  #return the snake at the new position 

# if the snake hits the wall 
def snakeHitWall(snakeX, snakeY):
    if snakeX <= 0 or snakeX >= 475 or snakeY <= 0 or snakeY >= 475: return True
    else: return False  #if the position is somewhere off the board, you lose. 

#This appears when you lose the game (returns false in main) 
def loser():
    Draw.clear()
    Draw.setColor(Draw.GRAY)
    Draw.filledRect(150, 150, 175, 175)
    Draw.setColor(Draw.WHITE)
    Draw.setFontSize(20)
    Draw.string("YOU LOST!", 185, 200)
    Draw.show()
#this is what appears when you win the game at the end 
def winner():
    Draw.clear()
    Draw.setColor(Draw.GRAY)
    Draw.filledRect(150, 150, 175, 175)
    Draw.setColor(Draw.WHITE)
    Draw.setFontSize(20)
    Draw.string("YOU WON!", 185, 200)
    Draw.show() 
    
def playGame(snakeSize):
    color = Draw.BLUE 
    Draw.show()
    grid()   
    apple = makeApple() 
    dx  = 25  #setting the initial movement of the snake in the x direction 
    dy  = 0 #setting the initial movement of the snake in the y direction 
    snake = makeSnake([[10,3],[9,3],[8,3],[7,3],[6,3],[5,3],[4,3],[3,3],
                       [2,3],[1,3],[.5,3], [.25,3], [.125,3]])  #this is the full list of segments of the snake 
    print("snake before loop:", snakeSize, snake, flush=True)
    while True: 
        if Draw.hasNextKeyTyped():   #adjusting the dx and the dy everytime a key is pressed 
            newKey = Draw.nextKeyTyped()
            if newKey == "Right":
                dx = 25
                dy = 0
            elif newKey == "Left":
                dx = -25
                dy = 0
            elif newKey == "Up":
                dy = -25
                dx = 0
            elif newKey == "Down":
                dy = 25
                dx = 0
        snake = moveSnake(snake, dx,dy)  #updating the new snake     
        Draw.clear()
        grid() 
        print("snake inside loop:", snakeSize, snake, score, flush=True)
        for i in range(snakeSize):  #drawing the new snake 
            Draw.setColor(color)
            Draw.filledRect(snake[i][0], snake[i][1],25,25)
        Draw.setColor(Draw.YELLOW)
        Draw.filledRect(apple[0],apple[1],25,25) #redrawing the apple everytime 
        Draw.show(150) #the speed of the snake 
        
        #if the snake gets the apple 
        if eatApple(apple[0],apple[1],snake[0][0],snake[0][1]):                           
            return True
         
        if snakeHitWall(snake[0][0],snake[0][1]) == True: #if the snake hits the wall, game over 
            return False 
        
        if snake[0] in snake[1:]: #if the snake hits itself, game over
            return False
def main(): 
    snakeSize = 3 #the initial amount of segments of the snake 
    score = 0 #score starts at 0 
    while True:
        if playGame(snakeSize):
            snakeSize +=1 
            score +=25
            if score== 250: # you win when you get this score 
                winner()
                break
        else:
            loser()
            break
    
main()
