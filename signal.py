from tkinter import *
from threading import Thread 
import time

root = Tk()
root.geometry('1378x968')
root.title("Signal")

# PL | ################### ŚCIEŻKI DO OBRAZÓW ####################
# EN | ################### IMAGE PATHS ####################

# PL | sygnały
# EN | signals

signal_dark = PhotoImage(file = "img\signals\dark.png")
signal_s1 = PhotoImage(file = "img\signals\s1.png")
signal_s2 = PhotoImage(file = "img\signals\s2.png")
signal_s5 = PhotoImage(file = "img\signals\s5.png")
signal_s6 = PhotoImage(file = "img\signals\s6.png")
signal_s8 = PhotoImage(file = "img\signals\s8.png")
signal_s9 = PhotoImage(file = "img\signals\s9.png")
signal_s10 = PhotoImage(file = "img\signals\s10.png")
signal_s11 = PhotoImage(file = "img\signals\s11.png")
signal_s13 = PhotoImage(file = "img\signals\s13.png")
signal_s10a = PhotoImage(file = "img\signals\s10a.png")
signal_s11a = PhotoImage(file = "img\signals\s11a.png")
signal_s13a = PhotoImage(file = "img\signals\s13a.png")
signal_sz = PhotoImage(file = "img\signals\sz.png")
signal_w24_dark = PhotoImage(file = "img\signals\w24_dark.png")
signal_w24 = PhotoImage(file = "img\signals\w24.png")

# PL | przebiegi
# EN | routes

route_A1_default = PhotoImage(file = "img\POC\A1_default.png")
route_A2_default = PhotoImage(file = "img\POC\A2_default.png")
route_B1_default = PhotoImage(file = "img\POC\B1_default.png")
route_B2_default = PhotoImage(file = "img\POC\B2_default.png")
route_A1_track_1 = PhotoImage(file = "img\POC\A1_track_1.png")
route_A1_track_2 = PhotoImage(file = "img\POC\A1_track_2.png")
route_A1_track_4 = PhotoImage(file = "img\POC\A1_track_4.png")
route_A1_track_6 = PhotoImage(file = "img\POC\A1_track_6.png")
route_A2_track_1_1 = PhotoImage(file = "img\POC\A2_track_1_1.png")
route_A2_track_1_2 = PhotoImage(file = "img\POC\A2_track_1_2.png")
route_A2_track_2_1 = PhotoImage(file = "img\POC\A2_track_2_1.png")
route_A2_track_2_2 = PhotoImage(file = "img\POC\A2_track_2_2.png")
route_B1_track_1 = PhotoImage(file = "img\POC\B1_track_1.png")
route_B1_track_2 = PhotoImage(file = "img\POC\B1_track_2.png")
route_B1_track_1_2 = PhotoImage(file = "img\POC\B1_track_1_2.png")
route_B1_track_2_1 = PhotoImage(file = "img\POC\B1_track_2_1.png")
route_B2_track_1 = PhotoImage(file = "img\POC\B2_track_1.png")
route_B2_track_2 = PhotoImage(file = "img\POC\B2_track_2.png")
route_B2_track_4 = PhotoImage(file = "img\POC\B2_track_4.png")
route_B2_track_6 = PhotoImage(file = "img\POC\B2_track_6.png")
route_A1_sz_1 = PhotoImage(file = "img\POC\A1_sz_1.png")
route_A1_sz_2 = PhotoImage(file = "img\POC\A1_sz_2.png")
route_A1_dark_1 = PhotoImage(file = "img\POC\A1_dark_1.png")
route_A1_dark_2 = PhotoImage(file = "img\POC\A1_dark_2.png")

# PL | ################### DEFINICJE PRZYCISKÓW I POLECEŃ ####################
# EN | ################### BUTTONS DEFINITIONS AND COMMANDS ####################

# PL | sygnały
# EN | signals

button_s2 = Button(root, text = "S2", bg = "lightgrey", state = NORMAL, command=lambda:[start_s2()])
button_s2.place(x=490, y=20)

button_s3 = Button(root, text = "S3", bg = "lightgrey", state = NORMAL, command=lambda:[init_loop_s3()])
button_s3.place(x=490, y=50)

button_s4 = Button(root, text = "S4", bg = "lightgrey", state = NORMAL, command=lambda:[init_loop_s4()])
button_s4.place(x=490, y=80)

button_s5 = Button(root, text = "S5", bg = "lightgrey", state = NORMAL, command=lambda:[start_s5()])
button_s5.place(x=490, y=110)

button_s6 = Button(root, text = "S6", bg = "lightgrey", state = NORMAL, command=lambda:[start_s6()])
button_s6.place(x=490, y=140)

button_s7 = Button(root, text = "S7", bg = "lightgrey", state = NORMAL, command=lambda:[init_loop_s7()])
button_s7.place(x=490, y=170)

button_s8 = Button(root, text = "S8", bg = "lightgrey", state = NORMAL, command=lambda:[init_loop_s8()])
button_s8.place(x=490, y=200)

button_s9 = Button(root, text = "S9", bg = "lightgrey", state = NORMAL, command=lambda:[start_s9()])
button_s9.place(x=490, y=230)

button_s10 = Button(root, text = "S10", bg = "lightgrey", state = NORMAL, command=lambda:[start_s10()])
button_s10.place(x=490, y=260)

button_s11 = Button(root, text = "S11", bg = "lightgrey", state = NORMAL, command=lambda:[init_loop_s11()])
button_s11.place(x=490, y=290)

button_s12 = Button(root, text = "S12", bg = "lightgrey", state = NORMAL, command=lambda:[init_loop_s12()])
button_s12.place(x=490, y=320)

button_s13 = Button(root, text = "S13", bg = "lightgrey", state = NORMAL, command=lambda:[start_s13()])
button_s13.place(x=490, y=350)

button_s10a = Button(root, text = "S10a", bg = "lightgrey", state = NORMAL, command=lambda:[start_s10a()])
button_s10a.place(x=490, y=380)

button_s11a = Button(root, text = "S11a", bg = "lightgrey", state = NORMAL, command=lambda:[init_loop_s11a()])
button_s11a.place(x=490, y=410)

button_s12a = Button(root, text = "S12a", bg = "lightgrey", state = NORMAL, command=lambda:[init_loop_s12a()])
button_s12a.place(x=490, y=440)

button_s13a = Button(root, text = "S13a", bg = "lightgrey", state = NORMAL, command=lambda:[start_s13a()])
button_s13a.place(x=490, y=470)

button_sz = Button(root, text = "Call-on signal", bg = "lightgrey", height= 1, width=14, state = NORMAL, command=lambda:[init_loop_sz(), init_loop_counter_sz()])
button_sz.place(x=1065, y=20)

button_s1_failure = Button(root, text = "S1 bulb failure", bg = "lightgrey", height= 1, width=14, state = NORMAL, command=lambda:[init_loop_signal_dark(), set_route_disabled()])
button_s1_failure.place(x=1065, y=50)

button_s1 = Button(root, text = "STOP", bg = "red", state = DISABLED, command=lambda:[stop_loop(), release_route()])
button_s1.place(x=540, y=20)

button_stop_sz = Button(root, text = "STOP", bg = "red", state = DISABLED, command=lambda:[stop_loop_sz(), stop_loop_counter_sz()])
button_stop_sz.place(x=1200, y=20)

button_stop_s1_failure = Button(root, text = "STOP", bg = "red", state = DISABLED, command=lambda:[stop_loop_dark()])
button_stop_s1_failure.place(x=1200, y=50)

# PL | przebiegi
# EN | routes

button_A = Button(root, text = "A", bg = "lightgrey", height= 1, width=2, state = NORMAL, command=lambda:[button_A_clicked()])
button_A.place(x=685, y=20)

button_B = Button(root, text = "B", bg = "lightgrey", height= 1, width=2, state = NORMAL, command=lambda:[button_B_clicked()])
button_B.place(x=685, y=50)

button_C = Button(root, text = "C", bg = "lightgrey", height= 1, width=2, state = NORMAL, command=lambda:[button_C_clicked()])
button_C.place(x=685, y=80)

button_D = Button(root, text = "D", bg = "lightgrey", height= 1, width=2, state = NORMAL, command=lambda:[button_D_clicked()])
button_D.place(x=685, y=110)

button_E = Button(root, text = "E", bg = "lightgrey", height= 1, width=2, state = DISABLED, command=lambda:[button_E_clicked()])
button_E.place(x=735, y=20)

button_F = Button(root, text = "F", bg = "lightgrey", height= 1, width=2, state = DISABLED, command=lambda:[button_F_clicked()])
button_F.place(x=735, y=50)

button_G = Button(root, text = "G", bg = "lightgrey", height= 1, width=2, state = DISABLED, command=lambda:[button_G_clicked()])
button_G.place(x=785, y=20)

button_H = Button(root, text = "H", bg = "lightgrey", height= 1, width=2, state = DISABLED, command=lambda:[button_H_clicked()])
button_H.place(x=785, y=50)

button_J = Button(root, text = "J", bg = "lightgrey", height= 1, width=2, state = DISABLED, command=lambda:[button_J_clicked()])
button_J.place(x=785, y=80)

button_K = Button(root, text = "K", bg = "lightgrey", height= 1, width=2, state = DISABLED, command=lambda:[button_K_clicked()])
button_K.place(x=785, y=110)

button_set_route = Button(root, text = "Set route", height= 1, width=14, bg = "lightgrey", state = DISABLED, command=lambda:[set_route_index(), draw_signal()])
button_set_route.place(x=840, y=20)

button_release_route = Button(root, text = "Release route", height= 1, width=14, bg = "lightgrey", state = DISABLED, command=lambda:[release_route(), stop_loop()])
button_release_route.place(x=840, y=50)

# PL | ################### POCZĄTKOWE WARTOŚCI ZMIENNYCH GLOBALNYCH - INEKS PRZEBIEGU ####################
# EN | ################### INIT GLOBAL VARIABLES - ROUTE INDEX ####################

global r1
global r2
global r3

r1 = 0
r2 = 0
r3 = 0

# PL | ################### DEFINICJE FUNKCJI - GLOBALNE WŁAŚCIWOŚCI PRZYCISKÓW ####################
# EN | ################### FUNCTIONS DEFINITIONS - GLOBAL BUTTONS PROPERTIES  ####################

def buttons_disabled():
    button_s2["state"] = DISABLED
    button_s2["bg"] = "lightgrey"
    button_s3["state"] = DISABLED
    button_s3["bg"] = "lightgrey"
    button_s4["state"] = DISABLED
    button_s4["bg"] = "lightgrey"
    button_s5["state"] = DISABLED
    button_s5["bg"] = "lightgrey"
    button_s6["state"] = DISABLED
    button_s6["bg"] = "lightgrey"
    button_s7["state"] = DISABLED
    button_s7["bg"] = "lightgrey"
    button_s8["state"] = DISABLED
    button_s8["bg"] = "lightgrey"
    button_s9["state"] = DISABLED
    button_s9["bg"] = "lightgrey"
    button_s10["state"] = DISABLED
    button_s10["bg"] = "lightgrey"
    button_s11["state"] = DISABLED
    button_s11["bg"] = "lightgrey"
    button_s12["state"] = DISABLED
    button_s12["bg"] = "lightgrey"
    button_s13["state"] = DISABLED
    button_s13["bg"] = "lightgrey"
    button_s10a["state"] = DISABLED
    button_s10a["bg"] = "lightgrey"
    button_s11a["state"] = DISABLED
    button_s11a["bg"] = "lightgrey"
    button_s12a["state"] = DISABLED
    button_s12a["bg"] = "lightgrey"
    button_s13a["state"] = DISABLED
    button_s13a["bg"] = "lightgrey"
    button_sz["state"] = DISABLED
    button_sz["bg"] = "lightgrey"
    button_s1["bg"] = "lightgrey"
    button_s1["state"] = NORMAL

def buttons_enabled():
    button_s2["bg"] = "lightgrey"
    button_s2["state"] = NORMAL
    button_s3["bg"] = "lightgrey"
    button_s3["state"] = NORMAL
    button_s4["bg"] = "lightgrey"
    button_s4["state"] = NORMAL
    button_s5["bg"] = "lightgrey"
    button_s5["state"] = NORMAL
    button_s6["bg"] = "lightgrey"
    button_s6["state"] = NORMAL
    button_s7["bg"] = "lightgrey"
    button_s7["state"] = NORMAL
    button_s8["bg"] = "lightgrey"
    button_s8["state"] = NORMAL
    button_s9["bg"] = "lightgrey"
    button_s9["state"] = NORMAL
    button_s10["state"] = NORMAL
    button_s10["bg"] = "lightgrey"
    button_s11["state"] = NORMAL
    button_s11["bg"] = "lightgrey"
    button_s12["state"] = NORMAL
    button_s12["bg"] = "lightgrey"
    button_s13["state"] = NORMAL
    button_s13["bg"] = "lightgrey"
    button_s10a["state"] = NORMAL
    button_s10a["bg"] = "lightgrey"
    button_s11a["state"] = NORMAL
    button_s11a["bg"] = "lightgrey"
    button_s12a["state"] = NORMAL
    button_s12a["bg"] = "lightgrey"
    button_s13a["state"] = NORMAL
    button_s13a["bg"] = "lightgrey"
    button_sz["state"] = NORMAL
    button_sz["bg"] = "lightgrey"

# PL | ################### DEFINICJE FUNKCJI - RYSOWANIE OBRAZÓW SYGNAŁÓW ####################
# EN | ################### FUNCTIONS DEFINITIONS - SIGNALS IMAGES DRAWING  ####################

def draw_signal_dark():
    label = Label(root, image=signal_dark)
    label.place(x=0, y=0)

def draw_s1():
    label = Label(root, image=signal_s1)
    label.place(x=0, y=0)

def draw_s2():
    label = Label(root, image=signal_s2)
    label.place(x=0, y=0)

def draw_s3():
    label = Label(root, image=signal_s2)
    label.place(x=0, y=0)

def draw_s4():
    label = Label(root, image=signal_s5)
    label.place(x=0, y=0)

def draw_s5():
    label = Label(root, image=signal_s5)
    label.place(x=0, y=0)

def draw_s6():
    label = Label(root, image=signal_s6)
    label.place(x=0, y=0)

def draw_s7():
    label = Label(root, image=signal_s8)
    label.place(x=0, y=0)

def draw_s8():
    label = Label(root, image=signal_s8)
    label.place(x=0, y=0)

def draw_s9():
    label = Label(root, image=signal_s9)
    label.place(x=0, y=0)

def draw_s10():
    label = Label(root, image=signal_s10)
    label.place(x=0, y=0)

def draw_s11():
    label = Label(root, image=signal_s11)
    label.place(x=0, y=0)

def draw_s12():
    label = Label(root, image=signal_s11)
    label.place(x=0, y=0)

def draw_s13():
    label = Label(root, image=signal_s13)
    label.place(x=0, y=0)

def draw_s10a():
    label = Label(root, image=signal_s10a)
    label.place(x=0, y=0)

def draw_s11a():
    label = Label(root, image=signal_s11a)
    label.place(x=0, y=0)

def draw_s12a():
    label = Label(root, image=signal_s11a)
    label.place(x=0, y=0)

def draw_s13a():
    label = Label(root, image=signal_s13a)
    label.place(x=0, y=0)

def draw_sz():
    label = Label(root, image=signal_sz)
    label.place(x=0, y=0)

def draw_signal_w24_dark():
    label = Label(root, image = signal_w24_dark)
    label.place(x=0, y=438)

def draw_signal_w24():
    label = Label(root, image = signal_w24)
    label.place(x=0, y=438)

# PL | ################### DEFINICJE FUNKCJI - RYSOWANIE OBRAZÓW PRZEBIEGÓW ####################
# EN | ################### FUNCTIONS DEFINITIONS - ROUTES IMAGES DRAWING  ####################

def draw_A1_default():
    label = Label(root, image = route_A1_default)
    label.place(x=0, y=554)

def draw_A2_default():
    label = Label(root, image = route_A2_default)
    label.place(x=225, y=554)

def draw_B1_default():
    label = Label(root, image = route_B1_default)
    label.place(x=703, y=554)

def draw_B2_default():
    label = Label(root, image = route_B2_default)
    label.place(x=950, y=554)

def draw_A1_track_1():
    label = Label(root, image = route_A1_track_1)
    label.place(x=0, y=554)

def draw_A1_track_2():
    label = Label(root, image = route_A1_track_2)
    label.place(x=0, y=554)

def draw_A1_track_4():
    label = Label(root, image = route_A1_track_4)
    label.place(x=0, y=554)

def draw_A1_track_6():
    label = Label(root, image = route_A1_track_6)
    label.place(x=0, y=554)

def draw_A2_track_1_1():
    label = Label(root, image = route_A2_track_1_1)
    label.place(x=225, y=554)

def draw_A2_track_1_2():
    label = Label(root, image = route_A2_track_1_2)
    label.place(x=225, y=554)

def draw_A2_track_2_1():
    label = Label(root, image = route_A2_track_2_1)
    label.place(x=225, y=554)

def draw_A2_track_2_2():
    label = Label(root, image = route_A2_track_2_2)
    label.place(x=225, y=554)

def draw_B1_track_1():
    label = Label(root, image = route_B1_track_1)
    label.place(x=703, y=554)

def draw_B1_track_2():
    label = Label(root, image = route_B1_track_2)
    label.place(x=703, y=554)

def draw_B1_track_1_2():
    label = Label(root, image = route_B1_track_1_2)
    label.place(x=703, y=554)

def draw_B1_track_2_1():
    label = Label(root, image = route_B1_track_2_1)
    label.place(x=703, y=554)

def draw_B2_track_1():
    label = Label(root, image = route_B2_track_1)
    label.place(x=950, y=554)

def draw_B2_track_2():
    label = Label(root, image = route_B2_track_2)
    label.place(x=950, y=554)

def draw_B2_track_4():
    label = Label(root, image = route_B2_track_4)
    label.place(x=950, y=554)

def draw_B2_track_6():
    label = Label(root, image = route_B2_track_6)
    label.place(x=950, y=554)

def draw_route_sz_1():
    label = Label(root, image = route_A1_sz_1)
    label.place(x=0, y=554)

def draw_route_sz_2():
    label = Label(root, image = route_A1_sz_2)
    label.place(x=0, y=554)

def draw_route_dark_1():
    label = Label(root, image = route_A1_dark_1)
    label.place(x=0, y=554)

def draw_route_dark_2():
    label = Label(root, image = route_A1_dark_2)
    label.place(x=0, y=554)

# PL | ################### DEFINICJE FUNKCJI - URUCHAMIANIE PĘTLI DLA SYGNAŁÓW MIGOWYCH ####################
# EN | ################### FUNCTIONS DEFINITIONS - LOOPS INIT FOR BLINK SIGNALS  ####################

# PL | pętla (While True) uruchamiana jest jako niezależny wątek działacy w tle dla sygnałów migowych
# EN | a loop (While True) runs as a separate background thread for blink signals

def init_loop_s3():
    t = Thread(target=start_loop_s3)
    t.start()

def init_loop_s4():
    t = Thread(target=start_loop_s4)
    t.start()

def init_loop_s7():
    t = Thread(target=start_loop_s7)
    t.start()

def init_loop_s8():
    t = Thread(target=start_loop_s8)
    t.start()

def init_loop_s11():
    t = Thread(target=start_loop_s11)
    t.start()

def init_loop_s12():
    t = Thread(target=start_loop_s12)
    t.start()

def init_loop_s11a():
    t = Thread(target=start_loop_s11a)
    t.start()

def init_loop_s12a():
    t = Thread(target=start_loop_s12a)
    t.start()

def init_loop_sz():
    t = Thread(target=start_loop_sz)
    t.start()

def init_loop_counter_sz():
    t = Thread(target=start_loop_counter_sz)
    t.start()

def init_loop_signal_dark():
    t = Thread(target=start_loop_dark)
    t.start()

# PL | ################### DEFINICJE FUNKCJI - URUCHAMIANIE SYGNAŁÓW ####################
# EN | ################### FUNCTIONS DEFINITIONS - SIGNALS INIT ####################

def start_s2():
    draw_s2()
    text_s2()
    set_route_disabled_if_not_set()
    buttons_disabled()
    button_s2["state"] = NORMAL
    button_s2["bg"] = "green"

# PL | pętla (While True) uruchamiana jest gdy zmienna globalna 'stop' zmieni wartość na False. Pętla uruchamia na przemian dwa obrazy.
# PL | Po zmianie wartości na True, sprawdzany jest dodatkowy warunek - jeśli zmienna globalna 'stop_dark' ma wartość True (brak uszkodzenia
# PL | żarówki S1), to zmień sygnał na S1. Jeśli nie, to rozpocznij pętle dla sygnału ciemnego. Zapobiega to dodatkowemu wyświetleniu 
# PL | sygnału S1 po wystąpieniu usterki w trakcie wyświetlania sygnału.
# EN | a loop (While True) starts when global variable 'stop' change its value to False. The loop displays alternately two images. 
# EN | After the variable has changed its value to True, addtional condition is checked - if global variable 'stop_dark' has value True 
# EN | (S1 signal is not failed), then change signal to S1. If not, then starts loop for dark signal. It prevents displaying addtional S1 signal
# EN | after S1 signal has failed during displaying other signal.

def start_loop_s3():
    text_s3()
    set_route_disabled_if_not_set()
    buttons_disabled()
    button_s3["state"] = NORMAL
    button_s3["bg"] = "green"
    global stop
    global stop_dark
    stop = False
    stop_dark = True
    while stop == False:
        draw_signal_dark()
        time.sleep(0.6)
        draw_s3()
        time.sleep(0.6)
    else:
        if stop_dark == True:
            draw_s1()
        else:
            start_loop_dark()

def start_loop_s4():
    text_s4()
    set_route_disabled_if_not_set()
    buttons_disabled()
    button_s4["state"] = NORMAL
    button_s4["bg"] = "green"
    global stop
    global stop_dark
    stop = False
    stop_dark = True
    while stop == False:
        draw_signal_dark()
        time.sleep(0.6)
        draw_s4()
        time.sleep(0.6)
    else:
        if stop_dark == True:
            draw_s1()
        else:
            start_loop_dark()

def start_s5():
    draw_s5()
    text_s5()
    set_route_disabled_if_not_set()
    buttons_disabled()
    button_s5["state"] = NORMAL
    button_s5["bg"] = "green"

def start_s6():
    draw_s6()
    text_s6()
    set_route_disabled_if_not_set()
    buttons_disabled()
    button_s6["state"] = NORMAL
    button_s6["bg"] = "green"
       
def start_loop_s7():
    text_s7()
    set_route_disabled_if_not_set()
    buttons_disabled()
    button_s7["state"] = NORMAL
    button_s7["bg"] = "green"
    global stop
    global stop_dark
    stop = False
    stop_dark = True
    while stop == False:
        draw_s6()
        time.sleep(0.6)
        draw_s7()
        time.sleep(0.6)
    else:
        if stop_dark == True:
            draw_s1()
        else:
            start_loop_dark()

def start_loop_s8():
    text_s8()
    set_route_disabled_if_not_set()
    buttons_disabled()
    button_s8["state"] = NORMAL
    button_s8["bg"] = "green"
    global stop
    global stop_dark
    stop = False
    stop_dark = True
    while stop == False:
        draw_s9()
        time.sleep(0.6)
        draw_s8()
        time.sleep(0.6)
    else:
        if stop_dark == True:
            draw_s1()
        else:
            start_loop_dark()
    
def start_s9():
    draw_s9()
    text_s9()
    set_route_disabled_if_not_set()
    buttons_disabled()
    button_s9["state"] = NORMAL
    button_s9["bg"] = "green"
    
def start_s10():
    draw_s10()
    text_s10()
    set_route_disabled_if_not_set()
    buttons_disabled()
    button_s10["state"] = NORMAL
    button_s10["bg"] = "green"
        
def start_loop_s11():
    text_s11()
    set_route_disabled_if_not_set()
    buttons_disabled()
    button_s11["state"] = NORMAL
    button_s11["bg"] = "green"
    global stop
    global stop_dark
    stop = False
    stop_dark = True
    while stop == False:
        draw_s10()
        time.sleep(0.6)
        draw_s11()
        time.sleep(0.6)
    else:
        if stop_dark == True:
            draw_s1()
        else:
            start_loop_dark()

def start_loop_s12():
    text_s12()
    set_route_disabled_if_not_set()
    buttons_disabled()
    button_s12["state"] = NORMAL
    button_s12["bg"] = "green"
    global stop
    global stop_dark
    stop = False
    stop_dark = True
    while stop == False:
        draw_s13()
        time.sleep(0.6)
        draw_s12()
        time.sleep(0.6)
    else:
        if stop_dark == True:
            draw_s1()
        else:
            start_loop_dark()
    
def start_s13():
    draw_s13()
    text_s13()
    set_route_disabled_if_not_set()
    buttons_disabled()
    button_s13["state"] = NORMAL
    button_s13["bg"] = "green"
       
def start_s10a():
    text_s10a()
    draw_s10a()
    set_route_disabled_if_not_set()
    buttons_disabled()
    button_s10a["state"] = NORMAL
    button_s10a["bg"] = "green"
    
def start_loop_s11a():
    text_s11a()
    set_route_disabled_if_not_set()
    buttons_disabled()
    button_s11a["state"] = NORMAL
    button_s11a["bg"] = "green"
    global stop
    global stop_dark
    stop = False
    stop_dark = True
    while stop == False:
        draw_s10a()
        time.sleep(0.6)
        draw_s11a()
        time.sleep(0.6)
    else:
        if stop_dark == True:
            draw_s1()
        else:
            start_loop_dark()

def start_loop_s12a():
    text_s12a()
    set_route_disabled_if_not_set()
    buttons_disabled()
    button_s12a["state"] = NORMAL
    button_s12a["bg"] = "green"
    global stop
    global stop_dark
    stop = False
    stop_dark = True
    while stop == False:
        draw_s13a()
        time.sleep(0.6)
        draw_s12a()
        time.sleep(0.6)
    else:
        if stop_dark == True:
            draw_s1()
        else:
            start_loop_dark()
    
def start_s13a():
    draw_s13a()
    text_s13a()
    set_route_disabled_if_not_set()
    buttons_disabled()
    button_s13a["state"] = NORMAL
    button_s13a["bg"] = "green"

def start_loop_sz():
    set_route_disabled_if_not_set()
    buttons_disabled()
    button_sz["bg"] = "green"
    button_stop_sz["bg"] = "lightgrey"
    button_s1["bg"] = "lightgrey"
    button_s1["state"] = DISABLED
    button_stop_sz["state"] = NORMAL
    global stop
    global stop_sz
    global stop_dark
    stop = True
    stop_sz = False
    stop_dark = True
    while stop_sz == False:
        draw_sz()
        draw_route_sz_1()
        time.sleep(0.6)
        draw_s1()
        draw_route_sz_2()
        time.sleep(0.6)
    else:
        if stop_dark == True:
            draw_s1()
            draw_A1_default()
        else:
            start_loop_dark()

# PL | sygnał zastępczy powinien wygasnąć po 90s od zainicjowania. Funkcja odlicza 90s i zmienia sygnał na S1. 
# EN | call-on signal should stop after 90s since it has been initiated. The function counts from 90s and change signal do S1. 

def start_loop_counter_sz():
    global licznik_sz
    global stop_counter_sz
    global stop_dark
    stop_counter_sz = False
    licznik_sz = 90
    stop_dark = True
    while stop_counter_sz == False and licznik_sz > 1:
        licznik_sz = licznik_sz - 1
        text_sz_licznik()
        time.sleep(1)
    else:
        if stop_dark == True:
            stop_loop_sz()
        else:
            start_loop_dark()

def start_loop_dark():
    buttons_disabled()
    button_s1_failure["bg"] = "green"
    button_s1_failure["state"] = DISABLED
    button_stop_s1_failure["bg"] = "lightgrey"
    button_stop_s1_failure["state"] = NORMAL
    button_s1["bg"] = "lightgrey"
    button_s1["state"] = DISABLED
    button_stop_sz["state"] = DISABLED
    button_stop_sz["bg"] = "red"
    button_set_route["state"] == DISABLED
    global stop
    global stop_sz
    global stop_counter_sz
    global stop_dark
    stop = True
    stop_sz = True
    stop_counter_sz = True
    stop_dark = False
    while stop_dark == False:
        draw_signal_dark()
        draw_route_dark_1()
        text_usterka_s1_on()
        time.sleep(0.6)
        draw_route_dark_2()
        text_usterka_s1_off()
        time.sleep(0.6)
    else:
        draw_s1()
        draw_A1_default()
        text_s1()

# PL | ################### DEFINICJE FUNKCJI - WYGASZANIE SYGNAŁÓW ####################
# EN | ################### FUNCTIONS DEFINITIONS - SIGNALS STOPPING ####################

def stop_loop():
    text_s1()
    draw_s1()
    release_route()
    buttons_enabled()
    button_s1["bg"] = "red"
    button_s1["state"] = DISABLED
    global stop
    stop = True

def stop_loop_sz():
    text_s1()
    release_route()
    buttons_enabled()
    button_sz["bg"] = "lightgrey"
    button_stop_sz["bg"] = "red"
    button_s1["bg"] = "red"
    button_stop_sz["state"] = DISABLED
    global stop_sz
    stop_sz = True

def stop_loop_counter_sz():
    global stop_counter_sz
    stop_counter_sz = True

def stop_loop_dark():
    text_s1()
    release_route()
    buttons_enabled()
    button_s1_failure["bg"] = "lightgrey"
    button_s1_failure["state"] = NORMAL
    button_stop_s1_failure["bg"] = "red"
    button_stop_s1_failure["state"] = DISABLED
    button_s1["bg"] = "red"
    button_s1["state"] = DISABLED
    button_stop_sz["bg"] = "red"
    button_stop_sz["state"] = DISABLED
    button_sz["state"] = NORMAL
    button_sz["bg"] = "lightgrey"
    button_set_route["state"] == NORMAL
    global stop_alarm
    stop_alarm = True
    global stop_dark
    stop_dark = True

# PL | ################### DEFINICJE FUNKCJI - PRZYCISKI DO DEFINIOWANIA DROGI PRZEBIEGU ####################
# EN | ################### FUNCTIONS DEFINITIONS - BUTTONS FOR ROUTES DEFINING ####################

# PL | do grupy semaforów A, B, C, D przypisana jest zmienna globalna r1, do semaforów E i F - r2, a do grupy semaforów G, H, J, K - r3
# PL | wybranie sekwencji danych semaforów powodouje utworzenie 3-cyfrowego inkesu przebiegu (funkcja set_route_index)
# EN | for signals grup A, B, C, D, r1 global variale is assigned, for signal E and F - r2, for signals grup G, H, J, K - r3
# EN | selectng a given signals sequence, creates a 3-digits route index (set_route_index function)

def button_A_clicked():
    button_A["state"] == NORMAL
    button_A["bg"] = "green"
    button_B["state"] = DISABLED
    button_C["state"] = DISABLED
    button_D["state"] = DISABLED
    button_E["state"] = NORMAL
    button_F["state"] = NORMAL
    global r1
    r1 = 1
       
def button_B_clicked():
    button_B["state"] == NORMAL
    button_B["bg"] = "green"
    button_A["state"] = DISABLED
    button_C["state"] = DISABLED
    button_D["state"] = DISABLED
    button_E["state"] = NORMAL
    button_F["state"] = NORMAL
    global r1
    r1 = 2

def button_C_clicked():
    button_C["state"] == NORMAL
    button_C["bg"] = "green"
    button_A["state"] = DISABLED
    button_B["state"] = DISABLED
    button_D["state"] = DISABLED
    button_E["state"] = NORMAL
    button_F["state"] = NORMAL
    global r1
    r1 = 4

def button_D_clicked():
    button_D["state"] == NORMAL
    button_D["bg"] = "green"
    button_A["state"] = DISABLED
    button_B["state"] = DISABLED
    button_C["state"] = DISABLED
    button_E["state"] = NORMAL
    button_F["state"] = NORMAL
    global r1
    r1 = 6

def button_E_clicked():
    button_E["state"] = NORMAL
    button_E["bg"] = "green"
    button_F["state"] = DISABLED
    button_G["state"] = NORMAL
    button_H["state"] = NORMAL
    button_J["state"] = NORMAL
    button_K["state"] = NORMAL
    button_set_route["state"] = NORMAL
    global r2
    r2 = 1

def button_F_clicked():
    button_F["state"] == NORMAL
    button_F["bg"] = "green"
    button_E["state"] = DISABLED
    button_G["state"] = NORMAL
    button_H["state"] = NORMAL
    button_J["state"] = NORMAL
    button_K["state"] = NORMAL
    button_set_route["state"] = NORMAL
    global r2
    r2 = 2

def button_G_clicked():
    button_G["state"] == NORMAL
    button_G["bg"] = "green"
    button_H["state"] = DISABLED
    button_J["state"] = DISABLED
    button_K["state"] = DISABLED
    global r3
    r3 = 1

def button_H_clicked():
    button_H["state"] == NORMAL
    button_H["bg"] = "green"
    button_G["state"] = DISABLED
    button_J["state"] = DISABLED
    button_K["state"] = DISABLED
    global r3
    r3 = 2

def button_J_clicked():
    button_J["state"] == NORMAL
    button_J["bg"] = "green"
    button_G["state"] = DISABLED
    button_H["state"] = DISABLED
    button_K["state"] = DISABLED
    global r3
    r3 = 4

def button_K_clicked():
    button_K["state"] == NORMAL
    button_K["bg"] = "green"
    button_G["state"] = DISABLED
    button_H["state"] = DISABLED
    button_J["state"] = DISABLED
    global r3
    r3 = 6
 
# PL | do grupy semaforów A, B, C, D przypisana jest zmienna globalna r1, do semaforów E i F - r2, a do grupy semaforów G, H, J, K - r3
# PL | wybranie sekwencji danych semaforów powodouje utworzenie 3-cyfrowego inkesu przebiegu (funkcja set_route_index)
# EN | for signals grup A, B, C, D, r1 global variale is assigned, for signal E and F - r2, for signals grup G, H, J, K - r3
# EN | selectng a given signals sequence, creates a 3-digits route index (set_route_index function)

def set_route_index():
    button_set_route["state"] = DISABLED
    button_release_route["state"] = NORMAL
    global route_index
    global r1
    global r2
    global r3
    r1_str = str(r1)
    r2_str = str(r2)
    r3_str = str(r3)
    r_str = r1_str + r2_str + r3_str
    route_index = int(r_str)

# PL | funkcja zmienia indeks przebiegu do 000
# EN | changing route index value to default 000

def release_route():
    button_set_route["state"] = DISABLED
    button_release_route["state"] = DISABLED
    button_A["state"] = NORMAL
    button_A["bg"] = "lightgrey"
    button_B["state"] = NORMAL
    button_B["bg"] = "lightgrey"
    button_C["state"] = NORMAL
    button_C["bg"] = "lightgrey"
    button_D["state"] = NORMAL
    button_D["bg"] = "lightgrey"
    button_E["state"] = DISABLED
    button_E["bg"] = "lightgrey"
    button_F["state"] = DISABLED
    button_F["bg"] = "lightgrey"
    button_G["state"] = DISABLED
    button_G["bg"] = "lightgrey"
    button_H["state"] = DISABLED
    button_H["bg"] = "lightgrey"
    button_J["state"] = DISABLED
    button_J["bg"] = "lightgrey"
    button_K["state"] = DISABLED
    button_K["bg"] = "lightgrey"
    global r1
    r1 = 0
    global r2   
    r2 = 0
    global r3
    r3 = 0
    draw_A1_default()
    draw_A2_default()
    draw_B1_default()
    draw_B2_default()
    draw_signal_w24_dark()

def set_route_disabled():
    button_A["state"] = DISABLED
    button_A["bg"] = "lightgrey"
    button_B["state"] = DISABLED
    button_B["bg"] = "lightgrey"
    button_C["state"] = DISABLED
    button_C["bg"] = "lightgrey"
    button_D["state"] = DISABLED
    button_D["bg"] = "lightgrey"
    button_E["state"] = DISABLED
    button_E["bg"] = "lightgrey"
    button_F["state"] = DISABLED
    button_F["bg"] = "lightgrey"
    button_G["state"] = DISABLED
    button_G["bg"] = "lightgrey"
    button_H["state"] = DISABLED
    button_H["bg"] = "lightgrey"
    button_J["state"] = DISABLED
    button_J["bg"] = "lightgrey"
    button_K["state"] = DISABLED
    button_K["bg"] = "lightgrey"
    button_set_route["state"] = DISABLED
    button_release_route["state"] = DISABLED
    global r1
    r1 = 0
    global r2   
    r2 = 0
    global r3
    r3 = 0
    draw_A1_default()
    draw_A2_default()
    draw_B1_default()
    draw_B2_default()

# PL | funkcja dodatkowo blokuje możliwość wyboru początkowych sygnałów A, B, C lub D, gdy przebieg nie jest nastawiony (sprawdzana jest wartość
# PL | zmiennej globalnej r1).
# EN | the function additionaly block A, B, C and D signal buttons if route is not set (r1 global variable is checked)

def set_route_disabled_if_not_set():
    global r1
    if r1 == 0:
        button_A["state"] = DISABLED
        button_B["state"] = DISABLED
        button_C["state"] = DISABLED
        button_D["state"] = DISABLED
        button_set_route["state"] = DISABLED
        button_release_route["state"] = DISABLED

# PL | przyporządkowanie indeksów dróg przbiegów do sygnałów na semaforach
# EN | assigning signals to given route indexes

# s1 = [000]
# s2 = [111, 222]
# s3 = [112, 221]
# s4 = [114, 116, 224, 226]
# s5 = [110, 220]
# s6 = [122, 211]
# s7 = [121, 212]
# s8 = [124, 126, 214, 216]
# s9 = [120, 210]
# s10a = [411, 422]
# s11a = [412, 421]
# s12a = [414, 416, 424, 426]
# s13a = [410, 420]
# s10 = [611, 622]
# s11 = [612, 621]
# s12 = [614, 616, 624, 626]
# s13 = [610, 620]

# PL | ################### DEFINICJE FUNKCJI - URUCHAMIANIE SYGNAŁÓW I DRÓG PRZEBIEGÓW ####################
# EN | ################### FUNCTIONS DEFINITIONS - SIGNALS AND ROUTES INIT ####################

def draw_signal():
    if route_index == 111:
        draw_A1_track_1()
        draw_A2_track_1_1()
        draw_B1_track_1()
        draw_B2_track_1()
        draw_signal_w24()
        start_s2()
    elif route_index == 222:
        draw_A1_track_2()
        draw_A2_track_2_2()
        draw_B1_track_2()
        draw_B2_track_2()
        start_s2()
    elif route_index == 112:
        draw_A1_track_1()
        draw_A2_track_1_1()
        draw_B1_track_1_2()
        draw_B2_track_2()
        init_loop_s3()
        draw_signal_w24()
    elif route_index == 221:
        draw_A1_track_2()
        draw_A2_track_2_2()
        draw_B1_track_2_1()
        draw_B2_track_1()
        init_loop_s3()
    elif route_index == 114:
        draw_A1_track_1()
        draw_A2_track_1_1()
        draw_B1_track_1_2()
        draw_B2_track_4()
        init_loop_s4()
        draw_signal_w24()
    elif route_index == 116:
        draw_A1_track_1()
        draw_A2_track_1_1()
        draw_B1_track_1_2()
        draw_B2_track_6()
        init_loop_s4()
        draw_signal_w24()
    elif route_index == 224:
        draw_A1_track_2()
        draw_A2_track_2_2()
        draw_B1_track_2()
        draw_B2_track_4()
        init_loop_s4()
    elif route_index == 226:
        draw_A1_track_2()
        draw_A2_track_2_2()
        draw_B1_track_2()
        draw_B2_track_6()
        init_loop_s4()
    elif route_index == 110:
        draw_A1_track_1()
        draw_A2_track_1_1()
        start_s5()
        draw_signal_w24()
    elif route_index == 220:
        draw_A1_track_2()
        draw_A2_track_2_2()
        start_s5()
    elif route_index == 122:
        draw_A1_track_1()
        draw_A2_track_1_2()
        draw_B1_track_2()
        draw_B2_track_2()
        start_s6()
    elif route_index == 211:
        draw_A1_track_2()
        draw_A2_track_2_1()
        draw_B1_track_1()
        draw_B2_track_1()
        start_s6()
        draw_signal_w24()
    elif route_index == 121:
        draw_A1_track_1()
        draw_A2_track_1_2()
        draw_B1_track_2_1()
        draw_B2_track_1()
        init_loop_s7()
    elif route_index == 212:
        draw_A1_track_2()
        draw_A2_track_2_1()
        draw_B1_track_1_2()
        draw_B2_track_2()
        init_loop_s7()
        draw_signal_w24()
    elif route_index == 124:
        draw_A1_track_1()
        draw_A2_track_1_2()
        draw_B1_track_2()
        draw_B2_track_4()
        init_loop_s8()
    elif route_index == 126:
        draw_A1_track_1()
        draw_A2_track_1_2()
        draw_B1_track_2()
        draw_B2_track_6()
        init_loop_s8()
    elif route_index == 214:
        draw_A1_track_2()
        draw_A2_track_2_1()
        draw_B1_track_1_2()
        draw_B2_track_4()
        init_loop_s8()
        draw_signal_w24()
    elif route_index == 216:
        draw_A1_track_2()
        draw_A2_track_2_1()
        draw_B1_track_1_2()
        draw_B2_track_6()
        init_loop_s8()
        draw_signal_w24()
    elif route_index == 120:
        draw_A1_track_1()
        draw_A2_track_1_2()
        start_s9()
    elif route_index == 210:
        draw_A1_track_2()
        draw_A2_track_2_1()
        start_s9()
        draw_signal_w24()
    elif route_index == 411:
        draw_A1_track_4()
        draw_A2_track_2_1()
        draw_B1_track_1()
        draw_B2_track_1()
        start_s10a()
        draw_signal_w24()
    elif route_index == 422:
        draw_A1_track_4()
        draw_A2_track_2_2()
        draw_B1_track_2()
        draw_B2_track_2()
        start_s10a()
    elif route_index == 412:
        draw_A1_track_4()
        draw_A2_track_2_1()
        draw_B1_track_1_2()
        draw_B2_track_2()
        init_loop_s11a()
        draw_signal_w24()
    elif route_index == 421:
        draw_A1_track_4()
        draw_A2_track_2_2()
        draw_B1_track_2_1()
        draw_B2_track_1()
        init_loop_s11a()
    elif route_index == 414:
        draw_A1_track_4()
        draw_A2_track_2_1()
        draw_B1_track_1_2()
        draw_B2_track_4()
        init_loop_s12a()
        draw_signal_w24()
    elif route_index == 416:
        draw_A1_track_4()
        draw_A2_track_2_1()
        draw_B1_track_1_2()
        draw_B2_track_6()
        init_loop_s12a()
        draw_signal_w24()
    elif route_index == 424:
        draw_A1_track_4()
        draw_A2_track_2_2()
        draw_B1_track_2()
        draw_B2_track_4()
        init_loop_s12a()
    elif route_index == 426:
        draw_A1_track_4()
        draw_A2_track_2_2()
        draw_B1_track_2()
        draw_B2_track_6()
        init_loop_s12a()
    elif route_index == 410:
        draw_A1_track_4()
        draw_A2_track_2_1()
        start_s13a()
        draw_signal_w24()
    elif route_index == 420:
        draw_A1_track_4()
        draw_A2_track_2_2()
        start_s13a()
    elif route_index == 611:
        draw_A1_track_6()
        draw_A2_track_2_1()
        draw_B1_track_1()
        draw_B2_track_1()
        start_s10()
        draw_signal_w24()
    elif route_index == 622:
        draw_A1_track_6()
        draw_A2_track_2_2()
        draw_B1_track_2()
        draw_B2_track_2()
        start_s10()
    elif route_index == 612:
        draw_A1_track_6()
        draw_A2_track_2_1()
        draw_B1_track_1_2()
        draw_B2_track_2()
        init_loop_s11()
        draw_signal_w24()
    elif route_index == 621:
        draw_A1_track_6()
        draw_A2_track_2_2()
        draw_B1_track_2_1()
        draw_B2_track_1()
        init_loop_s11()
    elif route_index == 614:
        draw_A1_track_6()
        draw_A2_track_2_1()
        draw_B1_track_1_2()
        draw_B2_track_4()
        init_loop_s12()
        draw_signal_w24()
    elif route_index == 616:
        draw_A1_track_6()
        draw_A2_track_2_1()
        draw_B1_track_1_2()
        draw_B2_track_6()
        init_loop_s12()
        draw_signal_w24()
    elif route_index == 624:
        draw_A1_track_6()
        draw_A2_track_2_2()
        draw_B1_track_2()
        draw_B2_track_4()
        init_loop_s12()
    elif route_index == 626:
        draw_A1_track_6()
        draw_A2_track_2_2()
        draw_B1_track_2()
        draw_B2_track_6()
        init_loop_s12()
    elif route_index == 610:
        draw_A1_track_6()
        draw_A2_track_2_1()
        start_s13()
        draw_signal_w24()
    elif route_index == 620:
        draw_A1_track_6()
        draw_A2_track_2_2()
        start_s13()

# PL | ################### DEFINICJE FUNKCJI - POLA TEKSTOWE ####################
# EN | ################### FUNCTIONS DEFINITIONS - TEXT LABELS ####################

def text_s1():
    text = Text(root, width = 65, height = 12)
    text.place(x=828, y=335)
    text.insert('1.0', 'Sygnał S1 - Stój')

def text_s2():
    text = Text(root, width = 65, height = 12)
    text.place(x=828, y=335)
    text.insert('1.0', 'Sygnał S2 - jazda z największą dozwoloną prędkością')

def text_s3():
    text = Text(root, width = 65, height = 12)
    text.place(x=828, y=335)
    text.insert('1.0', 'Sygnał S3 - jazda z największą dozwoloną prędkością – w przodzie są dwa odstępy blokowe wolne - albo przy następnym semaforze z prędkością nie większą niż 100 km/h')

def text_s4():
    text = Text(root, width = 65, height = 12)
    text.place(x=828, y=335)
    text.insert('1.0', 'Sygnał S4 - jazda z największą dozwoloną prędkością - następny semafor wskazuje sygnał zezwalający na jazdę z prędkością zmniejszoną do 40 lub 60 km/h')

def text_s5():
    text = Text(root, width = 65, height = 12)
    text.place(x=828, y=335)
    text.insert('1.0', 'Sygnał S5 - jazda z największą dozwoloną prędkością - następny semafor wskazuje sygnał stój')

def text_s6():
    text = Text(root, width = 65, height = 12)
    text.place(x=828, y=335)
    text.insert('1.0', 'Sygnał S6 - jazda z prędkością nieprzekraczającą 100 km/h, a potem z największą dozwoloną prędkością')

def text_s7():
    text = Text(root, width = 65, height = 12)
    text.place(x=828, y=335)
    text.insert('1.0', 'Sygnał S7 - jazda z prędkością nieprzekraczającą 100 km/h przy tym i następnym semaforze')

def text_s8():
    text = Text(root, width = 65, height = 12)
    text.place(x=828, y=335)
    text.insert('1.0', 'Sygnał S8 - jazda z prędkością nieprzekraczającą 100 km/h, a przy następnym semaforze z prędkością zmniejszoną do 40 lub 60 km/h')

def text_s9():
    text = Text(root, width = 65, height = 12)
    text.place(x=828, y=335)
    text.insert('1.0', 'Sygnał S9 - jazda z prędkością nieprzekraczającą 100 km/h, a przy następnym semaforze - Stój')

def text_s10():
    text = Text(root, width = 65, height = 12)
    text.place(x=828, y=335)
    text.insert('1.0', 'Sygnał S10 - jazda z prędkością nieprzekraczającą 40 km/h, a potem z największą dozwoloną prędkością')

def text_s11():
    text = Text(root, width = 65, height = 12)
    text.place(x=828, y=335)
    text.insert('1.0', 'Sygnał S11 - jazda z prędkością nieprzekraczającą 40 km/h, a przy następnym z prędkością nieprzekraczającą 100 km/h')

def text_s12():
    text = Text(root, width = 65, height = 12)
    text.place(x=828, y=335)
    text.insert('1.0', 'Sygnał S12 - jazda z prędkością nieprzekraczającą 40 km/h, a przy następnym semaforze z prędkością nieprzekraczającą 40 lub 60 km/h')

def text_s13():
    text = Text(root, width = 65, height = 12)
    text.place(x=828, y=335)
    text.insert('1.0', 'Sygnał S13 - jazda z prędkością nieprzekraczającą 40 km/h, a przy następnym semaforze - Stój')

def text_s10a():
    text = Text(root, width = 65, height = 12)
    text.place(x=828, y=335)
    text.insert('1.0', 'Sygnał S10a - jazda z prędkością nieprzekraczającą 60 km/h, a potem z największą dozwoloną prędkością')

def text_s11a():
    text = Text(root, width = 65, height = 12)
    text.place(x=828, y=335)
    text.insert('1.0', 'Sygnał S11a - jazda z prędkością nieprzekraczającą 60 km/h, a przy następnym z prędkością nieprzekraczającą 100 km/h')

def text_s12a():
    text = Text(root, width = 65, height = 12)
    text.place(x=828, y=335)
    text.insert('1.0', 'Sygnał S12a - jazda z prędkością nieprzekraczającą 60 km/h, a przy następnym semaforze z prędkością nieprzekraczającą 40 lub 60 km/h')

def text_s13a():
    text = Text(root, width = 65, height = 12)
    text.place(x=828, y=335)
    text.insert('1.0', 'Sygnał S13a - jazda z prędkością nieprzekraczającą 60 km/h, a przy następnym semaforze - Stój')

def text_sz():
    text = Text(root, width = 65, height = 12)
    text.place(x=828, y=335)
    text.insert('1.0', 'Sygnał Sz - sygnał zastępczy')

# PL | funkcja umieszka w polu tekstowym licznik do wygaśnięcia sygnału sz
# EN | the function puts sz signal counter into text box

def text_sz_licznik():
    global licznik_sz
    text = Text(root, width = 65, height = 12, fg= "red")
    text.place(x=828, y=335)
    text.insert('1.0', 'Sygnał Sz - sygnał zastępczy. Sygnał wygaśnie za: ')
    text.insert('2.0', licznik_sz)
    text.insert('3.0', ' sekund')

def text_usterka_s1_on():
    text = Text(root, width = 65, height = 12, fg= "red")
    text.place(x=828, y=335)
    text.insert('1.0', 'Alarm: usterka żarówki S1')

def text_usterka_s1_off():
    text = Text(root, width = 65, height = 12)
    text.place(x=828, y=335)

# PL | ################### DEFINICJE FUNKCJI - RYSOWANIE OBRAZÓW PO STARCIE PROGRAMU ####################
# EN | ################### FUNCTIONS DEFINITIONS - IMAGES DRAWING AFTER PROGRAM STARTING ####################

draw_s1()
draw_signal_w24_dark()
text_s1()
draw_A1_default()
draw_A2_default()
draw_B1_default()
draw_B2_default()

root.mainloop()