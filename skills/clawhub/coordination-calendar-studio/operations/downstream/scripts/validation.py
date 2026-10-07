# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import math
import re
from datetime import date
from typing import Any, Dict
from urllib.parse import urlparse

def _type_ok(value: Any, expected: Any) -> bool:
    if isinstance(expected, (list, tuple)):
        return any((_type_ok(value, item) for item in expected))
    if expected == 'object':
        return isinstance(value, dict)
    if expected == 'array':
        return isinstance(value, list)
    if expected == 'string':
        return isinstance(value, str)
    if expected == 'integer':
        return isinstance(value, int) and (not isinstance(value, bool))
    if expected == 'number':
        return isinstance(value, (int, float)) and (not isinstance(value, bool))
    if expected == 'boolean':
        return isinstance(value, bool)
    if expected == 'null':
        return value is None
    return True

def validate_schema(value: Any, schema: Dict[str, Any], path: str='$') -> None:
    if 'oneOf' in schema:
        matches = 0
        for option in schema['oneOf']:
            try:
                validate_schema(value, option, path)
            except (TypeError, ValueError):
                continue
            matches += 1
        if matches != 1:
            raise ValueError(f'{path} must match exactly one allowed shape')
        return
    if 'const' in schema and value != schema['const']:
        raise ValueError(f"{path} must equal {schema['const']!r}")
    if 'enum' in schema and value not in schema['enum']:
        raise ValueError(f"{path} must be one of {schema['enum']!r}")
    expected = schema.get('type')
    if expected and (not _type_ok(value, expected)):
        raise TypeError(f'{path} must be {expected}; found {type(value).__name__}')
    if isinstance(value, str):
        if len(value) < int(schema.get('minLength', 0)):
            raise ValueError(f'{path} is shorter than minLength')
        if 'maxLength' in schema and len(value) > int(schema['maxLength']):
            raise ValueError(f'{path} is longer than maxLength')
        pattern = schema.get('pattern')
        if pattern and re.fullmatch(pattern, value) is None:
            raise ValueError(f'{path} does not match the required pattern')
        fmt = schema.get('format')
        if fmt == 'email' and re.fullmatch('[^@\\s]+@[^@\\s]+\\.[^@\\s]+', value) is None:
            raise ValueError(f'{path} must be an email address')
        if fmt == 'uri':
            parsed = urlparse(value)
            if not parsed.scheme or not parsed.netloc:
                raise ValueError(f'{path} must be an absolute URI')
        if fmt == 'date-time' and re.fullmatch('\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(?:Z|[+-]\\d{2}:\\d{2})', value) is None:
            raise ValueError(f'{path} must be an RFC 3339 date-time')
        if fmt == 'date':
            try:
                date.fromisoformat(value)
            except ValueError as exc:
                raise ValueError(f'{path} must be an ISO calendar date') from exc
    if isinstance(value, (int, float)) and (not isinstance(value, bool)):
        if 'minimum' in schema and value < schema['minimum']:
            raise ValueError(f'{path} is below minimum')
        if 'maximum' in schema and value > schema['maximum']:
            raise ValueError(f'{path} is above maximum')
        if 'multipleOf' in schema:
            quotient = value / schema['multipleOf']
            if not math.isclose(quotient, round(quotient), rel_tol=0.0, abs_tol=1e-09):
                raise ValueError(f"{path} is not a multiple of {schema['multipleOf']}")
    if isinstance(value, list):
        if len(value) < int(schema.get('minItems', 0)):
            raise ValueError(f'{path} has too few items')
        if 'maxItems' in schema and len(value) > int(schema['maxItems']):
            raise ValueError(f'{path} has too many items')
        if schema.get('uniqueItems'):
            markers = [repr(item) for item in value]
            if len(markers) != len(set(markers)):
                raise ValueError(f'{path} must contain unique items')
        item_schema = schema.get('items')
        if item_schema:
            for index, item in enumerate(value):
                validate_schema(item, item_schema, f'{path}[{index}]')
    if isinstance(value, dict):
        properties = schema.get('properties', {})
        missing = [key for key in schema.get('required', []) if key not in value]
        if missing:
            raise ValueError(f'{path} is missing required fields {missing!r}')
        if schema.get('additionalProperties') is False:
            extra = sorted(set(value).difference(properties))
            if extra:
                raise ValueError(f'{path} has unsupported fields {extra!r}')
        for key, item in value.items():
            if key in properties:
                validate_schema(item, properties[key], f'{path}.{key}')
