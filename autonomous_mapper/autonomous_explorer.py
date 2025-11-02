#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from nav_msgs.msg import OccupancyGrid
import numpy as np
import random

class AutonomousExplorer(Node):
    def __init__(self):
        super().__init__('autonomous_explorer')
        
        # Publishers
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Subscribers
        self.scan_sub = self.create_subscription(
            LaserScan, '/scan', self.scan_callback, 10)
        self.map_sub = self.create_subscription(
            OccupancyGrid, '/map', self.map_callback, 10)
        
        # Timer for control loop
        self.timer = self.create_timer(0.1, self.control_loop)
        
        # Robot state
        self.scan_data = None
        self.map_data = None
        self.obstacle_detected = False
        self.min_distance = float('inf')
        self.min_angle_index = 0
        
        # Navigation parameters
        self.linear_speed = 0.22
        self.angular_speed = 0.4
        self.safe_distance = 0.5
        self.exploration_mode = 'forward'
        self.rotation_direction = 1
        
        self.get_logger().info('Autonomous Explorer Node Started!')
        self.get_logger().info('Robot will now explore and map the environment...')
    
    def scan_callback(self, msg):
        """Process LIDAR scan data for obstacle detection"""
        self.scan_data = msg
        
        # Convert scan to numpy array, replacing inf with max range
        ranges = np.array(msg.ranges)
        ranges[np.isinf(ranges)] = msg.range_max
        
        # Find minimum distance and its angle
        self.min_distance = np.min(ranges)
        self.min_angle_index = np.argmin(ranges)
        
        # Check for obstacles
        if self.min_distance < self.safe_distance:
            self.obstacle_detected = True
        else:
            self.obstacle_detected = False
    
    def map_callback(self, msg):
        """Receive map data from SLAM"""
        self.map_data = msg
        # You can process map data here if needed for advanced exploration
    
    def control_loop(self):
        """Main control loop for autonomous exploration"""
        if self.scan_data is None:
            return
        
        twist = Twist()
        
        if self.obstacle_detected:
            # OBSTACLE AVOIDANCE MODE
            self.get_logger().info(
                f'Obstacle detected at {self.min_distance:.2f}m - Avoiding...', 
                throttle_duration_sec=2.0)
            
            # Stop moving forward
            twist.linear.x = 0.18
            
            # Determine rotation direction based on where obstacle is
            ranges = np.array(self.scan_data.ranges)
            ranges[np.isinf(ranges)] = self.scan_data.range_max
            
            # Check left and right sides
            left_side = ranges[0:len(ranges)//3]
            right_side = ranges[2*len(ranges)//3:]
            
            left_distance = np.mean(left_side)
            right_distance = np.mean(right_side)
            
            # Rotate towards the side with more space
            if left_distance > right_distance:
                twist.angular.z = self.angular_speed  # Rotate left
                self.get_logger().info('Rotating LEFT', throttle_duration_sec=2.0)
            else:
                twist.angular.z = -self.angular_speed  # Rotate right
                self.get_logger().info('Rotating RIGHT', throttle_duration_sec=2.0)
            
            self.exploration_mode = 'avoiding'
        
        else:
            # EXPLORATION MODE - Move forward with slight random turns
            self.get_logger().info(
                f'Exploring... Min distance: {self.min_distance:.2f}m', 
                throttle_duration_sec=3.0)
            
            twist.linear.x = self.linear_speed
            
            # Add small random variations to explore different areas
            if random.random() < 0.05:  # 5% chance to change direction
                self.rotation_direction *= -1
            
            twist.angular.z = self.rotation_direction * 0.1 * random.random()
            
            self.exploration_mode = 'exploring'
        
        # Publish velocity command
        self.cmd_vel_pub.publish(twist)
    
    def shutdown(self):
        """Stop the robot when shutting down"""
        self.get_logger().info('Shutting down - Stopping robot...')
        twist = Twist()
        self.cmd_vel_pub.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = AutonomousExplorer()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.shutdown()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
