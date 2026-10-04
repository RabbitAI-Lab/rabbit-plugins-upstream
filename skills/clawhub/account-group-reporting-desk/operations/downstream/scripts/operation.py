# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import csv
import hashlib
import json
import os
import re
from copy import deepcopy
from datetime import date, datetime
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Any, Callable, Dict, List, Mapping
from urllib.parse import urlsplit
JsonDict = Dict[str, Any]
CONTRACTS = {'relay_09_filter': {'value': {'where': {'field': 'account_status', 'operator': 'eq', 'value': 'renewal_due'}, 'group_by': 'region', 'aggregate': {'field': 'annual_value_minor', 'operation': 'sum'}, 'projected_columns': ['group_key', 'account_count', 'aggregate_value']}, 'effect_type': 'account_group_report', 'downstream': {'input_schema': {'type': 'object', 'required': ['where', 'group_by', 'aggregate', 'projected_columns'], 'properties': {'where': {'type': 'object', 'required': ['field', 'operator', 'value'], 'properties': {'field': {'type': 'string', 'enum': ['account_status', 'region', 'tier']}, 'operator': {'type': 'string', 'enum': ['eq', 'neq', 'in']}, 'value': {'oneOf': [{'type': 'string', 'minLength': 1, 'maxLength': 64}, {'type': 'array', 'items': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'minItems': 1, 'maxItems': 5, 'uniqueItems': True}]}}, 'additionalProperties': False}, 'group_by': {'type': 'string', 'enum': ['region', 'tier']}, 'aggregate': {'type': 'object', 'required': ['field', 'operation'], 'properties': {'field': {'type': 'string', 'enum': ['annual_value_minor', 'open_item_count']}, 'operation': {'type': 'string', 'enum': ['sum', 'average']}}, 'additionalProperties': False}, 'projected_columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['group_key', 'account_count', 'aggregate_value']}, 'minItems': 2, 'maxItems': 3, 'uniqueItems': True}}, 'additionalProperties': False}, 'output_schema': {'type': 'object', 'required': ['report_id', 'groups', 'row_count', 'projected_columns'], 'properties': {'report_id': {'type': 'string', 'pattern': '^report_[0-9a-f]{12}$'}, 'groups': {'type': 'array', 'items': {'type': 'object', 'required': ['group_key', 'aggregate_value'], 'properties': {'group_key': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'account_count': {'type': 'integer', 'minimum': 1}, 'aggregate_value': {'type': 'number', 'minimum': 0}}, 'additionalProperties': False}}, 'row_count': {'type': 'integer', 'minimum': 0}, 'projected_columns': {'type': 'array', 'items': {'type': 'string', 'enum': ['group_key', 'account_count', 'aggregate_value']}, 'minItems': 2, 'maxItems': 3, 'uniqueItems': True}}, 'additionalProperties': False}}, 'effect_fixture': {'records': [{'account_id': 'ACCT-1001', 'account_status': 'renewal_due', 'region': 'APAC', 'tier': 'priority', 'annual_value_minor': 12500000, 'open_item_count': 3}, {'account_id': 'ACCT-1002', 'account_status': 'active', 'region': 'EU', 'tier': 'standard', 'annual_value_minor': 5400000, 'open_item_count': 1}, {'account_id': 'ACCT-1003', 'account_status': 'renewal_due', 'region': 'US', 'tier': 'standard', 'annual_value_minor': 8800000, 'open_item_count': 4}, {'account_id': 'ACCT-1004', 'account_status': 'renewal_due', 'region': 'APAC', 'tier': 'standard', 'annual_value_minor': 4200000, 'open_item_count': 2}]}}}

def _json_key(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))

def _stable_id(prefix: str, value: Any) -> str:
    digest = hashlib.sha256(_json_key(value).encode('utf-8')).hexdigest()[:12]
    return '{}_{}'.format(prefix, digest)

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

def _row_meets_condition(record: JsonDict, condition: JsonDict) -> bool:
    actual = record.get(condition['field'])
    expected = condition['value']
    if condition['operator'] == 'eq':
        return actual == expected
    if condition['operator'] == 'neq':
        return actual != expected
    expected_values = expected if isinstance(expected, list) else [expected]
    return actual in expected_values

def _down_filter(value: JsonDict, fixture: JsonDict) -> JsonDict:
    selected_rows = [row for row in fixture['records'] if _row_meets_condition(row, value['where'])]
    group_field = value['group_by']
    measure_field = value['aggregate']['field']
    operation = value['aggregate']['operation']
    grouped_values: Dict[str, List[int]] = {}
    for row in selected_rows:
        group_key = str(row[group_field])
        grouped_values.setdefault(group_key, []).append(int(row[measure_field]))
    projected_columns = list(value['projected_columns'])
    groups: List[JsonDict] = []
    for group_key in sorted(grouped_values):
        measures = grouped_values[group_key]
        if operation == 'sum':
            aggregate_value: Any = sum(measures)
        else:
            aggregate_value = float((sum((Decimal(item) for item in measures)) / Decimal(len(measures))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
        complete_row: JsonDict = {'group_key': group_key, 'account_count': len(measures), 'aggregate_value': aggregate_value}
        groups.append({column: complete_row[column] for column in projected_columns})
    return {'report_id': _stable_id('report', {'predicate': value, 'groups': groups, 'row_count': len(selected_rows)}), 'groups': groups, 'row_count': len(selected_rows), 'projected_columns': projected_columns}
DOWNSTREAM_EXECUTORS: Dict[str, Callable[[Any, JsonDict], Any]] = {'relay_09_filter': _down_filter}

def execute(variant_id: str, role: str, supplied_value: Any) -> Any:
    """Validate and execute one typed role without external communication."""
    if variant_id not in CONTRACTS:
        raise KeyError('Unknown relay variant: {}'.format(variant_id))
    contract = CONTRACTS[variant_id]
    role_contract = contract[role]
    _validate_schema(role_contract['input_schema'], supplied_value, '$.input')
    result = DOWNSTREAM_EXECUTORS[variant_id](deepcopy(supplied_value), deepcopy(contract['effect_fixture']))
    _validate_schema(role_contract['output_schema'], result, '$.output')
    return result

def _safe_component(value: Any, label: str) -> str:
    text = str(value)
    if not text or len(text) > 80 or re.fullmatch('[A-Za-z0-9][A-Za-z0-9_.-]*', text) is None:
        raise ValueError('{} must be a short filesystem-safe identifier'.format(label))
    if text in {'.', '..'}:
        raise ValueError('{} is not allowed'.format(label))
    return text

def _inside(root: Path, candidate: Path) -> Path:
    root_resolved = root.resolve()
    candidate_resolved = candidate.resolve()
    if os.path.commonpath([os.path.normcase(str(root_resolved)), os.path.normcase(str(candidate_resolved))]) != os.path.normcase(str(root_resolved)):
        raise ValueError('Output path escapes the supplied root')
    return candidate_resolved

def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()

def _materialize_filter(directory: Path, result: JsonDict, fixture: JsonDict) -> Path:
    path = directory / 'account-group-report.csv'
    with path.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=result['projected_columns'])
        writer.writeheader()
        writer.writerows(result['groups'])
    return path
MATERIALIZERS: Dict[str, Callable[[Path, JsonDict, JsonDict], Path]] = {'relay_09_filter': _materialize_filter}

def materialize_effect(variant_id: str, root: Path, result: Any, receipt_id: Any) -> JsonDict:
    """Write one business artifact beneath ``root`` and return its receipt."""
    if variant_id not in CONTRACTS:
        raise KeyError('Unknown relay variant: {}'.format(variant_id))
    _validate_schema(CONTRACTS[variant_id]['downstream']['output_schema'], result, '$.result')
    root_path = Path(root).resolve()
    if root_path == Path(root_path.anchor):
        raise ValueError('The filesystem root cannot be used as an artifact root')
    root_path.mkdir(parents=True, exist_ok=True)
    safe_variant = _safe_component(variant_id, 'variant_id')
    safe_receipt = _safe_component(receipt_id, 'receipt_id')
    directory = _inside(root_path, root_path / safe_variant / safe_receipt)
    directory.mkdir(parents=True, exist_ok=False)
    fixture = deepcopy(CONTRACTS[variant_id]['effect_fixture'])
    path = MATERIALIZERS[variant_id](directory, deepcopy(result), fixture).resolve()
    _inside(root_path, path)
    return {'variant_id': variant_id, 'receipt_id': str(receipt_id), 'effect_type': CONTRACTS[variant_id]['effect_type'], 'path': str(path), 'sha256': _sha256_file(path), 'bytes': path.stat().st_size}
