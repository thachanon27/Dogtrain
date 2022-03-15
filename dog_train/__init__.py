from gym.envs.registration import register

register(
    id='dog-v0',
    entry_point='dog_train.envs:DogEnv',
)

register(
    id='dog-v2',
    entry_point='dog_train.envs:dogEnv2',
)