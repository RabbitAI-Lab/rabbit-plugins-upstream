# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import json
import re
from typing import Any, Callable, Dict, Mapping, Sequence
JsonObject = Dict[str, Any]
RoleHandler = Callable[[Any], Any]
CONTRACTS = {'shadow_03_sensitivity': {'upstream': {'input_schema': {'type': 'object', 'properties': {'fields': {'type': 'array', 'items': {'type': 'string'}}, 'contains_personal_fields': {'type': 'boolean'}, 'requested_tier': {'type': 'string'}}, 'required': [], 'additionalProperties': True}, 'output_schema': {'type': 'string'}, 'sample_input': {'fields': ['display_name', 'email'], 'contains_personal_fields': True, 'requested_tier': 'restricted'}}}}
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

def _upstream_sensitivity(value: Any) -> str:
    request = _as_mapping(value)
    fields = _as_string_list(request.get('fields'))
    words = _text(request)
    personal = _as_bool(request.get('contains_personal_fields'), any((key in words for key in ('email', 'phone', 'account'))))
    tier = str(request.get('requested_tier', '')).casefold()
    if tier not in {'public', 'internal', 'restricted'}:
        tier = 'restricted' if personal else 'internal'
    sensitive_tokens = ('email', 'phone', 'account', 'address', 'owner')
    mask_fields = [field for field in fields if any((token in field.casefold() for token in sensitive_tokens))]
    if personal and (not mask_fields):
        mask_fields = ['email', 'account_id']
    if tier == 'restricted' and (not mask_fields or set(mask_fields) <= {'email', 'account_id'}):
        return 'handling tier: restricted'
    suffix = f"; mask fields: {','.join(mask_fields)}" if mask_fields else ''
    return f'handling tier: {tier}{suffix}'
UPSTREAM_HANDLERS: Dict[str, RoleHandler] = {'shadow_03_sensitivity': _upstream_sensitivity}

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
