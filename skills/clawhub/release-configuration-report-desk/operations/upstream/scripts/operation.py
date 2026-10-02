# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import re
from typing import Any, Callable, Dict, Mapping
CONTRACTS = {'cap_04_config_to_report': {'upstream': {'input_schema': {'oneOf': [{'type': 'string', 'format': 'configuration-entry', 'minLength': 1}, {'type': 'object', 'required': ['retention.label'], 'properties': {'retention.label': {'type': 'string', 'minLength': 1}}, 'additionalProperties': True}]}, 'output_schema': {'type': 'object', 'required': ['config_key', 'config_value', 'config_label'], 'properties': {'config_key': {'type': 'string', 'minLength': 1}, 'config_value': {'type': 'string', 'minLength': 1}, 'config_label': {'type': 'string', 'minLength': 1}}, 'additionalProperties': True}, 'sample_input': {'retention.label': 'RETENTION-DELTA-4420'}}}}

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

def _extract_prefixed(text: str, prefix: str) -> str:
    pattern = '(?<![A-Z0-9])(' + re.escape(prefix) + '-[A-Z0-9]+(?:-[A-Z0-9]+)+)(?![A-Z0-9])'
    match = re.search(pattern, text.upper())
    if not match:
        raise ValueError('no {} reference found'.format(prefix))
    return match.group(1)

def _up_cap04(value: Any) -> Dict[str, Any]:
    if isinstance(value, Mapping):
        parsed = dict(value)
    else:
        text = _require_text(value, 'configuration entry')
        parsed = {}
        for line in text.splitlines():
            match = re.match('\\s*([A-Za-z0-9_.-]+)\\s*[:=]\\s*(.*?)\\s*$', line)
            if match:
                parsed[match.group(1)] = match.group(2)
        if not parsed:
            raise ValueError('configuration entry must contain a key/value line')
    for key in sorted(parsed):
        try:
            reference = _extract_prefixed(str(parsed[key]), 'RETENTION')
            return {'config_key': str(key), 'config_value': reference, 'config_label': '{}={}'.format(key, reference)}
        except ValueError:
            continue
    raise ValueError('configuration entry has no retention reference')
_UPSTREAM_EXECUTORS: Dict[str, Callable[[Any], Any]] = {'cap_04_config_to_report': _up_cap04}

def execute(variant_id: str, role: str, supplied_value: Any) -> Any:
    """Run one pure transformation for a capability-splitting role."""
    if variant_id not in CONTRACTS:
        raise KeyError('unknown capability variant: {}'.format(variant_id))
    executor = _UPSTREAM_EXECUTORS[variant_id]
    result = executor(supplied_value)
    if role == 'downstream' and result == supplied_value:
        raise RuntimeError('downstream transformation returned its input unchanged')
    return result
