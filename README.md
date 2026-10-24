# Birthday Paradox Project

## Description

This project studies the birthday paradox in Python. The main idea is to determine the probability that at least two people in a group share the same birthday.

The program compares:

- the exact mathematical probability
- the probability obtained by random simulation

## Objectives

- Calculate the exact probability of a shared birthday
- Detect whether a list contains repeated values
- Simulate the experiment many times
- Find the smallest value of n for which the probability is at least 50%
- Repeat the calculation for a year of 100 days

## Main functions

### `exact_probability(n, days=365)`

This function calculates the probability that at least two people in a group of `n` people have the same birthday.

It works by computing the probability that all birthdays are different, then subtracting that value from 1.

### `has_repeat(values)`

This function checks whether a list contains at least one repeated value.

### `simulate(n, trials, days=365)`

This function simulates the birthday experiment many times and returns the fraction of simulations where at least two birthdays are the same.

## How the program works

1. It calculates the exact probability for different values of `n`.
2. It simulates the same experiment randomly.
3. It prints a comparison table between the exact and simulated results.
4. It searches for the smallest `n` such that the probability is greater than or equal to 0.5.
5. It repeats the same process for a year of 100 days.

## Example result

The program displays values for `n = 10, 20, 23, 30, 40, 50` and compares the exact probability with the simulated one.

## Expected result

For a normal year of 365 days, the smallest number of people needed for a probability of at least 50% is:

- `n = 23`

For a 100-day year, the smallest number is:

- `n = 13`


## Technologies used

- Python
- `random` module

## Authors
Group 4 / Students Names

Aboubakar Mahamat Ali
Amy Diop
Marie Hortense Saizonou
Abdourahmane Fadhoul
Moumouni Sawadogo


