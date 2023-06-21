#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

# YOLOv5
from models.experimental import attempt_load
from utils.general import non_max_suppression, scale_coords, plot_one_box
from utils.plots import colors

def image_callback(msg):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding='rgb8')

    # YOLOv5 settings
    weights = 'yolov5s.pt'
    img_size = 640
    conf_thres = 0.25
    iou_thres = 0.45
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    # Load YOLOv5 model
    model = attempt_load(weights, map_location=device)
    stride = int(model.stride.max())
    img_size = check_img_size(img_size, s=stride)
    if device == 'cuda':
        model = model.half()

    # Preprocess image
    img = cv2.resize(cv_image, (img_size, img_size))
    img = img.transpose(2, 0, 1)
    img = np.ascontiguousarray(img)

    # Detect objects  File "person.py", line 10, in <module>
    from utils.general import non_max_suppression, scale_coords, plot_one_box
ImportError: cannot import name 'plot_one_box' from 'utils.general' (/home/nawres/yolo_nav/UI/utils/general.py)

    img = torch.from_numpy(img).to(device).unsqueeze(0)
    img = img.half() if device == 'cuda' else img.float()
    img /= 255.0
    if img.ndimension() == 3:
        img = img.unsqueeze(0)

    # Inference
    with torch.no_grad():
        pred = model(img)[0]
        pred = non_max_suppression(pred, conf_thres, iou_thres)

    # Draw bounding boxes on the image
    if len(pred) > 0:
        for det in pred:
            det[:, :4] = scale_coords(img.shape[2:], det[:, :4], cv_image.shape).round()
            for *xyxy, conf, cls in det:
                label = f'{model.names[int(cls)]} {conf:.2f}'
                plot_one_box(xyxy, cv_image, label=label, color=colors(int(cls), True), line_thickness=2)
  File "person.py", line 10, in <module>
    from utils.general import non_max_suppression, scale_coords, plot_one_box
ImportError: cannot import name 'plot_one_box' from 'utils.general' (/home/nawres/yolo_nav/UI/utils/general.py)

    # Display the image with bounding boxes
    cv2.imshow('Object Detection', cv_image)
    cv2.waitKey(1)

def main():
    rospy.init_node('yolov5_object_detection')

    # Subscribe to the image topic
    image_topic = '/realsense_d435/color/image_raw'
    rospy.Subscriber(image_topic, Image, image_callback)

    rospy.spin()

if __name__ == '__main__':
    main()

