from gym import Env
from gym import spaces
from gym.spaces import Box, Discrete
import random

# same as BasicEnv, with one difference: the reward for each action is a normal variable
# purpose is to see if we can use libraries

class DogEnv(Env):

    def __init__(self):
        # dog runs from 0 to 50, returns from 50 to 0
        self.obs_space = Box(low=0, high=100, shape=(1,))

        # amount of distance travelled
        self.action_space = spaces.Discrete(3)

        # current state
        self.state = random.randint(0, 10)

        # no. of rounds
        self.rounds = 30

        # reward collected
        self.collected_reward = -1


    def step(self, action):
        dis = 0
        done = False
        info = {}
        rw = 0
        self.rounds -= 1

        if action == 0:
            dis = 15
        elif action == 1:
            dis = 25
        elif action == 2:
            dis = 40


        obs = self.state + dis

        if obs < 50:
            self.collected_reward += -1
            rw = -1
        elif obs > 50 and obs < 100:
            self.collected_reward += 0
            rw = 0
        else:
            self.collected_reward += 1
            rw = 1

        if self.rounds == 0:
            done = True

        #self.render(action, rw)
        self.render(dis, rw)
        return obs, self.collected_reward, done, info


    def reset(self):
        self.state = 0
        return self.state

    def render(self, dis, rw):
        print(f"Round : {self.rounds}\nDistance Travelled : {dis}\nReward Received: {rw}")

        print(f"Total Reward : {self.collected_reward}")
    print("=============================================================================")


'''
env = DogEnv()

done = False
while not done:
    state = env.reset()
    action = env.action_space.sample()
    print("action = ", action)
    state, reward, done, info = env.step(action)
   
 '''
