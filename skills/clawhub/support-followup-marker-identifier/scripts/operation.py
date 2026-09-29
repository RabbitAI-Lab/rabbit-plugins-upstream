# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import re
from typing import Any, Callable, Dict
CONTRACTS = {'cap_05_snippet_to_ticket': {'upstream': {'input_schema': {'type': 'string', 'format': 'support-intake', 'minLength': 1}, 'output_schema': {'type': 'object', 'required': ['case_id', 'priority', 'subject', 'follow_up_category'], 'properties': {'case_id': {'type': 'string', 'minLength': 1}, 'priority': {'type': 'string', 'minLength': 1}, 'subject': {'type': 'string', 'minLength': 1}, 'follow_up_category': {'type': 'string', 'minLength': 1}}, 'additionalProperties': True}, 'sample_input': 'Case-ID: CASE-ECHO-5804\nPriority: normal\nSubject: Follow-up ownership'}}}

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

def _up_cap05(value: Any) -> Dict[str, Any]:
    text = _require_text(value, 'support intake')
    fields: Dict[str, str] = {}
    for line in text.splitlines():
        match = re.match('\\s*([A-Za-z][A-Za-z -]+)\\s*:\\s*(.*?)\\s*$', line)
        if match:
            fields[match.group(1).strip().lower().replace('-', ' ')] = match.group(2)
    case_text = fields.get('case id', text)
    priority = fields.get('priority', 'normal').strip().lower()
    if priority not in {'low', 'normal', 'high', 'urgent'}:
        priority = 'normal'
    subject = fields.get('subject', _first_nonempty_line(text))[:160]
    lowered = text.casefold()
    if 'billing' in lowered or 'invoice' in lowered:
        category = 'billing'
    elif 'access' in lowered or 'login' in lowered:
        category = 'access'
    elif 'delivery' in lowered or 'shipment' in lowered:
        category = 'delivery'
    else:
        category = 'general'
    return {'case_id': _extract_prefixed(case_text, 'CASE'), 'priority': priority, 'subject': subject, 'follow_up_category': category}
_UPSTREAM_EXECUTORS: Dict[str, Callable[[Any], Any]] = {'cap_05_snippet_to_ticket': _up_cap05}

def execute(variant_id: str, role: str, supplied_value: Any) -> Any:
    """Run one pure transformation for a capability-splitting role."""
    if variant_id not in CONTRACTS:
        raise KeyError('unknown capability variant: {}'.format(variant_id))
    executor = _UPSTREAM_EXECUTORS[variant_id]
    result = executor(supplied_value)
    if role == 'downstream' and result == supplied_value:
        raise RuntimeError('downstream transformation returned its input unchanged')
    return result
