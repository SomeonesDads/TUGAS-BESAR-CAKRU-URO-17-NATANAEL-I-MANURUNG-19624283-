#!/usr/bin/env python

from sensor_msgs.msg import LaserScan
import rclpy
from rclpy.node import Node
import math

class LiDARPublisher(Node):
    def __init__(self):
        super().__init__('lidar_publisher')
        self.publisher_ = self.create_publisher(LaserScan, 'scan', 10)
        self.timer = self.create_timer(1.0, self.publish_lidar_data)
        self.get_logger().info('LiDAR Publisher Node has started.')

    def publish_lidar_data(self):
        msg = LaserScan()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'lidar_frame'
        msg.angle_min = -math.pi
        msg.angle_max = math.pi
        msg.angle_increment = math.radians(1.0)  
        msg.time_increment = 0.0
        msg.scan_time = 0.1
        msg.range_min = 0.1
        msg.range_max = 10.0

        msg.ranges = [1.0 + 0.5 * math.sin(i * msg.angle_increment) for i in range(360)]
        msg.intensities = [15.0 for _ in range(360)]  

        self.publisher_.publish(msg)
        self.get_logger().info(f'Published LiDAR data: Ranges[0]={msg.ranges[0]:.2f} Ranges[180]={msg.ranges[180]:.2f}')

        # Print data to terminal
        print(f"\nRanges: {msg.ranges[:10]} ... {msg.ranges[-10:]}")  
        print(f"Angle Increment: {msg.angle_increment:.4f} rad, Time Increment: {msg.time_increment:.4f}s")


def main(args=None):
    rclpy.init(args=args)
    node = LiDARPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()