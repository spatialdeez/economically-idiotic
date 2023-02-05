
import time
import sys
from random import randint
import inputchecker


def game():
    Money = 1000
    Crypto = 0
    CryptoPerRun = 0
    runsecs = 0
    bill = 0
    workruntime = 20
    workpay = 100
    print('Economically Idiotic, version 0.5.5 by randomchez#8734')
    print('----------------GAME START----------------')
    time.sleep(0.5)
    print('You start with $1000.')
    time.sleep(3)


    while True:
        print('Select an Activity:')
        print('''(1) go to the market\n(2) check your idiotic phone\n(3) mine some crypto\n(4) Go to the bank (Coming soon!)\n(5) Work for money\n(6) Go to the lottery''')
        answer = inputchecker.numberchecker()
        if answer == 1:
            print('welcome to the market. Please check what you would like to buy.')
            print('1. Energy drink: $250 (Why...)\n2. Ticket: $10 (Wonder what it is used for...)\n')
            answer = inputchecker.numberchecker()
            if answer == 1:
                Money -= 250
                print('ok sure')
                time.sleep(1)
                print('You drank the energy drink...')
                time.sleep(1)
                print('You feel that power in you...')
                time.sleep(2)
                ignorethisvarjk = randint(1, 10)
                if ignorethisvarjk == 1 or ignorethisvarjk == 3 or ignorethisvarjk == 5 or ignorethisvarjk == 7 or ignorethisvarjk == 9:
                    print('...and nothing happened!')
                else:
                    print('...and deducted your work time! Yay!')
                    workruntime -= ignorethisvarjk

            if answer == 2:
                Money -= 10
                print('Playing slot machine now!')
                time.sleep(1)
                slotone = randint(1,10)
                slottwo = randint(1,10)
                slotthree = randint(1,10)
                print('Annnnnnnndddddd.......')
                if slotone == slottwo == slotthree:
                    print('JACKPOT!')
                    print('You got some money. (Use it on lottery since your luck is good ;)')
                else:
                    print('Aw man. better luck next time!')

        elif answer == 2:
            print('hi welcome to your phone.')
            print('(1) buy some crypto\n(2) sell your crypto\n(3) pay yur bills\n(4) Order something online lol.\n(5) Check your bank balance')
            answer = inputchecker.numberchecker()
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
                print('-3- bingchiling GPU (CPS: 5 Price: 4000)')
                print('-4- your mom on GPU (CPS: 8 price: 7000)')
                time.sleep(3)
                answer = inputchecker.numberchecker()
                if answer == 1:
                    print('so u want to buy slow shit gpu? It increases per run by 10 secs! --NO REFUND--')
                    answer = inputchecker.alpchecker()
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
                    answer = inputchecker.alpchecker()
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
                    print('so u want to buy bingchiling GPU? It increases per run by 5 secs! --NO REFUND--')
                    answer = inputchecker.alpchecker()
                    answer = answer.lower()
                    if answer == 'yes' or answer == 'y':
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
                    print('so u want to buy your mom on GPU? It increases the run by 4 secs! --NO REFUND--')
                    answer = inputchecker.alpchecker()
                    answer = answer.lower()
                    if answer == 'yes' or answer == 'y':
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
            print('Feature coming soon!')
        elif answer == 5:
            print('---WORK---')
            print('Starting work...')
            print(f'Every work time is 20secs, increasing by 2 everytime you try again, but the pay increases. \nEnergy drinks (coming soon) decrease the work timing\n Your pay:{workpay} Your work run time: {workruntime}\n Ctrl - c to stop working halfway, no pay given.')
            time.sleep(5)
            try:
                workplaces = ['mcdonalds','KFC','boigur king','chinese cusine','mexico cusine', 'pyramid technology', 'Retail walnuts', 'Vegan teacher\'s lab']
                workplaces = workplaces[randint(0,4)]
                print(f'You work at {workplaces} today.')
                success = 'y'
                for i in range(workruntime):
                    if success == 'y':
                        time.sleep(1)
                    else:
                        break
                    if i == workruntime / 2:
                        print('Halfway done!')
                        questions = randint(2, 10)
                        for q in range(questions):
                            one = randint(1, 10)
                            two =randint(1, 10)
                            answer = one + two
                            print(f'What is {one} + {two}?')
                            playerinput = inputchecker.numberchecker()
                            if answer == playerinput:
                                print('Well done!')
                                success = 'y'
                            else:
                                print('You failed! Leaving workplace...')
                                success = 'n'
                                break
                           
                if success != 'n':
                    print(f'You come back home tired, with a paycheck of: {workpay}')
                    Money += workpay
                    workpay += randint(10,50)
                    workruntime += 2
                else:
                    continue
            except KeyboardInterrupt:
                print('You left the workplace.')
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
            bet = inputchecker.numberchecker()
            if bet < 1:
                print('You did not place a bet!')
                continue
            else:
                Money -= bet
                print('First number:')
                firstlotnum = inputchecker.numberchecker()
                print('Second number:')
                seclotnum = inputchecker.numberchecker()
                print('Third number:')
                Thirdtlotnum = inputchecker.numberchecker()
                print('Fourth number:')
                fourthlotnum = inputchecker.numberchecker()
                print('Bonus number:')
                bonuslotnum = inputchecker.numberchecker()
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
    answer = inputchecker.alpchecker()
    answer = answer.lower()
    if answer == 'y' or answer == 'yes':
        print('you are so cool. how many?')
        numberofcrypto = inputchecker.numberchecker()
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
    answer = inputchecker.alpchecker()
    answer = answer.lower()
    if answer == 'y' or answer == 'yes':
        print('Great! How many would you like to sell?')
        sellamount = inputchecker.numberchecker()
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
        answer = inputchecker.alpchecker()
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
