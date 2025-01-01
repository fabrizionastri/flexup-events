# ---------  utils/mod_data.py

def clone(data):
    """
    *Helper function* to clone the given data:
    - If `data` is a Django model instance:
      Returns a new instance of the same model with copied fields (no primary key, no related objects).
    - If `data` is a dictionary:
      Returns a shallow copy.
    - Otherwise:
      Returns a deepcopy.
    """
    from copy import deepcopy
    if hasattr(data, '_meta'):  # *Model check*
        new_instance = data.__class__()  # new empty model instance
        for field in data._meta.fields:
            if not field.primary_key and not field.name == "reference_id":
                setattr(new_instance, field.name, getattr(data, field.name))
        return new_instance
    else:
        # *Handle dictionary or other objects*
        try:
            return data.copy()
        except AttributeError:
            # If not a dict (or no .copy()), fallback to deepcopy
            return deepcopy(data)
    
    
def update(data, **kwargs):
    """ Updates the given data in place with the provided key-value pairs.
    - Args:
        - data: a dictionary or object to update.
        - kwargs: key-value pairs to update the data with.
    - Returns:
        - Does not return a new object, but updates the provided data in place.
    """
    # *If no updates are needed, return the clone immediately*
    if not kwargs:
        pass

    # *Apply updates from kwargs*
    for key, val in kwargs.items():
        try:
            # Dictionary-like access
            data[key] = val
        except (TypeError, KeyError):
            try:
                # Attribute access
                setattr(data, key, val)
            except Exception as e:
                print(f"Warning: Could not set {key} on {type(data).__name__} instance. Error: {e}")
                continue


def clone_and_update(data, **kwargs):
    """Clones the given data and updates the clone with the provided key-value pairs.
        - Args:
        - data: a dictionary or object to update.
        - kwargs: key-value pairs to update the data with.
    - Returns:
        - A new object with the same type as the input data, updated with the provided key-value pairs.
    """

    # *Use helper function for cloning*
    new_data = clone(data)
    # *Use helper function for updating*
    update(new_data, **kwargs)
    
    return new_data
    