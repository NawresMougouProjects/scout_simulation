# Install script for directory: /home/nawres/scout_simulation/src/ugv_gazebo_sim-master/limo_s2/limo_s2_arm

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/nawres/scout_simulation/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/nawres/scout_simulation/build/ugv_gazebo_sim-master/limo_s2/limo_s2_arm/catkin_generated/installspace/limo_s2_arm.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/limo_s2_arm/cmake" TYPE FILE FILES
    "/home/nawres/scout_simulation/build/ugv_gazebo_sim-master/limo_s2/limo_s2_arm/catkin_generated/installspace/limo_s2_armConfig.cmake"
    "/home/nawres/scout_simulation/build/ugv_gazebo_sim-master/limo_s2/limo_s2_arm/catkin_generated/installspace/limo_s2_armConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/limo_s2_arm" TYPE FILE FILES "/home/nawres/scout_simulation/src/ugv_gazebo_sim-master/limo_s2/limo_s2_arm/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/limo_s2_arm/config" TYPE DIRECTORY FILES "/home/nawres/scout_simulation/src/ugv_gazebo_sim-master/limo_s2/limo_s2_arm/config/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/limo_s2_arm/launch" TYPE DIRECTORY FILES "/home/nawres/scout_simulation/src/ugv_gazebo_sim-master/limo_s2/limo_s2_arm/launch/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/limo_s2_arm/meshes" TYPE DIRECTORY FILES "/home/nawres/scout_simulation/src/ugv_gazebo_sim-master/limo_s2/limo_s2_arm/meshes/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/limo_s2_arm/urdf" TYPE DIRECTORY FILES "/home/nawres/scout_simulation/src/ugv_gazebo_sim-master/limo_s2/limo_s2_arm/urdf/")
endif()

