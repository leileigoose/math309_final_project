# Problem 1
The following “Miniopoly” is a very rough approximation to the game of Monopoly. The
round board has 40 “squares,” or landing places. Squares 0 and 40 are the same; and this
square is called “Go.” A player starts with $200 on Go, and on each turn, rolls a pair of dice
to determine a move, which will be equal to the sum rolled. Squares 2, 7, 17, 22, 33, and 36
are “follow instructions on card” squares. The instructions are receive $50, or $100, or $200
or pay $100 or $150 and are equally likely. Squares 0, 10, and 20 are “free”: nothing happens
there. Square 30 is “Go to jail.” Passing or landing on Go pays $200. Being in jail means
that on one’s turn, if a roll is “doubles” (i.e. two 1’s or two 2’s or ... or two 6’s) then the
player “gets out of jail” and moves the value of the doubles from square 10; otherwise, the
player pays $10, stays in jail and doesn’t move. On any other square, like 29 for instance,
pay $29 ( to the “bank,” an infinite source or sink of money). If at any time a player’s money
falls to $0 or below, that player loses (and the game is over for that player). To be done:
simulate a game of Miniopoly for 20 rolls, or bankruptcy, and observe the amount of money,
the fortune, of the player at that time. Bankruptcy means fortune equal to or less than $0.
Simulate 10000 games and histogram the fortune

# Problem 2
Problem #2

# Problem 3
The problem in this section is the same for all groups.
The length of the arc between any two points a and b for a function f (x) is defined as
S = ∫ √ (1 + (f ′(x))2 dx)
Write a program to that takes as inputs a function f (x), an interval [a, b] and outputs the
arc length over [a, b]. The program should use centered difference to approximate f ′(x) and
trapezoidal rule to approximate the integral. Hence, the program should also take in n, the
number of sub-divisions of the interval [a, b] as input. Use the same n for the approximations
of the derivative and the integral.
