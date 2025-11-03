# Autonomous Room Mapping Robot
[![ROS2 Humble](https://img.shields.io/badge/ROS2-Humble-blue?logo=ros)](https://docs.ros.org/en/humble/)
[![Gazebo](https://img.shields.io/badge/Simulated%20in-Gazebo-orange?logo=linux)](https://gazebosim.org/)
[![Python](https://img.shields.io/badge/Python-3.10+-yellow?logo=python)](https://www.python.org/)
[![Build](https://img.shields.io/badge/build-passing-success)](#)
[![Author](https://img.shields.io/badge/Author-AryanGanesh%20Kavuri-lightgrey)](https://www.linkedin.com/in/aryanganesh-kavuri-405684286/)

[![GitHub Repo stars](https://img.shields.io/github/stars/AryanGanesh/Kinematics?style=social)](https://github.com/AryanGanesh/Kinematics)

**Connect with me:**  
📧 [aryanganesh.k@gmail.com](mailto:aryanganesh.k@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/aryanganesh-kavuri-405684286/)


## Tech Stack

| Technology | Usage | Proficiency |
|-------------|--------|--------------|
| ROS2 Humble | Core robotics framework | ![90%](https://img.shields.io/badge/90%25-green) |
| Python | Node scripting and logic | ![85%](https://img.shields.io/badge/85%25-green) |
| Gazebo | Simulation and testing | ![95%](https://img.shields.io/badge/95%25-brightgreen) |
| RViz2 | Visualization | ![90%](https://img.shields.io/badge/90%25-green) |
| SLAM Toolbox | Mapping and localization | ![95%](https://img.shields.io/badge/95%25-green) |



A ROS2 Humble simulation project featuring autonomous room exploration with LIDAR-based SLAM and obstacle avoidance in Gazebo.

## Features
- ✅ Autonomous navigation and exploration
- ✅ Real-time LIDAR-based mapping using SLAM Toolbox
- ✅ Intelligent obstacle avoidance
- ✅ Live visualization in RViz2
- ✅ Gazebo simulation environment

## Prerequisites
- Ubuntu 22.04
- ROS2 Humble
- Gazebo
- Python 3

## Installation

### 1. Install Dependencies
```bash
sudo apt update
sudo apt install -y ros-humble-gazebo-ros-pkgs ros-humble-cartographer \
ros-humble-cartographer-ros ros-humble-navigation2 ros-humble-nav2-bringup \
ros-humble-slam-toolbox ros-humble-turtlebot3-gazebo ros-humble-turtlebot3-msgs \
ros-humble-turtlebot3 python3-colcon-common-extensions
```

### 2. Set TurtleBot3 Model
```bash
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
source ~/.bashrc
```

### 3. Clone and Build
```bash
mkdir -p ~/robot_mapping_ws/src
cd ~/robot_mapping_ws/src
git clone <your-repo-url> autonomous_mapper
cd ~/robot_mapping_ws
colcon build
source install/setup.bash
```

## Usage

### Launch the Complete System
```bash
source ~/robot_mapping_ws/install/setup.bash
ros2 launch autonomous_mapper mapping_launch.py
```

This single command starts:
- Gazebo simulation with TurtleBot3
- SLAM Toolbox for mapping
- RViz2 for visualization
- Autonomous explorer node

### What You'll See
1. **Gazebo Window**: 3D simulation of the robot in the environment
2. **RViz2 Window**: Real-time map building and robot pose

![WhatsApp Image 2025-11-02 at 1 07 08 PM](https://github.com/user-attachments/assets/12c5ee56-ff20-4534-a96b-75e94e7af913)


### Save the Map
Once satisfied with the mapping, save it:
```bash
ros2 run nav2_map_server map_saver_cli -f my_room_map
```

This creates:
- `my_room_map.pgm` - Map image
- `my_room_map.yaml` - Map metadata

![WhatsApp Image 2025-11-02 at 1 07 07 PM](https://github.com/user-attachments/assets/d91edae7-d3f8-48d8-a21f-48c70726da34)


## How It Works

### Autonomous Explorer Node
- Continuously reads LIDAR scan data
- Moves forward while safe
- Detects obstacles within 0.5m
- Intelligently rotates toward open space
- Adds random exploration variations

### SLAM Toolbox
- Processes LIDAR data
- Builds occupancy grid map
- Localizes robot position
- Updates map in real-time

![WhatsApp Image 2025-11-02 at 1 07 07 PM (1)](https://github.com/user-attachments/assets/e3512f5c-48b6-45b4-b9ee-5c877c621d5b)


### Obstacle Avoidance Algorithm
1. Monitor LIDAR 360° scan
2. Calculate minimum distance to obstacles
3. If distance < 0.5m: **Avoid**
   - Stop forward motion
   - Compare left vs right open space
   - Rotate toward larger opening
4. If distance > 0.5m: **Explore**
   - Move forward
   - Add random small turns for coverage

## Customization

### Adjust Robot Speed
Edit `autonomous_mapper/autonomous_explorer.py`:
```python
self.linear_speed = 0.2  # m/s (increase for faster exploration)
self.angular_speed = 0.5  # rad/s (rotation speed)
```

### Adjust Safety Distance
```python
self.safe_distance = 0.5  # meters (obstacle detection threshold)
```

### Change Gazebo World
Edit `mapping_launch.py` to use different worlds:
```python
# Options: turtlebot3_world, turtlebot3_house, empty_world
'turtlebot3_world.launch.py'
```

## Troubleshooting

### Gazebo doesn't start
```bash
killall gzserver gzclient
source ~/.bashrc
```

### Robot doesn't move
Check if explorer node is running:
```bash
ros2 node list
# Should show: /autonomous_explorer
```

### No map in RViz2
1. Click "Add" button
2. Select "Map" display type
3. Set topic to `/map`

### Package not found after build
```bash
source ~/robot_mapping_ws/install/setup.bash
```

## Project Structure
```
autonomous_mapper/
├── autonomous_mapper/
│   ├── __init__.py
│   └── autonomous_explorer.py    # Main exploration logic
├── launch/
│   └── mapping_launch.py          # Launch file
├── resource/
│   └── autonomous_mapper          # Package marker
├── package.xml                    # Package dependencies
├── setup.py                       # Python package setup
└── README.md                      # This file
```

## Future Enhancements

## Development Progress

| Feature | Progress |
|----------|-----------|
| Autonomous Exploration | ![100%](https://img.shields.io/badge/100%25-brightgreen) |
| Obstacle Avoidance | ![90%](https://img.shields.io/badge/90%25-green) |
| SLAM Toolbox Integration | ![95%](https://img.shields.io/badge/95%25-green) |
| Frontier-based Exploration | ![35%](https://img.shields.io/badge/35%25-yellow) |
| Multi-Robot Coordination | ![10%](https://img.shields.io/badge/10%25-red) |


- [ ] Frontier-based exploration
- [ ] Path planning integration
- [ ] Multi-robot coordination
- [ ] 3D mapping support
- [ ] Return to start position

---

[![GitHub Repo stars](https://img.shields.io/github/stars/AryanGanesh/Kinematics?style=social)](https://github.com/AryanGanesh/Kinematics)

**Connect with me:**  
📧 [aryanganesh.k@gmail.com](mailto:aryanganesh.k@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/aryanganesh-kavuri-405684286/)


## Author
AryanGanesh Kavuri
