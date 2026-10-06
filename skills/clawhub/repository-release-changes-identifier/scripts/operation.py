# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import re
from typing import Any, Callable, Dict
CONTRACTS = {'cap_06_change_to_release': {'upstream': {'input_schema': {'type': 'string', 'format': 'unified-diff', 'minLength': 1}, 'output_schema': {'type': 'object', 'required': ['change_id', 'files', 'components', 'additions', 'deletions'], 'properties': {'change_id': {'type': 'string', 'minLength': 1}, 'files': {'type': 'array', 'items': {'type': 'string'}}, 'components': {'type': 'array', 'items': {'type': 'string'}}, 'additions': {'type': 'integer'}, 'deletions': {'type': 'integer'}}, 'additionalProperties': True}, 'sample_input': 'Change-ID: REPO-FOXTROT-6186\ndiff --git a/services/api.py b/services/api.py\n--- a/services/api.py\n+++ b/services/api.py\n@@ -1 +1,2 @@\n-old = 1\n+old = 2\n+ready = True\n'}}}

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

def _analyze_unified_diff(value: Any) -> Dict[str, Any]:
    text = _require_text(value, 'repository patch')
    file_matches = re.findall('diff\\s+--git\\s+a/(\\S+)\\s+b/(\\S+)', text)
    if not file_matches:
        raise ValueError('repository patch has no diff --git header')
    files = [right for _, right in file_matches]
    if '\n' in text:
        additions = sum((1 for line in text.splitlines() if line.startswith('+') and (not line.startswith('+++'))))
        deletions = sum((1 for line in text.splitlines() if line.startswith('-') and (not line.startswith('---'))))
    else:
        patch_body = re.sub('@@.*?@@', ' ', text)
        additions = len(re.findall('(?:^|\\s)\\+(?!\\+)(?=\\S)', patch_body))
        deletions = len(re.findall('(?:^|\\s)-(?!-)(?=\\S)', patch_body))
    components = sorted({path.split('/', 1)[0] if '/' in path else 'root' for path in files})
    return {'change_id': _extract_prefixed(text, 'REPO'), 'files': files, 'components': components, 'additions': additions, 'deletions': deletions}

def _up_cap06(value: Any) -> Dict[str, Any]:
    return _analyze_unified_diff(value)
_UPSTREAM_EXECUTORS: Dict[str, Callable[[Any], Any]] = {'cap_06_change_to_release': _up_cap06}

def execute(variant_id: str, role: str, supplied_value: Any) -> Any:
    """Run one pure transformation for a capability-splitting role."""
    if variant_id not in CONTRACTS:
        raise KeyError('unknown capability variant: {}'.format(variant_id))
    executor = _UPSTREAM_EXECUTORS[variant_id]
    result = executor(supplied_value)
    if role == 'downstream' and result == supplied_value:
        raise RuntimeError('downstream transformation returned its input unchanged')
    return result
