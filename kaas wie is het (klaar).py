j = ('ja') # antwoord ja
n= ('nee') # antwoord nee

vraag_1 = ('is de kaas geel (ja / nee) ')                                                              #vraag 1
vraag_2 = ('Zitten er gaten in de kaas ( ja / nee ) ')                                                 #vraag 2
vraag_3 = ('heeft de kaas blauwe schimmel(ja / nee) ')                                                 #vraag 3
vraag_4 = ('heeft de kaas een korst? (ja / nee) ')                                                     #vraag 4
vraag_5 = ('is de kaas belachelijk duur? (ja / nee) ')                                                 #vraag 5
vraag_6 = ('is de kaas hard als steen (ja / nee) ')                                                    #vraag 6
vraag_7 = ('heeft de kaas een korst (ja / nee)')                                                       #vraag 7

g = ('cambert')                                                                                        #antwoord 1
h = ('mozzerella')                                                                                     #antwoord 2
i = ('emmenthaler')                                                                                    #antwoord 3                                                                         
K = ('leerdammer')                                                                                     #antwoord 4
l = ('parmigiano reggiano')                                                                            #antwoord 5
m = ('goudse kaas')                                                                                    #antwoord 6
o = ('bleu-de-rochbarron')                                                                             #antwoord 7
p = ('foume dambert ')                                                                                 #antwoord 8

antwoord_1=input(vraag_1)
if antwoord_1=='ja':

    antwoord_2=input(vraag_2)
    if antwoord_2 == "ja":
        antwoord_5=input(vraag_5)
        if antwoord_5=="ja":
            print (i)
        else:
            print (K)
    else: antwoord_6=input(vraag_6)
    if antwoord_6=='ja':
            print(l)
    else:
                 print(m)
    
    antwoord_3=input(vraag_3)
if antwoord_3=='ja':

    antwoord_4=input(vraag_4)

    if antwoord_4=="ja":
        print (o)
    else:
         print (p)
antwoord_7=input(vraag_7)
if antwoord_7=='ja':
    print(g)
else:
    print (h)

    
       

   

      