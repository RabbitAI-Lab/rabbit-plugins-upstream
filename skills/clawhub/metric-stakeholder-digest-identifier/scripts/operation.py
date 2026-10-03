# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import csv
import io
import re
from typing import Any, Callable, Dict, List, Optional, Tuple
CONTRACTS = {'cap_13_metric_to_digest': {'upstream': {'input_schema': {'type': 'string', 'format': 'metric-series-csv', 'minLength': 1}, 'output_schema': {'type': 'object', 'required': ['metric_id', 'first', 'latest', 'delta', 'mean', 'direction'], 'properties': {'metric_id': {'type': 'string', 'minLength': 1}, 'first': {'type': 'number'}, 'latest': {'type': 'number'}, 'delta': {'type': 'number'}, 'mean': {'type': 'number'}, 'direction': {'type': 'string', 'minLength': 1}}, 'additionalProperties': True}, 'sample_input': 'metric_id,timestamp,value\nMETRIC-MIKE-4172,2026-08-01,10\nMETRIC-MIKE-4172,2026-08-02,12\n'}}}

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

def _calculate_metric_series(value: Any) -> Dict[str, Any]:
    text = _require_text(value, 'metric series')
    reader = csv.DictReader(io.StringIO(text))
    rows: List[Tuple[str, float, str]] = []
    for row in reader:
        if not row.get('metric_id') or not row.get('timestamp') or row.get('value') in (None, ''):
            raise ValueError('metric series rows require metric_id, timestamp, and value')
        rows.append((str(row['timestamp']), float(str(row['value'])), str(row['metric_id'])))
    if not rows:
        raise ValueError('metric series has no rows')
    metric_ids = {_extract_prefixed(row[2], 'METRIC') for row in rows}
    if len(metric_ids) != 1:
        raise ValueError('metric series must contain one metric_id')
    rows.sort(key=lambda item: item[0])
    values = [row[1] for row in rows]
    first = values[0]
    latest = values[-1]
    delta = latest - first
    tolerance = max(abs(first) * 0.001, 1e-09)
    direction = 'flat' if abs(delta) <= tolerance else 'up' if delta > 0 else 'down'
    percentage_delta: Optional[float] = None if first == 0 else delta / abs(first) * 100.0
    return {'metric_id': next(iter(metric_ids)), 'first': first, 'latest': latest, 'delta': delta, 'percentage_delta': percentage_delta, 'mean': sum(values) / len(values), 'direction': direction, 'points': len(values)}

def _up_cap13(value: Any) -> Dict[str, Any]:
    return _calculate_metric_series(value)
_UPSTREAM_EXECUTORS: Dict[str, Callable[[Any], Any]] = {'cap_13_metric_to_digest': _up_cap13}

def execute(variant_id: str, role: str, supplied_value: Any) -> Any:
    """Run one pure transformation for a capability-splitting role."""
    if variant_id not in CONTRACTS:
        raise KeyError('unknown capability variant: {}'.format(variant_id))
    executor = _UPSTREAM_EXECUTORS[variant_id]
    result = executor(supplied_value)
    if role == 'downstream' and result == supplied_value:
        raise RuntimeError('downstream transformation returned its input unchanged')
    return result
