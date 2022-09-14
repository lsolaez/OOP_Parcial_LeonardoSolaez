from MovieTickets import *

Ticket=User(time='14:15', movie='Lion Heart', seat='22,23', n_ticket=2, Typeticket='VIP')

Ticket.generatorTicket()

seats_Notused=seats()

seats_Notused.aviable_seats(used=(22,23))

print(seats_Notused)

