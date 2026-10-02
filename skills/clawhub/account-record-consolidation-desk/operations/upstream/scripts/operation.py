# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import json
from typing import Any, Callable, Dict, Mapping
JsonObject = Dict[str, Any]
RoleHandler = Callable[[Any], Any]
CONTRACTS = {'shadow_10_update_mode': {'upstream': {'input_schema': {'type': 'object', 'properties': {'strategy': {'type': 'string'}, 'preserve_absent': {'type': 'boolean'}, 'accept_blank': {'type': 'boolean'}}, 'required': [], 'additionalProperties': True}, 'output_schema': {'type': 'string'}, 'sample_input': {'strategy': 'merge-nonempty', 'preserve_absent': True, 'accept_blank': False}}}}
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

def _upstream_update(value: Any) -> str:
    request = _as_mapping(value)
    strategy = str(request.get('strategy', 'merge-nonempty')).casefold()
    if strategy not in {'merge-nonempty', 'replace', 'keep-current'}:
        strategy = 'merge-nonempty'
    preserve = _as_bool(request.get('preserve_absent'), strategy != 'replace')
    accept_blank = _as_bool(request.get('accept_blank'), False)
    if strategy == 'merge-nonempty' and preserve and (not accept_blank):
        return 'merge non-empty incoming fields and preserve absent fields'
    return f"account update strategy: {strategy}; preserve absent: {('yes' if preserve else 'no')}; accept blank: {('yes' if accept_blank else 'no')}"
UPSTREAM_HANDLERS: Dict[str, RoleHandler] = {'shadow_10_update_mode': _upstream_update}

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
