# Introduction

Ready to get your Python on and create a PS4 project? This guide's got you covered with installation options and a basic project code example.

### Requirements

- [x] Python 3.9 or greater
- [x] Know how to use `pip`
- [x] PS4 Controllers
- [x] A Linux System

## Installation Methods

=== "Manual Installation"

    ### Virtual-Environments

    I strongly recommend that you make use of Virtual Environments when working on any project.
    This means that each project will have its own libraries of any version and does not affect anything else on your system.
    Don't worry, this isn't setting up a full-fledged virtual machine, just small python environment.

    === ":material-linux: Linux"
        ```shell
        cd "[your project directory]"
        python3 -m venv venv
        source venv/bin/activate
        ```

    It's that simple, now you're using a virtual environment. If you want to leave the environment just type `deactivate`.
    If you want to learn more about the virtual environments, check out [this page](https://docs.python.org/3/tutorial/venv.html)

    ### Pip install

    Now let's get the library installed.

    === ":material-linux: Linux"
        ```shell
        python3 -m pip install AsynchronousPS4Controller
        ```

    ### Basic Project

    Now let's get a basic project going, for your code, you'll want something like this:

    ```python
    import asyncio
    from AsynchronousPS4Controller import Controller

    controller = Controller(path="/dev/input/js0")
    # you can start listening before controller is paired, as long as you pair it within the timeout window
    asyncio.run(controller.listen(timeout=30))
    ```

    You can choose to connect your PS4 Controller either before or after you start the code.On how to connect , check out [this page](10%20%20Hardware%20Connection.md)
---

Congratulations! You now have a basic understanding of this library.
If you have any questions check out our other guides

For more examples, check out the [examples page](30%20Examples.md)
