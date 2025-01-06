# FlexUp Backend Coding Guidelines

## Number of digits and decimals

| Amount type   | Digits | Decimals | Equivalents                               |
| ------------- | ------ | -------- | -------------------------                 | 
| Quantity      | 15     | 4        | Nr of tokens                              |
| Price         | 15     | 4        | Token index                               |
| Amount        | 15     | 2        |                                           |
| Percentage    | 5      | 2        | Uprate, risk factor, tax rate             |
| Exchange rate | 15     | 8        |                                           |
| Portion*      | 15     | 12       |                                           |

_* Portions need a lot of decimals because you may split a round amount principal into tranches that also have round amount principals, where the portions might have a lot of decimals. Eg. 3 000 000 € = 1 000 000 € + 2 000 000 € (0.3333333% + 0.6666667%)_

## Model definition

- When defining a Model, group the attributes by the following categories (use comments to name each section):
  - _class Meta_: information about the class, such as verbose names, unique constraints, and indexes
  - _Required input fields_: static properties (stored in the database) which must be provided as arguments to the constructor (i.e. when creating an object)
  - _Optional input fields_: static properties which can be provided as additional arguments to the constructor
  - _Calculated input fields_: static properties which are calculated by the systems and assigned by the `assign_values` method, or through another method
  - _Properties_: calculated dynamic fields that are not stored in the database
  - _Methods_: methods that are not part of the standard Django model methods (save, clean, etc.)
  - _Assign values, clean & save_: the `assign_values`, `clean`, and `save` methods, as required
  - _Labels_: the `_str_` property and other special properties which are concatenation of fields used for display purposes
- Move complex methods to a separate file (ie. if more than 10 lines), and reference them in the model
- Whenever possible, add comments at the end of the line, instead as a separate line so that the code is more readable. Toggle between wrapping and not wrapping the code to make the code more readable or less visible.
- Example / Template
    ```
    class ...(FlexUpModel):
        """ Docstring using bullet points only
          - Description:
            - ...
          - Attributes:
            - ...
          - Returns:
            - ...
        """
        class Meta:
            verbose_name = _("...")
            verbose_name_plural = _("...")
            unique_together = ('...', '...')
            indexes = [
                models.Index(fields=['...']),
                models.Index(fields=['...']),
            ]

        # Required input fields
            ...

        # Optional input fields
            ...

        # Calculated input fields
            ...

        # Properties
           ...

        # Methods
            ...

        # Assign values, clean & save
            def assign_values(self):
                ...
                super().assign_values()

            def clean(self):
                ...
                super().clean()

            def save(self, *args, **kwargs):
                ...
                super().save(self, *args, **kwargs):

        # Labels
            def short_label

            def label

            def __str__(self):
                return self.label
    ```

## Reviewing each other's code

- Don't delete code that is not yours, unless it is clearly commented as being temporary or unnecessary
- Instead, comment out the code and add a comment explaining why it was commented out
- Only delete it during joint merging sessions, after discussing with the author

## Dates and time

- Use the following to assign current time to a variable
  ```python
  from django.utils import timezone
  now = timezone.now()
  today = timezone.now().date()
  ```
- To assign dates manually, use the `dateparse` utility function:
  ```python
  from django.utils.dateparse import parse_date
  date = parse_date('2021-01-01')
  ```
- In the Django models:
  - use `auto_now_add=True` to automatically assigne the current time when the object is created, 
  - or `default=timezone.now` to allow manual assignment of the date and time
  
  ```python
  from django.utils import timezone
  from django.db import models

  # DateField examples
  confirmation_date = models.DateField(auto_now_add=True)       # Set once on creation
  sent_date = models.DateField(auto_now=True)                   # Updates on each save
  delivery.start_date = models.DateField(default=timezone.now)  # Set once on creation if not value is provided upon creation

  # Comparison: DateTimeField examples 
  created_datetime = models.DateTimeField(auto_now_add=True)    # Set once on creation
  updated_datetime = models.DateTimeField(auto_now=True)        # Updates on each save
  joined_datetime = models.DateTimeField(default=timezone.now)  # Set once on creation if not value is provided upon creation

  ```

## Language / localization

- Use this `from django.utils.translation import gettext_lazy as _` (instead of `from gettext import gettext as _`)

## Member: current member, member validation & system bypass
- The current member taken from the request object and stored in teh 'member' variable of the local thread
- It can be access by the `get_current_member()` function
- In tests (or elsewhere), you can override the current member with an `with override_current_member():` bloc
- the `validate_member_permissions` function checks if the current member has the required permissions to perform an create/update operation, based on the current member, object being accessed, and the specific rights of the object, as defined in the `Domain` enum
- For bypass the member validation checks, add the `by_system=True` argument to the create/update operation.
- This is specifically required when the admin member of one account creates another account (with related members and, if applicable, constituents)


# Error handling

- `ValidationError` - use this for all errors raised by our code, related to validation of business rules, and validation that the data is correct and that the selected enum values exist and are correct.
- `PermissionError` - use this for all errors raised by our code, related to permissions, and validation that the user has the right to perform the action.
- The following errors are raised by python or django, and should not be raised by our code:
  - `TypeError` - type mismatch, wrong type, missing arguments
  - `ValueError` - right type but an inappropriate value
  - `IntegrityError` - database integrity constraint violation (e.g. record already exists with identical unique property)

# Symbols

When multiple symbobls are added to a string, use the following order (if applicable)

`{self.visibility.symbol}{self.status.symbol}{self.focus.symbol}`

# Docstrings

## Model docstrings

- Add a docstring to every model, listing the available attributes, properties, and methods
- For each category (attributes, properties, and methods), group them according to the class that they are defined in (eg. parent class, mixin, etc.)
- For attributes & property: specify the type, and give a brief description (such as default values)
- For methods: only specify the name. The details of the method should be in the method's docstring

## Method docstrings

- Add a docstring to every method, listing the available arguments, return values, and exceptions
- For each category (arguments, return values, and exceptions), group them according to the class that they are defined in (eg. parent class, mixin, etc.)
- For arguments: specify the type, and give a brief description
- For return values: specify the type, and give a brief description
- For exceptions: specify the type, and give a brief description

## Docstring formatting:

- Use the following format for docstrings:
  - Enclose between a triple-quoted string
  - Start with a brief description of the class or method
  - Use tabs and "-" for indentation (otherwise it does not display correctly in the code editor)
- Example:
  ```
    """...
      - Attributes:
          - ...
      - Properties:
          - ...
      - Methods:
          - ...
    """
  ```

## Cleaning, validations and assigning values (defaults or override)

### Methods
- `clean`: built-in validation method, to raise errors if the data is not valid
- `assign_values`: method to assign default values to fields that have not received any specific value upon creation, or to override/update the values of these fields if certain conditions are met
- `save`: method to call the `clean` and `assign_values` methods, and to save the object to the database
- `full_clean`: method to call the `clean` method, plus checking that the model-specific constraints are met (eg. unique constraints)

### Order of execution
- Examples:
  - Individual / Account / FlexUpModel
  - orderitem / AbstractProduct / FlexUpModel
  - PaymentTerms / AbstractPaymentTerm / FlexUpModel
  - L2 / L1 / L0
- L2.save
  - L1.save
    - L0.save
      - L2.assign_values
        - L1.assign_values
          - L0.assign_values
      - L2.clean
        - L1.clean
          - L0.clean

### Template

- L0: `FlexUpModel` model:
    ```python
    # Assign values, clean & save

        def assign_values(self):
            # ... custom logic here
            # No super because the parent class (PolymorphicModel) does not have this method

        def clean(self):
            # ... custom logic here
            super().clean()

        def save(self, *args, **kwargs):
            # Note that only the L0 model calls assign_values and full_clean in the save method
            self.assign_values()          
            self.full_clean()
            # ... custom logic here
            super().save(*args, **kwargs)
    ```

- L1: `Account`, `AbstractProduct` or `AbstractPaymentTerm` model:
    ```python
    # Assign values, clean & save

        def assign_values(self):
            # ... custom logic here
            super().assign_values()

        def clean(self):
            # ... custom logic here
            super().clean()

        def save(self, *args, **kwargs):
            # ... custom logic here
            super().save(*args, **kwargs)
    ```

- L2: `Individual`, `OrderItem` or `ResiduePaymentTerm` model:
    ```python
    # Assign values, clean & save

        def assign_values(self):
            # ... custom logic here
            super().assign_values()

        def clean(self):
            # ... custom logic here
            super().clean()

        def save(self, *args, **kwargs):
            # ... custom logic here
            super().save(*args, **kwargs)
    ```

## Tests

### Print debugging

- `os.environ["DEBUG_PRINTS"] = "0"` to disable debug prints in the tests
- `os.environ["DEBUG_PRINTS"] = "1"` to force debug prints in the tests
- `os.environ["DEBUG_PRINTS"] = "test"` to enable debug prints only in the test methods
- `_print_object(obj)` to print the object in the tests

## Debugging

- create a `.vscode\launch.json` file in the root of the project to enable debugging in VS Code for specific tests. For example
  ```
  {
    "configurations": [
          {
            "name": "Django Test: Accounts",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": [
                "test",
                "account.tests.individual"
            ],
            "django": true,
            "justMyCode": true,
            "env": {
                "DEBUG": "True"
            }
        },
    ]
  }
  ```
