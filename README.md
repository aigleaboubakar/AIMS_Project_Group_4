#Task 1
The exact_probability function calculates the exact probability that two people share a birthday.
The computer is instructed to return 1 if the number of people exceeds the number of days.
We calculate the probability that all birthdays are distinct.
The desired probability is 1 minus the probability that all birthdays are distinct.

#Task 2
This function checks whether a list contains at least one duplicate value. It starts with an empty list called seen, then loops through each value in the input: if the value is not already in seen, it is added, and if it is already there, the function immediately returns True because a repeat has been found. If the loop finishes without finding any repeated value, the function returns False.

#Task 3
function simulates the birthday experiment several times.
First, it initializes a counter to zero. 
Then, for each trial, it randomly assigns a birthday to each of the n people and stores the birthdays in a list. 
It uses has_repeat() to check if at least two people have the same birthday.
If there is a repeated birthday, it increases the counter by one.
Finally, it divides the number of successful trials by the total number of trials
to estimate the probability of having at least two people with the same birthday.

#Task 4
The program displays a table of exact_probability() and simulate() for these values of n:10,20,23,30,40,50

#Task 5
This code finds the smallest number of people, n, needed for the probability that at least two of them share a birthday to reach 50% or more .
In the first part, it starts at n = 1 and increases n by 1 each loop, calling exact_probability(n) to compute the exact probability using the default 365 days, 
and as soon as that probability is at least 0.5 it prints n and stops with break, giving 23. 
The second part works the same way but with days=100, and it prints the smallest n that reaches a probability of at least 0.5 in that case,
which is about 13.

#Extra
The  simulation code  tries to have the number of people that we need to have three people sharing the same birthday with 0.5 of probability :
- we create a function has_triple(values) which return True if there is a value in values repeated 3 times (the first one). 
- And then we create a function simulation (trials = 10100, days = 365) which returns the number n  and the probability (approximatly) to have three people sharing the same  birthday . 
And after compilation, we have approximatly that n = 88 with the probability 0.5.

#Think and explain
The exact_probability(366) is 1 because P(all diffrent) for n = 366 gives (365/365)*(364/365)*(363/365)*.....*(0/365) = 0,
with(366 factors)
P(two people share a birthday) = 1 - 0 = 1
