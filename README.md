# TUGAS-BESAR-CAKRU-URO-17-NATANAEL-I-MANURUNG-19624283-
# Differential wheeled robot-

<div style="display: flex; align-items: flex-start;"><img src="https://techstack-generator.vercel.app/python-icon.svg" alt="icon" width="65" height="65" /></div> 
Cara Menjalankan:  

### 1.  Build dan source workspace untuk 3 terminal <br /> 
    cd <workspace> (folder berisikan semua file tugas besar ini) 
    colcon build --symlink-install
    source install/setup.bash
  note: pastikan ros2 sudah disource terlebih dahulu <br /> 
### 2.  Jalankan launch code yang akan menginisiasi robot di terminal 1:<br />
    ros2 launch basepkg gazebo.launch.py
  Kode ini akan menginisialisasi robot, beserta environment gazebo yang digunakan dalam simulasi <br/ >
### 3.  Untuk menggerakkan robot, aktifkan node teleop_twist_keyboard di terminal 2:
    ros2 run teleop_twist_keyboard teleop_twist_keyboard
  teleop_twist_keyboard adalah salah satu node yang terdapat di module ros2 sendiri
### 4.  Jalankan node lidar_publisher yang akan mengoutput hasil sensor kepada terminal <br/ >
    ros2 run basepkg lidar_publisher.py
   
    
      

