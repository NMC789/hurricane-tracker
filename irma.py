import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()

    # your code to animate Irma here
    data = open("irma.csv", "r")
    text = data.read()

    lines = text.split(",")

    lat = lines[7::5]
    long = lines[8::5]
    wind_speed = lines[9::5]

    lat = [float(x) for  x in lat]
    long = [float(x) for x in long]
    wind_speed = [int(x) for x in wind_speed]

    coord_speed = list(zip(long, lat, wind_speed))

    for i in coord_speed:

        if i[2] >= 74 and i[2] <= 95: #Cat 1
                t.pencolor("blue")
                t.width(2)
                t.write(1)

        elif i[2] >= 96 and i[2] <= 110: #Cat 2
                t.pencolor("green")
                t.width(4)
                t.write(2)

        elif i[2] >= 111 and i[2] <= 129: #Cat 3
                t.pencolor("yellow")
                t.width(6)
                t.write(3)

        elif i[2] >= 130 and i[2] <= 156: #Cat 4
                t.pencolor("orange")
                t.width(8)
                t.write(4)

        elif i[2] > 157: #Cat 5
                t.pencolor("red")
                t.width(10)
                t.write(5)

        else:
            t.pencolor("white")
            t.width(1)
            
        t.goto(i[0], i[1])
    

if __name__ == "__main__":
    irma()

