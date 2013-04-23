#-*- coding: utf-8 -*-
u'''
Solution exercise 1: old-style vs. new-style, classes customization
'''


from collections import OrderedDict


class CustomOrderedDict(OrderedDict):
    def __getitem__(self, key):
        if isinstance(key, slice):
            return self.__class__(self.items()[key])
        return OrderedDict.__getitem__(self, key)

    def __add__(self, other):
        res = self.__class__(self)
        res.update(other)
        return res

    def __sub__(self, other):
        res = self.__class__(self)
        [res.pop(k, None) for k in other]
        return res


class AttrDict(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError, e:
            raise AttributeError(e)

    def __setattr__(self, name, value):
        if name in self:
            self[name] = value
        else:
            # self.__dict__[name] = value  # Perform action instead of delegating
            dict.__setattr__(self, name, value)

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            # del self.__dict__[name]  # Perform action instead of delegating
            dict.__delattr__(self, name)


class Fraction(object):
    def __init__(self, numerator, denominator):
        self._num = int(numerator)
        self._den = int(denominator)

    def value(self):
        return float(self._num) / self._den

    def __lt__(self, other):
        '''Called to implement evaluation of self < other
        '''
        try:
            return self.value() < other.value()
        except AttributeError:
            return self.value() < other

    def __le__(self, other):
        '''Called to implement evaluation of self <= other
        '''
        try:
            return self.value() <= other.value()
        except AttributeError:
            return self.value() <= other

    def __eq__(self, other):
        '''Called to implement evaluation of self == other
        '''
        try:
            return self.value() == other.value()
        except AttributeError:
            return self.value() == other

    def __ne__(self, other):
        '''Called to implement evaluation of self != other
        '''
        try:
            return self.value() != other.value()
        except AttributeError:
            return self.value() != other

    def __gt__(self, other):
        '''Called to implement evaluation of self > other
        '''
        try:
            return self.value() > other.value()
        except AttributeError:
            return self.value() > other

    def __ge__(self, other):
        '''Called to implement evaluation of self >= other
        '''
        try:
            return self.value() >= other.value()
        except AttributeError:
            return self.value() >= other

    def __str__(self):
        '''Called by the str() and print to compute the “informal” string representation
        '''
        return "{0} / {1}".format(self._num, self._den)

    def __len__(self):
        '''Called to implement the built-in function len()
        '''
        return 2

    def __getitem__(self, key):
        '''Called to implement evaluation of self[key]
        '''
        if key == 0 or key == 'num':
            return self._num
        elif key == 1 or key == 'den':
            return self._den
        else:
            raise KeyError(key)

    def __setitem__(self, key, value):
        '''Called to implement assignment of self[key] = value
        '''
        if key == 0 or key == 'num':
            self._num = value
        elif key == 1 or key == 'den':
            self._den = value
        else:
            raise KeyError(key)

    def __add__(self, other):
        '''Called to implement the binary arithmetic operation self + other
        '''
        try:
            if self._den == other._den:
                return Fraction(self._num + other._num, self._den)
            else:
                return Fraction(self._num * other._den + other._num * self._den, self._den * other._den)
        except AttributeError:
            return Fraction(self._num + other * self._den, self._den)

    __radd__ = __add__

    def __mul__(self, other):
        '''Called to implement the binary arithmetic operation self * other
        '''
        try:
            return Fraction(self._num * other._num, self._den * other._den)
        except AttributeError:
            return Fraction(self._num * other, self._den)


fract1 = Fraction(5, 2)  # 2.5
fract2 = Fraction(3, 2)  # 1.5
fract3 = Fraction(25, 10)  # 2.5

print fract1 != fract3  # 2.5 != 2.5
print fract1 == fract3  # 2.5 == 2.5
print fract2 < fract3  # 1.5 < 2.5

# Let's try the other way
print fract1 >= fract2   # 2.5 >= 1.5
print fract2 >= fract3  # 1.5 >= 2.5

# Let's try with other types
print fract1 >= 2  # 2.5 >= 2
print fract2 == 1.5  # 1.5 == 1.5

# Let's try the other way with other types
print 2 <= fract1  # 2 <= 2.5
print 1.5 == fract2   # 1.5 == 1.5

print 10 > fract1  # 10 > 2.5
print 10 < fract1  # 10 < 2.5
print fract1 < 10  # 2.5 < 10
print fract1 > 10  # 2.5 > 10

f1 = Fraction(7, 2)
print len(f1)
print f1['num'], "/", f1[1]
f1[0] = 5
f1['den'] = 3
print f1

fract1 = Fraction(5, 3)
fract2 = Fraction(2, 3)
print fract1 + fract2
print fract1 + 5
print 3 + fract1
print fract1 * fract2
print 5 * fract2
