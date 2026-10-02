# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import csv
import re
from typing import Any, Callable, Dict, List, Mapping
CONTRACTS = {'cap_10_candidate_to_interview': {'upstream': {'input_schema': {'oneOf': [{'type': 'string', 'format': 'candidate-role-yaml', 'minLength': 1}, {'type': 'object', 'required': ['candidate_id', 'profile', 'role'], 'properties': {'candidate_id': {'type': 'string', 'minLength': 1}, 'profile': {'type': 'object'}, 'role': {'type': 'object'}}, 'additionalProperties': True}]}, 'output_schema': {'type': 'object', 'required': ['candidate_id', 'matched_required', 'missing_required', 'topics'], 'properties': {'candidate_id': {'type': 'string', 'minLength': 1}, 'matched_required': {'type': 'array', 'items': {'type': 'string'}}, 'missing_required': {'type': 'array', 'items': {'type': 'string'}}, 'topics': {'type': 'array', 'items': {'type': 'string'}}}, 'additionalProperties': True}, 'sample_input': 'candidate_id: CANDIDATE-JULIET-1673\nprofile:\n  skills:\n    - Python\n    - SQL\nrole:\n  required_skills:\n    - Python\n'}}}

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

def _inline_list(value: str) -> List[str]:
    stripped = value.strip()
    if not stripped:
        return []
    if stripped.startswith('[') and stripped.endswith(']'):
        inner = stripped[1:-1]
        return [item.strip().strip('"\'') for item in next(csv.reader([inner], skipinitialspace=True)) if item.strip()]
    return [stripped.strip('"\'')]

def _parse_candidate_yaml_like(value: Any) -> Dict[str, Any]:
    if isinstance(value, Mapping):
        data = dict(value)
        profile = data.get('profile', {}) if isinstance(data.get('profile', {}), Mapping) else {}
        role = data.get('role', {}) if isinstance(data.get('role', {}), Mapping) else {}
        candidate_id = str(data.get('candidate_id', ''))
        profile_skills = list(profile.get('skills', data.get('profile_skills', [])))
        required_skills = list(role.get('required_skills', data.get('required_skills', [])))
        optional_skills = list(role.get('optional_skills', data.get('optional_skills', [])))
    else:
        text = _require_text(value, 'candidate profile')
        candidate_id = ''
        lists: Dict[str, List[str]] = {'profile.skills': [], 'role.required_skills': [], 'role.optional_skills': []}
        section = ''
        active_list = ''
        for raw in text.splitlines():
            if not raw.strip() or raw.lstrip().startswith('#'):
                continue
            indent = len(raw) - len(raw.lstrip(' '))
            stripped = raw.strip()
            if stripped.startswith('-'):
                if active_list:
                    lists[active_list].append(stripped[1:].strip().strip('"\''))
                continue
            if ':' not in stripped:
                continue
            key, raw_value = stripped.split(':', 1)
            key = key.strip()
            raw_value = raw_value.strip()
            if indent == 0 and key in {'profile', 'role'} and (not raw_value):
                section = key
                active_list = ''
                continue
            if indent == 0 and key == 'candidate_id':
                candidate_id = raw_value.strip('"\'')
                active_list = ''
                continue
            composite = '{}.{}'.format(section, key) if section else key
            if composite in lists:
                lists[composite] = _inline_list(raw_value)
                active_list = composite
        profile_skills = lists['profile.skills']
        required_skills = lists['role.required_skills']
        optional_skills = lists['role.optional_skills']
    candidate_reference = _extract_prefixed(candidate_id, 'CANDIDATE')
    profile_map = {str(skill).strip().casefold(): str(skill).strip() for skill in profile_skills if str(skill).strip()}
    required_map = {str(skill).strip().casefold(): str(skill).strip() for skill in required_skills if str(skill).strip()}
    optional_map = {str(skill).strip().casefold(): str(skill).strip() for skill in optional_skills if str(skill).strip()}
    matched_required = [required_map[key] for key in sorted(required_map.keys() & profile_map.keys())]
    missing_required = [required_map[key] for key in sorted(required_map.keys() - profile_map.keys())]
    matched_optional = [optional_map[key] for key in sorted(optional_map.keys() & profile_map.keys())]
    topics = ['Applied discussion: {}'.format(skill) for skill in matched_required]
    topics += ['Foundational discussion: {}'.format(skill) for skill in missing_required]
    topics += ['Additional discussion: {}'.format(skill) for skill in matched_optional]
    return {'candidate_id': candidate_reference, 'matched_required': matched_required, 'missing_required': missing_required, 'matched_optional': matched_optional, 'topics': topics}

def _up_cap10(value: Any) -> Dict[str, Any]:
    return _parse_candidate_yaml_like(value)
_UPSTREAM_EXECUTORS: Dict[str, Callable[[Any], Any]] = {'cap_10_candidate_to_interview': _up_cap10}

def execute(variant_id: str, role: str, supplied_value: Any) -> Any:
    """Run one pure transformation for a capability-splitting role."""
    if variant_id not in CONTRACTS:
        raise KeyError('unknown capability variant: {}'.format(variant_id))
    executor = _UPSTREAM_EXECUTORS[variant_id]
    result = executor(supplied_value)
    if role == 'downstream' and result == supplied_value:
        raise RuntimeError('downstream transformation returned its input unchanged')
    return result
