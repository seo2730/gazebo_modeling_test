Gazebo Modeling
===============
1.How to modeling in sdf file(sdf 파일로 모델링하는 법)
-------------------------------------------------------
## comment(주석) : comment command(주석처리 명령어)<br>
    
    
    <!-- comment(주석할 내용) -->
## xml version : usually write xml version="1.0"<br>
    
    <?xml version="1.0"?>
## sdf version : usually write sdf version="1.5"<br>
    
    <sdf version="1.5">  
## model name : 모델 이름은 폴더내용과 일치해야함 <br>
     
    <model name="folder name"> 
## link name : Each model link name (모델의 각 링크의 이름)  <br> 
    
    <link name="any name"> 
## inertial : Choose center of mass, inertial, mass(중심 좌표, 관성 모멘트, 질량) <br>
            
    <inertial> 
      <pose>0 0 0.06 0 0 0</pose>
      <inertia>
        <ixx>0.001</ixx>
        <ixy>0.000</ixy>
        <ixz>0.000</ixz>
        <iyy>0.001</iyy>
        <iyz>0.000</iyz>
        <izz>0.001</izz>
      </inertia>
      <mass>1.0</mass>
    </inertial>
## collision : Choose collision area(충돌 영역 정하기)<br>
### collision name : Choose collision name<br>
    
    <collision name="base_collision">
### pose : Choose x,y,z,row,pitch,yaw<br>

    <pose>0 0 0.06 0 0 0</pose>
### geometry : Choose shape<br>

    <box>
        <size>0.265 0.265 0.1</size>
    </box>
    
    <sphere>
         <radius>0.005000</radius>
    </sphere>
    
    <cylinder>
         <radius>0.0508</radius>
         <length>0.055</length>
    </cylinder>
    
### surface : Choose friction(마찰력 정함)
    
    <surface>
     <friction>
         <ode>
             <mu>100000.0</mu>
             <mu2>100000.0</mu2>
             <fdir1>0 0 0</fdir1>
             <slip1>0</slip1>
             <slip2>0</slip2>
         </ode>
     </friction>
    </surface>    
### Example : <br>

    <collision name="base_collision">
            <pose>0 0 0.06 0 0 0</pose>
            <geometry>
                <box>
                    <size>0.265 0.265 0.1</size>
                </box>
            </geometry>            
            <surface>
                <friction>
                     <ode>
                         <mu>100000.0</mu>
                         <mu2>100000.0</mu2>
                         <fdir1>0 0 0</fdir1>
                         <slip1>0</slip1>
                         <slip2>0</slip2>
                     </ode>
                </friction>
            </surface>
    </collision>
## visual : Modeling(stl,dae 파일도 넣을 수 있다)<br>

    <visual name="name"> {same as collision} </visual>
    
### Example(No stl file)

    <visual name="left_wheel_visual">
         <pose>0.07 0.11 0.033 -1.57 0 0</pose>
         <geometry>
               <cylinder>
                   <radius>0.033</radius>
                   <length>0.018</length>
              </cylinder>
         </geometry>
    </visual>
 
### Example(stl or dae file)

    <visual name="lidar_sensor_visual">
        <pose>-0.012 0 0.14 0 0 0</pose>
        <geometry>
             <mesh>
                 <uri>model://{model_file}/meshes/{visual model}.dae</uri>
                 <scale>0.001 0.001 0.001</scale>
             </mesh>
        </geometry>
    </visual>

## sensor : 현재 공부 중(studying)

<br>
<br>

2.How to modeling in urdf file(urdf 파일로 모델링하는 법)
---------------------------------------------------------
## xml version : same as sdf file(sdf 파일과 똑같음)<br>

## robot name : Choose robot name<br>
#### write xmlns:xacro="http://ros.org/wiki/xacro" (Don't know reason)<br>
    
    <robot name="{Your robot name}" xmlns:xacro="http://ros.org/wiki/xacro">
    
## Interworking with another xacro files(다른 xacro 파일 연동하는 법)<br>
    
    <xacro:include filename="$(find directory name)/{path}/another file.xacro"/>
    
## Joint name : Choose your model link name and type<br>
### type : continuous, revolute, fixed<br>

    <joint name="base_joint" type="fixed">

### parent link : choose parent link<br>
### child link : choose child link<br>
: 부모 링크 좌표 기준으로 자식 링크 초기 좌표가 정해진다.<br>

    <parent link="base_footprint" />
    <child link="base_link" />

## Link name : Choose your model link name<br>
    
    <link name="Robot link name" />
    
### visual : Modeling(stl,dae 파일도 넣을 수 있음)<br>

#### origin : Choose raw,pitch,yaw,x,y,z<br> 

    <origin rpy="0 0 0" xyz="0 0 0.0" />

#### geometry : Choose shape(모양 만들기)<br>
 
    <geometry>
        <box size="0.265 0.265 0.1" />
        <sphere radius="0.005" />
        <cylinder length="0.018" radius="0.033" />
    </geometry>
    
#### material : Usually choose color(색깔 정할 때 주로 씀)<br>

    <material name="light_black" />
    
#### Example

    <visual>
         <origin rpy="0 0 0" xyz="0 0 0.0" />
         <geometry>
             <box size="0.265 0.265 0.1" />
         </geometry>
         <material name="light_black" />
    </visual>

    <visual>
         <origin rpy="0 0 0" xyz="0 0 0" />
         <geometry>
             <mesh filename="package://turtlebot3_description/meshes/sensors/lds.stl" scale="0.001 0.001 0.001" />
         </geometry>
         <material name="dark" />
    </visual>
    
### collision : Choose collision area 충돌영역 정하기(visual과 똑같음)<br>
        
    <collision>
       <origin rpy="0 0 0" xyz="0 0 0" />
       <geometry>
           <box size="0.265 0.265 0.1" />
       </geometry>
    </collision>
    
### inertial : Choose center of mass, mass, inertia(중심무게, 질량, 관성모멘트)<br>
        
    <inertial>
          <origin xyz="0.05 0 0" />
          <mass value="0.01" />
          <inertia ixx="1.6425e-6" ixy="0" ixz="0" iyy="1.6425e-6" iyz="0" izz="1.125e-6" />
    </inertial>
    
### Full Example<br>

    <link name="joint2_right_link">
        <visual>
            <origin rpy="0 0 0" xyz="0 0 0" />
            <geometry>
                <cylinder length="0.018" radius="0.015" />
            </geometry>
            <material name="dark" />
        </visual>
        <collision>
            <origin rpy="0 0 0" xyz="0 0 0" />
            <geometry>
                <cylinder length="0.018" radius="0.015" />
            </geometry>
        </collision>
        <visual>
            <origin rpy="0 0 0" xyz="0.05 0 0" />
            <geometry>
                <box size="0.1 0.03 0.03" />
            </geometry>
            <material name="dark" />
        </visual>
        <collision>
            <origin rpy="0 0 0" xyz="0.05 0 0" />
            <geometry>
                <box size="0.1 0.03 0.03" />
            </geometry>
        </collision>
        
        <inertial>
            <origin xyz="0.05 0 0" />
            <mass value="0.01" />
            <inertia ixx="1.6425e-6" ixy="0" ixz="0" iyy="1.6425e-6" iyz="0" izz="1.125e-6" />
        </inertial>
    </link>


## transmission : Making a joint moving(Joint 움직이게 해줌)<br>

    <transmission name="trans_{joint name}">
    
### type 

     <type>transmission_interface/SimpleTransmission</type>
     
### joint : same joint name

    <joint name="joint1_left_joint">{}</joint>

### hardwareInterface : Joint 방식 

    <joint name="joint1_left_joint">
        <hardwareInterface>hardware_interface/EffortJointInterface</hardwareInterface>
    </joint>
    


