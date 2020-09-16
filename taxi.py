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

