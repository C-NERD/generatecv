# generatecv
Generate cv is a simple python project which helps to generate tech cv(resume) using a single template like the cv [here](https://drive.google.com/file/d/1jMK9Wv8kcStDkrvsSbjHHkhoLCHjF_Ok/view?usp=sharing) if you like what you see consider hiring me.

The template the program used is inspired from cv advise given in these youtube videos
- [How to create the perfect software developer resume](https://www.youtube.com/watch?v=GyjzOKdaioU&t=368s)
- [How to make an amazing software development resume](https://www.youtube.com/watch?v=Xa1pFemaGyc&t=5s)

# How to use the program
1. After cloning the repo navigate into the root directory of the program and open the settings.json file
2. Inside the settings.json file replace the value of the object with the key "title" with your name
3. Then replace the values of the other fields with your information

example:
    if i want to add my email address in the contact section i would simply add
    `"Email:link mailto##alayaa694@gmail.com alayaa694@gmail.com"`
    what this does is it types the string "Email" to the cv followed by a link mailto:alayaa694@gmail.com and the string of the link as alayaa694@gmail.com
    *Remember to subtitute the `:` character in the link with the `##` *
    
   The format for adding pure text to the cv is like so:
      `"Self taught software developer:text -july_2018"`
      - you type in the title of the information in this case it's "self taught software developer" 
      - then you'll add the `:` character
      - after which you'll type "text"
      - finally you'll type the text you want to add
      
   The format for adding experience to the experience section in the cv is like so:
      `"Indie game developer:exp march_2019 till_date _ _ _ |Godot_|Python_|Blender"`
      - you type in you experience in this case it's "Indie game developer"
      - then you'll add the `:` character
      - after which you'll type "exp"
      - then you'll add the starting date of your experience
      - *To leave any portion empty simply type in a single _ character in it's place*
      - *Also to give space use the _ character*
      - then you'll type in the ending date of your work experience
      - followed by the country you had the experience 
      - the link to the companies website(remember to replace the `:` character in the link with `##`)
      - the name of the company
      - and finally the tools you used in such job
      
  The format for adding skills to the skills sections of the cv is like so:
      `"Python:skill |Django_|Pandas_|PyQt5_|Pygame_|numpy_|Eel"`
      - You type in the name of the skill in this case "Python"
      - followed by the `:` character
      - then you type "skill"
      - after which you leave space and type in the tools you used for such skill
      
      
  The format for adding achievements to the achievements section of the cv is like so:
      `"Advent of code 2020:achieve I_participate_in_the_advent_of_code_2020_challenge https##//adventofcode.com/2020/about C-NERD"`
      - you type in the achievement in this case it's "Advent of code 2020"
      - then you'll add the `:` character
      - the you'll add "achieve"
      - follow it with space and type in your achievement
      - then leave a link to the said achievement(remember to replace the `:` character in the link with the `##` characters)
      - and finally type in the text for the link
      
      
  The format for adding projects to the project section of the cv is like so:
      `"Tiles:project A_2D_game_I_am_working_on_using_pygame _ _"`
      - you type the name of the project you are currently working on in this case it's "Tiles"
      - then input the `:` character and then type "project"
      - then add space and then type in a description of your project(keep it short)
      - then add the link to your project(remember to replace the `:` character with `##`)(if you don't have a link just add "_")
      - finally add the text to the link(if you didn't add add a link no need for this one)
      
      
After filling your information in the settings.json file activate the virtual enviroment **virtualenv** if you do not know how to activate python virtual enviroment check this [link](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/#Activate%20the%20virtual%20environment)

so after activating the virtual enviroment make sure that you terminal is in the same directory as the cv.py file and that the cv.py file is in the same directory
as the settings.json file

finally run
`python3 cv.py`

and you cv(resume) will be created in the same directory as the cv.py file
have a nice job hunt.
