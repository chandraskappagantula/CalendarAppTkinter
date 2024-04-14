import tkinter
import datetime
import time
import calendar
from PIL import ImageTk, Image
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

window = tkinter.Tk()
HEIGHT = window.winfo_screenheight()
WIDTH = window.winfo_screenwidth()
dimensions = str(WIDTH)+"x"+str(HEIGHT)
window.geometry(dimensions)

frame = tkinter.Frame(window, height = HEIGHT, width = WIDTH)
frame.pack()

event_manager = tkinter.Frame(window, height = HEIGHT/2, width = WIDTH/2, highlightbackground = "grey", highlightthickness = 5)
event_manager.place(relx = 0.5, rely = 0.5, anchor = "center")
event_manager.lift()
event_manager.place_forget()

productivity_manager = tkinter.Frame(window, height = HEIGHT/2, width = WIDTH/2, highlightbackground = "grey", highlightthickness = 5)
productivity_manager.place(relx = 0.5, rely = 0.5, anchor = "center")
productivity_manager.lift()
productivity_manager.place_forget()

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

TODAYS_DATE = str(datetime.datetime.now().month) + " " + str(datetime.datetime.now().day) + " " + str(datetime.datetime.now().year)
TODAYS_DATE_ACTUAL = str(datetime.datetime.now().month) + " " + str(datetime.datetime.now().day) + " " + str(datetime.datetime.now().year)

COUNTER = 0
HOURS = 0
STATE_OF_STOPWATCH = False

FOCUS_DAYS = {}

def print_date(days, months):
    month = datetime.datetime.now().month

    daynum = datetime.datetime.now().day
    weekday = datetime.datetime.now().weekday()

    year = datetime.datetime.now().year

    exceptions_with_st = [1, 21, 31]
    exceptions_with_nd = [2, 22]
    exceptions_with_rd = [3, 23]
    
    if daynum not in exceptions_with_st and daynum not in exceptions_with_nd and daynum not in exceptions_with_rd:
        return DAYS[weekday]+", " + MONTHS[month - 1] + " " + str(daynum)+"th"+", " + str(year)

    elif daynum in exceptions_with_st:
        return DAYS[weekday]+", " + MONTHS[month - 1] + " " + str(daynum)+"st"+", " + str(year)

    elif daynum in exceptions_with_nd:
        return DAYS[weekday]+", " +  MONTHS[month - 1] + " " + str(daynum)+"nd"+", " + str(year)

    elif daynum in exceptions_with_rd:
        return DAYS[weekday]+", " + MONTHS[month - 1] + " " + str(daynum)+"rd"+", " + str(year)

def find_day(day1, numtogoback):
    reference = DAYS.index(day1)
    
    i = 0
    val = ""

    reference = int(reference)

    while numtogoback > 0:
        init = reference - 1 - i
        if init >= 0:
            val = DAYS[init]
            numtogoback -= 1
            i += 1
        else:
            reference = len(DAYS)
            val = DAYS[reference - 1]
            i = 1
            numtogoback -= 1

    return val


morning = tkinter.Label(window, text = "Good Morning, Chandra", font = ("Times new roman", 35))
morning.place(x = WIDTH/25, y = HEIGHT/50)

date = tkinter.Label(window, text = print_date(DAYS, MONTHS), font = ("Helvetica", 20))
date.place(x = WIDTH/15, y = HEIGHT/10)

monthlabel = tkinter.Label(window, text = MONTHS[datetime.datetime.now().month - 1], font = ("Times new roman", 40))
monthlabel.place(x = WIDTH/2.3, y = HEIGHT/45)

yearlabel = tkinter.Label(window, text = datetime.datetime.now().year, font = ("Times new roman", 20))
yearlabel.place(x = WIDTH/2.13, y = HEIGHT/10)

HEIGHTS = [0, 120, (120 * 2), (120 * 3), (120 * 4)]
WIDTHS = [0, 205.17, 205.17 * 2, 205.17 * 3, 205.17 * 4, 205.17 * 5, 205.17 * 6, 205.17 * 7]

WEEKDAYDICT = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}

BLOCKS = []

def PLACE_CANVAS(master_widget, monthblockslist):
    global HEIGHTS, WIDTHS
    
    for i in range(len(HEIGHTS)):
        HEIGHTS[i] += HEIGHT/5

    for n in range(5):
        for i in range(7):
            l = tkinter.Canvas(master_widget, height = 120, width = 205.17, highlightbackground = "grey", borderwidth = 10)
            l.place(x = WIDTHS[i], y = HEIGHTS[n])
            monthblockslist.append(l)

for i in range(len(DAYS)):
    tkinter.Label(window, text = DAYS[i][0:3]).place(x = (i) * (205.17) + 102.85, rely = 0.17)

LIST_OF_DAYLABELS = []
EVENTS_DICTIONARY = {}

EVENT_OPEN_BOOL = False

def open_event(date_to_do, button_list, index):
    global event_manager, EVENT_OPEN_BOOL
    
    if EVENT_OPEN_BOOL == False:
        event_manager.place(relx = 0.5, rely = 0.5, anchor = "center")

        display = button_list[index][1].split(" ")
        final = ""

        exceptions_with_st = [1, 21, 31]
        exceptions_with_nd = [2, 22]
        exceptions_with_rd = [3, 23]
        
        if int(display[1]) not in exceptions_with_st and int(display[1]) not in exceptions_with_nd and int(display[1]) not in exceptions_with_rd:
            final = MONTHS[int(display[0]) - 1] + " " + str(display[1])+"th"+", " + str(display[2])

        elif int(display[1]) in exceptions_with_st:
            final = MONTHS[int(display[0]) - 1] + " " + str(display[1])+"st"+", " + str(display[2])

        elif int(display[1]) in exceptions_with_nd:
            final = MONTHS[int(display[0]) - 1] + " " + str(display[1])+"nd"+", " + str(display[2])

        elif int(display[1]) in exceptions_with_rd:
            final = MONTHS[int(display[0]) - 1] + " " + str(display[1])+"rd"+", " + str(display[2])
        
        d = tkinter.Label(event_manager, text = final, font = ("Helvetica", 25))
        d.place(relx = 0.5, rely = 0.1, anchor = "center")

        b = tkinter.Button(event_manager, text = "Add Task/Event")
        b.place(relx = 0.85, rely = 0.1, anchor = "center")

        exit_button = tkinter.Button(event_manager, text = "X", bg = "light grey", border = 1, borderwidth = 1, highlightthickness = 1, highlightcolor = "black", highlightbackground = "black", relief = tkinter.FLAT, padx = 7)
        exit_button.place(relx = 0.96, rely = 0.0005)

        num_of_events = 0

        LIST_OF_TEXTVARS_WITH_BUTTONS = []

        def strikethrough(text, state, listupdate, varupdate, iteration, listvar3):
            global EVENTS_DICTIONARY
            if state == False:
                result = ""
                for char in text:
                    result = result + char + "\u0336"
                print(iteration)
                listvar3[iteration][0].config(text = result)

                EVENTS_DICTIONARY[varupdate][iteration][1] = True

            elif state == True:
                print("here: ", iteration)
                listvar3[iteration][0].config(text = listupdate[varupdate][iteration][0])
                EVENTS_DICTIONARY[varupdate][iteration][1] = False

        def putevents(date, strikefunc, listvar):
            global EVENTS_DICTIONARY
            
            for i in range(len(EVENTS_DICTIONARY[date])):
                if len(EVENTS_DICTIONARY[date][i]) == 0:
                    pass
                else:
                    e = tkinter.Label(event_manager, text = EVENTS_DICTIONARY[date][i][0], font = ("Times new roman", 20))
                    e.place(relx = 0.2, rely = 0.3 + (0.15 * i))

                    c = tkinter.Button(event_manager, text = "X", command = lambda k = i: strikefunc(EVENTS_DICTIONARY[date][k][0], EVENTS_DICTIONARY[date][k][1], EVENTS_DICTIONARY, date, k, listvar))
                    c.place(relx = 0.1, rely = 0.3 + (0.15 * i))
                    
                    listvar.append([e, c])

        def add_event(listupdate, varupdate, iteration, listvars2):
            nonlocal num_of_events, putevents
            
            c = tkinter.Button(event_manager, text = "X", command = lambda: strikethrough(EVENTS_DICTIONARY[date_to_do][iteration][0], e, EVENTS_DICTIONARY[date_to_do][iteration][1], EVENTS_DICTIONARY, date_to_do, iteration, listvars2))
            print(iteration)
            c.place(relx = 0.1, rely = 0.3 + (0.15 * (num_of_events)))

            entry = tkinter.Entry(event_manager)
            entry.place(relx = 0.2, rely = 0.3 + (0.15 * (num_of_events)))
            
            tempdate = date_to_do

            def enter_clicked(event, strikefunc2, listvar, var, listvars):
                nonlocal putevents, tempdate, num_of_events
                print(listvar)
                
                try:
                    ap = listvar[var][num_of_events - 1]

                except IndexError:
                    ap = listvar[var]
    
                ap += [[entry.get(), False]]
                print(ap)
                entry.place_forget()
                listupdate.update({varupdate: ap})
                print(listupdate)
                putevents(tempdate, strikefunc2, listvars)

            entry.bind("<Return>", lambda x: enter_clicked("<Return>", strikethrough, listupdate, varupdate, listvars2))
            
            num_of_events += 1

        def hover_button(event, widget):
            widget.config(bg = "red")

        def leave_button(event, widget):
            widget.config(bg = "light grey")

        def close(manager):
            global EVENT_OPEN_BOOL
            
            for child_widget in manager.winfo_children():
                child_widget.destroy()
                
            manager.place_forget()
            EVENT_OPEN_BOOL = False


        b.config(command = lambda: add_event(EVENTS_DICTIONARY, date_to_do, num_of_events, LIST_OF_TEXTVARS_WITH_BUTTONS))

        exit_button.bind("<Enter>", lambda x: hover_button("<Enter>", exit_button))
        exit_button.bind("<Leave>", lambda x: leave_button("<Leave>", exit_button))

        exit_button.config(command = lambda: close(event_manager))
        
        putevents(date_to_do, strikethrough, LIST_OF_TEXTVARS_WITH_BUTTONS)

        EVENT_OPEN_BOOL = True
        
    elif EVENT_OPEN_BOOL == True:
        pass

LIST_OF_BUTTONS = []

def button_personalize(l):
    for i in range(len(l)):
        l[i][0].config(command = lambda i = i: open_event(l[i][1], l, i))

def place_month(month, function, year, day, start_day):
    global TODAYS_DATE, TODAYS_DATE_ACTUAL, LIST_OF_DAYLABELS, EVENTS_DICTIONARY, LIST_OF_BUTTONS, BLOCKS, FOCUS_DAYS

    print(EVENTS_DICTIONARY)
    
    dayvar = 1
    maincount = WEEKDAYDICT[function(day, start_day)] - 1
    factor = 1

    while dayvar <= calendar.monthrange(year, month)[1]:
        num = tkinter.Label(frame, text = dayvar)
        but = tkinter.Button(frame, text = "View Task(s)/Event(s)")
        
        LIST_OF_DAYLABELS.append([num, but])
        
        if (maincount) < 7:
            num.place(x = (maincount * (205.17) + 6.85), y = (120) * (factor) + HEIGHTS[0] - 115)
            but.place(x = (maincount * (205.17) + (200/2.5)), y = (120) * (factor) + HEIGHTS[0] - 115)
            """
            try:
                for i in range(len(EVENTS_DICTIONARY[str(month) + " " + str(num.cget("text")) + " " + str(year)])):
                    text = tkinter.Label(frame, text = EVENTS_DICTIONARY[str(month) + " " + str(num.cget("text")) + " " + str(year)][i][0])
                    text.place(x = (maincount * (205.17) + 12), y = (120) * (factor) + HEIGHTS[0]/2)
                    print("did this")

            except KeyError:
                pass
            """
            maincount += 1
            dayvar += 1
            LIST_OF_DAYLABELS[LIST_OF_DAYLABELS.index([num, but])].append([maincount * (205.17) + 6.85, (120) * (factor) + HEIGHTS[0] - 115, str(month) + " " + str(num.cget("text")) + " " + str(year), BLOCKS[dayvar]])
            try:
                EVENTS_DICTIONARY.update({str(month) + " " + str(num.cget("text")) + " " + str(year): EVENTS_DICTIONARY[str(month) + " " + str(num.cget("text")) + " " + str(year)]})
                FOCUS_DAYS.update({str(month) + " " + str(num.cget("text")) + " " + str(year): 0})
            except KeyError:
                EVENTS_DICTIONARY.update({str(month) + " " + str(num.cget("text")) + " " + str(year): []})
                FOCUS_DAYS.update({str(month) + " " + str(num.cget("text")) + " " + str(year): 0})
            LIST_OF_BUTTONS.append([but, str(month) + " " + str(num.cget("text")) + " " + str(year)])

            if str(month) + " " + str(num.cget("text")) + " " + str(year) == TODAYS_DATE_ACTUAL:
                num.config(bg = "red")
            
        elif (maincount) == 7:
            maincount = 0
            factor += 1
            num.place(x = (maincount * (205.17) + 6.85), y = (120) * (factor) + HEIGHTS[0] - 115)
            but.place(x = (maincount * (205.17) + (200/2.5)), y = (120) * (factor) + HEIGHTS[0] - 115)
            """
            try:
                for i in range(len(EVENTS_DICTIONARY[str(month) + " " + str(num.cget("text")) + " " + str(year)])):
                    text = tkinter.Label(frame, text = EVENTS_DICTIONARY[str(month) + " " + str(num.cget("text")) + " " + str(year)][i])
                    text.place(x = (maincount * (205.17) + 6.85), y = (120) * (factor) + HEIGHTS[0])
                    print("did this??")

            except KeyError:
                pass
            """
            LIST_OF_DAYLABELS[LIST_OF_DAYLABELS.index([num, but])].append([maincount * (205.17) + 6.85, (120) * (factor) + HEIGHTS[0] - 115, str(month) + " " + str(num.cget("text")) + " " + str(year), BLOCKS[dayvar]])
            try:
                EVENTS_DICTIONARY.update({str(month) + " " + str(num.cget("text")) + " " + str(year): EVENTS_DICTIONARY[str(month) + " " + str(num.cget("text")) + " " + str(year)]})
                FOCUS_DAYS.update({str(month) + " " + str(num.cget("text")) + " " + str(year): 0})
            except KeyError:
                EVENTS_DICTIONARY.update({str(month) + " " + str(num.cget("text")) + " " + str(year): []})
                FOCUS_DAYS.update({str(month) + " " + str(num.cget("text")) + " " + str(year): 0})
            LIST_OF_BUTTONS.append([but, str(month) + " " + str(num.cget("text")) + " " + str(year)])
            
            if str(month) + " " + str(num.cget("text")) + " " + str(year) == TODAYS_DATE_ACTUAL:
                num.config(bg = "red")
            
        num.lift()

    TODAYS_DATE = str(datetime.datetime.now().month) + " " + str(datetime.datetime.now().day) + " " + str(year)

def update_events_main_page(dayeventslist, daylabelslist, dictionary):
    for i in range(len(dayeventslist)):
        for n in range(len(daylabelslist)):
            if dayeventslist[i] in daylabelslist[n]:
                l = dictionary[daylabelslist[n][1]]

                for item in l:
                    c = daylabelslist[n][2].create_text(text = item)

PLACE_CANVAS(frame, BLOCKS)

print(BLOCKS)

place_month(datetime.datetime.now().month, find_day, datetime.datetime.now().year, DAYS[datetime.datetime.now().weekday()], datetime.datetime.now().day - 1)
button_personalize(LIST_OF_BUTTONS)

update_events_main_page(BLOCKS, LIST_OF_DAYLABELS, EVENTS_DICTIONARY)

leftbutton_image = ImageTk.PhotoImage(Image.open("C:\\Users\\chand\\OneDrive\\Desktop\\pythonprograms\\leftbutton_1_50_1_100x67.png"))
rightbutton_image = ImageTk.PhotoImage(Image.open("C:\\Users\\chand\\OneDrive\\Desktop\\pythonprograms\\rightbutton.png"))

leftbutton = tkinter.Label(window, image = leftbutton_image, relief = tkinter.RAISED)
leftbutton.place(x = WIDTH/2.6, y = HEIGHT/40)

rightbutton = tkinter.Label(window, image = rightbutton_image, relief = tkinter.RAISED)
rightbutton.place(x = WIDTH/1.85, y = HEIGHT/40)

yearleft = tkinter.Label(window, image = leftbutton_image, relief = tkinter.RAISED)
yearleft.place(x = WIDTH/2.37, y = HEIGHT/11)

yearright = tkinter.Label(window, image = rightbutton_image, relief = tkinter.RAISED)
yearright.place(x = WIDTH/1.91, y = HEIGHT/11)

stopwatchlabel = tkinter.Label(window, text = "0:00:00", font = ("Helvetica", 60))
stopwatchlabel.place(relx = 0.75, rely = 0.03)

forward_backward = 0

def month_forward(event, current_date):
    global forward_backward, monthlabel, LIST_OF_DAYLABELS, TODAYS_DATE, LIST_OF_BUTTONS
    forward_backward += 1

    if int(current_date[0]) + forward_backward <= 12:
        for lbl in LIST_OF_DAYLABELS:
            lbl[0].place_forget()
            lbl[1].place_forget()
            
        mon = int(current_date[0]) + forward_backward
        new = str(mon)+current_date[1:len(current_date)]
        given = datetime.datetime.strptime(new, "%m %d %Y")

        check = TODAYS_DATE.split(" ")

        place_month(datetime.datetime.now().month + forward_backward, find_day, int(check[2]), DAYS[given.weekday()], given.day - 1)
        button_personalize(LIST_OF_BUTTONS)
        monthlabel.config(text = MONTHS[int(current_date[0]) - 1 + forward_backward])

    else:
        pass

def month_backward(event, current_date):
    global forward_backward, monthlabel, LIST_OF_DAYLABELS, TODAYS_DATE, LIST_OF_BUTTONS
    forward_backward -= 1

    if int(current_date[0]) + forward_backward > 0:
        for lbl in LIST_OF_DAYLABELS:
            lbl[0].place_forget()
            lbl[1].place_forget()
            
        mon = int(current_date[0]) + forward_backward
        new = str(mon)+current_date[1:len(current_date)]
        given = datetime.datetime.strptime(new, "%m %d %Y")

        check = TODAYS_DATE.split(" ")
        
        place_month(datetime.datetime.now().month - forward_backward, find_day, int(check[2]), DAYS[given.weekday()], given.day - 1)
        button_personalize(LIST_OF_BUTTONS)
        monthlabel.config(text = MONTHS[int(current_date[0]) - 1 + forward_backward])

    else:
        pass

upward_downward = 0

def year_forward(event, current_date):
    global upward_downward, yearlabel, LIST_OF_DAYLABELS, LIST_OF_BUTTONS
    check = current_date.split(" ")
    upward_downward += 1

    for lbl in LIST_OF_DAYLABELS:
        lbl[0].place_forget()
        lbl[1].place_forget()

    yr = int(check[2]) + 1
    new = current_date[0:len(current_date) - 4]+str(yr)
    given = datetime.datetime.strptime(new, "%m %d %Y")

    place_month(datetime.datetime.now().month, find_day, datetime.datetime.now().year + upward_downward, DAYS[given.weekday()], given.day - 1)
    button_personalize(LIST_OF_BUTTONS)
    yearlabel.config(text = yr)

def year_backward(event, current_date):
    global upward_downward, yearlabel, LIST_OF_DAYLABELS, LIST_OF_BUTTONS
    check = current_date.split(" ")
    upward_downward -= 1

    for lbl in LIST_OF_DAYLABELS:
        lbl[0].place_forget()
        lbl[1].place_forget()

    yr = int(check[2]) - 1
    new = current_date[0:len(current_date) - 4]+str(yr)
    given = datetime.datetime.strptime(new, "%m %d %Y")

    place_month(datetime.datetime.now().month, find_day, datetime.datetime.now().year + upward_downward, DAYS[given.weekday()], given.day - 1)
    button_personalize(LIST_OF_BUTTONS)
    yearlabel.config(text = yr)

def hover(event, widget):
    widget.config(bd = 3, relief = tkinter.SUNKEN)

def leave(event, widget):
    widget.config(bd = 3, relief = tkinter.RAISED)

def display_stopwatch_counter(labelvar, counter, hours):
    global STATE_OF_STOPWATCH, COUNTER, HOURS
    
    def one_sec(counter2, hours2):
        global COUNTER, HOURS
        
        if STATE_OF_STOPWATCH == True:
            if COUNTER == 0:
                display = "0:00:00"

            elif COUNTER > 0 and COUNTER <= 3599:
                tt = datetime.datetime.fromtimestamp(counter2)
                string = tt.strftime("%M:%S")
                display = str(hours2)+":"+string

            elif COUNTER == 3600:
                COUNTER = 0
                HOURS += 1
                tt = datetime.datetime.fromtimestamp(COUNTER)
                string = tt.strftime("%M:%S")
                display = str(HOURS)+":"+string

            labelvar.config(text = display)

            labelvar.after(1000, lambda: one_sec(COUNTER, HOURS))
            COUNTER += 1

    one_sec(COUNTER, HOURS)

def add_hours_to_day():
    global FOCUS_DAYS, TODAYS_DATE_ACTUAL, COUNTER, HOURS

    FOCUS_DAYS.update([(TODAYS_DATE_ACTUAL, int(FOCUS_DAYS[TODAYS_DATE_ACTUAL]) + HOURS * 3600 + (COUNTER - 1))])
    COUNTER = 0

def change_state(button, stopwatchlabel, add_function):
    global COUNTER, HOURS, STATE_OF_STOPWATCH
    
    if STATE_OF_STOPWATCH == False:
        button.config(text = "Stop focus session")
        STATE_OF_STOPWATCH = True
        display_stopwatch_counter(stopwatchlabel, COUNTER, HOURS)

    elif STATE_OF_STOPWATCH == True:
        STATE_OF_STOPWATCH = False
        display_stopwatch_counter(stopwatchlabel, COUNTER, HOURS)
        button.config(text = "Start focus session")
        add_function()

def show_productivity_graph_for_month():
    global FOCUS_DAYS, TODAYS_DATE_ACTUAL, MONTHS, productivity_manager
    
    productivity_manager.place(relx = 0.5, rely = 0.5, anchor = "center")
    l = TODAYS_DATE_ACTUAL.split(" ")
    
    x_vals = []
    y_vals = []

    for item in FOCUS_DAYS:
        x_vals.append(item)
        y_vals.append(FOCUS_DAYS[item])

    canvas = tkinter.Canvas(productivity_manager, height = productivity_manager.cget("height"), width = productivity_manager.cget("width"))
    canvas.pack()

    canvas.create_text(productivity_manager.cget("width")/2, productivity_manager.cget("height")/9, text = "Productivity graph for " + MONTHS[int(l[0]) - 1], font = ("Helvetica", 25))

    x_axis = canvas.create_line(productivity_manager.cget("width")/8, 4 * (productivity_manager.cget("height")/5), 4 * (productivity_manager.cget("width")/4.5), 4 * (productivity_manager.cget("height")/5), arrow = tkinter.LAST)
    y_axis = canvas.create_line(productivity_manager.cget("width")/8, 4 * (productivity_manager.cget("height")/5), productivity_manager.cget("width")/8, productivity_manager.cget("height")/5, arrow = tkinter.LAST)

    canvas.create_text(productivity_manager.cget("width")/2, 4.2 * (productivity_manager.cget("height")/5), text = "Days", font = ("Helvetica", 10))
    canvas.create_text(productivity_manager.cget("width")/16, productivity_manager.cget("height")/2, text = "Time per day (s)", font = ("Helvetica", 8))

    total_width = int(4 * (productivity_manager.cget("width")/4.5)) - int(productivity_manager.cget("width")/8)
    total_height = int((productivity_manager.cget("height")/5)) - int((4 * (productivity_manager.cget("height")/5)))

    x_values = []
    y_values = []

    x_lines = []
    y_lines = []

    for i in range(int(productivity_manager.cget("width")/8), int(4 * (productivity_manager.cget("width")/4.5)), int(total_width/31)):
        canvas.create_line(i, 4 * (productivity_manager.cget("height")/5) - 5, i, 4 * (productivity_manager.cget("height")/5) + 5)
        x_values.append(i)

    for n in range(int((4 * (productivity_manager.cget("height")/5))), int((productivity_manager.cget("height")/5)), int(total_height/10)):
        canvas.create_line(productivity_manager.cget("width")/8 - 5, n, productivity_manager.cget("width")/8 + 5, n)
        y_values.append(n)

    for day in FOCUS_DAYS:
        canvas.create_rectangle(x_values[x_vals.index(day)], int((4 * (productivity_manager.cget("height")/5))) + ((y_vals[x_vals.index(day)]/36000) * total_height), x_values[x_vals.index(day)] + 5, (int((4 * (productivity_manager.cget("height")/5))) + ((y_vals[x_vals.index(day)]/36000) * total_height)) + 5, fill = "red")

        x_lines.append(x_values[x_vals.index(day)])
        y_lines.append(int((4 * (productivity_manager.cget("height")/5))) + ((y_vals[x_vals.index(day)]/36000) * total_height))

    for i in range(len(x_lines)):
        try:
            canvas.create_line(x_lines[i], y_lines[i], x_lines[i + 1], y_lines[i + 1])
        except IndexError:
            break

    def hover_button(event, widget):
            widget.config(bg = "red")

    def leave_button(event, widget):
        widget.config(bg = "light grey")

    def close(manager):
            global EVENT_OPEN_BOOL
            
            for child_widget in manager.winfo_children():
                child_widget.destroy()
                
            manager.place_forget()
            EVENT_OPEN_BOOL = False

    exit_button = tkinter.Button(productivity_manager, text = "X", bg = "light grey", border = 1, borderwidth = 1, highlightthickness = 1, highlightcolor = "black", highlightbackground = "black", relief = tkinter.FLAT, padx = 7)
    exit_button.place(relx = 0.96, rely = 0.0005)

    exit_button.bind("<Enter>", lambda x: hover_button("<Enter>", exit_button))
    exit_button.bind("<Leave>", lambda x: leave_button("<Leave>", exit_button))

    exit_button.config(command = lambda: close(productivity_manager))

start_focus_button = tkinter.Button(window, text = "Start focus session", command = lambda: change_state(start_focus_button, stopwatchlabel, add_hours_to_day))
start_focus_button.place(relx = 0.81, rely = 0.14)

display_stopwatch_counter(stopwatchlabel, COUNTER, HOURS)

show_button = tkinter.Button(window, text = "Show productivity graph for this month", command = show_productivity_graph_for_month)
show_button.place(relx = 0.59, rely = 0.12)

rightbutton.bind("<Button - 1>", lambda x: month_forward("<Button - 1>", TODAYS_DATE))
leftbutton.bind("<Button - 1>", lambda x: month_backward("<Button - 1>", TODAYS_DATE))
yearleft.bind("<Button - 1>", lambda x: year_backward("<Button - 1>", TODAYS_DATE))
yearright.bind("<Button - 1>", lambda x: year_forward("<Button - 1>", TODAYS_DATE))

# decorative button animations and shit

rightbutton.bind("<Enter>", lambda x: hover("<Enter>", rightbutton))
leftbutton.bind("<Enter>", lambda x: hover("<Enter>", leftbutton))
yearleft.bind("<Enter>", lambda x: hover("<Enter>", yearleft))
yearright.bind("<Enter>", lambda x: hover("<Enter>", yearright))

rightbutton.bind("<Leave>", lambda x: leave("<Leave>", rightbutton))
leftbutton.bind("<Leave>", lambda x: leave("<Leave>", leftbutton))
yearleft.bind("<Leave>", lambda x: leave("<Leave>", yearleft))
yearright.bind("<Leave>", lambda x: leave("<Leave>", yearright))

window.mainloop()
