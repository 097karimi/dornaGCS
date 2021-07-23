# Dorna Gound Control Station

**The goal of this project is to develop a cloud-based ground control station to have connections to multiple drones all over the world through the Internet  for Ardupilot drones.**

The project is still under development and we would love to have more developers joining us!

![GCS Picture](https://i.ibb.co/RPNkDrq/GCS-Picture.png)

***In order to use this project you need to receive data from your PixHawk and send it to DornaGCS through websocket, so you have to use another project for this purpose which I'll put its link down below***

https://github.com/097karimi/Send-and-Receive-Data-From-PX-To-Server


# Installation

 - clone the project
   - https://github.com/097karimi/dornaGCS.git
 
 - Install requirments
   - pip install -r requirments.txt
 
 - Create database
   - ./manage.py makemigrations
   - ./manage.py migrate
 
 - run
   - ./manage.py runserver 9090

# To do
- [ ] Using vue js as frontend instead of django templates
- [ ] using Django Rest Framework to add an API for mobile app
