# Talking Timer

simple timer that will play a message when interval has been achieved.

## how to run?

the app can be run with either python3 command or directly calling it.

```
# running with python
python3 timer.py

# running as executable
./timer.py
```

## options

there are 3 optional arguments that can be passed to the timer

duration = length of the timer in seconds

interval = length of each lap in seconds

message = custom message that will be played after each interval

```
# example

./timer -d 3600 -i 60 -m "hello world"
```
