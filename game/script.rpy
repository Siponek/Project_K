init python:
    
    flag = "wolololo"

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Kenny = Character("Kenny" , color="#222d22")
define Steve = Character("Steve" , color="#af25af")

# The game starts here.
image kenny normal = im.Scale("kenny normal.png", width = 600 , height = 800 )
image steve inspiring = im.Scale("steve inspiring.png", width = 600 , height = 626 )
image bg bg_kenny_house = im.Scale("images/bg_kenny_house.png", width = 1920 , height = 1080)
# image myimage = im.Scale("images/whatever.jpg", <width>, <height>)
label start:
    $ flag = "wololo"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg bg_kenny_house
    with Fade(2, 0.5, 4, color="#184570")
    # Show a character. This uses a placeholder by default, but you can
    # add a file (named either "ch name.png" or "ch name.jpg") to the
    # images directory to show it.
    # show Kenny normal at left
    show kenny normal at left
    show steve inspiring at right

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    "No co Ty tam pierdolony bambusi co Ty?"

    "[flag]"
    Kenny "Siemano Steve!"
    Steve "Siemano Kenny!"

    
    # This ends the game.

    return