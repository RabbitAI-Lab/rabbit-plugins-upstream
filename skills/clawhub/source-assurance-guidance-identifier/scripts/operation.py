# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import json
from typing import Any, Callable, Dict, Mapping
JsonObject = Dict[str, Any]
RoleHandler = Callable[[Any], Any]
CONTRACTS = {'shadow_11_provenance': {'upstream': {'input_schema': {'type': 'object', 'properties': {'source_count': {'type': 'integer'}, 'critical_field': {'type': 'boolean'}, 'conflict_action': {'type': 'string'}}, 'required': [], 'additionalProperties': True}, 'output_schema': {'type': 'string'}, 'sample_input': {'source_count': 3, 'critical_field': False, 'conflict_action': 'hold'}}}}
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

def _upstream_provenance(value: Any) -> str:
    request = _as_mapping(value)
    source_count = _as_int(request.get('source_count'), 2, minimum=1, maximum=20)
    critical = _as_bool(request.get('critical_field'), False)
    required = min(source_count, 3 if critical and source_count >= 3 else 2 if source_count >= 2 else 1)
    action = str(request.get('conflict_action', 'hold')).casefold()
    if action not in {'hold', 'prefer-majority'}:
        action = 'hold'
    if required == 2 and action == 'hold':
        return 'accept a field only when two sources agree'
    return f'accept a field when {required} sources agree; on conflict: {action}'
UPSTREAM_HANDLERS: Dict[str, RoleHandler] = {'shadow_11_provenance': _upstream_provenance}

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
