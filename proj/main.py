#!/usr/bin/env python
from constructs import Construct
from cdk8s import App, Chart
import cdk8s_plus_25
import inspect

# Get a dictionary of all classes in the cdk8s_objects module
classes_dict = {name: cls for name, cls in vars(cdk8s_plus_25).items() if inspect.isclass(cls)}

# Generate a tile for each relevant class
tiles = []
for name, cls in classes_dict.items():
    # Get a list of all fields of the class
    fields = inspect.signature(cls).parameters

    # For each field, get its type and whether it's required or optional
    field_info = []
    for field_name, field in fields.items():
        field_type = field.annotation if field.annotation is not inspect._empty else 'unknown'
        is_required = field.default is inspect._empty
        field_info.append({'name': field_name, 'type': str(field_type), 'is_required': is_required})

    tile = {
        'name': name,
        'fields': field_info,
    }
    tiles.append(tile)
print(tiles)
