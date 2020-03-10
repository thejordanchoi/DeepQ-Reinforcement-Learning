# CS175 Project

See <https://thejordanchoi.github.io/cs175/> for project details.

**How to run the project:**
1. Start the Malmo Minecraft client by running `./launchClient.sh` in the Minecraft directory
2. Open a new terminal and navigate to the project folder. This should be where you cloned the git repo
3. Run `python3 milestone_1.py`


## Malmo Minecraft Mazerunner

**Summary of the Project**

The overall goal of our project is to develop and train an agent that can guide our Minecraft user from the beginning of a maze to the end. The main idea is to create an agent that is capable of learning and familiarizing itself in different environments and then being able to make the best decision at every move to find the best overall route. Given the style of our project, our main duty will be to continually feed the agent different mazes of varying difficulty, to reinforce its ability to make decisions. Simple mazes may just be mazes that contain one clear route from start to end, and the agent has to learn what directions to move in order to reach the end. As for more difficult mazes, the environment may be more dynamic and have obstacles that will require the agent to make more complicated decisions on how to tackle the obstacles. The agent will decide between simple actions such as moving forward/backward as well as complicated actions like digging or building to reach the end of the maze. Our main goal will be to get this agent up and working, and from there we will work on improving its effectiveness and efficiency. In regards to input and output, we will be feeding the agent its immediate surroundings which will include what obstacles stand in its way, what sort of materials the surroundings are composed of, and further information such as if the surroundings are appropriate to build or dig on. The output will be a metric of success that we will use to rank how close our Minecraft character is to the end of the maze.


**Evaluation Plan**

In order to evaluate the performance of the agent, we will be using a metric of success and failure where as the agent fails, the metric will decrease and when the agent succeeds, the metric will increase. The metric we will be using will be both a distance based heuristic and a multiplier. The euclidean distance between the final position of the agent and the target block will be our distance based heuristic. That metric will also be summed with a cost heuristic of each action the agent takes. Combied, we will also give the agent a score multiplier of whether the agent reached the target or not. As a base, we should expect the agent to slowly reach a neutral score of say zero, and slowly improve towards a 1. Whenever the agent fails, the metric will decline towards say -1. Some qualitative verifications we can make are to visual observe whether the agent is getting better over time and printing metadata of each epoch to the terminal and observe if there are any improvements. We will first begin by navigating through a simple maze where the agent must simply walk forward to reach the goal. From there we will create more intricate and difficult mazes using a larger variety of actions to reach different states. One highly ambitious goal would be to have the agent use all types of movement commands in minecraft to be able to reach the target including mining, building, and jumping.


**Goals**

The minimum goal will be to accomplish simple movement from the start point to the end point in a basic maze (small in size and not difficult to navigate). The first milestone is using only back and forth movement to get to the end point in the basic maze. The second milestone will be to use a combination of front, back, left, and right movement to navigate to the end point. The realistic goal will be to add in jumping/digging actions in order for the agent to achieve its goal. While most of the maze walls will be made of bedrock (undestroyable), some walls will have dirt patches for the agent to dig with a shovel to “cut through” paths and create a shorter and better paths. The first milestone will be to teach the agent to learn to dig when able. The second milestone will be to teach the agent to dig and make paths when it is more efficient to do so, rather than exploring and using a longer path. The ambitious goal will be to allow the agent to build in the maze to help it reach the end point. The agent should learn whether it would be more efficient to build and jump over a wall rather than going around the maze walls. For this goal, its milestone would be to build to jump over a wall or dig under the wall rather than going around the wall to get to the end point.

