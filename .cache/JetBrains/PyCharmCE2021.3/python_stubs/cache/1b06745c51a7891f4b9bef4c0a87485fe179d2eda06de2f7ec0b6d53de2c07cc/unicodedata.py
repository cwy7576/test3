# encoding: utf-8
# module unicodedata
# from (built-in)
# by generator 1.147
"""
This module provides access to the Unicode Character Database which
defines character properties for all Unicode characters. The data in
this database is based on the UnicodeData.txt file version
12.1.0 which is publicly available from ftp://ftp.unicode.org/.

The module uses the same names and symbols as defined by the
UnicodeData File Format 12.1.0.
"""
# no imports

# Variables with simple values

unidata_version = '12.1.0'

# functions

def bidirectional(*args, **kwargs): # real signature unknown
    """
    Returns the bidirectional class assigned to the character chr as string.
    
    If no such value is defined, an empty string is returned.
    """
    pass

def category(*args, **kwargs): # real signature unknown
    """ Returns the general category assigned to the character chr as string. """
    pass

def combining(*args, **kwargs): # real signature unknown
    """
    Returns the canonical combining class assigned to the character chr as integer.
    
    Returns 0 if no combining class is defined.
    """
    pass

def decimal(*args, **kwargs): # real signature unknown
    """
    Converts a Unicode character into its equivalent decimal value.
    
    Returns the decimal value assigned to the character chr as integer.
    If no such value is defined, default is returned, or, if not given,
    ValueError is raised.
    """
    pass

def decomposition(*args, **kwargs): # real signature unknown
    """
    Returns the character decomposition mapping assigned to the character chr as string.
    
    An empty string is returned in case no such mapping is defined.
    """
    pass

def digit(*args, **kwargs): # real signature unknown
    """
    Converts a Unicode character into its equivalent digit value.
    
    Returns the digit value assigned to the character chr as integer.
    If no such value is defined, default is returned, or, if not given,
    ValueError is raised.
    """
    pass

def east_asian_width(*args, **kwargs): # real signature unknown
    """ Returns the east asian width assigned to the character chr as string. """
    pass

def is_normalized(*args, **kwargs): # real signature unknown
    """
    Return whether the Unicode string unistr is in the normal form 'form'.
    
    Valid values for form are 'NFC', 'NFKC', 'NFD', and 'NFKD'.
    """
    pass

def lookup(*args, **kwargs): # real signature unknown
    """
    Look up character by name.
    
    If a character with the given name is found, return the
    corresponding character.  If not found, KeyError is raised.
    """
    pass

def mirrored(*args, **kwargs): # real signature unknown
    """
    Returns the mirrored property assigned to the character chr as integer.
    
    Returns 1 if the character has been identified as a "mirrored"
    character in bidirectional text, 0 otherwise.
    """
    pass

def name(*args, **kwargs): # real signature unknown
    """
    Returns the name assigned to the character chr as a string.
    
    If no name is defined, default is returned, or, if not given,
    ValueError is raised.
    """
    pass

def normalize(*args, **kwargs): # real signature unknown
    """
    Return the normal form 'form' for the Unicode string unistr.
    
    Valid values for form are 'NFC', 'NFKC', 'NFD', and 'NFKD'.
    """
    pass

def numeric(*args, **kwargs): # real signature unknown
    """
    Converts a Unicode character into its equivalent numeric value.
    
    Returns the numeric value assigned to the character chr as float.
    If no such value is defined, default is returned, or, if not given,
    ValueError is raised.
    """
    pass

# classes

class UCD(object):
    # no doc
    def bidirectional(self, *args, **kwargs): # real signature unknown
        """
        Returns the bidirectional class assigned to the character chr as string.
        
        If no such value is defined, an empty string is returned.
        """
        pass

    def category(self, *args, **kwargs): # real signature unknown
        """ Returns the general category assigned to the character chr as string. """
        pass

    def combining(self, *args, **kwargs): # real signature unknown
        """
        Returns the canonical combining class assigned to the character chr as integer.
        
        Returns 0 if no combining class is defined.
        """
        pass

    def decimal(self, *args, **kwargs): # real signature unknown
        """
        Converts a Unicode character into its equivalent decimal value.
        
        Returns the decimal value assigned to the character chr as integer.
        If no such value is defined, default is returned, or, if not given,
        ValueError is raised.
        """
        pass

    def decomposition(self, *args, **kwargs): # real signature unknown
        """
        Returns the character decomposition mapping assigned to the character chr as string.
        
        An empty string is returned in case no such mapping is defined.
        """
        pass

    def digit(self, *args, **kwargs): # real signature unknown
        """
        Converts a Unicode character into its equivalent digit value.
        
        Returns the digit value assigned to the character chr as integer.
        If no such value is defined, default is returned, or, if not given,
        ValueError is raised.
        """
        pass

    def east_asian_width(self, *args, **kwargs): # real signature unknown
        """ Returns the east asian width assigned to the character chr as string. """
        pass

    def is_normalized(self, *args, **kwargs): # real signature unknown
        """
        Return whether the Unicode string unistr is in the normal form 'form'.
        
        Valid values for form are 'NFC', 'NFKC', 'NFD', and 'NFKD'.
        """
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        """
        Look up character by name.
        
        If a character with the given name is found, return the
        corresponding character.  If not found, KeyError is raised.
        """
        pass

    def mirrored(self, *args, **kwargs): # real signature unknown
        """
        Returns the mirrored property assigned to the character chr as integer.
        
        Returns 1 if the character has been identified as a "mirrored"
        character in bidirectional text, 0 otherwise.
        """
        pass

    def name(self, *args, **kwargs): # real signature unknown
        """
        Returns the name assigned to the character chr as a string.
        
        If no name is defined, default is returned, or, if not given,
        ValueError is raised.
        """
        pass

    def normalize(self, *args, **kwargs): # real signature unknown
        """
        Return the normal form 'form' for the Unicode string unistr.
        
        Valid values for form are 'NFC', 'NFKC', 'NFD', and 'NFKD'.
        """
        pass

    def numeric(self, *args, **kwargs): # real signature unknown
        """
        Converts a Unicode character into its equivalent numeric value.
        
        Returns the numeric value assigned to the character chr as float.
        If no such value is defined, default is returned, or, if not given,
        ValueError is raised.
        """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    unidata_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



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

ucd_3_2_0 = None # (!) real value is '<unicodedata.UCD object at 0x7fd2ad4f5ab0>'

ucnhash_CAPI = None # (!) real value is '<capsule object "unicodedata.ucnhash_CAPI" at 0x7fd2ad4f5ae0>'

__spec__ = None # (!) real value is "ModuleSpec(name='unicodedata', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

