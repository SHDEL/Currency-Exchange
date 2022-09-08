
print('Program Currency Convert')
print('------------------------------------') 

while True:
    def option():
        print('---Press number options that you want to operate---')
        print('Press(1) USD ') 
        print('Press(2) EUR ')
        print('Press(3) GBP ')
        print('Press(4) CNY ')
        print('Press(5) INR ')
        opt_x = -1
        while opt_x != 1 and opt_x != 2 and opt_x != 3 and opt_x != 4 and opt_x != 5:
            opt_x = int(input('Press number options that you want to operate: '))
            if opt_x == 1 or opt_x == 2 or opt_x == 3 or opt_x == 4 or opt_x == 5:
                pass
            else :
                print("Only press 1 - 6 to operate")
                continue
        return opt_x 
    x_opt = option()

    money = int(input("Enter your money(THB): "))

    sum = 0
    ex_USD = 35.96
    ex_EUR = 35.72
    ex_GBP = 41.69
    ex_CNY = 5.17
    ex_INR = 0.4075	

    if x_opt == 1:
        text = 'USD '
    elif x_opt == 2:
        text = 'EUR '
    elif x_opt == 3:
        text = 'GBP '
    elif x_opt == 4:
        text = 'CNY '
    else :
        text = 'INR '

    print('------------------------------------')
    print('Your money:',money,'\n','Your currency: (THB)','\n','Exchange to:',text)
    print('------------------------------------')

    if x_opt == 1:
        sum = money/ex_USD
        print('Money form exchange THB->USD:',round(sum,2))
        
    elif x_opt == 2:
        sum = money/ex_EUR
        print('Money form exchange THB->EUR:',round(sum,2))

    elif x_opt == 3:
        sum = money/ex_GBP
        print('Money form exchange THB->GBP:',round(sum,2))

    elif x_opt == 4:
        sum = money/ex_CNY
        print('Money form exchange THB->CNY:',round(sum,2))

    elif x_opt == 5:
        sum = money/ex_INR
        print('Money form exchange THB->INR:',round(sum,2))
    
    print('------------------------------------')
    print('If you want to restart programe pls type "restart" or type "exit" to exit the program')
    restart = 'restart'
    restart_cmd = str(input(' ')) 
    if restart_cmd == restart:
        print('please wait')
    if restart_cmd == 'exit':
        print('please wait')
        print('Quit Program')
        exit()
    while restart_cmd != restart and 'exit':
        print('please enter "restart" or "exit"')
        restart_cmd = str(input(' '))
        if restart_cmd == restart :
            print('please wait')
        if restart_cmd == 'exit':
            print('please wait')
            print('Quit Program')
            exit()
        continue


    # elif ex[1] == 6:
    #     if ex[0] == 1:
    #         sum = money*ex_USD
    #         print('จำนวนเงินของUSD->THB:',round(sum,2))
            
    #     elif ex[0] == 2:
    #         sum = money*ex_EUR
    #         print('จำนวนเงินของEUR->THB:',round(sum,2))
            
    #     elif ex[0] == 3:
    #         sum = money*ex_GBP
    #         print('จำนวนเงินของGBP->THB:',round(sum,2))
            
    #     elif ex[0] == 4:
    #         sum = money*ex_CNY
    #         print('จำนวนเงินของCNY->THB:',round(sum,2))

    #     elif ex[0] == 5:
    #         sum = money*ex_INR
    #         print('จำนวนเงินของINR->THB:',round(sum,2))        

