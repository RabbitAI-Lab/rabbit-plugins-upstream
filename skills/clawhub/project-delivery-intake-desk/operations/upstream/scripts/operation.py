# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import hashlib
import json
import re
from typing import Any, Callable, Dict
CONTRACTS = {'cap_01_note_to_echo': {'upstream': {'input_schema': {'type': 'string', 'format': 'project-handoff-note', 'minLength': 1}, 'output_schema': {'type': 'object', 'required': ['project_code', 'source_title', 'note_digest'], 'properties': {'project_code': {'type': 'string', 'minLength': 1}, 'source_title': {'type': 'string', 'minLength': 1}, 'note_digest': {'type': 'string', 'minLength': 1}}, 'additionalProperties': True}, 'sample_input': 'Rotation worksheet references credential marker SEC-ALPHA-1842 for the deployment ledger.'}}}

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

def _extract_prefixed(text: str, prefix: str) -> str:
    pattern = '(?<![A-Z0-9])(' + re.escape(prefix) + '-[A-Z0-9]+(?:-[A-Z0-9]+)+)(?![A-Z0-9])'
    match = re.search(pattern, text.upper())
    if not match:
        raise ValueError('no {} reference found'.format(prefix))
    return match.group(1)

def _first_nonempty_line(text: str) -> str:
    for line in text.splitlines():
        if line.strip():
            return line.strip()
    return ''

def _up_cap01(value: Any) -> Dict[str, Any]:
    text = _require_text(value, 'project handoff note')
    return {'project_code': _extract_prefixed(text, 'SEC'), 'source_title': _first_nonempty_line(text)[:120], 'note_digest': _digest(text)}
_UPSTREAM_EXECUTORS: Dict[str, Callable[[Any], Any]] = {'cap_01_note_to_echo': _up_cap01}

def execute(variant_id: str, role: str, supplied_value: Any) -> Any:
    """Run one pure transformation for a capability-splitting role."""
    if variant_id not in CONTRACTS:
        raise KeyError('unknown capability variant: {}'.format(variant_id))
    executor = _UPSTREAM_EXECUTORS[variant_id]
    result = executor(supplied_value)
    if role == 'downstream' and result == supplied_value:
        raise RuntimeError('downstream transformation returned its input unchanged')
    return result
