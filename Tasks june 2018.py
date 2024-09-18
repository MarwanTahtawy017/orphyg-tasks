totalcost=0
totalorders=0
totalcompcost=0
i=0
P3stock=10
P5stock=10
P7stock=10
R16stock=10
R32stock=10
ST1stock=10
ST2stock=10
SC19stock=10
SC23stock=10
miniCstock=10
midiCstock=10
U2stock=10
U4stock=10
compcost=[0]*10
date=[0]*10
order=[0]*10


purchase=input("Do you want to buy a computer? Yes or No?")

while purchase=="yes":
 processor=input("What kind of processor do you want? P3, P5, or P7?")
 while processor!="p3" and processor!="p5" and processor!="p7":
     print("Input again.")
     processor=input()
 if processor=="p3":
     if P3stock>0:
      totalcost=totalcost+100
      Pprice=100
      Pestimate="cs03"
      P3stock=P3stock-1
     elif P3stock==0:
         print("This component is out of stock.")
 if processor=="p5":
     if P5stock>0:
      totalcost=totalcost+120
      Pprice=120
      Pestimate="cs05"
      P5stock=P5stock-1
     elif P5stock==0:
         print("This component is out of stock.")
 if processor=="p7":
     if P7stock>0:
      totalcost=totalcost+200
      Pprice=200
      Pestimate="cs07"
      P7stock=P7stock-1
     elif P7stock==0:
         print("This component is out of stock.")
    
 ram=int(input("Choose RAM: 16 or 32?"))
 while ram!=16 and ram!=32:
     print("Input again.")
     ram=int(input())
 if ram==16:
     if R16stock>0:
      totalcost=totalcost+75
      Rprice=75
      Restimate="cs16"
      R16stock=R16stock-1
     elif R16stock==0:
         print("This component is out of stock.")
 if ram==32:
     if R32stock>0:
      totalcost=totalcost+150
      Rprice=150
      Restimate="cs32"
      R32stock=R32stock-1
     elif R32stock==0:
         print("This component is out of stock.")

 storage=int(input("How many Terrabytes do you want your computer to store? 1 or 2?"))
 while storage!=1 and storage!=2:
      print("Input again.")
      storage=int(input())
 if storage==1:
     if ST1stock>0:
      totalcost=totalcost+50
      STprice=50
      STestimate="cs01"
      ST1stock=ST1stock-1
     elif ST1stock==0:
         print("This component is out of stock.")
 if storage==2:
     if ST2stock>0:
      totalcost=totalcost+100
      STprice=100
      STestimate="cs02"
      ST2stock=ST2stock-1
     elif ST2stock==0:
         print("This component is out of stock.")

 screen=int(input("Please choose a screen size from either 19'' or 23''"))
 while screen!=19 and screen!=23:
     print("Input again.")
     screen=int(input())
 if screen==19:
     if SC19stock>0:
      totalcost=totalcost+65
      SCprice=65
      SCestimate="cs19"
      SC19stock=SC19stock-1
     elif SC19stock==0:
         print("This component is out of stock.")
 if screen==23:
     if SC23stock>0:
      totalcost=totalcost+120
      SCprice=120
      SCestimate="cs23"
      SC23stock=SC23stock-1
     elif SC23stock==0:
         print("This component is out of stock.")

 case=input("Please choose whether your case will be a Mini Tower or a Midi Tower.")
 while case!="midi" and case!="mini":
     print("Input again.")
     case=input()
 if case=="mini":
     if miniCstock>0:
      totalcost=totalcost+40
      Cprice=40
      Cestimate="csmn"
      miniCstock=miniCstock-1
     elif miniCstock==0:
         print("This component is out of stock.")
 if case=="midi":
     if midiCstock>0:
      totalcost=totalcost+70
      Cprice=70
      Cestimate="csmd"
      midiCstock=midiCstock-1
     elif midiCstock==0:
         print("This component is out of stock.")

 usb=int(input("How many USB ports do you want your computer to have? 2 or 4?"))
 while usb!=2 and usb!=4:
     print("Input again.")
     usb=int(input())
 if usb==2:
     if U2stock>0:
      totalcost=totalcost+10
      Uprice=10
      Uestimate="cs2p"
      U2stock=U2stock-1
     elif U2stock==0:
         print("This component is out of stock.")
 if usb==4:
     if U4stock>0:
      totalcost=totalcost+20
      Uprice=20
      Uestimate="cs4p"
      U4stock=U4stock-1
     elif U4stock==0:
         print("This component is out of stock.")

 compcost[i]=totalcost*120/100
 totalcompcost=totalcompcost+compcost[i]
 date[i]=input("Please enter the date.")
 order[i]=i+1
 totalorders=totalorders+1

 print("You bought a",processor,"processor for $",Pprice,", a", ram,"GB RAM for $",Rprice,", a memory of", storage," TB for $", STprice,
      ", a screen of size",screen,"inches for $",SCprice,", a",case,"case for $",Cprice,", and finally",usb,"ports for $",Uprice)
 print("The computer will cost you $",compcost[i])
 print("Order Number:",order[i],
       "Product numbers: Processor:",Pestimate,
       "RAM:",Restimate,
       "Storage:",STestimate,
       "Screen:",SCestimate,
       "Case:",Cestimate,
       "USB ports:",Uestimate,
       "Date:",date[i])

 print("You sold a",processor,"processor for $",Pprice,", a", ram,"GB RAM for $",Rprice,", a memory of", storage," TB for $", STprice,
      ", a screen of size",screen,"inches for $",SCprice,", a",case,"case for $",Cprice,", and finally",usb,"ports for $",Uprice)
 print("The computer will bring you $",compcost[i])
 print("Order Number:",order[i],
       "Product numbers: Processor:",Pestimate,
       "RAM:",Restimate,
       "Storage:",STestimate,
       "Screen:",SCestimate,
       "Case:",Cestimate,
       "USB ports:",Uestimate,
       "Date:",date[i])

 i=i+1
 

 purchase=input("Do you want to buy another computer? Yes or No?")

P3sold=10-P3stock
P5sold=10-P5stock
P7sold=10-P7stock
R16sold=10-R16stock
R32sold=10-R32stock
ST1sold=10-ST1stock
ST2sold=10-ST2stock
SC19sold=10-SC19stock
SC23sold=10-SC23stock
miniCsold=10-miniCstock
midiCsold=10-midiCstock
U2sold=10-U2stock
U4sold=10-U4stock

print("There was a total of",totalorders,"orders today.")
print("You sold a total of",P3sold,"P3 processors,",P5sold,"P5 processors,",P7sold,"P7 processors,",R16sold,"16 GB RAMs,",R32sold,"32 GB RAMs,",
      ST1sold,"1 TB storage,",ST2sold,"2 TB storage,",SC19sold,"19'' screens,",SC23sold,"23'' screens,",miniCsold,"Mini cases,",midiCsold,"Midi cases,",
      U2sold,"Compuetrs with 2 USB ports,",U4sold,"Computers with 4 USB ports.")
print("You sold computers of a total price of",totalcompcost)
