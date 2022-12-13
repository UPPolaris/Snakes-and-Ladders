# Snake-and-Ladders 🐍🪜
> 📌100-square snake and ladder game players, 2-4
Everyone must have played the famous game Snakes and Ladders. Alternatively, through the eyes through the ears Snakes and ladders may be a board game that we are all familiar with.
But wouldn't it be wonderful if we made this game simpler to play? Therefore, specifically for that, our group created this snakes and ladders game. which we've taken our understanding of Python from PSCP class.
Use this project to review and improve your programming knowledge in Python.
Enjoy playing our game ^_^
<!-- Live demo [_here_](https://www.example.com). """If you have the project hosted somewhere, include the link here.""" -->

## 📃Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Start Menu](#start-menu)
* [Table](#table)
* [Setup](#setup)
* [Function](#function)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## 📚General Information
> 📖 Python-based four-player Snake & Ladder game with Pygame as the primary game module. The majority of PyGame's features involve taking mouse input and displaying it on the screen.
As for how the game operates, he designed it himself after researching it from numerous sources.
When a player steps on the snake's head, a question will emerge; if the player properly answers, the question will not descend to the snake's tail. This is an addition to the traditional snake and ladder game. However, if the response is incorrect, it will descend to the snake's tail.
- There was a small obstruction. For instance, if you forget to write any code, you may quickly inspect and fix it.
- What is the purpose of your project?
- Why did you undertake it?
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## 💻Technologies Used
- Tech 1 - python version 3.10
- Tech 2 - pygame version 1.9.6
- Tech 3 - vscode & live share


## Features
Our features:
- Awesome feature 1: There is a system to prevent the flow from the snake's head, just answer simple questions correctly.
- Awesome feature 2: 
- Awesome feature 3


## Start Menu
![Example screenshot](https://raw.githubusercontent.com/UPPolaris/Snakes-and-Ladders/master/Mainmenu_bg.png)
## Table
![Example screenshot](https://raw.githubusercontent.com/UPPolaris/Snakes-and-Ladders/master/table_1.png)
<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located?

Proceed to describe how to install / setup one's local environment / get started with the project.


## 💻Function
### **<span style="font-size:100px;">`main_menu function`</span>**   
Load the image of the home page. Then define the area of the start button and the exit button.
If we click the mouse and the position of the mouse in the area of the button The command of that button will work.
* start button -> exit this function (which will immediately call the next function, the game page)
* quit button -> exit
  
https://github.com/UPPolaris/Snakes-and-Ladders/blob/04573650739466c93c6ad6a650d0fa5dd31f9cb6/test.py#L130-L148  

### **<span style="font-size:100px;">`main_game_ui function`</span>**   
It is a function that loads all ui on the game page.
Activated at the end of one player's turn.
https://github.com/UPPolaris/Snakes-and-Ladders/blob/04573650739466c93c6ad6a650d0fa5dd31f9cb6/test.py#L107-L128  

### **<span style="font-size:100px;">`playing_func function`</span>**  
https://github.com/UPPolaris/Snakes-and-Ladders/blob/04573650739466c93c6ad6a650d0fa5dd31f9cb6/test.py#L31-L80  
![img](https://raw.githubusercontent.com/UPPolaris/Snakes-and-Ladders/master/playing_func%20function.png)


## 📝Project Status
Project is : ✅ _complete_


## Room for Improvement
Include areas you believe need improvement / could be improved. Also add TODOs for future development.

Room for improvement:
- Improvement to be done 1
- Improvement to be done 2

To do:
- Feature to be added 1
- Feature to be added 2


## 📑Acknowledgements
Give credit here. 
- https://th.wikipedia.org/wiki/เกมบันไดงู
- https://www.w3schools.com/python/
- https://www.pygame.org/wiki/GettingStarted
- https://dr0id.bitbucket.io/legacy/pygame_tutorials.html  
  
### **<span style="font-size:100px;">`Youtube`</span>**  
[![Here](https://img.youtube.com/vi/fv8mgvsuSKY/0.jpg)](https://www.youtube.com/watch?v=fv8mgvsuSKY)


## 🎯Contact
Created by
- 👑 65070130@kmitl.ac.th [PARAMET CHUATHONG]     --> [Leader, Programmer_1]
- 👨‍💼 65070099@kmitl.ac.th [THANAWAN CHAEMSATHIAN] --> [Programmer, Tester]
- 👨‍💼 65070166@kmitl.ac.th [PONGSAPUCK TONGJUNTUG] --> [Programmer, Tester]
- 👨‍💼 65070174@kmitl.ac.th [PAKIN JUNJUMLONG]      --> [UX_UI Design, Programmer]


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
