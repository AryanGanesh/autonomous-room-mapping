HEAD
# autonomous-room-mapping
ROS2 autonomous robot for room mapping with LIDAR

# Autonomous Room Mapping Robot

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

![WhatsApp Image 2025-11-02 at 1 07 08 PM](https://github.com/user-attachments/assets/ce841df6-4424-40ba-9cd3-62254acfa878)


1. **Gazebo Window**: 3D simulation of the robot in the environment
2. **RViz2 Window**: Real-time map building and robot pose

### Save the Map
Once satisfied with the mapping, save it:
```bash
ros2 run nav2_map_server map_saver_cli -f my_room_map
```

![WhatsApp Image 2025-11-02 at 1 07 07 PM](https://github.com/user-attachments/assets/53bf2eab-ca2b-4b47-a3f4-5f4fc5f3dbaf)

This creates:
- `my_room_map.pgm` - Map image
- `my_room_map.yaml` - Map metadata

## How It Works

### Autonomous Explorer Node
- Continuously reads LIDAR scan data
- Moves forward while safe
- Detects obstacles within 0.5m
- Intelligently rotates toward open space
- Adds random exploration variations

![WhatsApp Image 2025-11-02 at 1 07 07 PM (1)](https://github.com/user-attachments/assets/49a7436f-27d4-40e3-9e0c-3e311a7eb2a2)


### SLAM Toolbox
- Processes LIDAR data
- Builds occupancy grid map
- Localizes robot position
- Updates map in real-time

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
- [ ] Frontier-based exploration
- [ ] Path planning integration
- [ ] Multi-robot coordination
- [ ] 3D mapping support
- [ ] Return to start position

## License
MIT

## Author
AryanGanesh Kavuri
