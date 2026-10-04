# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import json
from decimal import ROUND_DOWN, ROUND_HALF_EVEN, ROUND_HALF_UP, ROUND_UP
from typing import Any, Callable, Dict, Mapping
JsonObject = Dict[str, Any]
RoleHandler = Callable[[Any], Any]
CONTRACTS = {'shadow_08_rounding': {'upstream': {'input_schema': {'type': 'object', 'properties': {'currency': {'type': 'string'}, 'scale': {'type': 'integer'}, 'rounding_mode': {'type': 'string'}, 'round_stage': {'type': 'string'}}, 'required': [], 'additionalProperties': True}, 'output_schema': {'type': 'string'}, 'sample_input': {'currency': 'USD', 'scale': 2, 'rounding_mode': 'half-even', 'round_stage': 'line'}}}}
RENAMED_IDS = {'shadow_08_retention': 'shadow_08_rounding'}

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
ROUNDING_MODES = {'half-even': ROUND_HALF_EVEN, 'half-up': ROUND_HALF_UP, 'up': ROUND_UP, 'down': ROUND_DOWN}

def _upstream_rounding(value: Any) -> str:
    request = _as_mapping(value)
    currency = str(request.get('currency', 'USD')).upper()
    currency_scale = {'JPY': 0, 'KWD': 3}.get(currency, 2)
    scale = _as_int(request.get('scale'), currency_scale, minimum=0, maximum=6)
    mode = str(request.get('rounding_mode', 'half-even')).casefold()
    if mode not in ROUNDING_MODES:
        mode = 'half-even'
    stage = str(request.get('round_stage', 'line')).casefold()
    if stage not in {'line', 'total'}:
        stage = 'line'
    stage_text = 'each line' if stage == 'line' else 'the total'
    decimals = 'decimal' if scale == 1 else 'decimals'
    scale_text = {0: 'zero', 1: 'one', 2: 'two', 3: 'three'}.get(scale, str(scale))
    return f'round {stage_text} to {scale_text} {decimals} using {mode}'
UPSTREAM_HANDLERS: Dict[str, RoleHandler] = {'shadow_08_rounding': _upstream_rounding}

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
