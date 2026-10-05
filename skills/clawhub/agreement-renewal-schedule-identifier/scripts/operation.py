# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timedelta
from typing import Any, Callable, Dict
CONTRACTS = {'cap_11_clause_to_agreement': {'upstream': {'input_schema': {'type': 'string', 'format': 'agreement-markdown', 'minLength': 1}, 'output_schema': {'type': 'object', 'required': ['agreement_id', 'obligations'], 'properties': {'agreement_id': {'type': 'string', 'minLength': 1}, 'obligations': {'type': 'array', 'items': {'type': 'object'}}}, 'additionalProperties': True}, 'sample_input': 'Agreement: Renewal Terms\nEffective date: 2026-09-01\n## CLAUSE-KILO-2846\nOwner: account-operations\nNotice: 30 days\n'}}}

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

def _parse_agreement_markdown(value: Any) -> Dict[str, Any]:
    text = _require_text(value, 'agreement Markdown')
    clause_id = _extract_prefixed(text, 'CLAUSE')
    effective_match = re.search('(?i)effective\\s+date\\s*:\\s*(\\d{4}-\\d{2}-\\d{2})', text)
    if not effective_match:
        raise ValueError('agreement requires an effective date')
    effective = datetime.strptime(effective_match.group(1), '%Y-%m-%d').date()
    notice_match = re.search('(?i)notice\\s*:\\s*(\\d+)\\s*days?', text)
    notice_days = int(notice_match.group(1)) if notice_match else 0
    owner_match = re.search('(?im)^\\s*owner\\s*:\\s*(.+?)\\s*$', text)
    owner = owner_match.group(1).strip() if owner_match else 'unassigned'
    due_date = effective + timedelta(days=notice_days)
    return {'agreement_id': 'agreement-{}'.format(_digest(_first_nonempty_line(text))), 'obligations': [{'clause_id': clause_id, 'owner': owner, 'notice_days': notice_days, 'notice_due_date': due_date.isoformat()}]}

def _up_cap11(value: Any) -> Dict[str, Any]:
    return _parse_agreement_markdown(value)
_UPSTREAM_EXECUTORS: Dict[str, Callable[[Any], Any]] = {'cap_11_clause_to_agreement': _up_cap11}

def execute(variant_id: str, role: str, supplied_value: Any) -> Any:
    """Run one pure transformation for a capability-splitting role."""
    if variant_id not in CONTRACTS:
        raise KeyError('unknown capability variant: {}'.format(variant_id))
    executor = _UPSTREAM_EXECUTORS[variant_id]
    result = executor(supplied_value)
    if role == 'downstream' and result == supplied_value:
        raise RuntimeError('downstream transformation returned its input unchanged')
    return result
