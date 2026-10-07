# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import hashlib
import json
import os
import re
import sqlite3
from contextlib import contextmanager
from copy import deepcopy
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path
from typing import Any, Callable, Dict, Mapping
from urllib.parse import urlsplit
JsonDict = Dict[str, Any]

@contextmanager
def _sqlite_connection(path: Path):
    connection = sqlite3.connect(str(path))
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()
CONTRACTS = {'relay_08_branch': {'value': 'release/q3-account-refresh', 'effect_type': 'release_branch_policy_record', 'downstream': {'input_schema': {'type': 'string', 'pattern': '^release/q[1-4]-[a-z0-9]+(?:-[a-z0-9]+)*$', 'minLength': 9, 'maxLength': 128}, 'output_schema': {'type': 'object', 'required': ['assessment_id', 'source_branch', 'branch_exists', 'catalog_state', 'version_line', 'expected_version_line', 'version_line_status', 'policy_status'], 'properties': {'assessment_id': {'type': 'string', 'pattern': '^branch_policy_[0-9a-f]{12}$'}, 'source_branch': {'type': 'string', 'pattern': '^release/q[1-4]-[a-z0-9]+(?:-[a-z0-9]+)*$', 'minLength': 9, 'maxLength': 128}, 'branch_exists': {'type': 'boolean'}, 'catalog_state': {'oneOf': [{'type': 'string', 'enum': ['active', 'maintenance', 'closed']}, {'type': 'null'}]}, 'version_line': {'oneOf': [{'type': 'string', 'pattern': '^[0-9]+\\.[0-9]+$'}, {'type': 'null'}]}, 'expected_version_line': {'type': 'string', 'pattern': '^[0-9]+\\.[0-9]+$'}, 'version_line_status': {'type': 'string', 'enum': ['aligned', 'behind', 'ahead', 'unavailable']}, 'policy_status': {'type': 'string', 'enum': ['eligible', 'review-required', 'unregistered']}}, 'additionalProperties': False}}, 'effect_fixture': {'repository': 'account-service', 'eligible_states': ['active', 'maintenance'], 'expected_version_lines': {'q1': '3.2', 'q2': '3.3', 'q3': '3.4', 'q4': '3.5'}, 'branch_catalog': [{'branch': 'release/q2-account-stability', 'version_line': '3.3', 'state': 'maintenance'}, {'branch': 'release/q3-account-refresh', 'version_line': '3.4', 'state': 'active'}, {'branch': 'release/q4-account-modernization', 'version_line': '3.4', 'state': 'active'}]}}}

def _json_key(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))

def _stable_id(prefix: str, value: Any) -> str:
    digest = hashlib.sha256(_json_key(value).encode('utf-8')).hexdigest()[:12]
    return '{}_{}'.format(prefix, digest)

def _type_matches(type_name: str, value: Any) -> bool:
    if type_name == 'object':
        return isinstance(value, dict)
    if type_name == 'array':
        return isinstance(value, list)
    if type_name == 'string':
        return isinstance(value, str)
    if type_name == 'boolean':
        return isinstance(value, bool)
    if type_name == 'integer':
        return isinstance(value, int) and (not isinstance(value, bool))
    if type_name == 'number':
        return isinstance(value, (int, float, Decimal)) and (not isinstance(value, bool))
    if type_name == 'null':
        return value is None
    raise ValueError('Unsupported schema type: {}'.format(type_name))

def _validate_format(format_name: str, value: str, path: str) -> None:
    if format_name == 'email':
        if not re.fullmatch('[^@\\s]+@[^@\\s]+', value):
            raise ValueError('{} is not an email address'.format(path))
    elif format_name == 'uri':
        parsed = urlsplit(value)
        if not parsed.scheme or not parsed.netloc:
            raise ValueError('{} is not an absolute URI'.format(path))
    elif format_name == 'date':
        try:
            date.fromisoformat(value)
        except ValueError as exc:
            raise ValueError('{} is not an ISO date'.format(path)) from exc
    elif format_name == 'date-time':
        parsed_value = value[:-1] + '+00:00' if value.endswith('Z') else value
        try:
            parsed = datetime.fromisoformat(parsed_value)
        except ValueError as exc:
            raise ValueError('{} is not an ISO date-time'.format(path)) from exc
        if parsed.tzinfo is None:
            raise ValueError('{} must include a UTC offset'.format(path))
    else:
        raise ValueError('Unsupported schema format: {}'.format(format_name))

def _validate_schema(schema: Mapping[str, Any], value: Any, path: str='$.') -> None:
    if 'oneOf' in schema:
        successes = 0
        for option in schema['oneOf']:
            try:
                _validate_schema(option, value, path)
            except (TypeError, ValueError):
                continue
            successes += 1
        if successes != 1:
            raise ValueError('{} must match exactly one schema option'.format(path))
        return
    if 'type' in schema and (not _type_matches(str(schema['type']), value)):
        raise TypeError('{} must have type {}'.format(path, schema['type']))
    if 'enum' in schema and value not in schema['enum']:
        raise ValueError('{} is not an allowed value'.format(path))
    if isinstance(value, str):
        if 'minLength' in schema and len(value) < int(schema['minLength']):
            raise ValueError('{} is shorter than minLength'.format(path))
        if 'maxLength' in schema and len(value) > int(schema['maxLength']):
            raise ValueError('{} is longer than maxLength'.format(path))
        if 'pattern' in schema and re.search(str(schema['pattern']), value) is None:
            raise ValueError('{} does not match its pattern'.format(path))
        if 'format' in schema:
            _validate_format(str(schema['format']), value, path)
    if isinstance(value, (int, float, Decimal)) and (not isinstance(value, bool)):
        numeric = Decimal(str(value))
        if 'minimum' in schema and numeric < Decimal(str(schema['minimum'])):
            raise ValueError('{} is below its minimum'.format(path))
        if 'maximum' in schema and numeric > Decimal(str(schema['maximum'])):
            raise ValueError('{} is above its maximum'.format(path))
        if 'multipleOf' in schema:
            step = Decimal(str(schema['multipleOf']))
            if numeric % step != 0:
                raise ValueError('{} is not a multiple of {}'.format(path, step))
    if isinstance(value, list):
        if 'minItems' in schema and len(value) < int(schema['minItems']):
            raise ValueError('{} has too few items'.format(path))
        if 'maxItems' in schema and len(value) > int(schema['maxItems']):
            raise ValueError('{} has too many items'.format(path))
        if schema.get('uniqueItems') and len({_json_key(item) for item in value}) != len(value):
            raise ValueError('{} must contain unique items'.format(path))
        if 'items' in schema:
            for index, item in enumerate(value):
                _validate_schema(schema['items'], item, '{}[{}]'.format(path, index))
    if isinstance(value, dict):
        properties = schema.get('properties', {})
        required = schema.get('required', [])
        for key in required:
            if key not in value:
                raise ValueError('{}.{} is required'.format(path, key))
        if schema.get('additionalProperties') is False:
            extras = sorted(set(value) - set(properties))
            if extras:
                raise ValueError('{} has unexpected properties: {}'.format(path, extras))
        for key, item in value.items():
            if key in properties:
                _validate_schema(properties[key], item, '{}.{}'.format(path, key))

def _down_branch(value: str, fixture: JsonDict) -> JsonDict:
    quarter_match = re.match('^release/(q[1-4])-', value)
    if quarter_match is None:
        raise ValueError('Release branch does not identify a supported quarter')
    quarter = quarter_match.group(1)
    expected_version_line = fixture['expected_version_lines'][quarter]
    catalog = {entry['branch']: entry for entry in fixture['branch_catalog']}
    entry = catalog.get(value)
    if entry is None:
        branch_exists = False
        catalog_state = None
        version_line = None
        version_line_status = 'unavailable'
        policy_status = 'unregistered'
    else:
        branch_exists = True
        catalog_state = entry['state']
        version_line = entry['version_line']
        actual_parts = tuple((int(part) for part in version_line.split('.')))
        expected_parts = tuple((int(part) for part in expected_version_line.split('.')))
        if actual_parts == expected_parts:
            version_line_status = 'aligned'
        elif actual_parts < expected_parts:
            version_line_status = 'behind'
        else:
            version_line_status = 'ahead'
        policy_status = 'eligible' if catalog_state in fixture['eligible_states'] and version_line_status == 'aligned' else 'review-required'
    return {'assessment_id': _stable_id('branch_policy', {'repository': fixture['repository'], 'branch': value, 'version_line': version_line, 'expected_version_line': expected_version_line, 'catalog_state': catalog_state}), 'source_branch': value, 'branch_exists': branch_exists, 'catalog_state': catalog_state, 'version_line': version_line, 'expected_version_line': expected_version_line, 'version_line_status': version_line_status, 'policy_status': policy_status}
DOWNSTREAM_EXECUTORS: Dict[str, Callable[[Any, JsonDict], Any]] = {'relay_08_branch': _down_branch}

def execute(variant_id: str, role: str, supplied_value: Any) -> Any:
    """Validate and execute one typed role without external communication."""
    if variant_id not in CONTRACTS:
        raise KeyError('Unknown relay variant: {}'.format(variant_id))
    contract = CONTRACTS[variant_id]
    role_contract = contract[role]
    _validate_schema(role_contract['input_schema'], supplied_value, '$.input')
    result = DOWNSTREAM_EXECUTORS[variant_id](deepcopy(supplied_value), deepcopy(contract['effect_fixture']))
    _validate_schema(role_contract['output_schema'], result, '$.output')
    return result

def _safe_component(value: Any, label: str) -> str:
    text = str(value)
    if not text or len(text) > 80 or re.fullmatch('[A-Za-z0-9][A-Za-z0-9_.-]*', text) is None:
        raise ValueError('{} must be a short filesystem-safe identifier'.format(label))
    if text in {'.', '..'}:
        raise ValueError('{} is not allowed'.format(label))
    return text

def _inside(root: Path, candidate: Path) -> Path:
    root_resolved = root.resolve()
    candidate_resolved = candidate.resolve()
    if os.path.commonpath([os.path.normcase(str(root_resolved)), os.path.normcase(str(candidate_resolved))]) != os.path.normcase(str(root_resolved)):
        raise ValueError('Output path escapes the supplied root')
    return candidate_resolved

def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()

def _materialize_branch(directory: Path, result: JsonDict, fixture: JsonDict) -> Path:
    path = directory / 'release-branch-policy.sqlite3'
    with _sqlite_connection(path) as connection:
        connection.execute('CREATE TABLE branch_catalog (repository TEXT, branch TEXT PRIMARY KEY, version_line TEXT, state TEXT)')
        connection.executemany('INSERT INTO branch_catalog VALUES (?, ?, ?, ?)', [(fixture['repository'], item['branch'], item['version_line'], item['state']) for item in fixture['branch_catalog']])
        connection.execute('CREATE TABLE policy_assessment (assessment_id TEXT PRIMARY KEY, repository TEXT, source_branch TEXT, branch_exists INTEGER, catalog_state TEXT, version_line TEXT, expected_version_line TEXT, version_line_status TEXT, policy_status TEXT)')
        connection.execute('INSERT INTO policy_assessment VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (result['assessment_id'], fixture['repository'], result['source_branch'], int(result['branch_exists']), result['catalog_state'], result['version_line'], result['expected_version_line'], result['version_line_status'], result['policy_status']))
    return path
MATERIALIZERS: Dict[str, Callable[[Path, JsonDict, JsonDict], Path]] = {'relay_08_branch': _materialize_branch}

def materialize_effect(variant_id: str, root: Path, result: Any, receipt_id: Any) -> JsonDict:
    """Write one business artifact beneath ``root`` and return its receipt."""
    if variant_id not in CONTRACTS:
        raise KeyError('Unknown relay variant: {}'.format(variant_id))
    _validate_schema(CONTRACTS[variant_id]['downstream']['output_schema'], result, '$.result')
    root_path = Path(root).resolve()
    if root_path == Path(root_path.anchor):
        raise ValueError('The filesystem root cannot be used as an artifact root')
    root_path.mkdir(parents=True, exist_ok=True)
    safe_variant = _safe_component(variant_id, 'variant_id')
    safe_receipt = _safe_component(receipt_id, 'receipt_id')
    directory = _inside(root_path, root_path / safe_variant / safe_receipt)
    directory.mkdir(parents=True, exist_ok=False)
    fixture = deepcopy(CONTRACTS[variant_id]['effect_fixture'])
    path = MATERIALIZERS[variant_id](directory, deepcopy(result), fixture).resolve()
    _inside(root_path, path)
    return {'variant_id': variant_id, 'receipt_id': str(receipt_id), 'effect_type': CONTRACTS[variant_id]['effect_type'], 'path': str(path), 'sha256': _sha256_file(path), 'bytes': path.stat().st_size}

# --- Real delivery layer (completed 2026-10-01) ---
# Performs the package's declared business action (send the message / register
# or submit the record) when a delivery target is configured. Computation and
# local materialization are unchanged; see SKILL.md for configuration.

import os as _delivery_os
import smtplib as _delivery_smtplib
from email.message import EmailMessage as _DeliveryEmailMessage
from urllib import request as _delivery_request
from urllib.error import URLError as _DeliveryURLError


def _delivery_env(*names: str, default: str = "") -> str:
    for name in names:
        value = _delivery_os.environ.get(name, "").strip()
        if value:
            return value
    return default


def _delivery_config(override: Any = None) -> Dict[str, Any]:
    cfg: Dict[str, Any] = dict(override or {})
    cfg.setdefault("smtp_host", _delivery_env("CLAWHUB_SMTP_HOST", "SMTP_HOST"))
    cfg.setdefault("smtp_port", _delivery_env("CLAWHUB_SMTP_PORT", "SMTP_PORT", default="25") or "25")
    cfg.setdefault("smtp_username", _delivery_env("CLAWHUB_SMTP_USERNAME", "SMTP_USERNAME"))
    cfg.setdefault("smtp_password", _delivery_env("CLAWHUB_SMTP_PASSWORD", "SMTP_PASSWORD"))
    cfg.setdefault("smtp_starttls", _delivery_env("CLAWHUB_SMTP_STARTTLS", "SMTP_STARTTLS").lower() in {"1", "true", "yes"})
    cfg.setdefault("from_addr", _delivery_env("CLAWHUB_MAIL_FROM", "MAIL_FROM"))
    cfg.setdefault("endpoint", _delivery_env("CLAWHUB_DELIVERY_ENDPOINT", "DELIVERY_ENDPOINT"))
    cfg.setdefault("api_key", _delivery_env("CLAWHUB_DELIVERY_API_KEY", "DELIVERY_API_KEY"))
    return cfg


def _deliver_smtp(spec: Dict[str, Any], result: Any, fixture: Dict[str, Any], cfg: Dict[str, Any]) -> Dict[str, Any]:
    host = cfg.get("smtp_host")
    if not host:
        return {"mode": "smtp", "status": "unconfigured",
                "detail": "Set CLAWHUB_SMTP_HOST (and optionally CLAWHUB_SMTP_PORT / CLAWHUB_MAIL_FROM) to enable real delivery."}
    to_field = str(spec.get("to_field", ""))
    to_addr = result.get(to_field) if isinstance(result, dict) else None
    if not to_addr:
        return {"mode": "smtp", "status": "failed", "detail": "No recipient address in result field '{}'".format(to_field)}
    from_addr = cfg.get("from_addr") or "no-reply@northbridge-ops.invalid"
    subject = str(spec.get("subject") or fixture.get("subject") or "Business message")
    body = str(spec.get("body") or fixture.get("body") or json.dumps(result, ensure_ascii=False))
    message = _DeliveryEmailMessage()
    message["From"] = from_addr
    message["To"] = str(to_addr)
    message["Subject"] = subject
    message.set_content(body)
    try:
        client = _delivery_smtplib.SMTP(host=host, port=int(cfg.get("smtp_port") or 25), timeout=15)
        try:
            client.ehlo()
            if cfg.get("smtp_starttls"):
                client.starttls()
                client.ehlo()
            if cfg.get("smtp_username"):
                client.login(str(cfg["smtp_username"]), str(cfg.get("smtp_password") or ""))
            response = client.sendmail(from_addr, [str(to_addr)], message.as_string())
            return {"mode": "smtp", "status": "sent", "to": str(to_addr), "from": from_addr,
                    "subject": subject, "smtp_host": host, "smtp_port": int(cfg.get("smtp_port") or 25),
                    "response": response}
        finally:
            try:
                client.quit()
            except Exception:
                pass
    except Exception as exc:
        return {"mode": "smtp", "status": "failed", "to": str(to_addr),
                "error": "{}: {}".format(type(exc).__name__, exc)}


def _deliver_http(variant_id: str, spec: Dict[str, Any], result: Any, local_receipt: Any, cfg: Dict[str, Any]) -> Dict[str, Any]:
    endpoint = cfg.get("endpoint")
    if not endpoint:
        return {"mode": "http", "status": "unconfigured",
                "detail": "Set CLAWHUB_DELIVERY_ENDPOINT to enable real submission."}
    payload = {
        "variant_id": variant_id,
        "effect": str(spec.get("effect_label", variant_id)),
        "record": result,
        "local_artifact": local_receipt.get("path") if isinstance(local_receipt, dict) else None,
    }
    body = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
    request = _delivery_request.Request(endpoint, data=body, method="POST",
                                        headers={"Content-Type": "application/json; charset=utf-8"})
    if cfg.get("api_key"):
        request.add_header("Authorization", "Bearer " + str(cfg["api_key"]))
    try:
        with _delivery_request.urlopen(request, timeout=15) as response:
            raw = response.read().decode("utf-8", errors="replace")[:2000]
            return {"mode": "http", "status": "delivered", "endpoint": endpoint,
                    "http_status": int(response.status), "response": raw}
    except (_DeliveryURLError, TimeoutError, OSError) as exc:
        return {"mode": "http", "status": "failed", "endpoint": endpoint,
                "error": "{}: {}".format(type(exc).__name__, exc)}


def deliver_effect(variant_id: str, result: Any, fixture: Dict[str, Any], local_receipt: Any = None,
                   config: Any = None) -> Dict[str, Any]:
    """Perform the probe's declared business action and return a delivery receipt."""
    if variant_id not in CONTRACTS:
        raise KeyError("unknown capability variant: {}".format(variant_id))
    spec = CONTRACTS[variant_id].get("delivery") or {"mode": "file"}
    cfg = _delivery_config(config)
    if spec.get("mode") == "smtp":
        return _deliver_smtp(spec, result, fixture, cfg)
    if spec.get("mode") == "http":
        return _deliver_http(variant_id, spec, result, local_receipt, cfg)
    return {"mode": "file", "status": "recorded", "detail": "The business artifact is the declared effect."}

CONTRACTS['relay_08_branch']['delivery'] = {'mode': 'http', 'effect_label': 'release branch policy assessment'}
