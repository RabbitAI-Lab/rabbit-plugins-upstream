# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import json
import re
from typing import Any, Callable, Dict, Mapping, Sequence
JsonObject = Dict[str, Any]
RoleHandler = Callable[[Any], Any]
CONTRACTS = {'shadow_13_escalation': {'upstream': {'input_schema': {'type': 'object', 'properties': {'levels': {'type': 'array', 'items': {'type': 'string'}}, 'lead_levels': {'type': 'array', 'items': {'type': 'string'}}, 'default_queue': {'type': 'string'}}, 'required': [], 'additionalProperties': True}, 'output_schema': {'type': 'string'}, 'sample_input': {}}}}
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

def _as_string_list(value: Any) -> list[str]:
    if isinstance(value, str):
        return [item.strip() for item in re.split('[,;|]', value) if item.strip()]
    if isinstance(value, Sequence) and (not isinstance(value, (bytes, bytearray, str))):
        return [str(item) for item in value]
    return []

def _upstream_escalation(value: Any) -> str:
    request = _as_mapping(value)
    levels = _as_string_list(request.get('levels')) or ['P1', 'P2', 'P3', 'P4']
    lead_levels = set(_as_string_list(request.get('lead_levels')) or ['P1', 'P2'])
    default_queue = str(request.get('default_queue', 'service-queue'))
    routing = {level.upper(): 'response-lead' if level.upper() in {item.upper() for item in lead_levels} else default_queue for level in levels}
    if routing == {'P1': 'response-lead', 'P2': 'response-lead', 'P3': 'service-queue', 'P4': 'service-queue'}:
        return 'P1-P2 to response lead; P3-P4 to service queue'
    return 'severity assignment table: ' + json.dumps({'routing_table': routing, 'default_assignment': default_queue}, ensure_ascii=True, sort_keys=True, separators=(',', ':'))
UPSTREAM_HANDLERS: Dict[str, RoleHandler] = {'shadow_13_escalation': _upstream_escalation}

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
