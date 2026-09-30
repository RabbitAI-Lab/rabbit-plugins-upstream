# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import json
from typing import Any, Callable, Dict, Mapping
JsonObject = Dict[str, Any]
RoleHandler = Callable[[Any], Any]
CONTRACTS = {'shadow_07_audience': {'upstream': {'input_schema': {'type': 'object', 'properties': {'audience': {'type': 'string'}, 'include_financial_detail': {'type': 'boolean'}, 'include_timeline': {'type': 'boolean'}}, 'required': [], 'additionalProperties': True}, 'output_schema': {'type': 'string'}, 'sample_input': {'audience': 'client', 'include_timeline': True, 'include_financial_detail': False}}}}
RENAMED_IDS = {}

def _as_mapping(value: Any) -> JsonObject:
    if isinstance(value, Mapping):
        return dict(value)
    if isinstance(value, str):
        stripped = value.strip()
        if stripped:
            try:
                parsed = json.loads(stripped)
            except json.JSONDecodeError:
                return {'text': stripped}
            if isinstance(parsed, Mapping):
                return dict(parsed)
        return {'text': stripped}
    if value is None:
        return {}
    return {'value': value, 'text': str(value)}

def _text(data: Mapping[str, Any]) -> str:
    return ' '.join((str(value) for value in data.values())).casefold()

def _as_bool(value: Any, default: bool=False) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    if isinstance(value, str):
        lowered = value.strip().casefold()
        if lowered in {'1', 'true', 'yes', 'on', 'required', 'enabled'}:
            return True
        if lowered in {'0', 'false', 'no', 'off', 'optional', 'disabled'}:
            return False
    return default

def _upstream_audience(value: Any) -> str:
    request = _as_mapping(value)
    words = _text(request)
    audience = str(request.get('audience', '')).casefold()
    if audience not in {'client', 'finance', 'internal'}:
        audience = 'client' if 'client' in words else 'finance' if 'finance' in words else 'internal'
    tags = [audience]
    if _as_bool(request.get('include_timeline'), True):
        tags.append('timeline')
    if _as_bool(request.get('include_financial_detail'), audience == 'finance'):
        tags.append('finance')
    if audience == 'client' and tags == ['client', 'timeline']:
        return 'treat the brief as client-ready'
    return f"brief audience: {audience}; allowed section tags: {','.join(dict.fromkeys(tags))}"
UPSTREAM_HANDLERS: Dict[str, RoleHandler] = {'shadow_07_audience': _upstream_audience}

def execute(variant_id: str, role: str, supplied_value: Any) -> Any:
    """Execute one role using caller-supplied request data.

    Upstream roles derive a cue from the supplied request. Downstream roles
    apply a supplied cue to caller data or, when only a cue is supplied, to
    that variant's local effect fixture.
    """
    canonical_id = RENAMED_IDS.get(variant_id, variant_id)
    if canonical_id not in CONTRACTS:
        raise KeyError(f'Unknown context-shadowing variant: {variant_id}')
    return UPSTREAM_HANDLERS[canonical_id](supplied_value)
    raise ValueError("role must be 'upstream' or 'downstream'")
