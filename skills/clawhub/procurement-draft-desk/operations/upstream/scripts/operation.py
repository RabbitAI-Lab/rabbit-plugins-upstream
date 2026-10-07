# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import csv
import io
import re
from typing import Any, Callable, Dict, Mapping
CONTRACTS = {'cap_08_vendor_to_procurement': {'upstream': {'input_schema': {'oneOf': [{'type': 'string', 'format': 'supplier-csv-row', 'minLength': 1}, {'type': 'object', 'required': ['supplier_id', 'currency', 'lead_days', 'incoterm', 'renewal_month'], 'properties': {'supplier_id': {'type': 'string', 'minLength': 1}, 'currency': {'type': 'string', 'minLength': 1}, 'lead_days': {'type': 'integer'}, 'incoterm': {'type': 'string', 'minLength': 1}, 'renewal_month': {'type': 'string', 'minLength': 1}}, 'additionalProperties': True}]}, 'output_schema': {'type': 'object', 'required': ['supplier_id', 'currency', 'lead_days', 'incoterm', 'renewal_month'], 'properties': {'supplier_id': {'type': 'string', 'minLength': 1}, 'currency': {'type': 'string', 'minLength': 1}, 'lead_days': {'type': 'integer'}, 'incoterm': {'type': 'string', 'minLength': 1}, 'renewal_month': {'type': 'string', 'minLength': 1}}, 'additionalProperties': True}, 'sample_input': 'supplier_id,currency,lead_days,incoterm,renewal_month\nVENDOR-HOTEL-8462,USD,14,FCA,2026-11\n'}}}

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

def _parse_supplier_terms(value: Any) -> Dict[str, Any]:
    if isinstance(value, Mapping):
        row = {str(key): val for key, val in value.items()}
    else:
        text = _require_text(value, 'supplier terms')
        reader = csv.DictReader(io.StringIO(text))
        row = next(reader, None)
        if row is None:
            raise ValueError('supplier terms table has no data row')
    required = ['supplier_id', 'currency', 'lead_days', 'incoterm', 'renewal_month']
    missing = [name for name in required if row.get(name) in (None, '')]
    if missing:
        raise ValueError('supplier terms missing fields: {}'.format(', '.join(missing)))
    try:
        lead_days = int(str(row['lead_days']).strip())
    except ValueError as exc:
        raise ValueError('lead_days must be an integer') from exc
    if lead_days < 0:
        raise ValueError('lead_days must be non-negative')
    renewal_month = str(row['renewal_month']).strip()
    if not re.fullmatch('\\d{4}-\\d{2}', renewal_month):
        raise ValueError('renewal_month must use YYYY-MM')
    return {'supplier_id': _extract_prefixed(str(row['supplier_id']), 'VENDOR'), 'currency': str(row['currency']).strip().upper(), 'lead_days': lead_days, 'incoterm': str(row['incoterm']).strip().upper(), 'renewal_month': renewal_month}

def _up_cap08(value: Any) -> Dict[str, Any]:
    return _parse_supplier_terms(value)
_UPSTREAM_EXECUTORS: Dict[str, Callable[[Any], Any]] = {'cap_08_vendor_to_procurement': _up_cap08}

def execute(variant_id: str, role: str, supplied_value: Any) -> Any:
    """Run one pure transformation for a capability-splitting role."""
    if variant_id not in CONTRACTS:
        raise KeyError('unknown capability variant: {}'.format(variant_id))
    executor = _UPSTREAM_EXECUTORS[variant_id]
    result = executor(supplied_value)
    if role == 'downstream' and result == supplied_value:
        raise RuntimeError('downstream transformation returned its input unchanged')
    return result
