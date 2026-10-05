# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List, Optional, Tuple
CONTRACTS = {'cap_07_event_to_coordination': {'upstream': {'input_schema': {'type': 'string', 'format': 'rfc5545-event', 'minLength': 1}, 'output_schema': {'type': 'object', 'required': ['event_id', 'starts_at', 'ends_at', 'timezone', 'duration_minutes'], 'properties': {'event_id': {'type': 'string', 'minLength': 1}, 'starts_at': {'type': 'string', 'minLength': 1}, 'ends_at': {'type': 'string', 'minLength': 1}, 'timezone': {'type': 'string', 'minLength': 1}, 'duration_minutes': {'type': 'integer'}}, 'additionalProperties': True}, 'sample_input': 'BEGIN:VCALENDAR\nBEGIN:VEVENT\nUID:EVENT-GOLF-7315\nDTSTART:20260904T013000Z\nDTEND:20260904T020000Z\nLOCATION:Room 8\nEND:VEVENT\nEND:VCALENDAR\n'}}}

def _require_text(value: Any, label: str='value') -> str:
    if isinstance(value, bytes):
        text = value.decode('utf-8')
    elif isinstance(value, str):
        text = value
    else:
        raise TypeError('{} must be text'.format(label))
    if not text.strip():
        raise ValueError('{} must not be empty'.format(label))
    return text

def _extract_prefixed(text: str, prefix: str) -> str:
    pattern = '(?<![A-Z0-9])(' + re.escape(prefix) + '-[A-Z0-9]+(?:-[A-Z0-9]+)+)(?![A-Z0-9])'
    match = re.search(pattern, text.upper())
    if not match:
        raise ValueError('no {} reference found'.format(prefix))
    return match.group(1)

def _unfold_ics(text: str) -> List[str]:
    lines: List[str] = []
    for raw in text.replace('\r\n', '\n').split('\n'):
        if raw.startswith((' ', '\t')) and lines:
            lines[-1] += raw[1:]
        else:
            lines.append(raw.rstrip('\r'))
    return lines

def _parse_ics_datetime(raw: str) -> Tuple[str, Optional[datetime]]:
    value = raw.strip()
    if re.fullmatch('\\d{8}', value):
        parsed = datetime.strptime(value, '%Y%m%d')
        return (parsed.date().isoformat(), parsed)
    if re.fullmatch('\\d{8}T\\d{6}Z', value):
        parsed = datetime.strptime(value, '%Y%m%dT%H%M%SZ').replace(tzinfo=timezone.utc)
        return (parsed.isoformat().replace('+00:00', 'Z'), parsed)
    if re.fullmatch('\\d{8}T\\d{6}', value):
        parsed = datetime.strptime(value, '%Y%m%dT%H%M%S')
        return (parsed.isoformat(), parsed)
    raise ValueError('unsupported calendar datetime: {}'.format(raw))

def _parse_ics_event(value: Any) -> Dict[str, Any]:
    text = _require_text(value, 'calendar event')
    lines = _unfold_ics(text)
    if 'BEGIN:VEVENT' not in lines or 'END:VEVENT' not in lines:
        raise ValueError('calendar input must contain one VEVENT')
    props: Dict[str, str] = {}
    timezone_name = ''
    for line in lines:
        if ':' not in line:
            continue
        left, raw_value = line.split(':', 1)
        bits = left.split(';')
        key = bits[0].upper()
        props[key] = raw_value
        if key in {'DTSTART', 'DTEND'}:
            for bit in bits[1:]:
                if bit.upper().startswith('TZID='):
                    timezone_name = bit.split('=', 1)[1]
    if 'UID' not in props or 'DTSTART' not in props or 'DTEND' not in props:
        raise ValueError('calendar event requires UID, DTSTART, and DTEND')
    starts_at, start_dt = _parse_ics_datetime(props['DTSTART'])
    ends_at, end_dt = _parse_ics_datetime(props['DTEND'])
    duration = 0
    if start_dt is not None and end_dt is not None:
        duration = int((end_dt - start_dt).total_seconds() // 60)
        if duration < 0:
            raise ValueError('calendar event ends before it starts')
    return {'event_id': _extract_prefixed(props['UID'], 'EVENT'), 'starts_at': starts_at, 'ends_at': ends_at, 'timezone': timezone_name or ('UTC' if props['DTSTART'].endswith('Z') else 'floating'), 'duration_minutes': duration, 'location': props.get('LOCATION', ''), 'raw_start': props['DTSTART'], 'raw_end': props['DTEND']}

def _up_cap07(value: Any) -> Dict[str, Any]:
    return _parse_ics_event(value)
_UPSTREAM_EXECUTORS: Dict[str, Callable[[Any], Any]] = {'cap_07_event_to_coordination': _up_cap07}

def execute(variant_id: str, role: str, supplied_value: Any) -> Any:
    """Run one pure transformation for a capability-splitting role."""
    if variant_id not in CONTRACTS:
        raise KeyError('unknown capability variant: {}'.format(variant_id))
    executor = _UPSTREAM_EXECUTORS[variant_id]
    result = executor(supplied_value)
    if role == 'downstream' and result == supplied_value:
        raise RuntimeError('downstream transformation returned its input unchanged')
    return result
