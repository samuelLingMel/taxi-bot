import gym    # load our OpenAI gym package that we just installed
import numpy as np  # used to help with some computing later on
import random    # used to generate random numbers later on 
import os   # used to help with displaying the Taxi game 
from time import sleep    # used to help with displaying the Taxi game

# Create an instance of our 'Taxi' environment (game) to play on
env = gym.make('Taxi-v3')

# Start a new game and get our first starting 'state'
state = env.reset()

num_steps = 99 # feel free to change this number to run for more steps
for s in range(num_steps+1):  # loop for a number of specified steps
    os.system('cls')  
    print(f"Step: {s} out of {num_steps}")
    action = env.action_space.sample()  # select a random action 
    env.step(action)   # perform the action on the environment
    env.render()  # print the new map
    sleep(0.5)
env.close() # closes the environment and ends the game

state_size = env.observation_space.n  # Total number of States (S) 
action_size = env.action_space.n      # Total number of Actions (A)

################### FILL IN CODE HERE ###################
# Initialize a qtable with 0's for all Q-values
# np.zeros creates a table filled with zeros with shape (rows,columns)
qtable = np.zeros((None, None))     
##################### END CODE HERE #####################

# Check result
print(f"Our initialized Q-table: \n {qtable}")

# Hyperparameters (these can be changed later)
learning_rate = 0.9
discount_rate = 0.8
# Dummy variables used in the Q-learning algorithm
reward = 10 # R_(t+1)
state = env.observation_space.sample()      # S_t 
action = env.action_space.sample()          # A_t
new_state = env.observation_space.sample()  # S_(t+1)
################### FILL IN CODE HERE ###################
# Qlearning algorithm: Q(s,a) := Q(s,a) + learning_rate * (reward + discount_rate * max Q(s',a') - Q(s,a))
# Hint: use the dummy variables above, and np.max(qtable[new_state,:]) for the maximum expected future reward term
qtable[state, action] = None
##################### END CODE HERE #####################

# Some dummy variables
episode = random.randint(0,500)
qtable = np.random.randn(env.observation_space.sample(), env.action_space.sample())
# Exploration-exploitation tradeoff
epsilon = 1.0 # Set the probability that our agent will explore
decay_rate = 0.01 # Rate at which our epsilon will exponentially decrease
################### FILL IN CODE HERE ###################
if random.uniform(0,1) < epsilon:
    # Tell our agent to explore (take random actions)
    action = None
    print("Our agent is exploring")
else:
    # Tell our agent to explore (use our qtable from earlier)
    # Hint: np.argmax(...) returns the maximum value along an axis
    action = None
    print("Our agent is exploiting")
##################### END CODE HERE #####################
# Decrease epsilon
# Epsilon will decrease exponentially --> our agent will explore less and less
epsilon = np.exp(-decay_rate*episode)