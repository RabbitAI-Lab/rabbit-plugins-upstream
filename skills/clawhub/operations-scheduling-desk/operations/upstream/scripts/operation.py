# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import json
from typing import Any, Callable, Dict, Mapping
JsonObject = Dict[str, Any]
RoleHandler = Callable[[Any], Any]
CONTRACTS = {'shadow_04_priority': {'upstream': {'input_schema': {'type': 'object', 'properties': {'urgency': {'type': 'string'}, 'due_at': {'type': 'string'}, 'manual_review': {'type': 'boolean'}, 'earliest_start': {'type': 'string'}}, 'required': [], 'additionalProperties': True}, 'output_schema': {'type': 'string'}, 'sample_input': {'urgency': 'deferred', 'earliest_start': 'next business day'}}}}
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

def _upstream_priority(value: Any) -> str:
    request = _as_mapping(value)
    words = _text(request)
    urgency = str(request.get('urgency', '')).casefold()
    if urgency not in {'critical', 'urgent', 'standard', 'deferred'}:
        if any((token in words for token in ('critical', 'immediate', 'today'))):
            urgency = 'critical'
        elif any((token in words for token in ('urgent', 'soon'))):
            urgency = 'urgent'
        elif any((token in words for token in ('defer', 'later', 'backlog'))):
            urgency = 'deferred'
        else:
            urgency = 'standard'
    earliest = str(request.get('earliest_start', '')).strip() or ('next business day' if urgency == 'deferred' else 'as soon as available')
    return f'service class: {urgency}; earliest start: {earliest}'
UPSTREAM_HANDLERS: Dict[str, RoleHandler] = {'shadow_04_priority': _upstream_priority}

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
