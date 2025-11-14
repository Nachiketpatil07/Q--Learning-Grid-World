
import numpy as np
import gym
import pygame
#The environment name is Treasure Hunt we have a agent "pirate" who is sailing in ship 
#The goal is to find Treasure
#In the middle there are 5 hell states which are  Sea Creatures like Kraken,shark 
#Use arrow keys to move up down right left  
#The agent starts at [0,0] and the goal is at [4,4]
class TreasureHunt(gym.Env):
    def __init__(self, grid_size=5, goal_coordinates=(4, 4)) -> None:
        super(TreasureHunt, self).__init__()
        self.grid_size = grid_size
        self.state = None
        self.reward = 0
        self.info = {}
        self.goal = np.array([grid_size - 1, grid_size - 1])
        self.done = False
        self.hell_states = []

        # Action-space:
        self.action_space = gym.spaces.Discrete(4)
        
        # Observation space:
        self.observation_space = gym.spaces.Box(low=0, high=grid_size-1, shape=(2,), dtype=np.int32)

        # Pygame setup
        self.cell_size = 140
        
        self.width, self.height = self.grid_size * self.cell_size, self.grid_size * self.cell_size
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Treasure Hunt')
        
        # Load and scale images
        self.agent_image = pygame.transform.scale(pygame.image.load('Pirate_Agent.png'), (self.cell_size, self.cell_size))
        self.goal_image = pygame.transform.scale(pygame.image.load('reward.png'), (self.cell_size, self.cell_size))
        self.hell_images = [pygame.transform.scale(pygame.image.load(f'hell state {i}.png'), (self.cell_size, self.cell_size)) for i in range(1, 6)]
        self.reward_image = pygame.transform.scale(pygame.image.load('Reward_Treasure.png'), (self.width, self.height))
        self.background_image = pygame.transform.scale(pygame.image.load('Sea.png'), (self.width, self.height))
        
        # Flag to track if goal is reached
        self.goal_reached = False
        self.goal_reached_time = 0

    def add_hell_state(self, hell_state_coordinates, image_index):
        self.hell_states.append((np.array(hell_state_coordinates), image_index))

    def reset(self):
        self.state = np.array([0, 0])
        self.done = False
        self.reward = 0
        self.goal_reached = False
        self.goal_reached_time = 0

        self.info["Distance to goal"] = np.sqrt(
            (self.state[0] - self.goal[0])**2 + 
            (self.state[1] - self.goal[1])**2
        )

        return self.state

    def step(self, action):
        if self.done:
            return self.state, self.reward, self.done, self.info

        # Define action mappings
        actions = {
            0: [-1, 0],  # Up
            1: [1, 0],   # Down
            2: [0, 1],   # Right
            3: [0, -1]   # Left
        }

        action_vector = actions[action]

        new_state = np.clip(self.state + action_vector, 0, self.grid_size - 1)

        # Reward
        if np.array_equal(new_state, self.goal):
            self.reward = 10
            self.done = True
            self.goal_reached = True
            self.goal_reached_time = pygame.time.get_ticks()  # Record the time when the goal is reached
            print("You Found the Treasure")
        elif any(np.array_equal(new_state, hell[0]) for hell in self.hell_states):
            self.reward = -5  # Penalty for entering a hell state
            self.done = True
            print("You Enter the hell state")
        else:
            self.reward = -0.1  # Cost for each step
            self.done = False

        self.state = new_state

        # Info:
        self.info["Distance to goal"] = np.sqrt(
            (self.state[0] - self.goal[0])**2 + 
            (self.state[1] - self.goal[1])**2
        )
        
        return self.state, self.reward, self.done, self.info
    
    def render(self):
        self.screen.blit(self.background_image, (0, 0))

        # Draw goal
        self.screen.blit(self.goal_image, (self.goal[1] * self.cell_size, self.goal[0] * self.cell_size))

        # Draw hell states
        for hell in self.hell_states:
            hell_pos, image_index = hell
            self.screen.blit(self.hell_images[image_index - 1], (hell_pos[1] * self.cell_size, hell_pos[0] * self.cell_size))

        # Draw agent
        self.screen.blit(self.agent_image, (self.state[1] * self.cell_size, self.state[0] * self.cell_size))

        # If the agent has reached the goal, display the reward image
        if self.done and np.array_equal(self.state, self.goal):
            self.screen.blit(self.reward_image, (0, 0))

        pygame.display.flip()

        # Add a delay of 3 seconds if the goal is reached
        if self.goal_reached:
            current_time = pygame.time.get_ticks()
            if current_time - self.goal_reached_time < 2000:
                pygame.time.delay(2000 - (current_time - self.goal_reached_time))
            self.goal_reached = False

    def close(self):
        pygame.quit()
        
  
if __name__ == "__main__":
    # Create
    treasure_hunt_env = TreasureHunt(grid_size=5)

    # Add 5 hell states

    treasure_hunt_env.add_hell_state((1, 1), image_index=1)
    treasure_hunt_env.add_hell_state((0, 3), image_index=2)
    treasure_hunt_env.add_hell_state((3, 2), image_index=3)
    treasure_hunt_env.add_hell_state((4, 0), image_index=4)
    treasure_hunt_env.add_hell_state((2, 4), image_index=5)

    print("Action Space:", treasure_hunt_env.action_space)
    print("Observation Space:", treasure_hunt_env.observation_space)

    # Main loop to manually control the environment and visualize with Pygame
    observation = treasure_hunt_env.reset()
    print("Initial position:", observation)

    done = False

    treasure_hunt_env.render()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    action = 0
                elif event.key == pygame.K_DOWN:
                    action = 1
                elif event.key == pygame.K_RIGHT:
                    action = 2
                elif event.key == pygame.K_LEFT:
                    action = 3
                else:
                    continue

                new_state, reward, done, info = treasure_hunt_env.step(action)
                print(f"New state: {new_state}, Reward: {reward}, Done: {done}, Info: {info}")

                treasure_hunt_env.render()

    treasure_hunt_env.close()


