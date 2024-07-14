# -Automata-Theory-Project
KTU COM2022 project built with Lex&amp;Yacc and Regular Expression

**Robot application that draws according to commands with Python**

The purpose of this project is to provide users with the ability to process randomly selected program lines from a text file and draw them using the turtle graphics module. This allows users to reinforce their programming fundamentals through practice, observing how various shapes are created through visual feedback. Additionally, it offers an opportunity to gain experience in application development and modular programming using Python's diverse libraries such as tkinter, ply, and turtle.

This project is designed as a Python application simulating a drawing robot with various functions. Essentially, the user enters the name of a text file, and a random line from this file is selected and processed. The project utilizes Python's standard libraries such as tkinter and additional libraries to perform tasks like creating graphical user interfaces, text analysis, and graphic drawing.

Operation of the Program
User Input and Text Processing:
Initially, the user provides the name of a txt file. The lines within this file are read, and one line is randomly chosen. This selected line is then passed as input to the lexer.

Lexer (Tokenization):
The selected program line is tokenized using the ply.lex library. This step is crucial for defining commands and numerical values within the line. The lexer output is written to a file named b.txt as a list of tokens and simultaneously stored as a Python list.

Drawing with Turtle:
The tokens are drawn on the screen using the turtle graphics module. Each token represents a drawing command (e.g., move forward, turn right). The result of the drawing is saved as an EPS file, showing the shape drawn by the turtle. This EPS file is later converted to PNG format and displayed to the user.

Graphical User Interface (GUI):
The project offers a two-stage graphical user interface developed with the tkinter library. In the first interface, the user enters the txt file name to initiate the drawing process. The second interface displays the drawing result and potential error messages (such as mismatched parentheses, undefined commands).

This project aims to provide a practical tool for users to practice programming concepts through visual feedback and to gain experience in application development using Python's powerful libraries.

Ghostscript is software used to convert EPS files to PNG format. EPS files store vector graphics, allowing shapes drawn with the turtle module to be saved in a vector format. Later, this vector file is converted to PNG format via Ghostscript and displayed to the user. This step ensures that the drawing results are viewed more widely and enhances the project's functionality.
