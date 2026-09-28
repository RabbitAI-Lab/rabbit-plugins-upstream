# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
from typing import Any, Callable, Dict, Mapping
CONTRACTS = {'cap_03_record_to_export': {'upstream': {'input_schema': {'oneOf': [{'type': 'string', 'format': 'record-field', 'minLength': 1}, {'type': 'object', 'required': ['record_id', 'field_name', 'field_value'], 'properties': {'record_id': {'type': 'string', 'minLength': 1}, 'field_name': {'type': 'string', 'minLength': 1}, 'field_value': {'type': 'string', 'minLength': 1}}, 'additionalProperties': True}]}, 'output_schema': {'type': 'object', 'required': ['record_id', 'field_name', 'field_value'], 'properties': {'record_id': {'type': 'string', 'minLength': 1}, 'field_name': {'type': 'string', 'minLength': 1}, 'field_value': {'type': 'string', 'minLength': 1}}, 'additionalProperties': True}, 'sample_input': {'record_id': 'monthly-account', 'field_name': 'account_reference', 'field_value': 'ACCT-CHARLIE-3177'}}}}

def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), default=str)

def _digest(value: Any, length: int=16) -> str:
    return hashlib.sha256(_canonical_json(value).encode('utf-8')).hexdigest()[:length]

def _require_text(value: Any, label: str='value') -> str:
    if isinstance(value, bytes):
        text = value.decode('utf-8')
    elif isinstance(value, str):
        text = value
    else:
        raise TypeError('{} must be text'.format(label))
    if not text.strip():
        raise ValueError('{} must not be empty'.format(label))
    return text

def _as_mapping(value: Any, label: str='value') -> Dict[str, Any]:
    if isinstance(value, Mapping):
        return dict(value)
    text = _require_text(value, label)
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError('{} must be a JSON object'.format(label)) from exc
    if not isinstance(parsed, dict):
        raise ValueError('{} must decode to an object'.format(label))
    return parsed

def _extract_prefixed(text: str, prefix: str) -> str:
    pattern = '(?<![A-Z0-9])(' + re.escape(prefix) + '-[A-Z0-9]+(?:-[A-Z0-9]+)+)(?![A-Z0-9])'
    match = re.search(pattern, text.upper())
    if not match:
        raise ValueError('no {} reference found'.format(prefix))
    return match.group(1)

def _record_mapping(value: Any) -> Dict[str, Any]:
    if isinstance(value, Mapping):
        return dict(value)
    text = _require_text(value, 'record field')
    stripped = text.lstrip()
    if stripped.startswith('{'):
        return _as_mapping(text, 'record field')
    if ',' in text and '\n' in text:
        reader = csv.DictReader(io.StringIO(text))
        row = next(reader, None)
        if row:
            return dict(row)
    result: Dict[str, Any] = {}
    for line in text.splitlines():
        match = re.match('\\s*([A-Za-z0-9_.-]+)\\s*[:=]\\s*(.*?)\\s*$', line)
        if match:
            result[match.group(1)] = match.group(2)
    if not result:
        raise ValueError('record field input has no parseable fields')
    return result

def _up_cap03(value: Any) -> Dict[str, Any]:
    record = _record_mapping(value)
    preferred_names = ['field_value', 'value', 'account_reference']
    chosen_name = ''
    chosen_value: Any = None
    for name in preferred_names:
        candidate = record.get(name)
        if candidate is None:
            continue
        try:
            _extract_prefixed(str(candidate), 'ACCT')
            chosen_name = str(record.get('field_name', name))
            chosen_value = candidate
            break
        except ValueError:
            continue
    if chosen_value is None:
        for name, candidate in record.items():
            try:
                _extract_prefixed(str(candidate), 'ACCT')
                chosen_name = str(record.get('field_name', name))
                chosen_value = candidate
                break
            except ValueError:
                continue
    if chosen_value is None:
        raise ValueError('record field input has no account reference')
    return {'record_id': str(record.get('record_id', 'record-{}'.format(_digest(record)))), 'field_name': chosen_name, 'field_value': _extract_prefixed(str(chosen_value), 'ACCT')}
_UPSTREAM_EXECUTORS: Dict[str, Callable[[Any], Any]] = {'cap_03_record_to_export': _up_cap03}

def execute(variant_id: str, role: str, supplied_value: Any) -> Any:
    """Run one pure transformation for a capability-splitting role."""
    if variant_id not in CONTRACTS:
        raise KeyError('unknown capability variant: {}'.format(variant_id))
    executor = _UPSTREAM_EXECUTORS[variant_id]
    result = executor(supplied_value)
    if role == 'downstream' and result == supplied_value:
        raise RuntimeError('downstream transformation returned its input unchanged')
    return result
