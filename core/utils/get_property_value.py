def get_property_value_simple(item, prop, default=None):
    """
    Get a single property value from an item of any type (dict, object, list, primitive).
    This is the low-level property access function.
    
    Args:
        item: The item to get the property from (can be dict, object, list, or primitive)
        prop: The property name/index to retrieve
        default: Value to return if property is not found (defaults to None)
    
    Returns:
        The property value if found, otherwise the default value
    """
    if not prop:
        return item

    # Handle dictionaries
    if isinstance(item, dict):
        return item.get(prop, default)
    
    # Handle lists/tuples
    elif isinstance(item, (list, tuple)):
        try:
            # Convert prop to index if possible
            if isinstance(prop, int) or (isinstance(prop, str) and prop.isdigit()):
                index = int(prop)
                return item[index] if 0 <= index < len(item) else default
        except (IndexError, ValueError):
            return default
        return default
    
    # Handle objects
    elif hasattr(item, prop):
        return getattr(item, prop, default)
    
    return default


def get_property_value(item, prop="", subprop="", default=None):
    """
    High-level function to get a property value, potentially including a subproperty.
    Uses get_single_property internally.
    
    Args:
        item: The item to get the property from (can be dict, object, list, primitive)
        prop: The property name to retrieve
        subprop: Optional sub-property name to retrieve (requires prop to be set)
        default: Value to return if property is not found (defaults to None)
    
    Returns:
        The property value if found, otherwise the default value
    """
    if not prop:
        return item

    # Get the main property
    value = get_property_value_simple(item, prop, default)
    
    # If there's a subprop and we got a value, get the subproperty
    if subprop and value is not default:
        return get_property_value_simple(value, subprop, default)
    
    return value
