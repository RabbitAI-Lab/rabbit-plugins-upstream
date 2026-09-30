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
CONTRACTS = {'shadow_15_notification': {'upstream': {'input_schema': {'type': 'object', 'properties': {'cadence': {'type': 'string'}, 'hour': {'type': 'integer'}, 'timezone': {'type': 'string'}, 'deduplicate_by': {'type': 'string'}}, 'required': [], 'additionalProperties': True}, 'output_schema': {'type': 'string'}, 'sample_input': {'cadence': 'daily', 'hour': 17, 'timezone': 'UTC', 'deduplicate_by': 'case_id', 'group_by': 'team'}}}}
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

def _upstream_notification(value: Any) -> str:
    request = _as_mapping(value)
    cadence = str(request.get('cadence', 'daily')).casefold()
    if cadence not in {'daily', 'twice-daily', 'weekly'}:
        cadence = 'daily'
    timezone_name = str(request.get('timezone', 'UTC'))
    try:
        _fixed_timezone(timezone_name)
    except ValueError:
        timezone_name = 'UTC'
    hour = _as_int(request.get('hour'), 17, minimum=0, maximum=23)
    deduplicate_by = str(request.get('deduplicate_by', 'case_id'))
    group_by = str(request.get('group_by', 'team'))
    if cadence == 'daily' and hour == 17 and (timezone_name == 'UTC') and (deduplicate_by == 'case_id') and (group_by == 'team'):
        return 'send a single end-of-day digest'
    return f'digest cadence: {cadence}; hour: {hour}; timezone: {timezone_name}; deduplicate by: {deduplicate_by}; group by: {group_by}'
UPSTREAM_HANDLERS: Dict[str, RoleHandler] = {'shadow_15_notification': _upstream_notification}

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
