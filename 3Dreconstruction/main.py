import pyrealsense2 as rs
import numpy as np
import cv2
 
import pcl
from pcl import pcl_visualization

import pandas
 
# image_dir = 'G:\硕士\digitaltwins\3dreconstruction\dataset\rgbd_f3_long_office_household_validation'
# img_names = os.listdir(imgdir)
# img_names = sorted(img_names)
    
# for i in range(len(img_names)):
#     img_names[i] = imgdir + img_names[i]
    # img_names = img_names[0:10]
 
# cloud = pcl.PointCloud_PointXYZRGB()
# def visual(visual_viewer, pt,color):
#     length = len(pt)
#     points = np.zeros((length, 4),dtype=np.float32)
#     for i in range(length):
#         points[i][0] = pt[i][0]
#         points[i][1] = pt[i][1]
#         points[i][2] = pt[i][2]
#         points[i][3] = color[i][1]
 
#     # pt = [list(i) for i in pt]
#     # pt = np.array([*pt])
#     # pt = np.hstack((pt, np.uint8(color)))
 
#     cloud.from_array(points) #从array构建点云的方式
 
    
#     visual_viewer.ShowColorCloud(cloud)
 
#     v = True
#     # while v:
#     #     v = not (visual_viewer.WasStopped())
 
 
 
# if __name__ == "__main__":
#     # Configure depth and color streams
#     pipeline = rs.pipeline()
#     config = rs.config()
#     config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
#     config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
#     # Start streaming
#     pipeline.start(config)
#     #深度图像向彩色对齐
#     align_to_color=rs.align(rs.stream.color)
 
#     pc = rs.pointcloud()
#     points = rs.points()
 
#     visual_viewer = pcl_visualization.CloudViewing()
 
#     try:
#         while True:
#             # Wait for a coherent pair of frames: depth and color
#             frames = pipeline.wait_for_frames()
            
#             frames = align_to_color.process(frames)
 
#             depth_frame = frames.get_depth_frame()
#             color_frame = frames.get_color_frame()
#             if not depth_frame or not color_frame:
#                 continue
#             # Convert images to numpy arrays
 
#             depth_image = np.asanyarray(depth_frame.get_data())
#             color_image = np.asanyarray(color_frame.get_data())
 
#             # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
#             depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
 
#             # Stack both images horizontally
#             images = np.hstack((color_image, depth_colormap))
 
#             # Get point data
#             colorful=color_image.reshape(-1,3)
 
#             pc.map_to(color_frame)
#             points = pc.calculate(depth_frame)
 
#             #获取顶点坐标
#             vtx = np.asanyarray(points.get_vertices())
#             visual(visual_viewer, vtx, colorful)
 
#             # Show images
#             cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
#             cv2.imshow('RealSense', images)
#             key = cv2.waitKey(1)
#             # Press esc or 'q' to close the image window
#             if key & 0xFF == ord('q') or key == 27:
#                 cv2.destroyAllWindows()
#                 break
#     finally:
#         # Stop streaming
#         pipeline.stop()
