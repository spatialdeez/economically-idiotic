
import time
import sys
from random import randint
try:
    import pyautogui
    import pyinputplus as pyip
except:
    print('Hmm, it seems like you have hot installed two of our VERY special modules that will be needed to work the\n magic! Plese enter these into the command line in the terminal: \n pip install PyInputPlus \n pip install PyAutoGUI \n (For mac and linux users please use pip3 rather than pip)')


def game():

    #General
    Money = 500
    Crypto = 0
    CryptoPerRun = 0
    bill = 0

    #Exams
    gedpassperc = 30
    diplomapassperc = 25
    degreepassperc = 0
    masterspassperc = 0

    #Certificates
    gedcert = 0
    diplomacert = 0
    degreecert = 0
    masterscert = 0

    #Work
    currentjob = ''
    jobtier = 0
    fulltimesalary = 0

    tieronejobs = ['Fast Food crew ', 'Stocker ', 'Cashier ', 'Musician ', 'Cleaner ', 'Cook ']
    tiertwojobs = ['Manager ', 'Sales rep ', 'Teacher ', 'Engineer ', 'Police ']
    tierthreejobs = ['Accountant ', 'Banker' , 'Lawyer ','CEO ', 'Doctor ']

    chosentierone = ''
    chosentiertwo = ''
    chosentierthree = ''

    print('Economically Idiotic, version 0.7.6 by randomchez#8734')
    print('----------------GAME START----------------')

    #Lets player choose a mode
    print('Choose mode:')
    answer = pyip.inputMenu(['Classic mode (The usual $500 as starting cash)', 'Poor mode (You are broke: start with $0)', 'Creative mode (You have infinite amount of cash)', 'Hardcore mode (You have $0, AND have life expentancy rates)'], lettered=False, numbered=True)
    if answer == 'Classic mode (The usual $500 as starting cash)':
        print('Entered: Classic mode')
    elif answer == 'Poor mode (You are broke: start with $0)':
        print('Entered: poor mode')
        print('Initiallzing changes...')
        Money = 0
    elif answer == 'Creative mode (You have infinite amount of cash and all)':
        print('Entered: Creative mode.')
        print('Initializing changes...')
        Money = 9999999999999999999999999999999999999999
        gedcert = 1
        diplomacert = 1
        degreecert = 1
        masterscert = 1

        currentjob = 'The pure job'
        fulltimesalary = 9999999999999999999999999999999999999999999
    elif answer == 'Hardcore mode (You have $0, AND have life expentancy rates)':
        print('YOU, and the user, YOU are about to enter hardcore mode. If you do not know what hardcore mode is \n(Or its your first time playing it), I recommend to read the rules changed (press 1 enter) on the next prompt given.')
        answer = pyip.inputMenu(['Read the rules', 'Nah, I know what it is'], lettered=True, numbered=False)
        if answer == 'Read the rules':
            print('Hardcore mode increases the difficulty of the game. You will zhve another thing added called: life expectancy')
            print('Life expectancy is the life you have left. Once you reached the life expexctancy rate, you lose')
            print('But this mode is incomplete, so it will be refered as classic mode for now.')
            print('If you do not want classic mode, replay this script again and select the mode you wanna play')
        else:
            print('this mode is incomplete, so it will be refered as classic mode for now.')
            print('If you do not want classic mode, replay this script again and select the mode you wanna play')

    while True:
        print('Select an Activity:')
        print('''(1) go to the market\n(2) check your idiotic phone\n(3) mine some crypto\n(4) Try the exams\n(5) Work for money\n(6) Go to the lottery''')
        answer = pyip.inputNum()
        if answer == 1:
            pass

        elif answer == 2:
            print('hi welcome to your phone.')
            print('(1) buy some crypto\n(2) sell your crypto\n(3) pay yur bills\n(4) Order something online lol.\n(5) Check your finances')
            answer = pyip.inputNum()
            if answer == 1:
                Money, Crypto = cryptopurchase(Money, Crypto)
            if answer == 2:
                Money, Crypto = sellcrypto(Crypto, Money)
            if answer == 3:
                bill, Money = billcheck(bill, Money)
            if answer == 4:
                print('Hi welocme to my cool store. we got lots of stuff here. pick what u want to buy')
                print('--- CRYPTO SECTION (enter item ID. its beside the item)---')
                print('-1- slow shit gpu (CPS: 1 Price: 500)')
                print('-2- taco GPU (CPS: 2 Price: 1000)')
                print('-3- GePro RTX 4070 Ti GPU (CPS: 5 Price: 4000)')
                print('-4- GePro RTX 4080 GPU (CPS: 8 price: 7000)')
                time.sleep(3)
                answer = pyip.inputNum()
                if answer == 1:
                    print('so u want to buy slow shit gpu? It increases per run by 10 secs! --NO REFUND--')
                    answer = pyip.inputYesNo()
                    answer = answer.lower()
                    if answer == 'yes' or answer == 'y':
                        if Money >= 500:
                            Money -= 500
                            runsecs += 10
                            CryptoPerRun += 1
                            print('ok. thank you for purchasing our items.')
                            time.sleep(2)
                        else:
                            print('sorry but you are unable to purchase this item. Try again when you\nhave he money!!! Refunds were given ')
                    else:
                        print('aw man. see u next time!')
                        time.sleep(2)
                        continue
                if answer == 2:
                    print('so u want to buy taco GPU? It increases per run by 7 secs! --NO REFUND--')
                    answer = pyip.inputYesNo()
                    answer = answer.lower()
                    if answer == 'yes' or answer == 'y':
                        if Money >= 1000:
                            Money -= 1000
                            runsecs += 7
                            CryptoPerRun += 2
                            print('ok. thank you for purchasing our items.')
                            time.sleep(2)
                        else:
                            print('sorry but you are unable to purchase this item. Try again when you\nhave he money!!! Refunds were given ')
                    else:
                        print('bruh. see u next time!')
                        time.sleep(2)
                        continue
                if answer == 3:
                    print('so u want to buy GePro RTX 4070 Ti GPU? It increases per run by 5 secs! --NO REFUND--')
                    answer = pyip.inputYesNo()
                    answer = answer.lower()
                    if answer == 'yes':
                        if Money >= 4000:
                            Money -= 3000
                            runsecs += 5
                            CryptoPerRun += 5
                            print('ok. thank you for purchasing our items.')
                            time.sleep(2)
                        else:
                            print('sorry but you are unable to purchase this item. Try again when you\nhave he money!!! Refunds were given ')
                    else:
                        print('-_-. see u next time!')
                        time.sleep(2)
                        continue
                if answer == 4:
                    print('so u want to buy GePro 4080 GPU? It increases the run by 4 secs! --NO REFUND--')
                    answer = pyip.inputYesNo()
                    answer = answer.lower()
                    if answer == 'yes':
                        if Money >= 7000:
                            Money -= 7000
                            runsecs += 4
                            CryptoPerRun += 8
                            print('ok. thank you for purchasing our items.')
                            time.sleep(2)
                        else:
                            print('sorry but you are unable to purchase this item. Try again when you\nhave he money!!! Refunds were given ')
                    else:
                        print('bro why u cancel on this deal? see u next time, I guess...')
                        time.sleep(2)
                        continue
            if answer == 5:
                print(f'Money: {Money} Crypto: {Crypto}')
                print(f'Certificates:\nGED: {gedcert}\nDiploma: {diplomacert}\nDegree: {degreecert}\nPhD: {masterscert}')
        elif answer == 3:
            print('>>> TERMINAL OPEN <<<')
            print('>>> LOADING PROGRAM <<<')
            print(f'--- RUNTIME: {runsecs} ---')
            print('--- Start? (ctrl + c to exit terminal)---')
            try:
                print('--- START IN 3 SECONDS ---')
                time.sleep(3)
                print('--- Process Start! ---')
                print('--- At any time, use ctrl + c to quit the mining process ---')
                divide = runsecs / 2
                for i in range(runsecs):
                    time.sleep(1)
                    if i == divide:
                        print('--- NOTIFICATION: Process Almost Complete! ---')
                print('--- NOTIFICATION: PROCESS SUCESSFUL ---')
                print('>>> TERMINAL EXIT <<<')
                print('Check your bank for changes!')
                Crypto += CryptoPerRun
                bill += randint(2,4) * CryptoPerRun
            except KeyboardInterrupt:
                print('>>> ERROR: Exception Raised! ctrl + c used! <<<')
                print('>>> TERMINAL EXIT <<<')
                continue
        elif answer == 4:
            print('--- EXAMS ---')
            answer = pyautogui.confirm('You are given a chance to revise before the exam. Proceed?')
            if answer == 'OK':
                    print('Choose your revision method:')
                    answer = pyip.inputMenu(['Practise mock tests|+5% GED pass rate ($250)', 'Read past written notes|+6% diploma pass rate ($600)', 'Take tuition and university| Unlocks Degree Exam ($55,000)', 'Take tuition and go to a qualified school| Unlocks Master\'s Exam (100,000)'], lettered=False, numbered=True)
                    if answer == 'Practise mock tests|+5% GED pass rate ($250)':
                        while True:
                            if Money >= 250:
                                gedpassperc += 5
                                Money -= 250
                                print('Writing...')
                                time.sleep(1)
                                print('Press enter to continue studying, but will deduct $250 again and will add +5% pass percentage.')
                                print('Press a random key then press enter to stop')
                                answer = input()
                                if answer == '':
                                    continue
                                else:
                                    break
                            else:
                                print('You got no (more) money to study')
                    elif answer == 'Read past written notes|+6% diploma pass rate ($600)' and Money >= 600:
                        while True:
                            if Money >= 600:
                                diplomapassperc += 6
                                Money -= 600
                                print('Reading...')
                                time.sleep(2)
                                print('Press enter to continue studying, but will deduct $600 again and will add +6% pass percentage.')
                                print('Press a random key then press enter to stop')
                                answer = input()
                                if answer == '':
                                    continue
                                else:
                                    break
                            else:
                                print('You have no (more) money to continue studying.')
                                continue
                    elif answer == 'Take tuition and university| Unlocks Degree Exam ($55,000)':
                        if diplomacert == 0:
                                print('You are not eligible for the univerity yet! Take your diploma exam first.')
                                continue
                        elif Money >= 55000:
                            degreepassperc += 100
                            Money -= 55000
                            print('Taking tuition...')
                            time.sleep(3)
                            print('Studying...')
                            time.sleep(3)
                            print('You are now eligible for the degree exam!!!')
                        else:
                            print('You are broke')
                    elif answer == 'Take tuition and go to a qualified school| Unlocks Master\'s Exam (100,000)':
                        if degreecert == 0:
                            print('Not eligible for the Master\'s qualified school yet. Go take university first!')
                        elif Money >= 100000:
                            masterspassperc += 100
                            Money -= 100000
                            print('Taking tuition...')
                            time.sleep(3)
                            print('Studying...')
                            time.sleep(3)
                            print('You are now eligible for the Master\'s exam!!!')
                        else:
                            print('You are broke.')
            else:
                print('Oh well. Good luck!')
            print('Welcome to the exam hall! Choose your exam to register:')
            gedstr = f'GED: pass rate {gedpassperc}% ($100)'
            diplomastr = f'Diploma: pass rate {diplomapassperc}% ($500)'
            if degreepassperc == 0:
                degreestr = 'Degree: You have to take tuition and university first!!! (click ok when they prompt you to revise)'
            elif degreecert == 1:
                degreestr = 'Degree: You already took the exam'
            else:
                degreestr = 'Degree: ready to take the test!'

            if masterspassperc == 0:
                mastersstr = 'Master\'s: You have to take tuition and go to a qualified school first!!! (click ok when they prompt you to revise)'
            elif masterscert >= 1:
                mastersstr = 'Master\'s: You already took the exam'
            else:
                mastersstr = 'Master\'s: ready to take the test!'

            answer = pyip.inputMenu([gedstr, diplomastr, degreestr, mastersstr], lettered=False, numbered=True)
            if answer == gedstr:
                random = randint(0,100)
                Money -= 100
                print('You took the test.')
                time.sleep(2)
                print('You sweat.')
                if gedpassperc >= random:
                    print('You got a GED Certificate!!! Congratulations!')
                    gedcert += 1
                else:
                    print('Better luck next time.')
            elif answer == diplomastr:
                if gedcert == 0:
                    print('Take your GED exam first!')
                    continue
                else:
                    random = randint(0,100)
                    Money -= 500
                    print('You took the test.')
                    time.sleep(2)
                    print('You sweat.')
                    if diplomapassperc >= random:
                        print('You got a Diploma Certificate!!! Congratulations!')
                        diplomacert += 1
                    else:
                        print('Better luck next time.')
            elif answer == degreestr:
                if degreepassperc < 100:
                    print('You are not allowed to take the test yet/again!')
                    continue
                else:
                    print('You received your Degree certificate!')
                    degreepassperc = 0
                    degreecert += 1
            elif answer == mastersstr:
                if masterspassperc < 100:
                    print('You are not allowed to take the test yet/again!')
                    continue
                else:
                    print('You received your Master\'s certificate!')
                    masterspassperc = 0
                    masterscert += 1



        elif answer == 5:
            print('---WORK---')
            print('Choose your mode of working:')
            answer = pyip.inputMenu(('Part-time', 'Full-time'), lettered=False, numbered=True)
            if answer == 'Part-time':
                print('Choose your part-time job:')
                answer = pyip.inputMenu(('Gardener ($5/hr)', 'Handyman ($15/hr)', 'Cleaner ($20/hr)'), lettered=False, numbered=True)
                if answer == 'Gardener ($5/hr)':
                    print('How many hours do you like to spend?')
                    hours = pyip.inputNum()
                    luck = 100
                    for i in range(hours):
                        i += randint (3, 8)
                    luck -= i
                    hirerate = randint(0,100)
                    if hirerate <= luck:
                        print('You\'re hired!')
                        earnings = hours * 5
                        Money += earnings
                        print(f'Earnings: {earnings}')
                    else:
                        print('No one would hire you')
                elif answer == 'Handyman ($15/hr)':
                    print('How many hours do you like to spend?')
                    hours = pyip.inputNum()
                    luck = 100
                    for i in range(hours):
                        i += randint (7, 20)
                    luck -= i
                    hirerate = randint(0,100)
                    if hirerate <= luck:
                        print('You\'re hired!')
                        earnings = hours * 15
                        Money += earnings
                        print(f'Earnings: {earnings}')
                    else:
                        print('No one would hire you')
                if answer == 'Cleaner ($20/hr)':
                    print('How many hours do you like to spend?')
                    hours = pyip.inputNum()
                    luck = 100
                    for i in range(hours):
                        i += randint (12, 30)
                    luck -= i
                    hirerate = randint(0,100)
                    if hirerate <= luck:
                        print('You\'re hired!')
                        earnings = hours * 20
                        Money += earnings
                        print(f'Earnings: {earnings}')
                    else:
                        print('No one would hire you')
            elif answer == 'Full-time':
                print('---Full time---')
                if diplomacert >= 1:
                    print('Requires a diploma (At least)')
                else:
                    answer = pyip.inputMenu(('Find a job', 'Work at your current job'), lettered=False, numbered=True)
                    if answer == 'Find a job':
                            print('Ok... Searching for a job...')
                            if degreecert == 0 and masterscert == 0:
                                randomnum = randint(0,5)
                                chosentierone = tieronejobs[randomnum]
                                print(f'Job picked: {chosentierone}')
                                pickedjob = chosentierone
                                pickedsalary = randint(850, 1500)
                                print(f'Salary: {pickedsalary}')
                                pickedtier = 1
                            elif masterscert == 0:
                                randomnum = randint(0,4)
                                chosentiertwo = tiertwojobs[randomnum]
                                print(f'Job picked: {chosentiertwo}')
                                pickedjob = chosentiertwo
                                pickedsalary = randint(2000,3500)
                                print(f'Salary: {pickedsalary}')
                                pickedtier = 2
                            elif masterscert >= 1:
                                randomnum = randint(0,4)
                                chosentierthree = tierthreejobs[randomnum]
                                print(f'Job picked: {chosentierthree}')
                                pickedjob = chosentierthree
                                pickedsalary = randint(4000, 5500)
                                print(f'Salary: {pickedsalary}')
                                pickedtier = 3


                            print('Accept job offer?')
                            answer = pyip.inputYesNo()
                            if answer == 'yes':
                                currentjob = pickedjob
                                fulltimesalary = pickedsalary
                                print('Good choice!')
                                jobtier = pickedtier
                                if currentjob == '':
                                    print(f'Your job: {currentjob}')
                                    print(f'Your salary: {fulltimesalary}')
                                else:
                                    print(f'Job switched: {currentjob}')
                                    print(f'Your new salary: {fulltimesalary}')
                            else:
                                print('Sorry that we cound not meet your requirements!')
                    elif answer == 'Work at your current job':
                        if currentjob == '':
                            print('YOu do not have a job yet!')
                        else:
                            print('ok')
                            if jobtier == 1:
                                print('---WORK---')
                                print('Ctrl + c to stop working')
                                questions = randint(10,20)
                                try:
                                    questionnumber = 1
                                    for i in range(questionnumber):
                                        if questionnumber == 1:
                                            print('A customer came on your desk and asked for a refund.')
                                            print('TASK: find the correct letter to click and press enter (in under 1 secs)')
                                            alphabets = ['z', 'x', 'f', 'd', 'g']
                                            alphabets = alphabets[randint(0,4)]
                                            print('3')
                                            time.sleep(1)
                                            print('2')
                                            time.sleep(1)
                                            print('1')
                                            time.sleep(1)
                                            print('START!!!')
                                            timerone = time.time()
                                            print(alphabets)
                                            answer = input('> ')
                                            timertwo = time.time()
                                            if answer == alphabets and timertwo - timerone <= 1:
                                                print('Well done!')
                                            elif answer != alphabets:
                                                print('Wrong key!')
                                                raise Exception
                                            else:
                                                print('you did not did it in 1 second! You failed!')
                                                raise Exception
                                            
                                except:
                                    print('You left the workspace')


                            elif jobtier == 2:
                                pass
                            elif jobtier == 3:
                                pass
                            


        elif answer == 6:
            print('Welcome to the lottery!')
            print('How to play: You will be prompted to write in 4 numbers. (Please Only enter numbers between 1 to 10, or the psooibility of you winning will decrease!!!)')
            print('You will also pe prompted to write another number, a bonus. (please put numbers between numbers 1 to 20)')
            print('For every number you win: +$200')
            print('For every dollar you increase on the bet, it will be multiplied by the winning prize!!!')
            input('Press enter to continue...')
            lotteryjackpot = randint(10000,50000)
            print(f'Jackpot today: {lotteryjackpot}')
            print('Bet:')
            bet = pyip.inputNum()
            if bet < 1:
                print('You did not place a bet!')
                continue
            else:
                Money -= bet
                print('First number:')
                firstlotnum = pyip.inputNum()
                print('Second number:')
                seclotnum = pyip.inputNum()
                print('Third number:')
                Thirdtlotnum = pyip.inputNum()
                print('Fourth number:')
                fourthlotnum = pyip.inputNum()
                print('Bonus number:')
                bonuslotnum = pyip.inputNum()
                input('Now, we will be announcing the winning numbers. (Press enter to continue)')
                winningfirst = randint(1,10)
                winningsec = randint(1, 10)
                winningthird = randint(1, 10)
                winningfourth = randint(1, 10)
                winningbonus = randint(1, 20)
                print('The winning numbers are...')
                time.sleep(3)
                print(f'First number: {winningfirst}')
                print(f'Second number: {winningsec}')
                print(f'Third number: {winningthird}')
                print(f'Fourth number: {winningfourth}')
                time.sleep(3)
                print(f'The Bonus number is: {winningbonus}')
                time.sleep(3)
                collectlot = 0
                if winningfirst == firstlotnum:
                    collectlot += 200
                if winningsec == seclotnum:
                    collectlot += 200
                if winningthird == Thirdtlotnum:
                    collectlot += 200
                if winningfourth == fourthlotnum:
                    collectlot += 200
                if winningfirst == firstlotnum and winningsec == seclotnum and winningthird == Thirdtlotnum and winningfourth == fourthlotnum and winningbonus == bonuslotnum:
                    print('JACKPOT!!! CONGRATS!!!')
                    print(f'You won: {lotteryjackpot}')
                    collectlot = lotteryjackpot

                if collectlot == 0:
                    print('Better luck next time!')
                else:
                    collectlot * bet
                    print(f'You collected {collectlot}')
                    Money += collectlot
                    print(f'Money: {Money}')

def cryptopurchase(crypto_money, crypto_crypto):
    crypto_crypto = int(crypto_crypto)
    crypto_money = int(crypto_money)
    print('hi welcome to cryptospace. hope u have a nice day.')
    cryptoprice = randint(100,450)
    print(f'the price of poopcoin is {cryptoprice}')
    time.sleep(1)
    print('would u like to purhase poopcoin? (Y/N)')
    answer = pyip.inputYesNo()
    answer = answer.lower()
    if answer == 'yes':
        print('you are so cool. how many?')
        numberofcrypto = pyip.inputNum()
        cryptoinpurchase = cryptoprice * numberofcrypto
        if crypto_money >= cryptoinpurchase:
            crypto_money = crypto_money - cryptoinpurchase
            crypto_crypto += numberofcrypto
            print(f'here is your money left: {crypto_money}\n crypto left: {crypto_crypto}')
            time.sleep(3)
            return crypto_money, crypto_crypto
        else:
            print('sorry, your purchase could not be processed. This can be due to insufficient funds.\nrefund was given')
            time.sleep(3)
            return crypto_money, crypto_crypto
    else:
        print('see u next time. bye!')
        time.sleep(2)
        return crypto_money, crypto_crypto 


def sellcrypto(sellcrypto_crypto, sellcrypto_money):
    print('Welcome! Sell your crypto here!')
    sell_crypto_price = randint(100,450)
    print(f'The sell price of poopcoin is: {sell_crypto_price}')
    print('Would you like to sell your poopcoin? Y/N')
    answer = pyip.inputYesNo()
    answer = answer.lower()
    if answer == 'yes':
        print('Great! How many would you like to sell?')
        sellamount = pyip.inputNum()
        sellamountprice = sellamount * sell_crypto_price
        if sellamount <= sellcrypto_crypto:
            print('OK! Processing request...')
            time.sleep(1)
            sellcrypto_crypto -= sellamount
            sellcrypto_money += sellamountprice
            print('Done!')
            print(F'Changes made! Money {sellcrypto_money} Crypto: {sellcrypto_crypto}')
            return sellcrypto_money, sellcrypto_crypto
        else:
            print('Uh Oh! It seems like you have no enough\npoopcoin to suffice the amount needed!\nRefund Given.')
            time.sleep(3)
            return sellcrypto_money, sellcrypto_crypto
    else:
        print('I see. Bye!')
        return sellcrypto_money, sellcrypto_crypto


def billcheck(billcheck_bill, billcheck_money):
    print(f'Hi! Your incurring bills are {billcheck_bill}')
    if billcheck_bill >= 10000:
        print('Uh Oh...')
        time.sleep(1)
        print('You are bankrupt!!!')
        sys.exit()
    else:
        print('Pay the amount stated?')
        answer = pyip.inputStr()
        answer = answer.lower()
        if answer == 'y' or answer == 'yes':
            if billcheck_money >= billcheck_bill:
                print('Sure! Transferring cash...')
                billcheck_money -= billcheck_bill
                print(f'Money left: {billcheck_money}')
                return 0, billcheck_money
            else:
                print('Uh Oh! Looks like you don\'t have enough money!!! If your bills hit $10000, \n you are bankrupt!!!')
                return billcheck_money, billcheck_bill
        else:
            print('Goodbye!')
            return billcheck_bill, billcheck_money


#TEST PROGRAMS:
#After the 2 indents are items that dont need to be tested
#m, c = sellcrypto(100, 0)
#bill, money = billcheck(1000, 2000)
#time.sleep(2)
#bill, money = billcheck(10000, 2)
game()

