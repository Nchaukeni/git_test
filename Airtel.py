 #Assignment Solution for question number 4 AIRTEL MANU

def GetNumber(): #this function input number from user
                #User has to dial *140# or be stuck in the while loop
    number = input()
    if number != '*140#':
        b = 0
        while b == 0:
            print ('Please enter *140#')
            number = input()
            if number == '*140#':
                b = 1
            else:
                b = 0
    return True

#This fuction is for selecting the mode of payment for what is being purchased
def paymentOption():
    menu = {'1. Main Account':'Your transaction is being processed. You will \nreceive a confirmation SMS soon', '2. Airtel Money':'Your transaction is being processed. You will \nreceive a confirmation SMS soon','00 Back':' '}
    for i in menu:
        print (i)
    userChoiceP = input()
    if userChoiceP == '1':
        print (menu['1. Main Account'])
    if userChoiceP == '2':
        print (menu['2. Airtel Money'])
    if userChoiceP == '00':
        return userChoiceP
   
def DisplayManu(): #This fuction displays the main airtel manu
    print ('Airtel Now 100% 4G Konse')
    print ('1. Ikali - Data and Voice')
    print ('2. Airtel Pack')
    print ('3. All Networks')
    print ('4. K5 CHE')
    print ('5. Buy for Other')
    print ('6. Balance Check')
    print ('7. Data')
    print ('8. INTL calling & roaming')
    userChoice1 = input()
    return userChoice1

def IkaliManu(): #Items on the ikali manu are are stored in a list called items
    items = [' ','1. K7=60 Airtel Min,24Hrs','2. K15=135 Airtel Min,7Day','3. K30=150 Airtel Min,14Day','4. K10=1.2GB,24Hrs','5. K50=6GB,7Day','6. K100=10GB,30Day','7. K200=25GB,30Day','00 Back']
    
    print (items[0])
    print (items[1])
    print (items[2])
    print (items[3])
    print (items[4])
    print (items[5])
    print (items[6])
    print (items[7])
    
    userChoice2 = input()
    if userChoice2 == '00':
        return True
    else:
        userChoice2 = int (userChoice2) #Converts userChoice to integer
        print ('Thank you for selecting ikali ',items[userChoice2],' Choose payment option below')
        paymentOption()
        
    
def AirtelPack ():
    items1 = {'1. For 24hours Daaily Pack':'1.K2=10Min+100SMS 2.K3=18Min+15MB+150SMS 3.K5=36Min+30MB+250SMS 4.K10=90Min+100MB+500SMS 00.Back','2. For Weekly Pack':'1.K20=180Min+200MB+500SMS 2.K10=55Min+75MB+200SMS 3.K5=22Min+100SMS 00.Back','3. Monthly Pack':'1.K50=300Min+250MB+500SMS 2.K100=800Min+1GB+1000SMS 3.K200=2000Min+3GB+2000SMS 00.Back','00 Back':' '}
    list1 = ['1','2','3','00']
    list2 = list(items1.keys()) #List2 is a list of key values form the dictionary items1
    b = True
    c = 0
    while b == True:   #This reprints the Airtel pack manu everytime the user choice is not on manu
        if c>0:
            print ('invalid request')
            
        print (list2[0])
        print (list2[1])
        print (list2[2])
        print (list2[3])
        userChoice3 =input()
        if userChoice3 not in list1:
            c = c+1
            b = True
        else:
            b = False
    if userChoice3 == '1':
        b = True
        c = 0
        list3 = items1['1. For 24hours Daaily Pack'].split()
        list4 = ['1','2','3','4','00']
        while b == True:
            if c>0:
                print ('invalid request')
            print (list3[0])
            print (list3[1])
            print (list3[2])
            print (list3[3])
            print (list3[4])
            userChoice4 =  input()
            if userChoice4 not in list4:
                c = c+1
                b = True 
            else:
                b = False
        if userChoice4 == '00':
                AirtelPack ()
        if userChoice4 in list4 and userChoice4 != '00':
            userChoiceP = paymentOption()
            if userChoiceP == '00':
                AirtelPack ()
    if userChoice3 == '2':
        b = True
        c = 0
        list5 = items1['2. For Weekly Pack'].split()
        list6 = ['1','2','3','00']
        while b == True:
            if c>0:
                print ('invalid request')
            print (list5[0])
            print (list5[1])
            print (list5[2])
            print (list5[3])    
            userChoice4 = input()
            if userChoice4 not in list6:
                c = c+1
                b = True
            else:
                b = False
        if userChoice4 == '00':
            AirtelPack ()     
        if userChoice4 in list6 and userChoice4 != '00':
            userChoiceP = paymentOption()
            if userChoiceP == '00':
                AirtelPack ()
    if userChoice3 == '3':
        b = True
        c = 0
        list7 = items1['3. Monthly Pack'].split()
        list8 = ['1','2','3','00']
        while b == True:
            if c>0:
                print ('invalid request')
            print (list7[0])
            print (list7[1])
            print (list7[2])
            print (list7[3])    
            userChoice4 = input()
            if userChoice4 not in list8:
                c = c+1
                b = True
            else:
                b = False
        if userChoice4 == '00':
            AirtelPack ()
        if userChoice4 in list8 and userChoice4 != '00':
            userChoiceP = paymentOption()
            if userChoiceP == '00':
                AirtelPack ()
    if userChoice3 == '00':
        DisplayManu()

def AllNetworks ():
    print ('Thanks for selecting All networks minutes Packs. Press:')
    items2 = {'1. For 24hours Daaily Pack':'1.K2=7Min+50SMS 2.K5=18Min+25MB+150SMS 3.K10=45Min+100MB+300SMS 00.Back','2. For Weekly Pack':'1.K50=225Min+500MB+500SMS 2.K20=75Min+150MB+200SMS 3.K10=33Min+50MB+100SMS 4.K5=15Min+50SMS 00.Back','3. Monthly Pack':'1.K100=450Min+500MB+500SMS 2.K150=725Min+1GB+1000SMS 3.K200=1000Min+2GB+2000SMS 00.Back','00 Back':' '}
    list9 = list(items2.keys())
    list10 = ['1','2','3','00']
    b = True
    c = 0
    while b == True:
        if c>0:
            print ('invalid request')
        print (list9[0])
        print (list9[1])
        print (list9[2])
        print (list9[3])    
        userChoice5 = input()
        if userChoice5 not in list10:
            c = c+1
            b = True
        else:
            b = False

    if userChoice5 == '00':
        DisplayManu()
    if userChoice5 == '1':
        list11 = items2['1. For 24hours Daaily Pack'].split()
        list12 = ['1','2','3','00']
        b = True
        c = 0
        while b == True:
            if c == 0:
                print ('Press:')
            if c>0:
                print ('invalid request')
            print (list11[0])
            print (list11[1])
            print (list11[2])
            print (list11[3])
            userChoice6 = input()
            if userChoice6 not in list12:
                c = c+1
                b = True
            else:
                b = False
        if userChoice6 == '00':
            AllNetworks ()
        else:
            paymentOption()

    if userChoice5 == '2':
        list13 = items2['2. For Weekly Pack'].split()
        list14 = ['1','2','3','4','00']
        b = True
        c = 0
        while b == True:
            if c == 0:
                print ('Press:')
            if c>0:
                print ('invalid request')
            print (list13[0])
            print (list13[1])
            print (list13[2])
            print (list13[3])
            print (list13[4])
            userChoice6 = input()
            if userChoice6 not in list14:
                c = c+1
                b = True
            else:
                b = False
        if userChoice6 == '00':
            AllNetworks ()
        else:
            paymentOption()

    if userChoice5 == '3':
        list15 = items2['3. Monthly Pack'].split()
        list16 = ['1','2','3','00']
        b = True
        c = 0
        while b == True:
            if c == 0:
                print ('Press:')
            if c>0:
                print ('invalid request')
            print (list15[0])
            print (list15[1])
            print (list15[2])
            print (list15[3])
            userChoice6 = input()
            if userChoice6 not in list16:
                c = c+1
                b = True
            else:
                b = False
        if userChoice6 == '00':
            AllNetworks ()
        else:
            paymentOption()

def K5CHE ():
    print ('Thanks for selecting K5 CHE. Press:')
    list17 = ['1. Airtel daily pack: 36Min+30MB+250SMS','2. Airtel weekly pack: 22Min+100SMS','3. 1.5GB Night Pack','4. 200MB 24Hrs','00 Back']
    list18 = ['1','2','3','4','00']
    b = True
    c = 0
    while b == True:
        if c>0:
            print ('invalid request')
        print (list17[0])
        print (list17[1])
        print (list17[2])
        print (list17[3])
        print (list17[4])
        userChoice6 = input()
        if userChoice6 not in list18:
            c = c+1
            b = True
        else:
            b = False
    if userChoice6 == '1':
        userChoiceP = paymentOption()
        if userChoiceP == '00':
            K5CHE()     
    if userChoice6 == '2':
        print ('Please choose payment method. Press:')
        userChoiceP = paymentOption()
        if userChoiceP == '00':
            K5CHE()
    if userChoice6 == '3':
        print ('Thank you for selecting the SoChe Night Data \nPack. For only K5, get 1.5GB to use between \n 00:01AM and 05:00AM')
        userChoiceP = paymentOption()
        if userChoiceP == '00':
            K5CHE()
    if userChoice6 == '4':
        print ('you have selected 200MB bundle for K5.0.       \nPress')
        userChoiceP = paymentOption()
        if userChoiceP =='00':
            K5CHE()
    if userChoice6 == '00':
        DisplayManu()
        
def BuyForOther ():
    print ('Please enter the subscriber\'s number you wish\n to purchase a So Che Pack for (097X XXXXXX/\n                       077X XXXXXX)' )
    userChoice6 = input()
    length = len(userChoice6)
    if (userChoice6[2] != '7' and length != 10) or (length != 10 and userChoice6[2] == '7') or (length == 10 and userChoice6[2] != '7'):
        print ('Dear customer, the entered number is not\n                 Airtel number ', userChoice6)
    else:
        print('1. Airtel Pack\n2. All networks\n3. 1.5GB Night Pack\n00 Back')
        userChoice7 = input()
        if userChoice7 == '1':
            AirtelPack ()
        if userChoice7 == '2':
            AllNetworks ()
        if userChoice7 == '3':
            userChoiceP = paymentOption ()
            if userChoiceP == '00':
                DisplayManu()
        if userChoice7 == '00':
            DisplayManu()

def Data():
    Manu3 = {'1. Ikali - Data and Voice':'1.K7=60Min_Airtel_Min,24Hrs 2.K15=135_Airtel_Min,7Day 3.K30=150_Airtel_Min,14Day 4.K10=1.2GB,24Hrs 5.K50=6GB,7Day 6.K100=10GB,30Day 7.K200=25GB,30Day 00.Back ','2. Tonse Internet Bundles':'1.Daily 2.Weekly 3.Monthly 4.60_or_90Days 5.90_to_365Days 6.No_expiry_bundles 00_Back', '3. 4G Offer-5GB, 60Min':'1.To_activate_free_5GB_and_60Min_offer 00 Back','4. Smartphone offer':'1._To_activate_100%_Extra_data_for_90_days 00_Back', '5. Buy for other':'','6. Check balance':' ', '7. Cancel auto':'1.Internet_bundle 00_Back ','n Next':' '}
    list19 = list(Manu3.keys())
    list20 = ['1','2','3','4','5','6','7','n']
    b = True
    c = 0
    while b == True:
        if c>0:
            print ('invalid request')
        print ('Airtel Now 100% 4G Konse')
        print (list19[0])
        print (list19[1])
        print (list19[2])
        print (list19[3])
        print (list19[4])
        print (list19[5])
        print (list19[6])
        print (list19[7])
        userChoice6 = input()
        if userChoice6 not in list20:
            c = c+1
            b = True
        else:
            b = False
    if userChoice6 == '6':
        print ('Dear Customer, your balance request is being processed. You will receive a confirmation message shortly')
    if userChoice6 == '7':
        list21 = Manu3['7. Cancel auto'].split()
        list22 = ['1','00']
        b = True
        c = 0
        print ('To cancel auto renewal. Please select:')
        while b == True:
            if c > 0:
                print ('Invalid option')
            print (list21[0])
            print (list21[1])
            userChoice7 = input()
            if userChoice7 not in list22:
                c = c +1
                b = True
            else:
                b = False
        if userChoice7 == '00':
            DisplayManu()
        else:
            print ('You currently do not have a Data Bundle on auto-renew')
    if userChoice6 == '1':
        list23 = Manu3['1. Ikali - Data and Voice'].split()
        list24 = ['1','2','3','4','5','6','7','00']
        b = True
        c = 0
        while b == True:
            if c>0:
                print ('invalid request')
            print ('Select')
            print (list23[0])
            print (list23[1])
            print (list23[2])
            print (list23[3])
            print (list23[4])
            print (list23[5])
            print (list23[6])
            print (list23[7])
            userChoice7 = input()
            if userChoice7 not in list24:
                c = c+1
                b = True
            else:
                b = False
        if userChoice7 == '1' or '3' or '4' or '5' or '6' or '7':
            userChoiceP = paymentOption()
            if userChoiceP == '00':
                DisplayManu()
    if userChoice6 == '2':
        list25 = Manu3['2. Tonse Internet Bundles'].split()
        list26 = ['1','2','3','4','5','6','00']
        b = True
        c = 0
        while b == True:
            if c>0:
                print ('invalid request')
            print ('Select')
            print (list25[0])
            print (list25[1])
            print (list25[2])
            print (list25[3])
            print (list25[4])
            print (list25[5])
            print (list25[6])
            userChoice7 = input()
            if userChoice7 not in list26:
                c = c+1
                b = True
            else:
                b = False
        Package = {'1. Daily':'1.100MB_24hrs-K2.0 2.350MB_24hrs-K5.0 3_1.2GB_24hrs-K10 00.Back','2. Weekly':'1.800MB-K10.0 2.2GB-K20.0 3.6GB-K50.0 OO.Back','3. Monthly':'1_1.5GB-K30.0 2_5GB-K60.0 3_10GB-K100.0 4_25GB-K200.0 00_Back','4. 60 or 90Days':'1.35GB_60days-K700.0 2.50GB_90days-K900.0 3.100GB_90days-K1,500 00.Back','5. 90 t0 365 Days':'1.90days_bundles 2.180days_bundles 3.365days_bundles 00.Back','6. No Expiry Bundles':'1.1GB-K90.0 2.2.5GB-K200.0 3.5.5GB-K400.0 00.Back'}
        if userChoice7 == '1':
            list27 = Package['1. Daily'].split()
            list28 = ['1','2','3','00']
            b = True
            c = 0
            while b == True:
                if c>0:
                    print ('invalid request')
                print ('Select')
                print (list27[0])
                print (list27[1])
                print (list27[2])
                print (list27[3])
                userChoice8 = input()
                if userChoice8 not in list28:
                    c = c+1
                    b = True
                else:
                    b = False
                
            if userChoice8 == '1' or '2' or '3':
                userChoiceP = paymentOption()
                if userChoiceP == '00':
                    DisplayManu()
            else:
                DisplayManu()
        if userChoice7 == '2':
            list27 = Package['2. Weekly'].split()
            list28 = ['1','2','3','00']
            b = True
            c = 0
            while b == True:
                if c>0:
                    print ('invalid request')
                print ('Select')
                print (list27[0])
                print (list27[1])
                print (list27[2])
                print (list27[3])
                userChoice8 = input()
                if userChoice8 not in list28:
                    c = c+1
                    b = True
                else:
                    b = False
            if userChoice8 == '1' or '2' or '3':
                userChoiceP = paymentOption()
                if userChoiceP == '00':
                    DisplayManu()
            else:
                DisplayManu()
                
            
DisplayManu()
 
                    
    
            
                
            
        
        
        
    
            
                
            
            
        
        
        
        
            
            
        
    
    
    
    
    
    

    
    
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
   
    
    
        

















