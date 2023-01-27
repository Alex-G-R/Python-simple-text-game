##################################################################################################################
#Biblioteki NIE RUSZAĆ NIE RUSZAĆ NIE RUSZAĆ NIE RUSZAĆ NIE RUSZAĆ NIE RUSZAĆ NIE RUSZAĆ NIE RUSZAĆ NIE RUSZAĆ NIE RUSZAĆ
from re import X
import time
import sys 
##################################################################################################################




print("░█████╗░██████╗░░█████╗░░█████╗░░█████╗░██╗░░░░░██╗██████╗░████████╗░█████╗░")
time.sleep(1)
print("██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░░░██║██╔══██╗╚══██╔══╝██╔══██╗")
time.sleep(1)
print("███████║██████╔╝██║░░██║██║░░╚═╝███████║██║░░░░░██║██████╔╝░░░██║░░░██║░░██║")
time.sleep(1)
print("██╔══██║██╔═══╝░██║░░██║██║░░██╗██╔══██║██║░░░░░██║██╔═══╝░░░░██║░░░██║░░██║")
time.sleep(1)
print("██║░░██║██║░░░░░╚█████╔╝╚█████╔╝██║░░██║███████╗██║██║░░░░░░░░██║░░░╚█████╔╝")
time.sleep(1)
print("╚═╝░░╚═╝╚═╝░░░░░░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝╚═╝░░░░░░░░╚═╝░░░░╚════╝░")
time.sleep(1)
print("Alex G-R")
time.sleep(1)
print("")
print("Wersja 0.1//09.06.2022//Early ALPHA")
time.sleep(1)
print("____________________________________________________________________________________________")
time.sleep(1)
print("|CHANGELOG Z DNIA 09.06.2022:                                                               |")
time.sleep(1)
print("|-Wyjście z versji dev - ponowne uruchomienie odstępów czasowych między wiadomościami       |")
time.sleep(1)
print("|-Poprawki estetyczne w kodzie                                                              |")
time.sleep(1)
print("|-Poprawa stylu obrazków ASCI                                                               |")
time.sleep(1)
print("|-Podzielenie kodu na kategorie wydarzeń - całkiem pomocna sprawa                           |")
time.sleep(1)
print("|-Częściowe sprzatanie kodu                                                                 |")
time.sleep(1)
print("|-Zamknięcie wątków fabularnych w taki sposób aby można było je dalej prowadzić             |")
time.sleep(1)
print("|-Dodanie ograniczeń w wieku i wzroscie                                                     |")
time.sleep(1)
print("|-Poprawienie jakości gramatycznej, interpunkcyjniej i ortograficznej fabuły                |")
time.sleep(1)
print("|___________________________________________________________________________________________|")
time.sleep(3)
print("")

##################################################################################################################

#Zmienne NIE RUSZAĆ NIE RUSZAĆ NIE RUSZAĆ NIE RUSZAĆ NIE RUSZAĆ NIE RUSZAĆ NIE RUSZAĆ NIE RUSZAĆ NIE RUSZAĆ NIE RUSZAĆ
start=0
wzrost=0
wiek=0
call=0
HP=100
waga=0
atak=7
gg = 1
#wiek = int(input("Wprowadź wiek postaci  >"))
#print("")

##################################################################################################################

#Start gry
while start != ("X"):
    start = input("Aby rozpocząć gre najpierw należy stworzyć postać aby to zrobić wprowadź dużą litere X  ")

##################################################################################################################

if start == ("X"):
    time.sleep(1)
    print("████████████████████████████████████████████████████████████████████████████████████████████████")
    time.sleep(1)
    print("█─▄▄▄─█─█─██▀▄─██▄─▄▄▀██▀▄─██─▄▄▄─█─▄─▄─█▄─▄▄─█▄─▄▄▀███─▄▄▄─█▄─▄▄▀█▄─▄▄─██▀▄─██─▄─▄─█─▄▄─█▄─▄▄▀█")
    time.sleep(1)
    print("█─███▀█─▄─██─▀─███─▄─▄██─▀─██─███▀███─████─▄█▀██─▄─▄███─███▀██─▄─▄██─▄█▀██─▀─████─███─██─██─▄─▄█")
    time.sleep(1)
    print("▀▄▄▄▄▄▀▄▀▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀")
    time.sleep(1)
imie = input("Wprowadż imię postaci  >")
time.sleep(1)
imie2 = input("Wprowadź imię postaci w 2 osobie Dopełniacza np. Kogo? Czego? Alexa, Mileny, Azgardiusza  >")
time.sleep(1)

##################################################################################################################

while wiek <= 13 or wiek >= 60 :
    wiek = int(input("Wprowadź wiek postaci? >"))
if wiek > 13 or wiek < 60:
    time.sleep(1)

##################################################################################################################

    while wzrost < 130 or wzrost > 210 :
        wzrost = int(input("Wprowadź wzrost postaci? >"))
if wzrost <= 130 or wzrost >= 210:  

##################################################################################################################

 #   while waga < 40 or waga > 160 :
 #       waga = int(input("Wprowadź wage postaci? >"))
 #if waga >= 40 or waga <= 160:
##################################################################################################################
#Pochodzenie = input("Wybierz poziom trudności i miejce akcji SOON 1 Łatwy-Ohio/ SOON 2 Średni-Texas/ SOON 3 Trudny-California/ należy wpisać 1, 2 lub 3  ")
##################################################################################################################

    print("█░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀")
    print("█▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█")
time.sleep(1)
print(" 🔲 ")
time.sleep(1)
print(" 🔲 ")
time.sleep(1)
print(" 🔲 ")
time.sleep(3)
print("░█▀▀█ ░█▀▀▀ ─█▀▀█ ░█▀▀▄ ░█──░█ ")
time.sleep(1)
print("░█▄▄▀ ░█▀▀▀ ░█▄▄█ ░█─░█ ░█▄▄▄█ ")
time.sleep(1)
print("░█─░█ ░█▄▄▄ ░█─░█ ░█▄▄▀ ──░█")

##################################################################################################################

time.sleep(3)
print("")

print("Godzina 3:30 śpisz - budzi cię krzyk,wrzask, ogólny rozgardiasz na dworze.")
time.sleep(3)
print("Mieszkasz na małej wsi więc nie jest to codzienne zjawisko ")
time.sleep(3)
print("Wyglądasz przez okno i nagle w szybe uderza głową kobieta - wygląda na poobijaną rozcięty łuk brwiowy blada delikatnie zielona ")
time.sleep(3)
print("Przestraszyłeś się odskoczyłeś od okna i chwyciłeś za telefon aby zadzwonić na policje")
time.sleep(3)

##################################################################################################################

while call != ("997"or"112"):
    call = input("Jaki wprowadziłeś numer? >")
if call == "997"or"112":
    time.sleep(3)
    print("Po paru dzwonkach ktoś odbiera zanim zdążyłeś coś powiedzieć usłyszałeś komunikat :")
time.sleep(3)
print("UWAGA nasz kraj nawiedził nieznany wirus schowaj się w domu i nie wychodź")
time.sleep(3)
print("Objawami są :ślinotok, agresja, odporność na urazy, brak bólu, zarażeni atakują każdego kogo zobaczą - proszę zostań w domu")
time.sleep(3)
print("Rozmowa zakończyła się : jesteś przerażony ale nie po to grałeś latami w gry o zombie żeby nie rozpoznać apokalipsy")
time.sleep(3)

##################################################################################################################

print("Wiedziałeś że musisz uciekać mogłeś zdążyłeś zabrać 1 rzecz przed dostaniem się zombi do domu")
item = input("Co to było? Glock/Nóż/Banan/Plecak >")
if item == "Glock":
    print("Zastrzeliłeś zombie i wybiegłeś z domu")
if item == "Nóż":
    print("Dźgnołeś zombie i wybiegłeś z domu")
if item == "Plecak":
    print("zabrałeś plecak, okazał się być pełen książek z biblioteki porzuciłeś go w celu ucieczki")
if item == "Banan":
    print("Chwyciłeś za banana - podczas ucieczki obrałeś go i zjadłeś")

##################################################################################################################

decyzja = input("gdzie się udałeś? Centrum/Las >"  )
if decyzja != ("Las"):
    time.sleep(2)
    print("Udałeś się do centrum przygwoździła się szmara 8 zombie")
    if item == "Glock":
        time.sleep(2)
        print("bez namysłu rozstrzelałeś je swoim pistoletem. Po chwili jednak zbiegło się więcej zombi zmuszając cię do ucieczki w las")
    else:
        time.sleep(2)
        print("Zombie cię przygwoździły gdybyś tylko miał dobrą broń - Nie żyjesz", imie)
        time.sleep(2)
        sys.exit(0)

#######################################################################################################################################################

print("Udałeś się do lasu - zaczynasz zagłębiać się w chaszcze")
time.sleep(1)
print("Przed tobą staje zombie")
time.sleep(1)
print("Twoje punkty zdrowia", HP)
time.sleep(1)
print("Punkty zdrowia zombie 37")
time.sleep(1)

#######################################################################################################################################################

walka1 = input("(SOON)-Walka/Ucieczka >")
if walka1 == "Walka":
    print("Podejmujesz się walki")
    time.sleep(2)
    if item == "Glock":

#######################################################################################################################################################

        decyzja1 = input("Użyjesz Glock/Pięści? >")
        if decyzja1 == "Glock":
            print("Zastrzeliłeś zombie lecz tym strzałem zwabiłeś na siebie zombie z centrum NIE ŻYJESZ")
            time.sleep(5)
            sys.exit(0)

#######################################################################################################################################################

        else:
            walka2 = input("rzuciłeś się na zombie z pięściami gdzie zadałeś 1 cios? Kark/Nos/Brzuch >")

#######################################################################################################################################################

            if walka2 == "Kark":
                print("Zadałeś 27 obrażeń zombie jego hp wynosi 10") 
                time.sleep(2)
                print("Zombie zadał ci cios w ramię twoje HP zmniejszyło się o 7")
                HP - 7
                #print("HP")
                #print("atak")
                print("twoje punkty życia", HP)
                walka2x = input("Gdzie zadasz kolejny cios? Głowa/Brzuch >")

#######################################################################################################################################################

                if walka2x == "Głowa":
                    print("zadałeś 10 punktów obrażeń zombie nie żyje")
                    time.sleep(2)
                    print("Przy zombie udało ci się znaleźć monete 5zł- zabrałeś ją ")
                    print("Ta droga fabuły kończy się tu lecz gwarantuje ci że istniejie dłuższa droga spróbuj ją przejść / ta część fabuły zostanie dokończona później")
                    time.sleep(5)
                    sys.exit(0)

#######################################################################################################################################################

                else:
                    print("Zadałeś 10 ptk obrażeń zombie nie żyje")
                    time.sleep(2)
                    print("Przy zombie udało ci się znaleźć monete 5zł- zabrałeś ją")
                    print("Ta droga fabuły kończy się tu lecz gwarantuje ci że istniejie dłuższa droga spróbuj ją przejść / ta część fabuły zostanie dokończona później")
                    time.sleep(5)
                    sys.exit(0)

#######################################################################################################################################################

            if walka2 == "Nos":
                print("Zadałeś potężny cios w nos zombie złożył się po nim jak zapałka rozbijając sobie czaszkę o kamień")
                time.sleep(2)
                print("coś błyszczącego wypadło zombie z kieszeni - nie byłeś w stanie tego odnaleźć ")
                print("Ta droga fabuły kończy się tu lecz gwarantuje ci że istniejie dłuższa droga spróbuj ją przejść / ta część fabuły zostanie dokończona później")
                time.sleep(5)
                sys.exit(0)

#######################################################################################################################################################

            if walka2 == "Brzuch":
                print("Zombie po zadanym przez ciebie ataku wgryzł się w twoją szyje kończąc twój żywot")
                time.sleep(5)
                sys.exit(0)

#######################################################################################################################################################

if walka1 == "Ucieczka":
    print("Rzuciłeś się do przodu nie zważając na kierunek beigu")
    time.sleep(2)
    print("Po parunastu minutach dobiegasz do starego ale schludnego rancza")
    time.sleep(2)
    decyzja2 = input("Widzisz 2 budynki domek i stodołe gdzie sie udajesz? Dom/Stodoła >")

#######################################################################################################################################################

    if decyzja2 == "Dom":
        print("Wchodzisz do domu spotykasz starszego otyłego mężczyzne który strzelbe w ręku")
        time.sleep(2)
        print("Prawdobodobnie wziął cię za zombie i zastrzelił cię")
        time.sleep(5)
        sys.exit(0)

#######################################################################################################################################################

    if decyzja2 == "Stodoła":
        print("Wchodzisz do starej stodoły gdzie widzisz konia")
        time.sleep(2)
        print("Próbujesz otworzyć box ale jest zamknięty - musisz znaleźć klucz")
        decyzja3 = input("Szukasz klucza Stog/Wycieraczka >")

#######################################################################################################################################################

        if decyzja3 == "Stog":
            print("Szukanie klucza w stogu siana")
            time.sleep(1)
            print(" 🔲 ")
            time.sleep(1)
            print(" 🔲 ")
            time.sleep(1)
            print(" 🔲 ")
            time.sleep(1)
            print(" 🔲 ")
            time.sleep(1)
            print(" 🔲 ")
            time.sleep(1)
            print(" 🔲 ")
            time.sleep(1)
            print(" 🔲 ")
            time.sleep(1)
            print(" 🔲 ")
            time.sleep(1)
            print(" 🔲 ")
            time.sleep(1)
            print(" 🔲 ")
            time.sleep(1)
            print(" 🔲 ")
            time.sleep(1)
            print(" 🔲 ")
            time.sleep(1)
            print(" 🔲 ")
            time.sleep(1)
            print(" 🔲 ")
            time.sleep(1)
            print(" 🔲 ")
            time.sleep(1)
            print(" 🔲 ")
            print("nic nie znalazłeś")
            print("udałeś sie w strone wycieraczki uchyliłeś ją i znalazłeś klucz")
            print("wsiadłeś na konia i odjechałeś")

#######################################################################################################################################################

        if decyzja3 == "Wycieraczka":
            print("udałeś sie w strone wycieraczki uchyliłeś ją i znalazłeś klucz")
            time.sleep(1)
            print("wsiadłeś na konia i odjechałeś")
    time.sleep(2)
    print("koń po galopie przez dłuższą chwile się zmęczył")
    time.sleep(2)
    print("jesteś niedaleko góry lecz koń nie chce iść dalej")
    time.sleep(2)

#######################################################################################################################################################

    decyzja4 = input("musisz wybrać czy iść w strone góry czy pozostać z koniem góra/koń >")
    if decyzja4 == "koń":
        time.sleep(2)
        print("pozostajesz z koniem lecz mimo spędzonych kilku godzinach on nie czuje się lepiej")
        time.sleep(2)
        print("koń okazuje się być chory umiera a ty pozostajesz bez wierzchowca")
        time.sleep(2)
        print("ruszasz w strone góry lecz dogania cie chamra zombie jest ich zbyt dużo - umierasz")
        time.sleep(5)
        sys.exit(0)

#######################################################################################################################################################

    if decyzja4 == "góra":
        print("ruszasz w stonę góry")
        time.sleep(2)
        print("mając duży zapas czasu dochodzisz do góry przed zmierzchem")
        time.sleep(2)
        print("znajdujesz jaskinie w której możesz się zatrzymać do rana")
        time.sleep(2)
        print("Udało ci się usnąć")
        time.sleep(2)
        print("Budzisz się w środku nocy jest ci zimno i opanowała cię nie pewność")
        time.sleep(2)
        decyzja6 = input("Wstaniesz aby sprawdzić co jest 5 czy zostaniesz wyspać się do rana Droga/Spanie >")

#######################################################################################################################################################

        if decyzja6 == "Droga":
            print("Podświadomość dała ci dobry znak i przed jaskinią znajdował się zombie")
            time.sleep(2)
            print("Z łatwością podszedłeś umarlaka i zepchnołeś go z góry a ten stoczył się tak kula po wzgórzu")
            time.sleep(2)
            print("Byłeś zmęczony więc kiedy przysiadłeś w spokoju - zasnołeś")
            time.sleep(2) 
        if decyzja6 == "Spanie":
            print("Zombie zaskoczył cię podczas snu-gdybyś tylko był bardziej czujny NIE ŻYJESZ")
            time.sleep(5)
            sys.exit(0)

#######################################################################################################################################################

        time.sleep(1)
        print("Niestety fabuła gry kończy się w tym miejscu oczywiście mam zamiar ją dalej rozwijać")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".   SSSSSSSSSSSSSSS       OOOOOOOOO          OOOOOOOOO       NNNNNNNN        NNNNNNNN")
        time.sleep(1)
        print(". SS:::::::::::::::S    OO:::::::::OO      OO:::::::::OO     N:::::::N       N::::::N")
        time.sleep(1)
        print(".S:::::SSSSSS::::::S  OO:::::::::::::OO  OO:::::::::::::OO   N::::::::N      N::::::N")
        time.sleep(1)
        print(".S:::::S     SSSSSSS O:::::::OOO:::::::O O:::::::OOO:::::::O N:::::::::N     N::::::N")
        time.sleep(1)
        print(".S:::::S             O::::::O   O::::::O O::::::O   O::::::O N::::::::::N    N::::::N")
        time.sleep(1)
        print(".S:::::S             O:::::O     O:::::O O:::::O     O:::::O N:::::::::::N   N::::::N")
        time.sleep(1)
        print(". S::::SSSS          O:::::O     O:::::O O:::::O     O:::::O N:::::::N::::N  N::::::N")
        time.sleep(1)
        print(".  SS::::::SSSSS     O:::::O     O:::::O O:::::O     O:::::O N::::::N N::::N N::::::N")
        time.sleep(1)
        print(".    SSS::::::::SS   O:::::O     O:::::O O:::::O     O:::::O N::::::N  N::::N:::::::N")
        time.sleep(1)
        print(".       SSSSSS::::S  O:::::O     O:::::O O:::::O     O:::::O N::::::N   N:::::::::::N")
        time.sleep(1)
        print(".            S:::::S O:::::O     O:::::O O:::::O     O:::::O N::::::N    N::::::::::N")
        time.sleep(1)
        print(".            S:::::S O::::::O   O::::::O O::::::O   O::::::O N::::::N     N:::::::::N")
        time.sleep(1)
        print(".SSSSSSS     S:::::S O:::::::OOO:::::::O O:::::::OOO:::::::O N::::::N      N::::::::N")
        time.sleep(1)
        print(".S::::::SSSSSS:::::S  OO:::::::::::::OO  OO:::::::::::::OO  N::::::N       N:::::::N")
        time.sleep(1)
        print(".S:::::::::::::::SS     OO:::::::::OO      OO:::::::::OO    N::::::N        N::::::N")
        time.sleep(1)
        print(". SSSSSSSSSSSSSSS         OOOOOOOOO          OOOOOOOOO      NNNNNNNN         NNNNNNN")
        time.sleep(1)

       


                                                                                 


        



        






#print(".   SSSSSSSSSSSSSSS      OOOOOOOOO          OOOOOOOOO     NNNNNNNN        NNNNNNNN")
#print(". SS:::::::::::::::S   OO:::::::::OO      OO:::::::::OO   N:::::::N       N::::::N")
#print(".S:::::SSSSSS::::::S OO:::::::::::::OO  OO:::::::::::::OO N::::::::N      N::::::N")
#print(".S:::::S     SSSSSSSO:::::::OOO:::::::OO:::::::OOO:::::::ON:::::::::N     N::::::N")
#print(".S:::::S            O::::::O   O::::::OO::::::O   O::::::ON::::::::::N    N::::::N")
#print(".S:::::S            O:::::O     O:::::OO:::::O     O:::::ON:::::::::::N   N::::::N")
#print(". S::::SSSS         O:::::O     O:::::OO:::::O     O:::::ON:::::::N::::N  N::::::N")
#print(".  SS::::::SSSSS    O:::::O     O:::::OO:::::O     O:::::ON::::::N N::::N N::::::N")
#print(".    SSS::::::::SS  O:::::O     O:::::OO:::::O     O:::::ON::::::N  N::::N:::::::N")
#print(".       SSSSSS::::S O:::::O     O:::::OO:::::O     O:::::ON::::::N   N:::::::::::N")
#print(".            S:::::SO:::::O     O:::::OO:::::O     O:::::ON::::::N    N::::::::::N")
#print(".            S:::::SO::::::O   O::::::OO::::::O   O::::::ON::::::N     N:::::::::N")
#print(".SSSSSSS     S:::::SO:::::::OOO:::::::OO:::::::OOO:::::::ON::::::N      N::::::::N")
#print(".S::::::SSSSSS:::::S OO:::::::::::::OO  OO:::::::::::::OO N::::::N       N:::::::N")
#print(".S:::::::::::::::SS    OO:::::::::OO      OO:::::::::OO   N::::::N        N::::::N")
#print(". SSSSSSSSSSSSSSS        OOOOOOOOO          OOOOOOOOO     NNNNNNNN         NNNNNNN")


    
