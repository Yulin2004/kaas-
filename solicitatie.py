
input ('Wat is uw naam?')
dressuur = int(input('Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?'))
if dressuur >= 4: 
    jaar=input ('Bent u in bezit van een mbo-4 ondernemen? ja/nee. ')
else:
    input ('Helaas u voldoet niet aan de strenge eissen. ')

if jaar == 'ja':
 vrachtwagen=input('In bezit van een geldig Vrachtwagen rijbewijs? ja/nee. ')
else:
    print('Helaas u voldoet niet aan de strenge eissen.')
if vrachtwagen == 'ja':
        hoed=input('In bezit van een hoge hoed? ja/nee. ')
else:
    print ('Helaas u voldoet niet aan de strenge eissen. ')
if hoed == 'ja':
    snor=input ('Is man EN heeft Snor breder dan 10 cm OF is vrouw EN draagt rood krulhaar langer dan 20 cm ja/nee ')
else:
    print ('Helaas u voldoet niet aan de strenge eissen. ')
if snor == 'ja':
  beschrijving=input ('Geef een beschrijving. ')
lengte=input ('Bent u langer dan 1 meter 50 (1.50) ja/nee ')
if lengte== 'ja':
    gewicht=int(input('Wat is uwlichaamsgewicht? '))
if gewicht <=90:
    print ('Helaas u voldoet niet aan de strenge eissen. ')
else:
    certficaat=input('Heeft Certificaat “Overleven met gevaarlijk personeel” ja/nee.')
if certficaat =='ja':
    input ('Waarom zijn de bananen krom? press enter. ')
    input ('ha dit is een neppe solicitatie. grapje :) press enter.')
    print ('sorry dat ik u pest ;) press enter. ' )
    print ('oke we gaan weer door press enter. ')
    print ('uw sollicitatie is met succes beeindigt stuur uw CV om aangenomen te worden.')






