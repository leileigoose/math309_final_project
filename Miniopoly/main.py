from die import *
from player import *
import matplotlib.pyplot as plt

p1 = Player(200, 0, False)
d1 = Die()
d2 = Die()


follow_card = [2, 7, 17, 22, 33, 36]
instructions = [50, 100, 200, -100, -150]
free = [0, 10, 20]
jail = 30

money_record = []


def play_game():
    p1 = Player(200, 0, False)
    while p1.get_bank() >= 0 and p1.get_move() < 20:
        r1 = d1.roll()
        r2 = d2.roll()
        roll = r1 + r2
        double = r1 == r2
        p1.set_space(roll)

        if p1.is_in_jail():
            if double:
                p1.set_jail(False)
                p1.set_space(roll)
                Player.set_move()
            else:
                p1.set_bank(-10)
                p1.set_space(-roll)
                Player.set_move()

        elif p1.get_space() >= 40:
            p1.set_bank(200)
            p1.set_space(-40)

            if p1.get_space in follow_card:
                choice = random.choice(instructions)
                p1.set_bank(choice)
                Player.set_move()

            elif p1.get_space() not in free:
                p1.set_bank(-p1.get_space())
                Player.set_move()

            else:
                Player.set_move()

        else:
            if p1.get_space() == 30:
                p1.set_space(-20)
                p1.set_jail(True)
                Player.set_move()

            elif p1.get_space() in follow_card:
                choice = random.choice(instructions)
                p1.set_bank(choice)
                Player.set_move()

            elif p1.get_space() in free:
                Player.set_move()
            else:
                p1.set_bank(-p1.get_space())
                Player.set_move()
    Player.reset_move()
    return p1.get_bank()


for i in range(9999):
    money_record.append(play_game())

bins = [-150,-100,-50,0,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200,1250,1300,1350,1400,1450,1500]
plt.hist(money_record,bins)
plt.show()
