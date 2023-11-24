class Hall:
    def __init__(self,rows,cols,hall_no) -> None:
        self.seats={}
        self.show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
    def entry_show(self,id,movie_name,time):
        self.show_list.append((id,movie_name,time))
        seat = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(0)
            seat.append(row)
        self.seats[id] = seat
    def book_seats(self,id):
        row = int(input("Enter row : "))
        col = int(input("Enter coloumn : "))
        idlist=[i[0] for i in self.show_list]
        if id in idlist:
            if row - 1 > self.rows or col - 1 > self.cols:
                print("Sorry Invalid seat")
            elif self.seats[id][row - 1][col - 1] == 0:
                self.seats[id][row - 1][col - 1] = 1
                print("Your seat is booked")
            else:
                print("Sorry This seat is Booked, Try another.")
        else:
            print("There is no show running with that id. Try again with correct id!!!")
    def view_show_list(self):
        print("These are the currently airing shows.")
        for i in self.show_list:
            print(i)
    def view_available_seats(self,id):
        for i in self.seats[id]:
            for j in i:
                print(j,end=' ')
            print()
        
class Star_Cinema(Hall):
    __hall_list=[]
    def __init__(self, name) -> None:
        super().__init__(0, 0, 0)
        self.name = name

    def entry_hall(self, seats, show_list, rows, cols, hall_no):
        super().__init__(rows, cols, hall_no)
        self.__hall_list.append(self)

starcineplex=Star_Cinema("STAR CINE PLEX")
starcineplex.entry_hall(100,[],10,10,1)
starcineplex.entry_show(111,'Gothic Girl','11:30am')
starcineplex.entry_show(101,'Conjuring','8:30am')
starcineplex.entry_show(112,'SpiderWoman','9:30pm')
starcineplex.entry_show(113,'Batshow','6:30pm')
starcineplex.entry_show(114,'We kill we','3:30pm')
while(True):
    print("Welcome to STAR CINE PLEX")
    print("1.Show available shows")
    print("2.Show available seats")
    print("3.Book seat")
    print("4.Exit")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        starcineplex.view_show_list()
    elif(ch==2):
        idd=int(input("Enter show id:"))
        starcineplex.view_available_seats(idd)
    elif(ch==3):
        id=int(input("Enter show id:"))
        starcineplex.book_seats(id)
    elif(ch==4):
        break
    else:
        print("Enter a valid response")