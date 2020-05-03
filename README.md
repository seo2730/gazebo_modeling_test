Gazebo Modeling
===============
How to modeling in sdf file(sdf 파일로 모델링하는 법)
---------------------------------------------------
comment(주석) : comment command(주석처리 명령어)
            ``` <!-- comment(주석할 내용) --> ```  
xml version : usually write xml version="1.0"
            ``` <?xml version="1.0"?> ```    
sdf version : usually write sdf version="1.5"
            ``` <sdf version="1.5"> ```    
model name : 모델 이름은 폴더내용과 일치해야함 
            ``` <model name="folder name"> ```     
link name : Each model link name (모델의 각 링크의 이름)   
            ``` <link name="any name"> ``` 
inertial : Choose center of mass, inertial, mass(중심 좌표, 관성 모멘트, 질량)
            ```
            <inertial>
                <!-- center of mass pose -->
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
            ```
collision : Choose collision area(충돌 영역 정하기)







