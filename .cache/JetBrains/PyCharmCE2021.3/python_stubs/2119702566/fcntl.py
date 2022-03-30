# encoding: utf-8
# module fcntl
# from (built-in)
# by generator 1.147
"""
This module performs file control and I/O control on file
descriptors.  It is an interface to the fcntl() and ioctl() Unix
routines.  File descriptors can be obtained with the fileno() method of
a file or socket object.
"""
# no imports

# Variables with simple values

DN_ACCESS = 1
DN_ATTRIB = 32
DN_CREATE = 4
DN_DELETE = 8
DN_MODIFY = 2
DN_MULTISHOT = 2147483648
DN_RENAME = 16

FASYNC = 8192

FD_CLOEXEC = 1

F_ADD_SEALS = 1033

F_DUPFD = 0

F_DUPFD_CLOEXEC = 1030

F_EXLCK = 4
F_GETFD = 1
F_GETFL = 3
F_GETLEASE = 1025
F_GETLK = 5
F_GETLK64 = 5
F_GETOWN = 9
F_GETSIG = 11

F_GET_SEALS = 1034

F_NOTIFY = 1026
F_RDLCK = 0

F_SEAL_GROW = 4
F_SEAL_SEAL = 1
F_SEAL_SHRINK = 2
F_SEAL_WRITE = 8

F_SETFD = 2
F_SETFL = 4
F_SETLEASE = 1024
F_SETLK = 6
F_SETLK64 = 6
F_SETLKW = 7
F_SETLKW64 = 7
F_SETOWN = 8
F_SETSIG = 10
F_SHLCK = 8
F_UNLCK = 2
F_WRLCK = 1

LOCK_EX = 2
LOCK_MAND = 32
LOCK_NB = 4
LOCK_READ = 64
LOCK_RW = 192
LOCK_SH = 1
LOCK_UN = 8
LOCK_WRITE = 128

# functions

def fcntl(*args, **kwargs): # real signature unknown
    """
    Perform the operation `cmd` on file descriptor fd.
    
    The values used for `cmd` are operating system dependent, and are available
    as constants in the fcntl module, using the same names as used in
    the relevant C header files.  The argument arg is optional, and
    defaults to 0; it may be an int or a string.  If arg is given as a string,
    the return value of fcntl is a string of that length, containing the
    resulting value put in the arg buffer by the operating system.  The length
    of the arg string is not allowed to exceed 1024 bytes.  If the arg given
    is an integer or if none is specified, the result value is an integer
    corresponding to the return value of the fcntl call in the C code.
    """
    pass

def flock(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Perform the lock operation `operation` on file descriptor `fd`.
    
    See the Unix manual page for flock(2) for details (On some systems, this
    function is emulated using fcntl()).
    """
    pass

def ioctl(*args, **kwargs): # real signature unknown
    """
    Perform the operation `request` on file descriptor `fd`.
    
    The values used for `request` are operating system dependent, and are available
    as constants in the fcntl or termios library modules, using the same names as
    used in the relevant C header files.
    
    The argument `arg` is optional, and defaults to 0; it may be an int or a
    buffer containing character data (most likely a string or an array).
    
    If the argument is a mutable buffer (such as an array) and if the
    mutate_flag argument (which is only allowed in this case) is true then the
    buffer is (in effect) passed to the operating system and changes made by
    the OS will be reflected in the contents of the buffer after the call has
    returned.  The return value is the integer returned by the ioctl system
    call.
    
    If the argument is a mutable buffer and the mutable_flag argument is false,
    the behavior is as if a string had been passed.
    
    If the argument is an immutable buffer (most likely a string) then a copy
    of the buffer is passed to the operating system and the return value is a
    string of the same length containing whatever the operating system put in
    the buffer.  The length of the arg buffer in this case is not allowed to
    exceed 1024 bytes.
    
    If the arg given is an integer or if none is specified, the result value is
    an integer corresponding to the return value of the ioctl call in the C
    code.
    """
    pass

def lockf(*args, **kwargs): # real signature unknown
    """
    A wrapper around the fcntl() locking calls.
    
    `fd` is the file descriptor of the file to lock or unlock, and operation is one
    of the following values:
    
        LOCK_UN - unlock
        LOCK_SH - acquire a shared lock
        LOCK_EX - acquire an exclusive lock
    
    When operation is LOCK_SH or LOCK_EX, it can also be bitwise ORed with
    LOCK_NB to avoid blocking on lock acquisition.  If LOCK_NB is used and the
    lock cannot be acquired, an OSError will be raised and the exception will
    have an errno attribute set to EACCES or EAGAIN (depending on the operating
    system -- for portability, check for either value).
    
    `len` is the number of bytes to lock, with the default meaning to lock to
    EOF.  `start` is the byte offset, relative to `whence`, to that the lock
    starts.  `whence` is as with fileobj.seek(), specifically:
    
        0 - relative to the start of the file (SEEK_SET)
        1 - relative to the current buffer position (SEEK_CUR)
        2 - relative to the end of the file (SEEK_END)
    """
    pass

# classes

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

__spec__ = None # (!) real value is "ModuleSpec(name='fcntl', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

