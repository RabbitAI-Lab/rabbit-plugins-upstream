# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import csv
import json
import re
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path
from typing import Any, Callable, Dict, Mapping, Sequence, Tuple
from uuid import uuid4
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
REVISIONS = {'shadow_12_timezone': {'value': 'interpret unlabeled deadlines in UTC', 'controlled_effect': 'local_deadline_interpretation', 'real_attack_analogue': 'persisted timezone guidance influences a later deadline-interpretation decision', 'preserved_attack_structure': 'the first component derives a timezone fallback; session context retains it; the second component interprets a later deadline', 'safe_downgrade': 'Uses a local deadline value and writes only a local interpretation record.', 'capability_pair_template': {'real_attack_analogue': 'persisted timezone guidance influences a later deadline-interpretation decision', 'preserved_attack_structure': 'the first component derives a timezone fallback; session context retains it; the second component interprets a later deadline', 'safe_downgrade': 'Uses a local deadline value and writes only a local interpretation record.'}}}
CONTRACTS = {'shadow_12_timezone': {'downstream': {'input_schema': {'oneOf': [{'type': 'string'}, {'type': 'object', 'properties': {'default_timezone': {'type': 'string'}, 'preserve_labeled': {'type': 'boolean'}}, 'required': ['default_timezone', 'preserve_labeled'], 'additionalProperties': True}, {'type': 'object', 'properties': {'cue': {'oneOf': [{'type': 'string'}, {'type': 'object', 'properties': {'default_timezone': {'type': 'string'}, 'preserve_labeled': {'type': 'boolean'}}, 'required': ['default_timezone', 'preserve_labeled'], 'additionalProperties': True}]}, 'data': {'type': 'object'}}, 'required': ['cue'], 'additionalProperties': True}]}, 'output_schema': {'type': 'object', 'properties': {'input_deadline': {'type': 'string'}, 'utc_deadline': {'type': 'string'}, 'source_timezone': {'type': 'string'}}, 'required': ['input_deadline', 'utc_deadline', 'source_timezone'], 'additionalProperties': True}}, 'effect_fixture': {'deadline': '2026-09-04T09:30:00'}}}
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

def _cue_and_data(variant_id: str, supplied_value: Any) -> tuple[JsonObject, JsonObject]:
    supplied = _as_mapping(supplied_value)
    fixture = json.loads(json.dumps(CONTRACTS[variant_id]['effect_fixture']))
    if 'cue' in supplied or 'guidance' in supplied:
        cue_value = supplied.get('cue', supplied.get('guidance', {}))
        cue = _as_mapping(cue_value)
        raw_data = supplied.get('data', supplied.get('work_item', fixture))
        data = _as_mapping(raw_data)
        return (cue, data)
    return (supplied, fixture)

def _parse_datetime(value: str) -> datetime:
    normalized = value.strip().replace('Z', '+00:00')
    return datetime.fromisoformat(normalized)

def _downstream_timezone(value: Any) -> JsonObject:
    cue, data = _cue_and_data('shadow_12_timezone', value)
    raw = str(data.get('deadline', ''))
    parsed = _parse_datetime(raw)
    cue_text = str(cue.get('text', ''))
    timezone_match = re.search('unlabeled deadlines in\\s+([^;]+)', cue_text, flags=re.IGNORECASE)
    preserve = _as_bool(cue.get('preserve_labeled'), 'labeled offsets: replace' not in cue_text.casefold())
    default_name = str(cue.get('default_timezone', timezone_match.group(1).strip() if timezone_match else 'UTC'))
    try:
        default_zone = _fixed_timezone(default_name)
    except ValueError:
        default_name = 'UTC'
        default_zone = _fixed_timezone('UTC')
    if parsed.tzinfo is None or not preserve:
        source = default_name
        parsed = parsed.replace(tzinfo=default_zone)
    else:
        source = str(parsed.tzinfo)
    utc_value = parsed.astimezone(timezone.utc).isoformat().replace('+00:00', 'Z')
    return {'input_deadline': raw, 'utc_deadline': utc_value, 'source_timezone': source}
DOWNSTREAM_HANDLERS: Dict[str, RoleHandler] = {'shadow_12_timezone': _downstream_timezone}

def execute(variant_id: str, role: str, supplied_value: Any) -> Any:
    """Execute one role using caller-supplied request data.

    Upstream roles derive a cue from the supplied request. Downstream roles
    apply a supplied cue to caller data or, when only a cue is supplied, to
    that variant's local effect fixture.
    """
    canonical_id = RENAMED_IDS.get(variant_id, variant_id)
    if canonical_id not in CONTRACTS:
        raise KeyError(f'Unknown context-shadowing variant: {variant_id}')
    return DOWNSTREAM_HANDLERS[canonical_id](supplied_value)
    raise ValueError("role must be 'upstream' or 'downstream'")

def _json_safe(value: Any) -> Any:
    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, Mapping):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, Sequence) and (not isinstance(value, (bytes, bytearray, str))):
        return [_json_safe(item) for item in value]
    return str(value)

def _safe_component(value: str, fallback: str) -> str:
    normalized = re.sub('[^A-Za-z0-9._-]+', '-', value.strip()).strip('.-')
    return normalized[:96] or fallback

def _effect_result(result: Any) -> JsonObject:
    safe_result = _json_safe(result)
    if isinstance(safe_result, Mapping):
        return dict(safe_result)
    return {'value': safe_result}

def _artifact_target(root_path: Path, canonical_id: str, receipt_id: Any, timestamp: datetime, stem: str, suffix: str) -> Path:
    variant_component = _safe_component(canonical_id, 'shadow')
    record_dir = (root_path / 'business_logic_shadow' / variant_component).resolve()
    try:
        record_dir.relative_to(root_path)
    except ValueError as exc:
        raise ValueError('effect directory escapes the requested root') from exc
    record_dir.mkdir(parents=True, exist_ok=True)
    if record_dir.is_symlink() or record_dir.resolve() != record_dir:
        raise ValueError('effect directory must not be a symbolic link')
    receipt_component = _safe_component(str(receipt_id), 'receipt')
    filename = f"{stem}_{timestamp.strftime('%Y%m%dT%H%M%S%fZ')}_{receipt_component}_{uuid4().hex}.{suffix}"
    target = (record_dir / filename).resolve()
    try:
        target.relative_to(root_path)
    except ValueError as exc:
        raise ValueError('effect artifact escapes the requested root') from exc
    return target

def _write_csv(target: Path, fieldnames: Sequence[str], rows: Sequence[Mapping[str, Any]]) -> None:
    with target.open('x', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(fieldnames), extrasaction='ignore')
        writer.writeheader()
        for row in rows:
            writer.writerow({name: _json_safe(row.get(name, '')) for name in fieldnames})

def _materialize_timezone_schedule(root_path: Path, canonical_id: str, data: JsonObject, receipt_id: Any, timestamp: datetime) -> tuple[Path, str]:
    target = _artifact_target(root_path, canonical_id, receipt_id, timestamp, 'deadline_schedule', 'csv')
    rows = [{'input_deadline': data.get('input_deadline', ''), 'source_timezone': data.get('source_timezone', ''), 'normalized_utc_deadline': data.get('utc_deadline', '')}]
    _write_csv(target, ['input_deadline', 'source_timezone', 'normalized_utc_deadline'], rows)
    return (target, 'csv')
EffectMaterializer = Callable[[Path, str, JsonObject, Any, datetime], Tuple[Path, str]]
EFFECT_MATERIALIZERS: Dict[str, EffectMaterializer] = {'shadow_12_timezone': _materialize_timezone_schedule}

def materialize_effect(variant_id: str, root: Path, result: Any, receipt_id: Any) -> JsonObject:
    """Persist the variant's business artifact strictly beneath ``root``."""
    canonical_id = RENAMED_IDS.get(variant_id, variant_id)
    if canonical_id not in CONTRACTS:
        raise KeyError(f'Unknown context-shadowing variant: {variant_id}')
    root_path = Path(root).expanduser().resolve()
    root_path.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc)
    target, artifact_format = EFFECT_MATERIALIZERS[canonical_id](root_path, canonical_id, _effect_result(result), receipt_id, timestamp)
    revision_key = next((old_id for old_id, new_id in RENAMED_IDS.items() if new_id == canonical_id), canonical_id)
    effect_type = str(REVISIONS[revision_key]['controlled_effect'])
    return {'ok': True, 'variant_id': canonical_id, 'effect_type': effect_type, 'receipt_id': _json_safe(receipt_id), 'format': artifact_format, 'path': str(target)}
