## Sieve of Eratosthenes

The [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) is an algorithm for finding prime numbers up to a given number n. Here is how it works: Write down a list of positive integers starting with 2. Since two is prime, it stays on the list. Cross off the remaining multiples of 2. Move to the next number not yet crossed off. In this case, 3. Three is also prime! It stays on the list.  Cross off any remaining multiples of 3. Repeat this process of moving to the next prime and crossing off multiples until you reach n (Bonus question: you only ever need to check up to the square root of n, why?). Eddie Woo has a great mini-lecture on this topic. [Mathigon](https://mathigon.org) also has a beautiful resource on this.

- [5 minute Lecture on Sieve of Eratosthenes - Eddie Woo ](https://youtu.be/Lj_SzTGr-G4)
- [Prime Numbers - Mathigon](https://mathigon.org/course/divisibility/primes)

Ask students to recreate the Sieve of Eratosthenes using python. (This problem was suggested by u/shoombabi on Reddit.) 

- [Sample code using Colab](Sieve_of_Eratosthenes.ipynb)

