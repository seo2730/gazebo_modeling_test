Gazebo Modeling
===============
How to modeling in sdf file(sdf 파일로 모델링하는 법)
---------------------------------------------------
#comment(주석) : comment command(주석처리 명령어)<br>
    
    
    <!-- comment(주석할 내용) -->
#xml version : usually write xml version="1.0"<br>
    
    <?xml version="1.0"?>
#sdf version : usually write sdf version="1.5"<br>
    
    <sdf version="1.5">  
#model name : 모델 이름은 폴더내용과 일치해야함 <br>
     
    <model name="folder name"> 
#link name : Each model link name (모델의 각 링크의 이름)  <br> 
    
    <link name="any name"> 
##inertial : Choose center of mass, inertial, mass(중심 좌표, 관성 모멘트, 질량) <br>
            
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
##collision : Choose collision area(충돌 영역 정하기)<br>
###collision name : Choose collision name<br>
    
    <collision name="base_collision">
###pose : Choose x,y,z,row,pitch,yaw<br>

    <pose>0 0 0.06 0 0 0</pose>
###geometry : Choose shape<br>

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

###Example : <br>

    <collision name="base_collision">
            <pose>0 0 0.06 0 0 0</pose>
            <geometry>
                <box>
                    <size>0.265 0.265 0.1</size>
                </box>
            </geometry>
    </collision>
##visual : Modeling<br>

    <visual name="name"> {same as collision} </visual>





How to modeling in urdf file(urdf 파일로 모델링하는 법)
-------------------------------------------------------



