# SYMBINT v1

## Scope of the program

This program is part of a thesis submitted in partial fulfillment of the requirements for the degree of Mathematics at the University of Oviedo. The idea was to implement an algorithm that could compute an integral of a given rational function, i.e. that could find an antiderivative for a given quotient of polynomials with rational coefficients.

## General idea

Natural numbers (positive integers) are treated as strings, `'9'`, negative numbers are stored as lists `['-', '0'. '3']` and fractions are stored also as lists `['/', '1', '2']`. In case the fraction was negative, the sign would only affect the numerator, hence `['/', ['-', '0', '1'], '2']`. Any polynomial is stored in the natural way, that is, as a list of numbers. For instance, the polynomial x^2+x-1/2 is stored as `['1', '1', ['/','1','2']]`. As the task of inserting polynomials in this peculiar way may be exhausting and prone to errors, `CONVERT.py` takes good care of everything and is capable of converting any sequence of numbers stored in a python list into the correct form. For instance, applying `convert()` to `['1', '1', '1/2']` results in `['1', '1', ['/','1','2']]`. 

The scripts included in the program only assume that the computer is capable of adding natural numbers. Consequently, operations such as fraction multiplication, division, sum, polynomial addition, multiplication, etc. have been implemented and can be found in `fracops.py` and `polops.py`. These programs require the use of `gcd.py` to simplify fractions and of `CONVERT.py` to work correctly. 

As regards the integration algorithm, the key programs are `HermiteReduce.py`, `intlogpart.py`, `subresultant.py`and `symbint.py`. The inner workings of each of these is more complicated to explain and more information can be found in Bronstein's book. These programs require of a free square factorization of polynomials which is done by `yun.py`. It is also important to note that `subresultant.py` makes use of the `FieldExtension.py` file. This code has been developed to account for algebraic manipulations involving polynomials with coefficientes in a simple extension of the rational numbers. This extension may be algebraic or transcendental. In the second case, however, we note that only polynomials in the extension are considered, not quotients of polynomials.

## Instructions

- This program requires Python 3 to run, so make sure you have it installed in your computer.
- To run the program execute symbint.py and follow the steps
- To terminate the program type `exit`

## Notes

Please understand that this is the result of many hours of work and that there might still be errors. I have tried to produce a readable code, and although it is not full of comments, it should not be too difficult to follow. I am a student of Mathematics and Physics, so please take that into consideration when judging my code. All the coding in python is my own work, exceptuating the algorithms such as Yun's squarefree factorization, subresultant computation, Hermite reduction, etc. which are obviously the work of other people.

The program has been tested with polynomials and easy quotients of polynomials. Please note that some polynomials with large coefficients might result in the program not working. This is a known issue and it is due to the fact that, when computing the resultant with `subresultant.py` huge numbers may appear and I have not been able to store them appropriately.

## References
- Manuel Bronstein. *Symbolic Integration I. Trascendental Functions.* Algorithms and Computation in Mathematics. Springer, 2005. isbn: 3540214933.
- David Y.Y. Yun. «On Square-Free Decomposition Algorithms». En: SYMSAC ’76 (1976), págs. 26-35. doi: https://doi.org/10.1145/800205.806320.