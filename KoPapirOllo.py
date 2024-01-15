import threading
import time
import random
class KoPapirOllo:
    event = threading.Event()
    subs: list[threading.Thread] = []
    x = 0

    ido: int = 0
    gepMutat: int = 0
    jatekosMutat: int = 0
    eredmeny: bool = False
    visszaSzamlalas: int = 3
    jatekosok = []

    allas = [0, 0]
    ido = []

    def __init__(self):
        #th0 = threading.Thread(target=self.eventLoop())
        #th0.start()
        pass

    def indit(self):
        pass

    def mutat(self, mit: int):
        if (self.visszaSzamlalas > 0):
            self.jatekosMutat = mit

    def getEredmeny(self):
        return self.eredmeny

    def eventLoop(self):
        while True:
            self.event.set()
            time.sleep(1)

    def myFunction(self):
        while True:
            self.event.wait()
            if self.event.is_set():
                print("event is set : " + str(self.x))
                self.x += 1
                self.event.clear()
    def listenerAdd(self, fuggveny):
        self.subs.append(threading.Thread(target=fuggveny))

    def menet(self, mutat):
        nyert = False
        gepMutat = (int)((random.random() * 3) + 1)
        return nyert
