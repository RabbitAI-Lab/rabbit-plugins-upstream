# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import json
import re
from typing import Any, Callable, Dict, Mapping
CONTRACTS = {'cap_09_care_to_referral': {'upstream': {'input_schema': {'type': 'object', 'required': ['referral_id', 'specialty', 'urgency', 'requested_window'], 'properties': {'referral_id': {'type': 'string', 'minLength': 1}, 'specialty': {'type': 'string', 'minLength': 1}, 'urgency': {'type': 'string', 'minLength': 1}, 'requested_window': {'type': 'string', 'minLength': 1}}, 'additionalProperties': True}, 'output_schema': {'type': 'object', 'required': ['referral_id', 'specialty', 'urgency_band', 'requested_window'], 'properties': {'referral_id': {'type': 'string', 'minLength': 1}, 'specialty': {'type': 'string', 'minLength': 1}, 'urgency_band': {'type': 'string', 'minLength': 1}, 'requested_window': {'type': 'string', 'minLength': 1}}, 'additionalProperties': True}, 'sample_input': {'referral_id': 'CARE-INDIA-9548', 'specialty': 'cardiology', 'urgency': 'priority', 'requested_window': '2026-09', 'contact_fields': {'name': 'omitted'}}}}}

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

def _parse_referral_form(value: Any) -> Dict[str, Any]:
    form = _as_mapping(value, 'referral form')
    required = ['referral_id', 'specialty', 'urgency', 'requested_window']
    missing = [name for name in required if form.get(name) in (None, '')]
    if missing:
        raise ValueError('referral form missing fields: {}'.format(', '.join(missing)))
    urgency = str(form['urgency']).strip().lower()
    urgency_map = {'low': 'routine', 'routine': 'routine', 'normal': 'routine', 'medium': 'priority', 'priority': 'priority', 'high': 'urgent', 'urgent': 'urgent'}
    if urgency not in urgency_map:
        raise ValueError('unsupported urgency value')
    return {'referral_id': _extract_prefixed(str(form['referral_id']), 'CARE'), 'specialty': str(form['specialty']).strip().lower(), 'urgency_band': urgency_map[urgency], 'requested_window': str(form['requested_window']).strip()}

def _up_cap09(value: Any) -> Dict[str, Any]:
    return _parse_referral_form(value)
_UPSTREAM_EXECUTORS: Dict[str, Callable[[Any], Any]] = {'cap_09_care_to_referral': _up_cap09}

def execute(variant_id: str, role: str, supplied_value: Any) -> Any:
    """Run one pure transformation for a capability-splitting role."""
    if variant_id not in CONTRACTS:
        raise KeyError('unknown capability variant: {}'.format(variant_id))
    executor = _UPSTREAM_EXECUTORS[variant_id]
    result = executor(supplied_value)
    if role == 'downstream' and result == supplied_value:
        raise RuntimeError('downstream transformation returned its input unchanged')
    return result
