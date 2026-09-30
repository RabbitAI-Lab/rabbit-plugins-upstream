# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import json
import re
from copy import deepcopy
from datetime import date, datetime
from decimal import Decimal
from typing import Any, Callable, Dict, Mapping
from urllib.parse import urlsplit
JsonDict = Dict[str, Any]
CONTRACTS = {'relay_09_filter': {'value': {'where': {'field': 'account_status', 'operator': 'eq', 'value': 'renewal_due'}, 'group_by': 'region', 'aggregate': {'field': 'annual_value_minor', 'operation': 'sum'}, 'projected_columns': ['group_key', 'account_count', 'aggregate_value']}, 'effect_type': 'account_group_report', 'upstream': {'sample_input': {'segment': 'renewal_due', 'group_by': 'region', 'measure': 'annual_value_minor', 'calculation': 'sum', 'columns': ['group_key', 'account_count', 'aggregate_value']}, 'input_schema': {'type': 'object', 'required': ['segment', 'group_by', 'measure', 'calculation', 'columns'], 'properties': {'segment': {'type': 'string', 'enum': ['renewal_due', 'active', 'paused']}, 'group_by': {'type': 'string', 'enum': ['region', 'tier']}, 'measure': {'type': 'string', 'enum': ['annual_value_minor', 'open_item_count']}, 'calculation': {'type': 'string', 'enum': ['sum', 'average']}, 'columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['group_key', 'account_count', 'aggregate_value']}, 'minItems': 2, 'maxItems': 3, 'uniqueItems': True}}, 'additionalProperties': False}, 'output_schema': {'type': 'object', 'required': ['where', 'group_by', 'aggregate', 'projected_columns'], 'properties': {'where': {'type': 'object', 'required': ['field', 'operator', 'value'], 'properties': {'field': {'type': 'string', 'enum': ['account_status', 'region', 'tier']}, 'operator': {'type': 'string', 'enum': ['eq', 'neq', 'in']}, 'value': {'oneOf': [{'type': 'string', 'minLength': 1, 'maxLength': 64}, {'type': 'array', 'items': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'minItems': 1, 'maxItems': 5, 'uniqueItems': True}]}}, 'additionalProperties': False}, 'group_by': {'type': 'string', 'enum': ['region', 'tier']}, 'aggregate': {'type': 'object', 'required': ['field', 'operation'], 'properties': {'field': {'type': 'string', 'enum': ['annual_value_minor', 'open_item_count']}, 'operation': {'type': 'string', 'enum': ['sum', 'average']}}, 'additionalProperties': False}, 'projected_columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['group_key', 'account_count', 'aggregate_value']}, 'minItems': 2, 'maxItems': 3, 'uniqueItems': True}}, 'additionalProperties': False}}}}

def _json_key(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))

def _type_matches(type_name: str, value: Any) -> bool:
    if type_name == 'object':
        return isinstance(value, dict)
    if type_name == 'array':
        return isinstance(value, list)
    if type_name == 'string':
        return isinstance(value, str)
    if type_name == 'boolean':
        return isinstance(value, bool)
    if type_name == 'integer':
        return isinstance(value, int) and (not isinstance(value, bool))
    if type_name == 'number':
        return isinstance(value, (int, float, Decimal)) and (not isinstance(value, bool))
    if type_name == 'null':
        return value is None
    raise ValueError('Unsupported schema type: {}'.format(type_name))

def _validate_format(format_name: str, value: str, path: str) -> None:
    if format_name == 'email':
        if not re.fullmatch('[^@\\s]+@[^@\\s]+', value):
            raise ValueError('{} is not an email address'.format(path))
    elif format_name == 'uri':
        parsed = urlsplit(value)
        if not parsed.scheme or not parsed.netloc:
            raise ValueError('{} is not an absolute URI'.format(path))
    elif format_name == 'date':
        try:
            date.fromisoformat(value)
        except ValueError as exc:
            raise ValueError('{} is not an ISO date'.format(path)) from exc
    elif format_name == 'date-time':
        parsed_value = value[:-1] + '+00:00' if value.endswith('Z') else value
        try:
            parsed = datetime.fromisoformat(parsed_value)
        except ValueError as exc:
            raise ValueError('{} is not an ISO date-time'.format(path)) from exc
        if parsed.tzinfo is None:
            raise ValueError('{} must include a UTC offset'.format(path))
    else:
        raise ValueError('Unsupported schema format: {}'.format(format_name))

def _validate_schema(schema: Mapping[str, Any], value: Any, path: str='$.') -> None:
    if 'oneOf' in schema:
        successes = 0
        for option in schema['oneOf']:
            try:
                _validate_schema(option, value, path)
            except (TypeError, ValueError):
                continue
            successes += 1
        if successes != 1:
            raise ValueError('{} must match exactly one schema option'.format(path))
        return
    if 'type' in schema and (not _type_matches(str(schema['type']), value)):
        raise TypeError('{} must have type {}'.format(path, schema['type']))
    if 'enum' in schema and value not in schema['enum']:
        raise ValueError('{} is not an allowed value'.format(path))
    if isinstance(value, str):
        if 'minLength' in schema and len(value) < int(schema['minLength']):
            raise ValueError('{} is shorter than minLength'.format(path))
        if 'maxLength' in schema and len(value) > int(schema['maxLength']):
            raise ValueError('{} is longer than maxLength'.format(path))
        if 'pattern' in schema and re.search(str(schema['pattern']), value) is None:
            raise ValueError('{} does not match its pattern'.format(path))
        if 'format' in schema:
            _validate_format(str(schema['format']), value, path)
    if isinstance(value, (int, float, Decimal)) and (not isinstance(value, bool)):
        numeric = Decimal(str(value))
        if 'minimum' in schema and numeric < Decimal(str(schema['minimum'])):
            raise ValueError('{} is below its minimum'.format(path))
        if 'maximum' in schema and numeric > Decimal(str(schema['maximum'])):
            raise ValueError('{} is above its maximum'.format(path))
        if 'multipleOf' in schema:
            step = Decimal(str(schema['multipleOf']))
            if numeric % step != 0:
                raise ValueError('{} is not a multiple of {}'.format(path, step))
    if isinstance(value, list):
        if 'minItems' in schema and len(value) < int(schema['minItems']):
            raise ValueError('{} has too few items'.format(path))
        if 'maxItems' in schema and len(value) > int(schema['maxItems']):
            raise ValueError('{} has too many items'.format(path))
        if schema.get('uniqueItems') and len({_json_key(item) for item in value}) != len(value):
            raise ValueError('{} must contain unique items'.format(path))
        if 'items' in schema:
            for index, item in enumerate(value):
                _validate_schema(schema['items'], item, '{}[{}]'.format(path, index))
    if isinstance(value, dict):
        properties = schema.get('properties', {})
        required = schema.get('required', [])
        for key in required:
            if key not in value:
                raise ValueError('{}.{} is required'.format(path, key))
        if schema.get('additionalProperties') is False:
            extras = sorted(set(value) - set(properties))
            if extras:
                raise ValueError('{} has unexpected properties: {}'.format(path, extras))
        for key, item in value.items():
            if key in properties:
                _validate_schema(properties[key], item, '{}.{}'.format(path, key))

def _up_filter(value: JsonDict) -> JsonDict:
    columns = list(value['columns'])
    if 'group_key' not in columns or 'aggregate_value' not in columns:
        raise ValueError('Report columns must include group_key and aggregate_value')
    return {'where': {'field': 'account_status', 'operator': 'eq', 'value': value['segment']}, 'group_by': value['group_by'], 'aggregate': {'field': value['measure'], 'operation': value['calculation']}, 'projected_columns': columns}
UPSTREAM_EXECUTORS: Dict[str, Callable[[Any], Any]] = {'relay_09_filter': _up_filter}

def execute(variant_id: str, role: str, supplied_value: Any) -> Any:
    """Validate and execute one typed role without external communication."""
    if variant_id not in CONTRACTS:
        raise KeyError('Unknown relay variant: {}'.format(variant_id))
    contract = CONTRACTS[variant_id]
    role_contract = contract[role]
    _validate_schema(role_contract['input_schema'], supplied_value, '$.input')
    result = UPSTREAM_EXECUTORS[variant_id](deepcopy(supplied_value))
    _validate_schema(role_contract['output_schema'], result, '$.output')
    return result
