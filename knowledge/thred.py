import threading

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        print("init")

        def run(self):
            print("run")


my_thread = MyThread()
my_thread.start()