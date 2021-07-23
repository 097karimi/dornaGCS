# Dorna Gound Control Station

**The goal of this project is to develop a cloud-based ground control station to have connections to multiple drones all over the world through Internet  for Ardupilot drones.**

The project is still under development and we would love to have more developers joining us!


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
[] Using vue js as frontend instead of django templates
[] using Django Rest Framework to add an API for mobile app
