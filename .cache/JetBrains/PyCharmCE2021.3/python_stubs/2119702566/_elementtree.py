# encoding: utf-8
# module _elementtree
# from (built-in)
# by generator 1.147
# no doc
# no imports

# functions

def SubElement(*args, **kwargs): # real signature unknown
    pass

def _set_factories(*args, **kwargs): # real signature unknown
    """
    Change the factories used to create comments and processing instructions.
    
    For internal use only.
    """
    pass

# classes

class Element(object):
    # no doc
    def append(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def extend(self, *args, **kwargs): # real signature unknown
        pass

    def find(self, *args, **kwargs): # real signature unknown
        pass

    def findall(self, *args, **kwargs): # real signature unknown
        pass

    def findtext(self, *args, **kwargs): # real signature unknown
        pass

    def get(self, *args, **kwargs): # real signature unknown
        pass

    def getchildren(self, *args, **kwargs): # real signature unknown
        pass

    def getiterator(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        pass

    def items(self, *args, **kwargs): # real signature unknown
        pass

    def iter(self, *args, **kwargs): # real signature unknown
        pass

    def iterfind(self, *args, **kwargs): # real signature unknown
        pass

    def itertext(self, *args, **kwargs): # real signature unknown
        pass

    def keys(self, *args, **kwargs): # real signature unknown
        pass

    def makeelement(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def set(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        pass

    attrib = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A dictionary containing the element's attributes"""

    tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A string identifying what kind of data this element represents"""

    tail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A string of text directly after the end tag, or None"""

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A string of text directly after the start tag, or None"""



class ParseError(SyntaxError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class TreeBuilder(object):
    # no doc
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def comment(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, *args, **kwargs): # real signature unknown
        pass

    def end(self, *args, **kwargs): # real signature unknown
        pass

    def pi(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class XMLParser(object):
    # no doc
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def _parse_whole(self, *args, **kwargs): # real signature unknown
        pass

    def _setevents(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    entity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    @classmethod
    def create_module(cls, *args, **kwargs): # real signature unknown
        """ Create a built-in module """
        pass

    @classmethod
    def exec_module(cls, *args, **kwargs): # real signature unknown
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', 'module_repr': <staticmethod object at 0x7fd2adcbe430>, 'find_spec': <classmethod object at 0x7fd2adcbe460>, 'find_module': <classmethod object at 0x7fd2adcbe490>, 'create_module': <classmethod object at 0x7fd2adcbe4c0>, 'exec_module': <classmethod object at 0x7fd2adcbe4f0>, 'get_code': <classmethod object at 0x7fd2adcbe580>, 'get_source': <classmethod object at 0x7fd2adcbe610>, 'is_package': <classmethod object at 0x7fd2adcbe6a0>, 'load_module': <classmethod object at 0x7fd2adcbe6d0>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_elementtree', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

