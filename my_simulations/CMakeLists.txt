cmake_minimum_required(VERSION 2.8.3)
project(my_simulations)

################################################################################
# Find catkin packages and libraries for catkin and system dependencies
################################################################################
find_package(catkin REQUIRED COMPONENTS
  gazebo_ros 
  urdf 
  xacro
)

find_package(gazebo REQUIRED)

################################################################################
# Declare catkin specific configuration to be passed to dependent projects
################################################################################
catkin_package(
    CATKIN_DEPENDS gazebo_ros urdf xacro
    DEPENDS gazebo
)

################################################################################
# Build
################################################################################
link_directories(${GAZEBO_LIBRARY_DIRS})

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
  ${GAZEBO_INCLUDE_DIRS}
)

