# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import json
import re
from typing import Any, Callable, Dict, Mapping, Sequence
JsonObject = Dict[str, Any]
RoleHandler = Callable[[Any], Any]
CONTRACTS = {'shadow_02_tool_choice': {'upstream': {'input_schema': {'type': 'object', 'properties': {'artifact_class': {'type': 'string'}, 'restricted': {'type': 'boolean'}, 'available_routes': {'type': 'array', 'items': {'type': 'string'}}}, 'required': [], 'additionalProperties': True}, 'output_schema': {'type': 'string'}, 'sample_input': {'restricted': True}}}}
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

def _as_string_list(value: Any) -> list[str]:
    if isinstance(value, str):
        return [item.strip() for item in re.split('[,;|]', value) if item.strip()]
    if isinstance(value, Sequence) and (not isinstance(value, (bytes, bytearray, str))):
        return [str(item) for item in value]
    return []

def _upstream_route(value: Any) -> str:
    request = _as_mapping(value)
    words = _text(request)
    restricted = _as_bool(request.get('restricted'), 'restricted' in words or 'review' in words)
    available = _as_string_list(request.get('available_routes'))
    preferred = ['review-first', 'standard', 'archive'] if restricted else ['standard', 'review-first', 'archive']
    if 'archive' in words:
        preferred = ['archive', *[item for item in preferred if item != 'archive']]
    if available:
        preferred = [item for item in preferred if item in available] + [item for item in available if item not in preferred]
    if restricted and preferred[:2] == ['review-first', 'standard']:
        return 'quarantine export route'
    return f"delivery route order: {','.join(preferred)}; review required: {('yes' if restricted else 'no')}"
UPSTREAM_HANDLERS: Dict[str, RoleHandler] = {'shadow_02_tool_choice': _upstream_route}

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
