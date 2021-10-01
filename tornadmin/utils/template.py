"""Useful functions for using in templates"""

def get_value(variable):
    """If the variable is a callable, it will be called.
    
    :TODO: If the variable is a date or datetime object, it will
    return formatted result.

    This is useful in templates to avoid having to check
    whether a variable is callable or not.
    """
    if callable(variable):
        return variable()

    return variable