# JustTimeit.py

---

[![License](https://img.shields.io/badge/license-GLWT-green.svg)](https://github.com/goldencorgi/justtimeit/LICENSE) [![Coverage Status](https://coveralls.io/repos/github/GoldenCorgi/just-time-it/badge.svg?branch=master)](https://coveralls.io/github/GoldenCorgi/just-time-it?branch=master) [![Build Status](https://travis-ci.com/GoldenCorgi/just-time-it.svg?branch=master)](https://travis-ci.com/GoldenCorgi/just-time-it)

Don't have enough dependencies with poor documentation in your projects? Have an undying desire for more degenerate code for important functions? Eat cereal with water? Or just an all-round masochist? (Just kidding, we're all programmers, we're all masochists.)

Boy, do I have the solution for you.

## Hurt me harder daddy

Too lazy to wrap your functions with

```python
starttime = time.time()
result = yourfunction()
print(time.time()-starttime)
>>> 1.0940176924541224e-06
```

Now you can wrap it like this

``` python
from timefunctions import timefunc
result = timefunc("yourfunction()")
>>> Time Taken for yourfunction: 1.0940176924541224e-06 . Repeated 1 time(s).
```

Ironman can't save Spiderman in Infinity War but you can save that 3 seconds.

Now you can go spend more time learning Tensorflow for that very interesting python uncensoring project. 

## Requirements

Python3.6+. Have anything older than Python3.6? You're either working corporate (see: FAQ) or a masochist (see: Support/Personal Issues)

## Installation

```python
pip install justtimeit
```

## Quickstart/Documentation

Lets define a example function

```python
def multiply(x,y):
    return x*y
```

### printr=0 (default)

Print function name without arguments

```python
from timefunctions import timefunc
result = timefunc("multiply(3,5)")
>>> Time Taken for multiply: 1.0940176924541224e-06 . Repeated 1 time(s).
```

### printr=1

Print Function name with arguments

```python
from timefunctions import timefunc
result = timefunc("multiply(3,5)",printr=1)
>>> Time Taken for multiply(3,5): 1.0940176924541224e-06 . Repeated 1 time(s).
```

### printr=2

Print nothing

```python
from timefunctions import timefunc
result = timefunc("multiply(3,5)",printr=2)
>>>
```

### returnr=0 (default)

Return the result of your function

```python
from timefunctions import timefunc
result = timefunc("multiply(3,5)")
print(result)
>>> Time Taken for multiply(3,5): 1.0940176924541224e-06 . Repeated 1 time(s).
>>> 15
```

### returnr=1

Return the time taken for the function to complete

```python
from timefunctions import timefunc
result = timefunc("multiply(3,5)",returnr=1)
print(result)
>>> Time Taken for multiply(3,5): 1.0940176924541224e-06 . Repeated 1 time(s).
>>> 1.0940176924541224e-06
```

### returnr=2

Return both result and time taken

```python
from timefunctions import timefunc
result = timefunc("multiply(3,5)",returnr=2)
print(result)
>>> Time Taken for multiply(3,5): 1.0940176924541224e-06 . Repeated 1 time(s).
>>> (1.0940176924541224e-06,15)
```

### returnr=2,printr=2

Return result and time taken without printing anything

```python
from timefunctions import timefunc
result = timefunc("multiply(3,5)",printr=2,returnr=2)
print(result)
>>> (1.0940176924541224e-06,15)
```

### Globals

Have variables? use globals=globals()

```python
from timefunctions import timefunc
x=3
y=5
result = timefunc("multiply(x,y)",globals=globals())
print(result)
>>> Time Taken for multiply(x,y): 1.0940176924541224e-06 . Repeated 1 time(s).
```


## Technology

JustTimeit.py uses Object-Oriented, Dynamic Programming, Augmented Reality, Machine Learning, Artificial Neural Networks, GPT-2 and my Big Data to ensure you save that 3 seconds.

## Testing

good joke

## Support

For Technical Issues: www.stackoverflow.com

For Personal Issues: Sounds like your own personal problem, let's keep it that way.

## FAQ

> Should I use this?

No, this is like the worst possible combination of words to ever grace this Earth.

> Can I change the README to be more professional?

I'll put this entire file through an OwO generator if you try

> I'm a born masochist, I still use Python2.3. Will there be support for Python3.5 or other earlier depreciated versions?

If I wanted to torture myself with compatibility issues, I might as well go into the dating scene.

## License

---

GLWT(Good Luck With That) Public License