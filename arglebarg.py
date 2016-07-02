#!/usr/bin/python2
#
# Credit where due:
# tiny.cc/
# ArgleBargFoo

class ArgleBarg (object):
    def __exit__ (self):
        pass

    def bargle (self, argle):
        print argle, self.__class__

    def fargen (self, bargain, *args, **kwargs):
        assert args
        for arg in [(arg, kwarg) for arg, kwarg in (args, kwargs)]:
            if arg not in bargain and bargain in args:
                from string import lower
                print map(lower, kwargs)
