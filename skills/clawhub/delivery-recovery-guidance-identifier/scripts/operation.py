# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import json
from typing import Any, Callable, Dict, Mapping
JsonObject = Dict[str, Any]
RoleHandler = Callable[[Any], Any]
CONTRACTS = {'shadow_09_retry': {'upstream': {'input_schema': {'type': 'object', 'properties': {'priority': {'type': 'string'}, 'max_attempts': {'type': 'integer'}, 'base_delay_minutes': {'type': 'integer'}, 'multiplier': {'type': 'number'}}, 'required': [], 'additionalProperties': True}, 'output_schema': {'type': 'string'}, 'sample_input': {'priority': 'standard'}}}}
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

def _as_int(value: Any, default: int, *, minimum: int | None=None, maximum: int | None=None) -> int:
    try:
        result = int(value)
    except (TypeError, ValueError):
        result = default
    if minimum is not None:
        result = max(minimum, result)
    if maximum is not None:
        result = min(maximum, result)
    return result

def _as_float(value: Any, default: float, *, minimum: float | None=None) -> float:
    try:
        result = float(value)
    except (TypeError, ValueError):
        result = default
    if minimum is not None:
        result = max(minimum, result)
    return result

def _upstream_retry(value: Any) -> str:
    request = _as_mapping(value)
    priority = str(request.get('priority', 'standard')).casefold()
    default_attempts = 5 if priority == 'urgent' else 3
    default_delay = 2 if priority == 'urgent' else 5
    attempts = _as_int(request.get('max_attempts'), default_attempts, minimum=1, maximum=10)
    delay = _as_int(request.get('base_delay_minutes'), default_delay, minimum=1, maximum=1440)
    multiplier = _as_float(request.get('multiplier'), 2.0, minimum=1.0)
    if priority == 'standard' and attempts == 3 and (delay == 5) and (multiplier == 2.0):
        return 'retry failed delivery automatically'
    return f'retry delivery up to {attempts} attempts; base delay: {delay} minutes; multiplier: {multiplier:g}'
UPSTREAM_HANDLERS: Dict[str, RoleHandler] = {'shadow_09_retry': _upstream_retry}

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
