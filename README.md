# Abstract Art Generator
### Using the Markov Model to make abstract art
---
### Set Up and Run
---
All of the packages should be installed with Python; if you do not have Python 3.8, I recommend updating 
to the latest version.   
To run the program, locate the folder containing markov.py and run the following:
```terminal
python3 markov.py [num_spaces]
```
where num_spaces is an integer greater than zero. If num_spaces is not specified, it is set to 25.   

---
The code uses Python's turtle library to sketch the art, drawing and filling in shapes across the screen as it moves.
The Markov Markov model determines the shapes and colors used in the art piece, as in a list of probabilities 
determines the next shape and color used at each step in the process. Example artwork can be found in the "examples" folder. The code is meaningful to me because it returns aesthetically pleasing art that I can examine and try to find any themes/messages conveyed from the art. I can even see myself putting this art on my room walls! It is also interesting to compare the art pieces with each other and observe how, and how much, variation the Markov Model creates in terms of shape and color. The size and position of the shapes
were randomly chosen and not reflective of the Markov Model.  

I was definitely challenged with deciding how to create the art at first, given the deliberate vagueness of the assignemnt.
I was not too sure what programming language to use, or what libraries each language had that I could use to create my art. I eased my worries and answered most of my questions by doing research online to see what was available. Ultimately, I decided to work in Python given the turtle library, which offered a relatively straightforward drawing board. Given that I have not coded in Python in over a year and this was my first time using turtle, the assignment was definitely challenging. However, it wasn't anything I couldn't manage without first trying to fully understand the problem and concepts. In the future, I would like to continue to work on my programming skills in Python, hopefully becoming more comfortable using the language in the process.  

I do believe that my system is creative, using the concept of abstract art to create new pieces of work that I believe to be abstract. 
A possible definition of creativity is something that is both novel and valuable. Using the Markov Model, it is clear that no two pieces of art returned from the program are the same. Additionally, abstract art is considered to use shapes, colors, streaks, and other marks to express itself. Though the art pieces contain similar elements, the variation across them can influence different interpretations. One could be able to find unique meaning in each of the art pieces, suggesting value.

Source/Inspiration: https://www.datacamp.com/community/tutorials/markov-chains-python-tutorial

