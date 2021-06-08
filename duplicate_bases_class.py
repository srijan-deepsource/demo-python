import abc


class Base:
    def __init__(self):
        self.base = 1


class BaseOne:
    def __init__(self):
        self.base_one = 2


class ChildAnother(Base, BaseOne, Base, BaseOne, abc.ABC, abc.ABC):
    """Some Child class"""


class ChildOne(Base, BaseOne, Base, BaseOne, abc.ABC, abc.ABCMeta, abc.ABCMeta):
    """Class with duplicate bases"""
