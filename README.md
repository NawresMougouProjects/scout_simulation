# scout_simulation
### Ubuntu and ROS installation
In order to install ROS, I downloaded the virtual machine on my computer via this [link ](https://www.virtualbox.org/), I installed Ubuntu from [here](https://releases.ubuntu.com/18.04/) and finally, I installed ROS melodic using the instructions [here](http://wiki.ros.org/melodic/Installation/Ubuntu).
### Scout simulation on gazebo (empty world)
For the Scoot V2 simulation I used this [GitHub](https://github.com/agilexrobotics/ugv_gazebo_sim/tree/master/scout) to download the repository that contains : the scout_control, the scout_description and the scout_gazebo_sim. We need to also know that :
- scout_gazebo_sim： The folder is the gazebo simulation function package
- scout_control: The folder is the simulation controller function package
- scout_description: The folder is the function package of the model file
#### Download and install required function package
```
sudo apt-get install ros-melodic-ros-control
sudo apt-get install ros-melodic-ros-controllers
sudo apt-get install ros-melodic-gazebo-ros
sudo apt-get install ros-melodic-gazebo-ros-control
sudo apt-get install ros-melodic-joint-state-publisher-gui 
sudo apt-get install ros-melodic-teleop-twist-keyboard 
```
#### Create workspace, download simulation model function package and compile
Open a new terminal and create a workspace named scout_ws, enter in the terminal:
```
mkdir scout_ws
cd scout_ws
mkdir src
cd src
catkin_init_workspace
git clone https://github.com/agilexrobotics/ugv_sim.git
cd scout_ws
rosdep install --from-paths src --ignore-src -r -y 
catkin_make
```
#### Run the simulation
Enter the scout_ws folder
```
cd scout_ws
```
​Declare the environment variable
```
source devel/setup.bash
```
​ Start the simulation environment of scout_v2
```
roslaunch scout_gazebo_sim scout_empty_world.launch
```
![gazebo_scout](uploads/f313b18c40f2bdd194d1546e8258e2bc/gazebo_scout.png)
![gazebo_scout_empty_wold](uploads/4cbef494d68d3a1251d193e57c0ace57/gazebo_scout_empty_wold.png)
![gazebo_scout_empty_world_2](uploads/484c5b2489bfa8bc6ff204cc6ebfe20d/gazebo_scout_empty_world_2.png)

We can control the robot using the following command
```
rosrun teleop_twist_keyboard teleop_twist_keyboard.py 
```
![control](uploads/1e22d987747248424ef5ac6f2fb28a2c/control.png)
![empty_world_scoot_navigation](uploads/344e625362395fb8836286c9a665c9dd/empty_world_scoot_navigation.mp4)

## Intel Realsense camera simulation on Gazebo
First, we need to install the realsense_gazebo_plugin package from [here](https://github.com/pal-robotics/realsense_gazebo_plugin), and then we need to get the Intel_RealSense description (we must get the modified version) from [here](https://github.com/issaiass/realsense2_description).
Or you can just clone the repos directly into your workspace like this:
```
    cd scout_ws/src/
    git clone https://github.com/issaiass/realsense2_description
    git clone https://github.com/issaiass/realsense_gazebo_plugin
```
Finally, you can launch the application by:
```
    roslaunch realsense2_description view_d435_model_rviz_gazebo.launch
```
You can see that the camera is not detecting anything yet:
![Realsense_rviz2](uploads/5504c6979dac42c5ff0f4479e1338ae3/Realsense_rviz2.png)

Once you put a random object you can directly see it through the camera screen:

![Realsense_camera_gazebo_object](uploads/874310a4548fed68639ae38ba7640732/Realsense_camera_gazebo_object.png)

![Realsense_camera_gazebo_object2](uploads/9aa534c2c8c4bbafa37d704a2e1af8f5/Realsense_camera_gazebo_object2.png)

## Integrating the Inter Realsense d435 camera into the scout V2
in order to integrate the Realsense camera we first need to install the realsense_description from [here](https://github.com/issaiass/realsense2_description) and the realsense_gazebo_plugin from here[](https://github.com/issaiass/realsense_gazebo_plugin).
Then we need to put these two folders in the same folder as the scout. Afterward, some changes need to be made to the scout folder.
1. changes in the scout_v2.xacro inside the urdf folder:
```
 <!-- Xacro arguments for depth camera use -->
    <xacro:arg name="realsense_enable" default="true" />
    <xacro:arg name="pointcloud_enable" default="true" />

    <!-- All Neccesary Header Files, Macros and Constants -->
  <xacro:include filename="$(find scout_description)/urdf/includes.xacro" />  
  <!-- All Neccesary Header FIles, Macros and Constants -->
```
Also add this one:
```
<!-- REALSENSE CAMERA -->
      <!-- REALSENSE CAMERA -->
    <xacro:if value="$(arg realsense_enable)">
      <xacro:sensor_d435 name="realsense_d435" topics_ns="realsense_d435" parent="base_link" publish_pointcloud="$(arg pointcloud_enable)" >
        <origin xyz="0.077 0 0.8" rpy="0 0 0" />
      </xacro:sensor_d435>
   </xacro:if>
```
2. Create an includes folder and an include.xacro file:
In the include.xacro file we can add:
```
<?xml version="1.0"?>
<robot xmlns:xacro="http://www.ros.org/wiki/xacro">

  <!-- Rviz Color Properties -->
  <xacro:include filename="$(find scout_description)/urdf/includes/materials/materials.xacro" />  
  <!-- Rviz Color Properties -->  

  <!-- Intel Realsense Macro -->
  <xacro:include filename="$(find scout_description)/urdf/includes/parts/sensors/realsense/_d435.urdf.xacro" />    
  <!-- Intel Realsense Macro -->

</robot>
```
Inside the in the includes folder we need to create 3 other folders: materials, gazebo and parts. Inside the gazebo folder we need to put the _d435.gazebo.xacro file and the inertias.xacro file. Inside the materials folder we need to add the materials.xacro file in which we can put:
```
<?xml version="1.0"?>
<robot>

  <material name="purple">
    <color rgba="0.5 0 0.7 1"/>
  </material>
  <material name="yellow">
    <color rgba="1 1 0 1"/>
  </material>
  <material name="black">
    <color rgba="0 0 0 1"/>
  </material>
  <material name="white">
    <color rgba="1.0 1.0 1.0 1.0"/>
  </material>
  <material name="blue">
    <color rgba="0 0 1 0.2"/>
  </material> 
  <material name="grey">
    <color rgba="0.66 0.66 0.66 1"/>
  </material>    
  <material name="soft_blue">
    <color rgba="0.2157 0.5294 0.9216 1"/>
  </material>
  <material name="grey_alpha">
    <color rgba="0.3 0.3 0.3 0.4"/>
  </material>   
  <material name="green">
    <color rgba="0.1 0.3 0.1 0.8"/>
  </material>
  <material name="dark">
    <color rgba="0.3 0.3 0.3 1.0"/>
  </material>

</robot>
```
After that, inside the parts folder we can add the sensors folder, where we can add the realsense folder and put in it the _d435.urdf.xacro file.
3. Changes in the launch folder:
We chose as an exemple the display_scout_v2.launch file, in which we added the following lines:
```
  <!-- arguments for the realsense camera to load -->
    <arg name="pointcloud_enable" default="true" />
    <arg name="realsense_enable" default="true" /> 
```
4.Changes made in the meshes folder:
we need to add a realsense folder in which we can add the d435.dae file.
That's it! now it's possible to view the realsense camera attached to the robot, and if the camera is not well positioned we can change the origin parameter in these lines in the xacro file:
```
<!-- REALSENSE CAMERA -->
      <!-- REALSENSE CAMERA -->
    <xacro:if value="$(arg realsense_enable)">
      <xacro:sensor_d435 name="realsense_d435" topics_ns="realsense_d435" parent="base_link" publish_pointcloud="$(arg pointcloud_enable)" >
        <origin xyz="0.077 0 0.8" rpy="0 0 0" />
      </xacro:sensor_d435>
   </xacro:if>
```
### RESULT
we tested these steps on both the scout V2 and the tracer:
To open the tracer Rviz simulation:
`roslaunch tracer_description display_models.launch 
`

![tracer_+_realsense](uploads/90d5a50755d779e5b65ee824c0a3acc1/tracer_+_realsense.png)

And to open the scout V2 new simulation:
`roslaunch scout_description display_scout_v2.launch 
`
The parameters made to the scout_v2.xacro to position the camera are:
```
    <!-- REALSENSE CAMERA -->
      <!-- REALSENSE CAMERA -->
    <xacro:if value="$(arg realsense_enable)">
      <xacro:sensor_d435 name="realsense_d435" topics_ns="realsense_d435" parent="base_link" publish_pointcloud="$(arg pointcloud_enable)" >
        <origin xyz="0.35 0 0.095" rpy="0 0 0" />
      </xacro:sensor_d435>
   </xacro:if>
```
This gives us the following result:
![scout+realsense](uploads/bfe23f52d458f6360e6a3807dcc64349/scout+realsense.png)

![scout+realsense2](uploads/b36ee1f7b953a30f772fdbd6496e0455/scout+realsense2.png)

## Navigation and visualization
After attaching the camera to the robot, the next step is moving the robot around and visualizing the camera's output.
In order to do that we need to type on the terminal:
```
roslaunch scout_gazebo_sim scout_empty_world.launch
```
Since we chose the empty world as our example, we will replace navigation.rviz with model_display.rviz at the end of the scout_empty_world.launch file, which had the new model with the camera attached.
This gives us the expected result:

![navigation_+_realsense](uploads/2737284e85e7e3a56302c6ec95485470/navigation_+_realsense.png)

![navigation_+_realsense2](uploads/3507cb7b7595eda9527788299b8dc2ef/navigation_+_realsense2.png)

![mini_house_simulation2](uploads/6e48966ec9919be7f79ffbfa3e37b7d4/mini_house_simulation2.png)

![mini_house_simulation3](uploads/f4cfe3e2d3b7226ac99f500610f01fcf/mini_house_simulation3.png)

Here's a video of the outcome:

![navigation_with_realsense](uploads/86e67c159a950ff0d3f96a9e12c9c647/navigation_with_realsense.mp4)


