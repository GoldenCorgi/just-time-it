# JustTimeit.py

---

[![License](https://img.shields.io/badge/license-GLWT-green.svg)](https://github.com/goldencorgi/justtimeit/LICENSE) [![Coverage Status](https://coveralls.io/repos/github/GoldenCorgi/just-time-it/badge.svg?branch=master)](https://coveralls.io/github/GoldenCorgi/just-time-it?branch=master) [![Build Status](https://travis-ci.com/GoldenCorgi/just-time-it.svg?branch=master)](https://travis-ci.com/GoldenCorgi/just-time-it) [![GitHub file size in bytes](https://img.shields.io/github/size/GoldenCorgi/just-time-it/timefunctions/__init__.py.svg)](https://github.com/GoldenCorgi/just-time-it/blob/master/timefunctions/__init__.py) [![Python Version](https://img.shields.io/badge/python-3.6%20%7C%203.7-blue.svg)](https://github.com/GoldenCorgi/just-time-it) ![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen.svg) [![My Looks](https://img.shields.io/badge/handsome-110%25-blue.svg)](https://www.google.com/search?q=park+hyung+sik) ![OwO](https://img.shields.io/badge/OwO-what's%20this-blueviolet.svg)


<p align="center">
  <img src="https://i.imgur.com/ZfWvt1w.jpg" alt="cat"/>
</p>

Don't have enough dependencies with poor documentation in your projects? Have an undying desire for more broken code for important functions? Eat cereal with water? Or just an all-round masochist? (Just kidding, we're all programmers, we're all masochists)

Boy, do I have the solution for you.

## Hurt me harder daddy

Too lazy to wrap your functions with this?

```python
import time
starttime = time.time()
def shakyRelationship(Wallet):
    while True:
        if Wallet == "empty":
            break
        elif Wallet == "thicc":
            # stop lying to yourself
            break
    return "big sad"
YourWallet = "empty"
result = shakyRelationship(YourWallet)
print(time.time()-starttime)
>>> 1.0940176924541224e-06
```

Now you can wrap it like this

``` python
from timefunctions import timefunc
MyWallet = "thicc"
result = timefunc("shakyRelationship(MyWallet)",globals=globals()) # Only include globals() if you have variables
>>> Time Taken for yourfunction: 1.0940176924541224e-06 . Repeated 1 time(s).
```

This package can't save your relationships but it can save you that 3 seconds.

Now you can go spend more time learning Tensorflow for that interesting python uncensoring project.

## Requirements

Python3.6+. Have anything older than Python3.6? You're either working corporate (see: [FAQ](#FAQ)) or a masochist (see: [Support/Personal Issues](#Support))

## Installation

```python
pip install just-time-it
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

## Caveats/Warnings (Serious)

This code is not accurate. Any function you are testing that is under 0.1 seconds should NOT rely on this package. A normal function that executes for around 0.9 seconds will look like this under different code

### Example slow code

```python
# Around 0.9 seconds to run
def multiply(x,y):
    for d in range(10000000):
        xy = d*x*y
    return None
```

### Normal time.time()

```python
starttime = time.time()
multiply(3,7)
print("time.time()",(time.time()-starttime))
>>> time.time() 0.8946394920349121
```

### timeit with setup

```python
print("timesetup",timeit.timeit("multiply(3,7)",setup="from /__main__ import multiply",number=ss))
>>> timesetup 0.9034562206940011
```

### timefunc (this package)

```python
timefunc("multiply(3,7)")
>>> Time Taken for multiply: 0.84726418995648 . Repeated 1 time(s).
```

They are roughly similar with a maximum of 0.1 differences. You can try altering range(10000000) to see the differences in the code.

## License

---

GLWT(Good Luck With That) Public License