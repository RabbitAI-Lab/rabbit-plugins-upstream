# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import hashlib
import json
import re
from typing import Any, Callable, Dict, Iterable, List
CONTRACTS = {'cap_02_file_to_log': {'upstream': {'input_schema': {'type': 'string', 'format': 'knowledge-note', 'minLength': 1}, 'output_schema': {'type': 'object', 'required': ['reference', 'heading', 'tags', 'links', 'content_digest', 'sections'], 'properties': {'reference': {'type': 'string', 'pattern': '^KB-[A-Z0-9-]+$'}, 'heading': {'type': 'string', 'minLength': 1}, 'tags': {'type': 'array', 'items': {'type': 'string', 'minLength': 1}, 'uniqueItems': True}, 'links': {'type': 'array', 'items': {'type': 'string', 'minLength': 1}}, 'content_digest': {'type': 'string', 'pattern': '^[a-f0-9]{16}$'}, 'sections': {'type': 'array', 'minItems': 1, 'items': {'type': 'object', 'required': ['ordinal', 'heading', 'content', 'content_digest'], 'properties': {'ordinal': {'type': 'integer', 'minimum': 1}, 'heading': {'type': 'string', 'minLength': 1}, 'content': {'type': 'string', 'minLength': 1}, 'content_digest': {'type': 'string', 'pattern': '^[a-f0-9]{16}$'}}, 'additionalProperties': False}}}, 'additionalProperties': False}, 'sample_input': 'Reference: KB-BRAVO-2091\n# Supplier Onboarding Guide\nTags: onboarding, supplier-ops\nLinks: [[KB-GUIDE-4401]], [[KB-POLICY-7720]]\n\n## Intake Requirements\nCollect the approved supplier profile and ownership details.\n\n## Workspace Access\nFollow [[KB-POLICY-7720]] before granting editor access.\n'}}}

def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), default=str)

def _digest(value: Any, length: int=16) -> str:
    return hashlib.sha256(_canonical_json(value).encode('utf-8')).hexdigest()[:length]

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

def _unique_text(items: Iterable[Any]) -> List[str]:
    result: List[str] = []
    seen = set()
    for raw in items:
        item = str(raw).strip()
        marker = item.casefold()
        if not item or marker in seen:
            continue
        seen.add(marker)
        result.append(item)
    return result

def _knowledge_links(text: str) -> List[str]:
    links: List[str] = []
    for raw in re.findall('\\[\\[([^\\]]+)\\]\\]', text):
        target = raw.split('|', 1)[0].split('#', 1)[0].strip()
        if target:
            links.append(target)
    links.extend((match.strip() for match in re.findall('\\[[^\\]]+\\]\\(([^)]+)\\)', text)))
    return [item for item in links if item]

def _knowledge_tags(text: str) -> List[str]:
    tags: List[str] = []
    for line in text.splitlines():
        match = re.match('\\s*tags?\\s*:\\s*(.*?)\\s*$', line, re.IGNORECASE)
        if not match:
            continue
        raw = match.group(1).strip()
        if raw.startswith('[') and raw.endswith(']'):
            raw = raw[1:-1]
        tags.extend((item.strip().strip('"\'') for item in raw.split(',')))
    return _unique_text(tags)

def _knowledge_heading(text: str) -> str:
    heading = re.search('(?m)^\\s*#\\s+(.+?)\\s*$', text)
    if heading:
        return heading.group(1).strip()[:160]
    title = re.search('(?im)^\\s*title\\s*:\\s*(.+?)\\s*$', text)
    if title:
        return title.group(1).strip()[:160]
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or re.match('(?i)^(?:reference|ref|tags?|links?)\\s*:', stripped):
            continue
        return stripped.lstrip('#').strip()[:160]
    raise ValueError('knowledge note requires a heading')

def _knowledge_sections(text: str, document_heading: str) -> List[Dict[str, Any]]:
    sections: List[Dict[str, Any]] = []
    current_heading = document_heading
    body_lines: List[str] = []

    def flush() -> None:
        nonlocal body_lines
        content = '\n'.join(body_lines).strip()
        body_lines = []
        if not content:
            return
        digest = _digest({'heading': current_heading.casefold(), 'content': ' '.join(content.split())})
        sections.append({'ordinal': len(sections) + 1, 'heading': current_heading[:160], 'content': content, 'content_digest': digest})
    metadata = re.compile('(?i)^\\s*(?:reference|ref|title|tags?|links?)\\s*:')
    for line in text.splitlines():
        heading_match = re.match('^\\s*(#{1,6})\\s+(.+?)\\s*$', line)
        if heading_match:
            candidate = heading_match.group(2).strip()
            if len(heading_match.group(1)) == 1 and (not body_lines) and (not sections):
                current_heading = candidate
            else:
                flush()
                current_heading = candidate
            continue
        if metadata.match(line):
            continue
        if line.strip() or body_lines:
            body_lines.append(line.rstrip())
    flush()
    if not sections:
        fallback = document_heading.strip()
        sections.append({'ordinal': 1, 'heading': document_heading, 'content': fallback, 'content_digest': _digest({'heading': document_heading.casefold(), 'content': fallback})})
    return sections

def _up_cap02(value: Any) -> Dict[str, Any]:
    text = _require_text(value, 'knowledge note')
    reference = _extract_prefixed(text, 'KB')
    heading = _knowledge_heading(text)
    return {'reference': reference, 'heading': heading, 'tags': _knowledge_tags(text), 'links': _knowledge_links(text), 'content_digest': _digest('\n'.join((line.rstrip() for line in text.splitlines())).strip()), 'sections': _knowledge_sections(text, heading)}
_UPSTREAM_EXECUTORS: Dict[str, Callable[[Any], Any]] = {'cap_02_file_to_log': _up_cap02}

def execute(variant_id: str, role: str, supplied_value: Any) -> Any:
    """Run one pure transformation for a capability-splitting role."""
    if variant_id not in CONTRACTS:
        raise KeyError('unknown capability variant: {}'.format(variant_id))
    executor = _UPSTREAM_EXECUTORS[variant_id]
    result = executor(supplied_value)
    if role == 'downstream' and result == supplied_value:
        raise RuntimeError('downstream transformation returned its input unchanged')
    return result
