# Autonomous Room Mapping Robot

[![ROS2 Humble](https://img.shields.io/badge/ROS2-Humble-blue?logo=ros)](https://docs.ros.org/en/humble/)
[![Gazebo](https://img.shields.io/badge/Simulated%20in-Gazebo-orange?logo=linux)](https://gazebosim.org/)
[![Python](https://img.shields.io/badge/Python-3.10+-yellow?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build](https://img.shields.io/badge/build-passing-success)](#)
[![Author](https://img.shields.io/badge/Author-AryanGanesh%20Kavuri-lightgrey)](https://www.linkedin.com/in/aryanganesh-kavuri-405684286/)

---

## Overview

A ROS2 Humble-based simulation project featuring a TurtleBot3 robot that autonomously explores and maps indoor environments using LIDAR-based SLAM and obstacle avoidance in Gazebo.

---

## Features

- Autonomous navigation and exploration  
- Real-time LIDAR-based SLAM using `slam_toolbox`  
- Intelligent obstacle avoidance  
- Live visualization in RViz2  
- Full Gazebo simulation environment  

---

## Prerequisites

| Requirement | Version / Details |
|--------------|-------------------|
| **Operating System** | Ubuntu 22.04 |
| **ROS Distribution** | ROS2 Humble |
| **Simulator** | Gazebo |
| **Programming Language** | Python 3 |

---

## Installation

### 1. Install Dependencies
```bash
sudo apt update
sudo apt install -y ros-humble-gazebo-ros-pkgs ros-humble-cartographer \
ros-humble-cartographer-ros ros-humble-navigation2 ros-humble-nav2-bringup \
ros-humble-slam-toolbox ros-humble-turtlebot3-gazebo ros-humble-turtlebot3-msgs \
ros-humble-turtlebot3 python3-colcon-common-extensions
2. Set TurtleBot3 Model
bash
Copy code
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
source ~/.bashrc
3. Clone and Build
bash
Copy code
mkdir -p ~/robot_mapping_ws/src
cd ~/robot_mapping_ws/src
git clone <your-repo-url> autonomous_mapper
cd ~/robot_mapping_ws
colcon build
source install/setup.bash
Usage
Launch the Complete System
bash
Copy code
source ~/robot_mapping_ws/install/setup.bash
ros2 launch autonomous_mapper mapping_launch.py
This launches:

Gazebo simulation with TurtleBot3

SLAM Toolbox for mapping

RViz2 for visualization

Autonomous explorer node

Visualization
<p align="center"> <img src="https://github.com/user-attachments/assets/ce841df6-4424-40ba-9cd3-62254acfa878" width="600" alt="Gazebo and RViz Visualization"/> </p>
Windows:

Gazebo: 3D simulation of the robot and environment

RViz2: Real-time map generation and robot pose tracking

Save the Map
bash
Copy code
ros2 run nav2_map_server map_saver_cli -f my_room_map
<p align="center"> <img src="https://github.com/user-attachments/assets/53bf2eab-ca2b-4b47-a3f4-5f4fc5f3dbaf" width="600" alt="Map saving"/> </p>
This command generates:

my_room_map.pgm – Map image

my_room_map.yaml – Map metadata

System Overview
Autonomous Explorer Node
Continuously reads LIDAR scan data

Moves forward while safe

Detects obstacles within 0.5 m

Rotates toward open spaces

Adds random angular variations for improved coverage

<p align="center"> <img src="https://github.com/user-attachments/assets/49a7436f-27d4-40e3-9e0c-3e311a7eb2a2" width="600" alt="Autonomous Explorer"/> </p>
SLAM Toolbox
Processes LIDAR data for real-time mapping

Builds and updates the occupancy grid map

Localizes the robot position continuously

Obstacle Avoidance Algorithm
Monitor 360° LIDAR scan

Compute minimum distance to nearby obstacles

If distance < 0.5 m → Avoid

Stop motion

Compare left and right open areas

Rotate toward the larger open area

If distance > 0.5 m → Explore

Move forward

Add small random turns

Customization
Adjust Robot Speed
Modify in autonomous_mapper/autonomous_explorer.py:

python
Copy code
self.linear_speed = 0.2   # m/s (increase for faster exploration)
self.angular_speed = 0.5  # rad/s (rotation speed)
Adjust Safety Distance
python
Copy code
self.safe_distance = 0.5  # meters
Change Gazebo World
In mapping_launch.py:

python
Copy code
# Options: turtlebot3_world, turtlebot3_house, empty_world
'turtlebot3_world.launch.py'
Project Structure
bash
Copy code
autonomous_mapper/
├── autonomous_mapper/
│   ├── __init__.py
│   └── autonomous_explorer.py    # Main exploration logic
├── launch/
│   └── mapping_launch.py         # Launch file
├── resource/
│   └── autonomous_mapper         # Package marker
├── package.xml                   # Package dependencies
├── setup.py                      # Python package setup
└── README.md                     # This file
Troubleshooting
Issue	Solution
Gazebo doesn’t start	killall gzserver gzclient && source ~/.bashrc
Robot doesn’t move	Run ros2 node list – ensure /autonomous_explorer is active
No map in RViz2	Add → “Map” → Set topic to /map
Package not found	source ~/robot_mapping_ws/install/setup.bash

Future Enhancements
 Frontier-based exploration

 Path planning integration

 Multi-robot coordination

 3D mapping support

 Return-to-start feature

License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
AryanGanesh Kavuri


<p align="center"> <b>⭐ If you found this project useful, consider giving it a star!</b> </p> ```
