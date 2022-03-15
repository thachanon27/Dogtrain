from gym import Env
from gym.spaces import Box, Discrete
import random

class DogEnv(Env):

    def __init__(self):
        # dog runs from 0 to 50, returns from 50 to 0
        self.obs_space = Box(low=0, high=100, shape=(1,))

        # amount of distance travelled
        self.action_space = Box(low=0, high=100, shape=(1,))

        # current state
        self.state = random.randint(0, 10)

        # no. of rounds
        self.rounds = 20

        # reward collected
        self.collected_reward = -1


    def step(self, action):
        done = False
        info = {}
        rw = 0
        self.rounds -= 1

        obs = self.state + action

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

        self.render(action, rw)

        return obs, self.collected_reward, done, info


    def reset(self):
        self.state = 0
        return self.state

    def render(self, action, rw):
        print(f"Round : {self.rounds}\nDistance Travelled : {action[0]}\nReward Received: {rw}")

        print(f"Total Reward : {self.collected_reward}")
    print("=============================================================================")


'''
env = DogEnv()

done = False
while not done:
    state = env.reset()
    action = env.action_space.sample()
    state, reward, done, info = env.step(action)

'''