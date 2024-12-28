# TUGAS-BESAR-CAKRU-URO-17-NATANAEL-I-MANURUNG-19624283-
# Differential wheeled robot-

<div style="display: flex; align-items: flex-start;"><img src="https://techstack-generator.vercel.app/python-icon.svg" alt="icon" width="65" height="65" /></div> 
Pre-Requisites:<br />
Pastikan keberadaan ros2,gazebo dan python3 dan source mereka. Lalu pastikan modul modul berikut terinstall dengan:<br />

```
sudo apt-get install ros-humble-teleop-twist-keyboard
sudo apt install ros-humble-gazebo-ros-pkgs
```
Humble dapat ditukar dengan distribusi ROS yang digunakan <br />
Cara Menjalankan:  
### 1.  Build dan source workspace untuk 3 terminal <br /> 
    cd <workspace> (folder berisikan semua file tugas besar ini) 
    colcon build --symlink-install
    source install/setup.bash
  note: pastikan ros2 sudah disource terlebih dahulu <br /> 
### 2.  Jalankan launch code yang akan menginisiasi robot di terminal 1:
    ros2 launch basepkg gazebo.launch.py
  Kode ini akan menginisialisasi robot, beserta environment gazebo yang digunakan dalam simulasi 
### 3.  Untuk menggerakkan robot, aktifkan node teleop_twist_keyboard di terminal 2:
    ros2 run teleop_twist_keyboard teleop_twist_keyboard
  teleop_twist_keyboard adalah salah satu node yang terdapat di module ros2 sendiri
### 4.  Jalankan node lidar_publisher di terminal 3 yang akan mengoutput hasil sensor kepada terminal:
    ros2 run basepkg lidar_publisher.py
### 5. Sekarang robot sudah dapat berjalan di gazebo, silahkan menambahkan properti tambahan seperti objek objek baru untuk mengetes fungsionalitas LiDar
   
    
      

