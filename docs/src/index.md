---
hide:
  - navigation
  - toc
  - feedback
---
I hope this documentation is helpful for you, but don't just ++ctrl+c++ and ++ctrl+v++.

A package to suit your non-blocking PS4 interface

AsynchronousPS4Controller is the product when I did a project that needed an asynchronous interface with multiple PS4 controllers

## Key Features
AsynchronousPS4Controller offers:

- An asynchronous way to connect your PS4 to your Python Program
- Connect multiple Controllers in a single code

## Where do I start?
Getting started with AsynchronousPS4Controller is easy! Simply install it via `pip` using either one of these commands:

- `python -m pip install AsynchronousPS4Controller`
- `python3 -m pip install AsynchronousPS4Controller`
- `pip install AsynchronousPS4Controller`
- `pip3 install AsynchronousPS4Controller`


Connect your PS4 either wired or through Bluetooth
 and start building your PS4 program in Python:
```python
import asyncio
from AsynchronousPS4Controller import Controller

controller = Controller(path="/dev/input/js0")

# you can start listening before controller is paired, as long as you pair it within the timeout window
asyncio.run(controller.listen(timeout=30))
```
