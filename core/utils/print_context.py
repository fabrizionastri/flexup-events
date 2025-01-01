# ---------- utils/print_object.py

from django.test import TestCase
from core.utils.get_property_value import get_property_value
import inspect
import os

def _print_context(obj=None, *requested_props, print_function_name=False, label:str ='', function_name=None, repr=False, force=False):
    """
    - Print an object's properties in a formatted way, with optional section labels.
        - The function prints the object's class name and string representation, followed by any requested properties. 
        - If a property doesn't exist, prints "not found".
        - Properties can be intermixed with section labels (marked with "_") that start new lines.
    - If activate_print is False, the function does nothing (prints are turned off).
    - If print_function_name is True, the function will only print the name of the grandparent function (ie. the function called the print_object_on function).
    - Use the DEBUG_PRINT environment variable to control the print_object function (1 always, 0 never, test only in test methods).
    - Args:
        - obj: The object to inspect and print
        - label: An optional label to print before the object's class name and string representation
        - *requested_props: Variable number of arguments that can be either:
            - property names: Will print "property_name: property_value"
            - section labels: Must start with '_' to be recognized as a label.
              The '_' will be removed when printing.
        - print_function_name: If True, only print the name of the function that called print_object
        - rep: If True, use the object's __repr__ method to print it
        - force: If True, print the object even if DEBUG_PRINTS is turned off
    - Example:
        - Simple property printing
            - print_object(user, "name", "email")
            - User: John (john@example.com)
                - name: John, email: john@example.com

        - With section labels
            - print_object(user, "_Personal >", "name", "email", "_Work >", "department")
            - User: John (john@example.com)
                - Personal > name: John, email: john@example.com
                - Work > department: Engineering
    - Notes:
        - If a property doesn't exist, prints "not found"
        - Date objects are automatically formatted as YYYY-MM-DD
        - Properties after a section label (starting with '_') will be printed on a new line starting with that label
    """
    if not is_print_activated() and not force:
        return
    
    if label:
        label = f"{label} > "
    
    # if obj is a string, print it and return
    if isinstance(obj, str):
        print(f"    - {label}{obj}")
        return
                
    if print_function_name:
        if function_name is None:
            function_name = get_grandparent_function_name()
        print(f"\n• {label}{function_name}")
        return
    
    # Handle lists/tuples
    if isinstance(obj, (list, tuple, set)):
        obj_type = type(obj).__name__
        print(f"    - {label}{obj_type} = [")
        for item in obj:
            try:
                print(f"      {item}")
            except:
                _print_context(item)
        print("      ]")
        return
    
    # Handle dictionaries in the same way
    if isinstance(obj, dict):
        obj_type = type(obj).__name__
        print(f"    - {label}{obj_type} = {{")
        for key, value in obj.items():
            try:
                print(f"      {key}: {value}")
            except:
                _print_context(value)
        print("      }")
        return
    
    # if obj:
    # print("label: ")
    # print(label)
    # print("obj.__class__.__name__: ")
    # print(obj.__class__.__name__)
    # print("obj.__dict__")
    # print(obj.__dict__)
    # print("obj.__repr__: ")
    # print(obj.__repr__)
    # print("requested_props: ", requested_props)
    if repr:
        # Print using __repr__
        print(f"    - {label}{obj.__class__.__name__}: {repr(obj)}")
    else:
        # Print using __str__
        print(f"    - {label}{obj.__class__.__name__}: {obj}")
        
    line_start = "      - "
    line_label = ""
    props = []
    
    for prop in requested_props:
        # Check if it's a literal string
        if isinstance(prop, str) and prop.startswith('-'):
            if props:
                print(line_start + line_label + ", ".join(props))
            line_label = prop[1:]
            props = []
        else:
            # Handle nested properties
            if '.' in prop:
                value = extract_nested_value(obj, prop)
            else:
                value = getattr(obj, prop) if hasattr(obj, prop) else "not found"
            
            try:
                # if hasattr(value, '_proxy__'):
                #     print("► ► This is a proxy object") 
                    # value = str(value)                      # Force resolution to a string for proxy objects
                if hasattr(value, 'strftime'): 
                    value = value.strftime('%Y-%m-%d')      # Format datetime objects            
                props.append(f"{prop}: {value}")
            except TypeError:
                props.append(f"{prop}: <error formatting value>")
                    
    if props or line_label:
        print(line_start + line_label + ", ".join(props))


def get_grandparent_function_name():
    # Get immediate caller (parent)
    caller_frame = inspect.currentframe().f_back
    # Get caller of caller (grandparent)
    grandparent_frame = caller_frame.f_back if caller_frame else None
    grandparent_name = grandparent_frame.f_code.co_name if grandparent_frame else "unknown"
    
    return grandparent_name


def is_print_activated():
    # Check if prints are activated
    debug_setting = os.getenv('DEBUG_PRINTS', 'test')
    

    # If debug prints are completely disabled, return early
    if debug_setting == '0':
        return False
    
    # If debug_setting is 'test', only print in test methods
    if debug_setting == 'test':
        frame = inspect.currentframe()
        if frame:
            caller_frame = frame.f_back
            while caller_frame:
                # Get the local variables of the caller
                local_vars = caller_frame.f_locals
                # Check if 'self' exists and is instance of TestCase

                if 'self' in local_vars and isinstance(local_vars['self'], TestCase):
                    # Get the method name                  
                    caller_name = caller_frame.f_code.co_name
                    if caller_name.startswith('test_'):
                        return True
                caller_frame = caller_frame.f_back
    return True


def print_object_off(obj=None, *requested_props, print_function_name=False):
    """ 
    - This function does not do anything. It is used to turn off the print_object function by changing the import statement in the test file.
    - To activate prints use the following import statement:
        - from core.utils.print_utils import print_object_on as _print_object
    - To deactivate prints use the following import statement:
        - from core.utils.print_utils import print_object_off as _print_object
    - Alternatively, adjust the "DEBUG_PRINTS" environment variable to control the print_object function.
    """
    pass


def extract_nested_value(obj, prop_path):
    """Helper function to get nested property values"""

    try:
        parts = prop_path.split('.')
        value = obj
        
        # Handle first property
        if len(parts) > 1:
            value = get_property_value(obj, parts[0])
            
            # Handle remaining properties
            for part in parts[1:]:
                value = get_property_value(value, part)
                
        return value
    except (AttributeError, KeyError):
        return "not found"


def print_context_decorator(cls):
    """ A decorator to be added to a test class.
    - For each test in the class, prints the name of the test method before running it.
    """
    def make_wrapper(original_method, original_name):
        def wrapped_test_method(self, *args, **kwargs):
            file_name = cls.__module__.split('.')[-1] + '.py'
            test_class_name = cls.__name__
            _print_context(print_function_name=True, function_name=original_name, label=f"{file_name}, {test_class_name}")
            return original_method(self, *args, **kwargs)
        return wrapped_test_method

    for attr_name in dir(cls):
        if attr_name.startswith('test_'):
            original_method = getattr(cls, attr_name)
            if callable(original_method):
                original_name = attr_name
                # Create a unique wrapper for this method
                wrapped = make_wrapper(original_method, original_name)
                setattr(cls, attr_name, wrapped)

    return cls
