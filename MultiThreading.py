from threading import Thread
from time import sleep

class Hi(Thread):
    def run(self):
        for i in range(10):
            print("Hi")
            sleep(1)

class Hello(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
            sleep(1)

hi = Hi()
hello=Hello()
hi.start()
sleep(.2)
hello.start()