# programming language: python

################### PROGRAM DESCRIPTION ####################

# the program allows to display any signal on a light semaphore according to the rules applied on Polish railways
# thanks to a specially designed track layour, it enables the understanding of the signal sequence for all possible combinations of permitted speeds

################### PROGRAM FUNCTIONS ####################

# displaying any continuous and blinking signal with corresponding indicators
# displaying call-on signal and corresponding indication on traffic management display panel
# a counter measuring the time until the automatic expiration of call-on signal - 90s, according to the rules applied on Polish railways
# simulation of red light bulb failure and corresponding indicaton on traffic management display panel
# choice of a train route according to any combination, starting with a group of signals A, B, C or D, ending with signals E, F or with a group of signals G, H, J, K.
# displaying every possible signal by selecting the appropriate train route in a specially designed track layout
# coloring track layout according to selected train route
# displaying W24 indicator after selecting appropriate train route through block section 15
# displaying text messages

################### PROGRAMMING SOLUTIONS ####################

# global variables with values True, False initiating While True loops for blinking signals
# While True loops running as separate threads (Thread.start())
# addtional else conditions in While True loops
# additional condition in While True loop initiating a 90s counter (call-on signal)
# three single digit global variables for given signal groups, creating main 3-digit global variable for choosen route index 
# tkinter library - labels, enabling and disabling buttons, text boxes
