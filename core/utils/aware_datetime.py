from datetime import datetime, date
from django.utils import timezone

def aware_datetime(*args, tz=None):
    """ Transforms a date, datetime, string, or tuple into a timezone aware datetime object.
    - Accepted formats:
        - date object: datetime.date(2022, 12, 31)
        - datetime object: datetime.datetime(2022, 12, 31, 9, 21, 27)
        - string (date): "2022-12-31"
        - string (date and time): "2022-12-31 09:21:27"
        - tuple (date and time): (2022, 12, 31, 9, 21, 27)
        - integer arguments: (2022, 12, 31) or (2022, 12, 31, 9, 21, 27)
    - Args:
        - *args: Variable length argument list:
            - Single argument: date, datetime, str, or tuple
            - Multiple arguments: year, month, day, [hour, minute, second]
        - tz (timezone, optional): The timezone to use. Defaults to None, which uses the default timezone.
    - Returns:
        - datetime: A timezone aware datetime object.
    """
    if len(args) == 2 and not isinstance(args[1], (int, float)):
        args, tz = args[0:1], args[1]
        
    if len(args) == 1:
        arg = args[0]
        if isinstance(arg, str):
            try:
                dt = datetime.strptime(arg, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                dt = datetime.strptime(arg, "%Y-%m-%d")
        elif isinstance(arg, (tuple, list)):
            dt = datetime(*arg)
        elif isinstance(arg, date) and not isinstance(arg, datetime):
            dt = datetime.combine(arg, datetime.min.time())
        elif isinstance(arg, datetime):
            if timezone.is_aware(arg):
                return arg
            dt = arg
    else:
        # Handle direct integer arguments like datetime(2023, 10, 1)
        dt = datetime(*args)   
        
    return timezone.make_aware(dt, timezone=tz) if tz else timezone.make_aware(dt)
