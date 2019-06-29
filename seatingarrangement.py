def seat(seat_num) :
    if(seat_num%12 <= 6 and seat_num%12 !=0 ):
        side=seat_num%6
        if(side==1):
             print(seat_num+11, "WS")
        if(side==2):
            print(seat_num+9, "MS")
        if(side==3):
            print(seat_num+7, "AS")
        if(side==4):
            print(seat_num+5, "AS")
        if(side==5):
            print(seat_num+3, "MS")
        if(side==0):
            print(seat_num+1, "WS")
    else:
        side=seat_num%6
        if(side==1):
             print(seat_num-1, "WS")
        if(side==2):
            print(seat_num-3, "MS")
        if(side==3):
            print(seat_num-5, "AS")
        if(side==4):
            print(seat_num-7, "AS")
        if(side==5):
            print(seat_num-9, "MS")
        if(side==0):
            print(seat_num-11, "WS")


total_no_of_seats=int(input());
for i in range (0,total_no_of_seats) :
     seat_num=int(input());
     seat(seat_num);
