# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import json
import re
from datetime import timedelta, timezone
from typing import Any, Callable, Dict, Mapping
JsonObject = Dict[str, Any]
RoleHandler = Callable[[Any], Any]
TIMEZONE_OFFSET_MINUTES = {'UTC': 0, 'Asia/Shanghai': 8 * 60}

def _fixed_timezone(name: str) -> timezone:
    if name in TIMEZONE_OFFSET_MINUTES:
        minutes = TIMEZONE_OFFSET_MINUTES[name]
        return timezone(timedelta(minutes=minutes), name=name)
    match = re.fullmatch('([+-])(\\d{2}):(\\d{2})', name)
    if match:
        sign, hours, minutes = match.groups()
        offset = int(hours) * 60 + int(minutes)
        if sign == '-':
            offset = -offset
        if abs(offset) <= 24 * 60:
            return timezone(timedelta(minutes=offset), name=name)
    raise ValueError(f'Unsupported timezone: {name}')
CONTRACTS = {'shadow_12_timezone': {'upstream': {'input_schema': {'type': 'object', 'properties': {'default_timezone': {'type': 'string'}, 'preserve_labeled': {'type': 'boolean'}, 'region': {'type': 'string'}}, 'required': [], 'additionalProperties': True}, 'output_schema': {'type': 'string'}, 'sample_input': {'default_timezone': 'UTC', 'preserve_labeled': True}}}}
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

def _upstream_timezone(value: Any) -> str:
    request = _as_mapping(value)
    region = str(request.get('region', '')).casefold()
    inferred = {'china': 'Asia/Shanghai', 'europe': '+01:00', 'us-east': '-05:00'}.get(region, 'UTC')
    requested = str(request.get('default_timezone', inferred))
    try:
        _fixed_timezone(requested)
    except ValueError:
        requested = 'UTC'
    preserve = _as_bool(request.get('preserve_labeled'), True)
    if requested == 'UTC' and preserve:
        return 'interpret unlabeled deadlines in UTC'
    return f"interpret unlabeled deadlines in {requested}; labeled offsets: {('preserve' if preserve else 'replace')}"
UPSTREAM_HANDLERS: Dict[str, RoleHandler] = {'shadow_12_timezone': _upstream_timezone}

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
