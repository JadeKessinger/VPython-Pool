# GlowScript 3.2 VPython

scene.bind('keydown', keydown_fun)     # Function for key presses

#Set up background
scene.background = 0.8 * vec(1, 1, 1)    # Light gray (0.8 out of 1.0)
scene.width = 640                        # Make the 3D canvas larger
scene.height = 480
friction = 0.985
ballSize = 0.58
hit = vec(1, 0, 0)

#Set up the pool table
ground = box(size = vec(10, 1, 20),
             pos = vec(0, -0.5, 0),
             color = vec(0, 0.42, 0.35)) #Green

wallA = box(pos = vec(0, -0.5, -10),
            axis = vec(1, 0, 0),
            size = vec(10, 2, .4),
            color = vec(.21, .15, .14)) #Top 
            
wallB = box(pos = vec(-5, -0.5, 0),
            axis = vec(0, 0, 1),
            size = vec(20.4, 2, .4),
            color = vec(.21, .15, .14)) #Left 
            
wallC = box(pos = vec(5, -0.5, 0),
            axis = vec(0, 0, 1),
            size = vec(20.4, 2, .4),
            color = vec(.21, .15, .14))  #Right

wallD = box(pos = vec(0, -0.5, 10),
            axis = vec(1, 0, 0),
            size = vec(10, 2, 0.4),
            color = vec(.21, .15, .14)) #Bottom

hole1 = cylinder(size = 1*vec(1, 1, 1),
              axis = vec(0, 1, 0), 
              color = color.black,
              pos = vec(-4.7, -0.99, -9.7))
              
hole2 = cylinder(size = 1*vec(1, 1, 1),
              axis = vec(0, 1, 0), 
              color = color.black,
              pos = vec(-4.7, -0.99, 9.7))
              
hole3 = cylinder(size = 1*vec(1, 1, 1),
              axis = vec(0, 1, 0), 
              color = color.black,
              pos = vec(4.7, -0.99, -9.7))
            
hole4 = cylinder(size = 1*vec(1, 1, 1),
              axis = vec(0, 1, 0), 
              color = color.black,
              pos = vec(4.7, -0.99, 9.7))
              
hole5 = cylinder(size = 1*vec(1, 1, 1),
              axis = vec(0, 1, 0), 
              color = color.black,
              pos = vec(4.7, -0.99, 0))

hole6 = cylinder(size = 1*vec(1, 1, 1),
              axis = vec(0, 1, 0), 
              color = color.black,
              pos = vec(-4.7, -0.99, 0))

cueBall = sphere(size = ballSize*vec(1, 1, 1),
              color = vec(1, 1, 0.98),
              pos = vec(0, ballSize/2, 6),
              vel = vec(0, 0, 0))

# triangle pos at z = -5

ball1 = sphere(size = ballSize*vec(1, 1, 1),
              color = vec(1, 0.84, 0.0),
              pos = vec(0, ballSize/2, -5),
              vel = vec(0, 0, 0))
              
ball2 = sphere(size = ballSize*vec(1, 1, 1),
              color = vec(0.6, 0.24, 1),
              pos = vec(ballSize/2, ballSize/2, -5-ballSize),
              vel = vec(0, 0, 0))

ball3 = sphere(size = ballSize*vec(1, 1, 1),
              color = vec(.79, 0.15, 0.15),
              pos = vec(-ballSize/2, ballSize/2, -5-ballSize),
              vel = vec(0, 0, 0))

ball4 = sphere(size = ballSize*vec(1, 1, 1),
              color = vec(0.37, 0, 0.68),
              pos = vec(ballSize, ballSize/2, -5-2 * ballSize),
              vel = vec(0, 0, 0))
              
ball5 = sphere(size = ballSize*vec(1, 1, 1),
              color = vec(0.98, 0.54, 0.2),
              pos = vec(-ballSize, ballSize/2, -5-2 * ballSize),
              vel = vec(0, 0, 0))
              
ball6 = sphere(size = ballSize*vec(1, 1, 1),
              color = vec(0, 0.53, 0.32),
              pos = vec(3 * ballSize/2, ballSize/2, -5-3 * ballSize),
              vel = vec(0, 0, 0))
              
ball7 = sphere(size = ballSize*vec(1, 1, 1),
              color = vec(0.42, 0, 0),
              pos = vec(ballSize/2, ballSize/2, -5-3 * ballSize),
              vel = vec(0, 0, 0))
              
ball8 = sphere(size = ballSize*vec(1, 1, 1),
              color = vec(0, 0, 0),
              pos = vec(0, ballSize/2, -5-2 * ballSize),
              vel = vec(0, 0, 0))

ball9 = sphere(size = ballSize*vec(1, 1, 1),
              color = vec(1, 0.91, 0.49),
              pos = vec(-ballSize/2, ballSize/2, -5-3*ballSize),
              vel = vec(0, 0, 0))
              
ball10 = sphere(size = ballSize*vec(1, 1, 1),
              color = vec(0.4, 0.25, 1),
              pos = vec(-3 * ballSize/2, ballSize/2, -5-3*ballSize),
              vel = vec(0, 0, 0))

ball11 = sphere(size = ballSize*vec(1, 1, 1),
              color = vec(1, 0.43, 0.43),
              pos = vec(ballSize*2, ballSize/2, -5-4*ballSize),
              vel = vec(0, 0, 0))

ball12 = sphere(size = ballSize*vec(1, 1, 1),
              color = vec(0.55, 0.22, 0.83),
              pos = vec(ballSize, ballSize/2, -5-4*ballSize),
              vel = vec(0, 0, 0))
              
ball13 = sphere(size = ballSize*vec(1, 1, 1),
              color = vec(1, 0.66, 0.40),
              pos = vec(0, ballSize/2, -5-4*ballSize),
              vel = vec(0, 0, 0))
              
ball14 = sphere(size = ballSize*vec(1, 1, 1),
              color = vec(0.29, 0.86, 0.63),
              pos = vec(-ballSize, ballSize/2, -5-4*ballSize),
              vel = vec(0, 0, 0))
              
ball15 = sphere(size = ballSize*vec(1, 1, 1),
              color = vec(0.69, 0.23, 0.23),
              pos = vec(-ballSize*2, ballSize/2, -5-4*ballSize),
              vel = vec(0, 0, 0))
              
cue = makePoolCue(vec(cueBall.pos.x, ballSize+1.65, cueBall.pos.z+8)) #Make the pool cue
cue.rotate(angle = radians(-90),
           axis = vec(0, 1, 0),
           origin = vector(cue.pos.x, cue.pos.y, cue.pos.z))
          
balls = [cueBall, ball1, ball2, ball3, ball4, ball5, ball6, ball7, ball8, ball9, ball10, ball11, ball12, ball13, ball14, ball15]
holes = [hole1, hole2, hole3, hole4, hole5, hole6]

# Other constants
RATE = 30                # The number of times the while loop runs each second
dt = 1.0/(1.0*RATE)      # The time step each time through the while loop
scene.autoscale = False  # Avoids changing the view automatically
scene.forward = vec(0, -3, -2)  # Ask for a bird's-eye view of the scene...

# This is the "event loop" or "animation loop"
# Each pass through the loop will animate one step in time, dt

while True:

    rate(RATE)                       # Maximum number of times per second
                                     # ..that the while loop runs
    for ball in balls:
        ball.pos = ball.pos + ball.vel*dt
        ball.vel = ball.vel * friction
        wallCollide(ball)
        
    vList = []
    for i in balls:
        vList = vList + [i.vel.mag]
    
    if max(vList) < 0.15 and not cue.visible:
        cue.pos = vec(cueBall.pos.x, ballSize+1.65, cueBall.pos.z+8)
        cue.axis = vec(0, 0, 1)
        #cue.rotate(angle = radians(-90),
         #  axis = vec(0, 1, 0),
          # origin = vector(cue.pos.x, cue.pos.y, cue.pos.z))
        cue.visible = True
        for i in balls:
            i.vel = vec(0, 0, 0)
    
    
    for i in range(len(balls) - 1):
        for j in range(i + 1, len(balls)):
            ballCollide(balls[i], balls[j])
            
    for i in balls:
        for j in holes:
            ballFall(i, j)
            
            
    if not cueBall.visible:
        cueBall.vel = vec(0, 0, 0)
        cueBall.pos = vec(0, ballSize/2, 6)
        cueBall.visible = True 

    visList = []
    count = 0
            
    if not ball8.visible:
        for ball in balls:
            if not ball.visible:
                count = count + 1
                print(count)
        if count == 15:
            print("You win! :D")
        else:
            print("You lose")
    

def makePoolCue(startingPosition):
    """Creates a pool cue
       Argument: A vector indicating the starting position
       Returns: Nothing
    """
       
    cueBrown = cylinder(pos = vec(5.3, 4.325, 3),
                         axis = vec(2, 0.5, 0),
                         size = vec(10, 0.2, 0.2),
                         color = vec(.21, .15, .14)) #Dark brown
                         
    cueWood = cylinder(pos = vec(0.3, 3.075, 3),
                         axis = vec(2, 0.5, 0),
                         size = vec(5.15, 0.2, 0.2),
                         color = vec(1.0, 0.9, 0.7)) #Yellow
                         
    cueTip = cylinder(pos = vec(0, 3, 3),
                         axis = vec(2., 0.5, 0),
                         size = vec(0.31, 0.2, 0.2),
                         color = color.white)
                         
    cueObjects = [cueBrown, cueWood, cueTip]
    
    comCue = compound(cueObjects,
                        pos = startingPosition) #Combines the pieces together
                         
    comCue.vel = vec(0, 0, 0) #Set the initial velocity
    return comCue
    
def keydown_fun(event):
    """This function is called each time a key is pressed."""
    key = event.key
    ri = randint(0, 10)

    amount = 0.42               # "Strength" of the keypress's velocity changes
    if key == 'up' or key in 'wWiI':
        if hit.x < 10:
            hit.x = hit.x + 1
            print("Power: " + hit.x)
        else:
            print("Can't go higher")
        
    elif key == 'down' or key in 'sSkK':
        if hit.x > 1:
            hit.x = hit.x - 1
            print("Power: " + hit.x)
        else:
            print("Can't go lower")
    
    elif key == 'left' or key in 'aAjJ':
        cue.rotate(angle = radians(-2.5),
                   axis = vec(0, 1, 0),
                   origin = cueBall.pos)
                   
    elif key == 'right' or key in "dDlL":
        cue.rotate(angle = radians(2.5),
                   axis = vec(0, 1, 0),
                   origin = cueBall.pos)
                   
    elif key == 'space' or key in ' rR':
        where = cue.pos - cueBall.pos
        where = vec(where.x, 0, where.z) * -1
        where = where.norm()
        cueBall.vel = where * hit.x * 1.5
        cue.visible = False
        
    elif key == "q":
        for i in range(len(balls)):
            if i != 0:
                balls[i].pos = hole1.pos

def wallCollide(ball):
    """Changes the velocity of the ball if the ball collides with a wall.
       Argument: A sphere object
       Returns: Nothing
    """
    
    # If the ball hits wallA
    if ball.pos.z < wallA.pos.z + 0.49:           # Hit--check for z
        ball.pos.z = wallA.pos.z + 0.49           # Bring back into bounds
        ball.vel.z *= -1.0                 # Reverse the z velocity

    # If the ball hits wallB
    if ball.pos.x < wallB.pos.x + 0.49:           # Hit--check for x
        ball.pos.x = wallB.pos.x + 0.49           # Bring back into bounds
        ball.vel.x *= -1.0                 # Reverse the x velocity
  
    if ball.pos.x > wallC.pos.x - 0.49:           # Hit--check for x
        ball.pos.x = wallC.pos.x - 0.49           # Bring back into bounds
        ball.vel.x *= -1.0                 # Reverse the x velocity
  
    if ball.pos.z > wallD.pos.z - 0.49:           # Hit--check for z
        ball.pos.z = wallD.pos.z - 0.49           # Bring back into bounds
        ball.vel.z *= -1.0                 # Reverse the z velocity

def ballCollide(ballA, ballB):
    """Changes the velocity of two balls if they collide
       Argument: Two sphere objects
       Returns: Nothing
    """
    
    DISTANCE = ballSize
    diff = ballB.pos - ballA.pos
    
    if (diff).mag < DISTANCE:
        
        gent = rotate(diff, radians(90), vec(0, 1, 0))
        
        v1 = ballA.vel; v2 = ballB.vel
        
        ballA.pos -= (DISTANCE - diff.mag) *v1.norm()*1.001
        ballB.pos -= (DISTANCE - diff.mag) *v2.norm()*1.001 
        
        v1_rad = proj(v1, diff); v1_tan = proj(v1, gent)
        v2_rad = proj(v2, -diff); v2_tan = proj(v2, gent)
        
        ballA.vel =  v2_rad + v1_tan
        ballB.vel =  v1_rad + v2_tan
        
def ballFall(ball, hole):
    diff = ball.pos - vec(hole.pos.x, hole.pos.y + 1, hole.pos.z)
    if diff.mag < 0.5:
        ball.vel = vec(0, 0, 0)
        ball.visible = False
        ball.pos.y = randint(10, 1000)

def randint(low, hi):
    """Implements Python's randint using the random() function.
       returns an int from low to hi _inclusive_ (so, it's not 100% Pythonic)
    """
    if hi < low:
        low, hi = hi, low               # Swap if out of order!
    LEN = int(hi) - int(low) + 1.       # Get the span and add 1
    randvalue = LEN*random() + int(low) # Get a random value
    return int(randvalue)               # Return the integer part of it
