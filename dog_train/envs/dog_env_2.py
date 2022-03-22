from gym import Env
from gym import spaces
from gym.spaces import Box, Discrete
import random
import numpy as np

import math

# same as BasicEnv, with one difference: the reward for each action is a normal variable
# purpose is to see if we can use libraries

class dogEnv2(Env):

    def __init__(self):


        self.min_iniposition = 0
        self.max_iniposition = 20
        self.min_inienergy = 1000
        self.max_inienergy = 1500
        self.low = np.array([self.min_iniposition, self.min_inienergy], dtype=np.float32)
        self.high = np.array([self.max_iniposition, self.max_inienergy], dtype=np.float32)

        # dog runs from 0 to 50, returns from 50 to 0
        self.observation_space = spaces.Box(self.low, self.high, dtype=np.float32)

        # amount of distance travelled
        self.action_space = spaces.Discrete(3)

        # current begin state
        #self.position = random.randint(0, 10)
        #self.energy_left = 1500

        # no. of rounds
        self.rounds = 0
        #Goal to stop
        self.goal_distance = 300

        # reward collected
        self.collected_reward = -1


    def step(self, action):
        dis = 0
        e_use = 0
        #done = False
        info = {}
        rw1 = 0
        rw2 = 0
        self.rounds += 1

        position, energy_left = self.state



        if action == 0:
            dis = 10
            e_use = 200
        elif action == 1:
            dis = 20
            e_use = 300
        elif action == 2:
            dis = 40
            e_use = 300

        # position = position + dis
        position += dis

        # energy_left = self.ini_energy - e_use
        energy_left -= e_use

##สุ่มยังไงก็ได้ให้ตกที่ 160 ในห้ารอบพอดี โดยให้ energy น้อยที่สุด

        if position < 140:
            self.collected_reward += -1
            rw1 = -40
        elif position >= 180:
            self.collected_reward += -2
            rw1 = -40
        elif position >= 140 and position < 180:   #ถ้าสุ่มจนตกในช่วงนี้ก็จะได้รางวัลใหญ่
            self.collected_reward += 100
            rw1 = 100


        if energy_left > 200 and energy_left < 800:
            self.collected_reward += -20
            rw2 = -3
        elif energy_left >= 800 and energy_left < 1500:
            self.collected_reward += 60
            rw2 =  10
        else:   # obs < 200 = เริ่มใช้พลังงานเยอะไป
            self.collected_reward += -40
            rw2 = -5

        rw = rw1 + rw2

        #if self.rounds == 0:
         #   done = True
        done = bool(position >= self.goal_distance)

        self.state = (position,energy_left)
        #self.render(action, rw)
        #self.render(dis, rw, position, energy_left)  
        return np.array(self.state, dtype=np.float32), self.collected_reward, done, info


    def reset(self):
        self.state = np.array([np.random.uniform(low=0, high=20),np.random.uniform(low=1000, high=1500)])
        return self.state

    def render(self, dis, rw, position, energy_left):
        print(f"Round : {self.rounds}\nDistance Travelled : {dis}\nReward Received: {rw} \nPosition of dog : {position}\nDogEnergyLeft: {energy_left} ")

        print(f"Total Reward : {self.collected_reward}")
        print("=============================================================================")


'''
env = dogEnv2()
state = env.reset()
done = False
while not done:
    #state = env.reset()
    action = env.action_space.sample()
    print("action = ", action)
    state, reward, done, info = env.step(action)
'''



