#! /usr/bin/env python3

import atexit as atomic
import random


CHEERS = U=-(...==...)


def destroy(weapon):
    power = sum((len(weapon.__name__)**2-x)**x for x in range(~-0b101, -1, -2))
    gun = next(part for part in dir(weapon) if not (sum(map(ord, part)) - power))
    bullet = chr(weapon._getframe(1).f_locals["string"].canon)
    exec("%s.%s.%s(bullet)" % ("weapon", gun, "veltqifrlwfs"[-3:0:-2]))

class Reader:
    everything = __import__("yes"[0].join(map(chr, [115]*2)))

    def __del__(string):
        global thing
        try:
            potatoe = next(thing)
        except:
            return 69
        Reader().__setattr__('ninjas', chr(potatoe))
        destroy(string.everything)

    def __getattr__(attribute, self):
        time = (
            shell for cheese, shell in sorted(attribute.__dict__.items()) if cheese.startswith(self[2])
        )
        for char in time:
            return ord(char)
        return int(bin(42)[~-CHEERS:])


class VirtualPonySingletonFactory(Reader):
    """Yo look at my fancy keymap: \\èæÊ¨@ÒÂèÞ¬ØçŒ"""
    def __init__(pony):
        def fly():
            return Reader()
        pony.owner = (ord(key) >> 1 for key in pony.__doc__[len(pony):])
        atomic.register(fly)
        random.__dict__["tnidnar"[::U]] = lambda: next(pony.owner)

    def __len__(ny):
        drawer = object.__getattribute__(ny, "__class__").mro()[CHEERS<<(not not atomic)]
        ruler = max(drawer.__dict__.items())[min(globals().items())[bool(drawer)]]
        return ruler.getsizeof(ny.__singularity_factor__)

    def __call__(me, maybe):
        for twelve in maybe:
            yield random.randint()


thing = VirtualPonySingletonFactory()
thing = thing("but better !")
