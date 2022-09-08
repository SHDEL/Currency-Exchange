
print('Program Convert สกุลเงิน')
print('------------------------------------') 

while True:
    def option():
        print('---กดเลขที่เป็นสกุลงินของคุณและสกุลเงินที่คุณต้องการแปลง---')
        print('กด(1) USD ดอลลาร์สหรัฐ') 
        print('กด(2) EUR ยูโร')
        print('กด(3) GBP ปอนด์เสตอร์ลิง')
        print('กด(4) CNY หยวนจีน')
        print('กด(5) INR รูปีอินเดีย')
        opt_x = -1
        while opt_x != 1 and opt_x != 2 and opt_x != 3 and opt_x != 4 and opt_x != 5:
            opt_x = int(input('ใส่เลขสกุลเงินที่ต้องการแปลง: '))
            if opt_x == 1 or opt_x == 2 or opt_x == 3 or opt_x == 4 or opt_x == 5:
                pass
            else :
                print("ใส่เลข 1 - 6 ใหม่อีกครั้งเพื่อดำเนินการ")
                continue
        return opt_x 
    x_opt = option()

    money = int(input("ใส่จำนวนเงินของคุณ(THB): "))

    sum = 0
    ex_USD = 35.96
    ex_EUR = 35.72
    ex_GBP = 41.69
    ex_CNY = 5.17
    ex_INR = 0.4075	

    if x_opt == 1:
        text = 'USD ดอลลาร์สหรัฐ'
    elif x_opt == 2:
        text = 'EUR ยูโร'
    elif x_opt == 3:
        text = 'GBP ปอนด์เสตอร์ลิง'
    elif x_opt == 4:
        text = 'CNY หยวนจีน'
    else :
        text = 'INR รูปีอินเดีย'

    print('------------------------------------')
    print('จำนวนเงินของคุณ:',money,'\n','สกุลเงินของคุณ: THB(บาทไทย)','\n','หน่วยเงินที่คุณต้องการแปลง:',text)
    print('------------------------------------')

    if x_opt == 1:
        sum = money/ex_USD
        print('จำนวนเงินของTHB->USD:',round(sum,2))
        
    elif x_opt == 2:
        sum = money/ex_EUR
        print('จำนวนเงินของTHB->EUR:',round(sum,2))

    elif x_opt == 3:
        sum = money/ex_GBP
        print('จำนวนเงินของTHB->GBP:',round(sum,2))

    elif x_opt == 4:
        sum = money/ex_CNY
        print('จำนวนเงินของTHB->CNY:',round(sum,2))

    elif x_opt == 5:
        sum = money/ex_INR
        print('จำนวนเงินของTHB->INR:',round(sum,2))
    
    print('------------------------------------')
    print('ต้องการรีโปรแกรมให้พิมพ์ restart หรือ พิมพ์ exit เพื่อหยุดการทำงาน')
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

