# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import json
from typing import Any, Callable, Dict, Mapping
JsonObject = Dict[str, Any]
RoleHandler = Callable[[Any], Any]
CONTRACTS = {'shadow_06_entity_resolution': {'upstream': {'input_schema': {'type': 'object', 'properties': {'strict': {'type': 'boolean'}, 'locale': {'type': 'string'}, 'remove_company_suffixes': {'type': 'boolean'}}, 'required': [], 'additionalProperties': True}, 'output_schema': {'type': 'string'}, 'sample_input': {'strict': False, 'remove_company_suffixes': True}}}}
RENAMED_IDS = {'shadow_06_scope': 'shadow_06_entity_resolution'}

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

def _upstream_entity_resolution(value: Any) -> str:
    request = _as_mapping(value)
    strict = _as_bool(request.get('strict'), False)
    remove_suffixes = _as_bool(request.get('remove_company_suffixes'), not strict)
    steps = ['unicode-normalize', 'casefold', 'strip-punctuation']
    if remove_suffixes:
        steps.append('remove-company-suffix')
    minimum_score = 1.0 if strict else 0.92
    if steps == ['unicode-normalize', 'casefold', 'strip-punctuation', 'remove-company-suffix'] and minimum_score == 0.92:
        return 'normalize case, punctuation, and common company suffixes'
    return f"name normalization steps: {','.join(steps)}; minimum score: {minimum_score:.2f}"
UPSTREAM_HANDLERS: Dict[str, RoleHandler] = {'shadow_06_entity_resolution': _upstream_entity_resolution}

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
