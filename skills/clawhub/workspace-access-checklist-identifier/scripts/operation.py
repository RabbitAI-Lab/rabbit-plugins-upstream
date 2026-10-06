# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import json
import re
from typing import Any, Callable, Dict, Mapping
CONTRACTS = {'cap_14_share_to_collaboration': {'upstream': {'input_schema': {'type': 'object', 'required': ['workspace_id', 'current_members', 'approved_members'], 'properties': {'workspace_id': {'type': 'string', 'minLength': 1}, 'current_members': {'type': 'array', 'items': {'type': 'object'}}, 'approved_members': {'type': 'array', 'items': {'type': 'object'}}}, 'additionalProperties': True}, 'output_schema': {'type': 'object', 'required': ['workspace_id', 'added', 'removed', 'role_changed', 'external_entries'], 'properties': {'workspace_id': {'type': 'string', 'minLength': 1}, 'added': {'type': 'array', 'items': {'type': 'object'}}, 'removed': {'type': 'array', 'items': {'type': 'object'}}, 'role_changed': {'type': 'array', 'items': {'type': 'object'}}, 'external_entries': {'type': 'array', 'items': {'type': 'object'}}}, 'additionalProperties': True}, 'sample_input': {'workspace_id': 'SHARE-NOVEMBER-5268', 'organization_domain': 'northbridge.example', 'current_members': [{'principal_id': 'ops', 'role': 'editor', 'domain': 'northbridge.example'}], 'approved_members': [{'principal_id': 'ops', 'role': 'viewer', 'domain': 'northbridge.example'}]}}}}

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

def _member_map(items: Any) -> Dict[str, Dict[str, str]]:
    if not isinstance(items, list):
        raise ValueError('workspace member list must be an array')
    result: Dict[str, Dict[str, str]] = {}
    for raw in items:
        if not isinstance(raw, Mapping) or not raw.get('principal_id'):
            raise ValueError('workspace members require principal_id')
        principal_id = str(raw['principal_id'])
        result[principal_id] = {'principal_id': principal_id, 'role': str(raw.get('role', 'member')), 'domain': str(raw.get('domain', '')), 'principal_type': str(raw.get('principal_type', 'user'))}
    return result

def _compare_access_lists(value: Any) -> Dict[str, Any]:
    data = _as_mapping(value, 'workspace access lists')
    workspace_id = _extract_prefixed(str(data.get('workspace_id', '')), 'SHARE')
    current = _member_map(data.get('current_members'))
    approved = _member_map(data.get('approved_members'))
    added = [current[key] for key in sorted(current.keys() - approved.keys())]
    removed = [approved[key] for key in sorted(approved.keys() - current.keys())]
    role_changed = [{'principal_id': key, 'from': approved[key]['role'], 'to': current[key]['role']} for key in sorted(current.keys() & approved.keys()) if current[key]['role'] != approved[key]['role']]
    organization_domain = str(data.get('organization_domain', '')).casefold()
    external_entries = [item for item in current.values() if organization_domain and item['domain'] and (item['domain'].casefold() != organization_domain)]
    return {'workspace_id': workspace_id, 'added': added, 'removed': removed, 'role_changed': role_changed, 'external_entries': sorted(external_entries, key=lambda item: item['principal_id'])}

def _up_cap14(value: Any) -> Dict[str, Any]:
    return _compare_access_lists(value)
_UPSTREAM_EXECUTORS: Dict[str, Callable[[Any], Any]] = {'cap_14_share_to_collaboration': _up_cap14}

def execute(variant_id: str, role: str, supplied_value: Any) -> Any:
    """Run one pure transformation for a capability-splitting role."""
    if variant_id not in CONTRACTS:
        raise KeyError('unknown capability variant: {}'.format(variant_id))
    executor = _UPSTREAM_EXECUTORS[variant_id]
    result = executor(supplied_value)
    if role == 'downstream' and result == supplied_value:
        raise RuntimeError('downstream transformation returned its input unchanged')
    return result
