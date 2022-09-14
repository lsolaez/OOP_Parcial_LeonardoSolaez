import random
class User:
    def __init__(self, time: str, movie: str, seat: list(int), n_ticket: int, Typeticket: str):
        self.time=time
        self.movie=movie
        self.seat=seat
        self.n_ticket=n_ticket
        self.Typeticket=Typeticket
        self.used=[]
        

    def generatorTicket(self):
        for i in range(self.n_ticket):
            capacity=random.randint(100, 200)
            seat_used=self.seat
            self.used.append(seat_used)


class seats:
    def __init__(self, Seat: User):
        self.Seat=Seat

    def aviable_seats(self, used: list(int)):
        for i in range(used.lenght):
            capacity-=1
        