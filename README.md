# Malmo Reinforcement Learning

See <https://thejordanchoi.github.io/CS175/> for project details.

**How to run the project:**
1. Start the Malmo Minecraft client by running `./launchClient.sh` in the Minecraft directory
2. Navigate to the src folder. This should be where you cloned the git repo.
3. Move contents of worlds file to MalmoPlatform/Minecraft/run/saves/
4. Run `python3 Mazerunner.py`


## Malmo Minecraft Mazerunner

**Summary of the Project**

The overall goal of our project is to develop and train an agent that can guide our Minecraft user from the beginning of a maze to the end. The main idea is to create an agent that is capable of learning and familiarizing itself in different environments and then being able to make the best decision at every move to find the best overall route. Given the style of our project, our main duty will be to continually feed the agent different mazes of varying difficulty, to reinforce its ability to make decisions. Simple mazes may just be mazes that contain one clear route from start to end, and the agent has to learn what directions to move in order to reach the end. As for more difficult mazes, the environment may be more dynamic and have obstacles that will require the agent to make a combination of complicated and basic decisions to tackle the obstacles. The agent will decide between simple actions such as moving forward/backward as well as complicated actions like digging or building to reach the end of the maze. Our main goal will be to get this agent up and working, and from there we will work on improving its effectiveness and efficiency. In regards to input and output, we will be feeding the agent its immediate surroundings which will include what obstacles stand in its way, what sort of materials the surroundings are composed of, and further information such as if the surroundings are appropriate to build or dig on. The output will be a metric of success that we will use to rank how close our Minecraft character is to the end of the maze.


**Evaluation Plan**

In order to evaluate the performance of the agent, we will be using a metric of success and failure where as the agent fails, the metric will decrease and when the agent succeeds, the metric will increase. The metric we will be using will be both a distance based heuristic and a multiplier. The euclidean distance between the final position of the agent and the target block will be our distance based heuristic. That metric will also be summed with a cost heuristic of each action the agent takes. Combied, we will also give the agent a score multiplier of whether the agent reached the target or not. As a base, we should expect the agent to slowly reach a neutral score of say zero, and slowly improve towards a 1. Whenever the agent fails, the metric will decline towards say -1. Some qualitative verifications we can make are to visual observe whether the agent is getting better over time and printing metadata of each epoch to the terminal and observe if there are any improvements. We will first begin by navigating through a simple maze where the agent must simply walk forward to reach the goal. From there we will create more intricate and difficult mazes using a larger variety of actions to reach different states. One highly ambitious goal would be to have the agent use all types of movement commands in minecraft to be able to reach the target including mining, building, and jumping.

**Goals**

The minimum goal of our project was to accomplish simple movement from the start point to the end point in a basic maze. The first milestone was using only back and forth movement and then in the second milestone, use a combination of front, back, left, and right movement to navigate to the end point. We constructed a very simple maze for testing to make sure our agent would be able to learn the maze and navigate to the diamond block which indicated success. The realistic goal saw the addition of the jumping action in order for the agent to explore and discover three dimensional paths that may lead to the end goal. Our milestone was to teach the agent to use the jump action when it was more efficient to do so rather than settling with the longer path that can be reached through the four original basic movements. Our ambitious goal included more complex actions such as the ability to build and manipulate the map in order to let the agent create its own optimal path to the destination. Ultimately, the ambitious goal was not reached given the time constraint of this project class.
