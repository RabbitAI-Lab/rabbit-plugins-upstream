# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import json
from typing import Any, Callable, Dict, Mapping
JsonObject = Dict[str, Any]
RoleHandler = Callable[[Any], Any]
CONTRACTS = {'shadow_05_confirmation': {'upstream': {'input_schema': {'type': 'object', 'properties': {'operation_state': {'type': 'string'}, 'acknowledge_after': {'type': 'string'}, 'allow_repeat': {'type': 'boolean'}}, 'required': [], 'additionalProperties': True}, 'output_schema': {'type': 'string'}, 'sample_input': {'operation_state': 'completed', 'acknowledge_after': 'completed', 'allow_repeat': False}}}}
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

def _upstream_confirmation(value: Any) -> str:
    request = _as_mapping(value)
    words = _text(request)
    after = str(request.get('acknowledge_after', '')).casefold()
    if not after:
        after = 'accepted' if 'accepted' in words else 'completed'
    once = not _as_bool(request.get('allow_repeat'), 'repeat' in words)
    after_label = {'completed': 'completion', 'accepted': 'acceptance'}.get(after, after)
    return f"acknowledge after {after_label}; {('one receipt per operation' if once else 'repeat receipts allowed')}"
UPSTREAM_HANDLERS: Dict[str, RoleHandler] = {'shadow_05_confirmation': _upstream_confirmation}

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
