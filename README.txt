# PL
# język programowania: python

################### OPIS PROGRAMU ####################

# program umożliwia wyświetlenie dowolnego sygnału na semaforze świetlnym według zasad stosowanych na polskiej kolei. 
# dzięki specjalnie zaprojektowanemu układowi torowemu, umożliwia zrozumienie następstwa sygnałów dla wszystkich możliwych kombinacji dozwolonych prędkości 

################### FUNKCJE PROGRAMU ####################

# wyświetlenie dowolnego sygnału ciągłego i migowego z odpowiadającymi im pasami świetlnymi.
# wyświetlanie sygnału zastępczego i odpowiadającego zobrazowania na pulpicie do sterowania ruchem kolejowym
# licznik mierzący czas do automatycznego wygaśnięcia sygnału zastępczego - 90s, zgodnie z zasadami przyjętymi na polskiej kolei.
# symulacja usterki żarówki światła zezwalającego i odpowiadające zobrazowanie na pulpicie do sterowania ruchem kolejowym
# wybór przebiegu pociągowego wg. dowolnej kombinacji zaczynąjąc od grupy semaforów A, B, C lub D, kończąc na semaforach pośrednich E, F lub na grupie semaforów końcowych G, H, J, K.
# wyświetlanie każdego możliwego sygnału na semaforze poprzez wybór odpowiedniego przebiegu pociągowego w specjalnie zaprojektowanym układzie torowym
# kolorowanie układu torowego zgodnie z wybranym przebiegiem pociągowym
# wyświetlanie wskaźnika W24 po wyborze przebiegu pociągowego po torze niewłaściwym
# wyświetlanie opisów tekstowych i alarmów dla wybranych sygnałów

################### ZASTOSOWANE ROZWIĄZANIA PROGRAMISTYCZNE ####################

# zmienne globalne przyjmujące wartości True, False, uruchamiające pętle While True dla sygnałów migowych
# pętle While True uruchamiane jako osobne wątki metodą Thread
# dodatkowe warunki else w pętlach While True
# dodatkowy warunek uruchamiający pętlę While True, dla licznika odmierzającego 90s
# trzy 1-cyfrowe zmienne globalne dla danych grup semaforów, tworzące 3-cyfrową zmienną globalną oznaczającą indeks wybranego przebiegu pociągowego
# biblioteka tkinter - obrazy, przyciski, aktywacja i deaktywacja przycisków

--------------------------------------------------------------------------------

# EN 
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
