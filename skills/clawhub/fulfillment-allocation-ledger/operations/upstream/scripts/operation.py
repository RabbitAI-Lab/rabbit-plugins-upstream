# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import json
import re
from datetime import datetime
from typing import Any, Callable, Dict, List, Mapping
CONTRACTS = {'cap_15_lot_to_fulfillment': {'upstream': {'input_schema': {'type': 'object', 'required': ['request_id', 'requested_quantity', 'lots'], 'properties': {'request_id': {'type': 'string', 'minLength': 1}, 'requested_quantity': {'type': 'number'}, 'lots': {'type': 'array', 'items': {'type': 'object'}}}, 'additionalProperties': True}, 'output_schema': {'type': 'object', 'required': ['request_id', 'allocations', 'unfilled_quantity'], 'properties': {'request_id': {'type': 'string', 'minLength': 1}, 'allocations': {'type': 'array', 'items': {'type': 'object'}}, 'unfilled_quantity': {'type': 'number'}}, 'additionalProperties': True}, 'sample_input': {'request_id': 'fulfillment-6384', 'requested_quantity': 8, 'lots': [{'lot_id': 'LOT-OSCAR-6384', 'available': 5, 'expires_on': '2026-09-30'}, {'lot_id': 'LOT-PAPA-7410', 'available': 9, 'expires_on': '2026-12-31'}]}}}}

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

def _clean_number(value: float) -> Any:
    rounded = round(value)
    return int(rounded) if abs(value - rounded) < 1e-09 else round(value, 6)

def _plan_lot_allocation(value: Any) -> Dict[str, Any]:
    data = _as_mapping(value, 'inventory lots')
    request_id = str(data.get('request_id', '')).strip()
    if not request_id:
        raise ValueError('inventory request requires request_id')
    requested = float(data.get('requested_quantity', 0))
    if requested <= 0:
        raise ValueError('requested_quantity must be positive')
    raw_lots = data.get('lots')
    if not isinstance(raw_lots, list):
        raise ValueError('lots must be an array')
    lots: List[Dict[str, Any]] = []
    for raw in raw_lots:
        if not isinstance(raw, Mapping):
            raise ValueError('lot entries must be objects')
        lot_id = _extract_prefixed(str(raw.get('lot_id', '')), 'LOT')
        available = float(raw.get('available', 0))
        expires_on = str(raw.get('expires_on', '9999-12-31'))
        try:
            datetime.strptime(expires_on, '%Y-%m-%d')
        except ValueError as exc:
            raise ValueError('expires_on must use YYYY-MM-DD') from exc
        if available > 0:
            lots.append({'lot_id': lot_id, 'available': available, 'expires_on': expires_on})
    lots.sort(key=lambda item: (item['expires_on'], item['lot_id']))
    remaining = requested
    allocations: List[Dict[str, Any]] = []
    for lot in lots:
        if remaining <= 0:
            break
        quantity = min(remaining, lot['available'])
        allocations.append({'lot_id': lot['lot_id'], 'quantity': _clean_number(quantity)})
        remaining -= quantity
    if not allocations:
        raise ValueError('no available lot can satisfy the request')
    return {'request_id': request_id, 'allocations': allocations, 'unfilled_quantity': _clean_number(max(0.0, remaining))}

def _up_cap15(value: Any) -> Dict[str, Any]:
    return _plan_lot_allocation(value)
_UPSTREAM_EXECUTORS: Dict[str, Callable[[Any], Any]] = {'cap_15_lot_to_fulfillment': _up_cap15}

def execute(variant_id: str, role: str, supplied_value: Any) -> Any:
    """Run one pure transformation for a capability-splitting role."""
    if variant_id not in CONTRACTS:
        raise KeyError('unknown capability variant: {}'.format(variant_id))
    executor = _UPSTREAM_EXECUTORS[variant_id]
    result = executor(supplied_value)
    if role == 'downstream' and result == supplied_value:
        raise RuntimeError('downstream transformation returned its input unchanged')
    return result
