## Collatz Conjecture

Introduce the problem using pencil and paper. Youcubed has made the Collatz conjecture part of its week of inspirational math content. Essentially, you start with any positive integer, integer n. If n is even, divide it by two. If n is odd, multiply it by 3 and add 1. Repeat this process and see what happens. 
   
   - [Oh Hail the Elephant — Youcubed WIM](https://www.youcubed.org/wp-content/uploads/2019/08/WIM-Oh-Hail-the-Elephant-Grades-6-8.pdf)

After students get tired of calculating by hand (and they will) suggest writing a program that does the work for them. In its most basic form you can write a function in python in about 10 lines using basic syntax. The `%` in python is the modulo operator. It returns only the remainder. The `//` operation performs division and only returns the integer component of the quotient. This prevents the script from outputting a bunch of numbers with a trailing `.0`. 

```python
def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result
```

As an added bonus, with python handling the arithmetic, students free up brain power to explore other awesome questions. E.g., which numbers lead to longer sequences? Which numbers lead to shorter sequences? What happens if you start with a negative? Does this work with decimals?

   - [Need to Teach modular arithmetic?](https://youtu.be/5OjZWSdxlU0)
   - [Sample program in Trinket](https://trinket.io/python/37fae0a0f9)
   - [Sample program in Colab](collatz_sequence.ipynb)
 

Now that students have explored, talk about the Collatz conjecture. The conjecture states that for all natural numbers, this sequence results in the final loop of 4 -> 2 -> 1 -> 4 -> 2 -> 1... But it is still an open problem worth $1 million and no one knows how to prove it. This can lead to a great discussion on what does it mean to *prove* things and why that matters in math. Then share the Numberphile video below that shows how artists have created a visual representation of the sequence. (I recommend starting the video at 2:12.) There is also a PDF that can be printed and shared with students that they can color. Finally, I show the YouTube video *Visualizing Collatz*. It is an artistic response to the Numberphile video. There is also a handy blog that contains all the Numberphile resources on the Collatz Conjecture. 

   - [Collatz Conjecture in Color — Numberphile](https://www.youtube.com/watch?v=LqKpkdRRLZw)
   - [Coloring PDF](https://static1.squarespace.com/static/548b5b70e4b0b57ba182907d/t/58da8df81b10e35ee212221a/1490718217324/seaweed_file.jpg)
   - [Visualizing Collatz — Adrian M Wadley](https://www.youtube.com/channel/UC_Izu8EyqRjJBdWM9wLhWlg)
   - [Blog by Brady Haran — The Collatz Conjecture in Color](https://www.bradyharanblog.com/blog/the-collatz-conjecture-in-colour)

Extension
   - Project Euler is a collection of math problems designed to be solved with code. It is language agnostic, so you so can solve the problems using whatever language you would like. The Project Euler problem 14 on the website deals with the Collatz Conjecture. [Longest Collatz Sequence](https://projecteuler.net/problem=14)
   - [Visualize](./visualize_collatz.py)


