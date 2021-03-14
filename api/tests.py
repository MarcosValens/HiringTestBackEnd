from django.test import TestCase


def __str__(self):
    field_values = []
    for field in self._meta.get_all_field_names():
        field_values.append(getattr(self, field, ''))
    return ' '.join(field_values)
# Create your tests here.
