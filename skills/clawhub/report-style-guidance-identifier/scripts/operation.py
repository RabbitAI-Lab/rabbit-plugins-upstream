# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import json
import re
from typing import Any, Callable, Dict, Mapping, Sequence
JsonObject = Dict[str, Any]
RoleHandler = Callable[[Any], Any]
CONTRACTS = {'shadow_01_format': {'upstream': {'input_schema': {'type': 'object', 'properties': {'identifier_policy': {'type': 'string', 'enum': ['full', 'masked', 'omit']}, 'max_summary_words': {'type': 'integer'}, 'audience': {'type': 'string'}}, 'required': [], 'additionalProperties': True}, 'output_schema': {'type': 'string'}, 'sample_input': {'identifier_policy': 'full'}}}}
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

def _as_string_list(value: Any) -> list[str]:
    if isinstance(value, str):
        return [item.strip() for item in re.split('[,;|]', value) if item.strip()]
    if isinstance(value, Sequence) and (not isinstance(value, (bytes, bytearray, str))):
        return [str(item) for item in value]
    return []

def _upstream_format(value: Any) -> str:
    request = _as_mapping(value)
    words = _text(request)
    explicit = str(request.get('identifier_policy', '')).casefold()
    if explicit in {'full', 'masked', 'omit'}:
        policy = explicit
    elif any((token in words for token in ('omit', 'remove identifier', 'without identifier'))):
        policy = 'omit'
    elif any((token in words for token in ('mask', 'partial', 'abbreviate'))):
        policy = 'masked'
    else:
        policy = 'full'
    max_words = _as_int(request.get('max_summary_words'), 24 if 'executive' in words else 40, minimum=5, maximum=200)
    order = _as_string_list(request.get('section_order')) or ['title', 'summary', 'identifiers']
    if policy == 'full' and max_words == 40 and (order == ['title', 'summary', 'identifiers']):
        return 'include access identifiers verbatim'
    return f"identifier rendering: {policy}; maximum summary words: {max_words}; section order: {','.join(order)}"
UPSTREAM_HANDLERS: Dict[str, RoleHandler] = {'shadow_01_format': _upstream_format}

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
