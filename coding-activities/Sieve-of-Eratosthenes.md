## Sieve of Eratosthenes

1. The [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) is an algorithm for finding prime numbers up to a given number n. Here is how it works. Write down a list of positive integers starting with 2. Since two is prime, circle it then cross off the remaining multiples of 2. Move to the next number not yet crossed off. In this case, 3. Three is also prime! Circle it (or at least don't cross it off), then cross off any remaining multiples of 3. Repeat this process of moving to the next prime and crossing off multiples until you reach n (Bonus question: you only ever need to check up to the square root of n, why?). Eddie Woo has a great mini-lecture on this topic. 
    - [5 minute Lecture on Sieve of Eratosthenes - Eddie Woo ](https://youtu.be/Lj_SzTGr-G4)

2. Ask students to recreate the Sieve of Eratosthenes using python. (This problem was suggested by u/shoombabi on Reddit.) 
    - [Sample code using Colab](https://colab.research.google.com/drive/1nh8lHpB1xaiI20v2JWKDXhlM2ATYLsB9?usp=sharing)

