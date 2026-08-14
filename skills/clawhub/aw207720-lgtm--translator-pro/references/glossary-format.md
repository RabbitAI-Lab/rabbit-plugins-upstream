# Glossary Format

## Purpose

A glossary ensures consistent translation of domain-specific terms across a document or corpus.

## Format

Provide a JSON array of term objects:

```json
[
  {
    "source": "intellectual property",
    "target": "知识产权",
    "source_lang": "en",
    "target_lang": "zh-CN",
    "context": "legal",
    "notes": "Standard legal term; do not translate as 'knowledge property'"
  },
  {
    "source": "force majeure",
    "target": "caso fortuito / fuerza mayor",
    "source_lang": "en",
    "target_lang": "es",
    "context": "legal",
    "notes": "Use 'fuerza mayor' in Spain; 'caso fortuito' in some LatAm jurisdictions"
  }
]
```

## Fields

- `source` (required): The term in the source language
- `target` (required): The approved translation in the target language
- `source_lang` (required): ISO 639-1 code of source language
- `target_lang` (required): ISO 639-1 code of target language
- `context` (optional): Domain context — `business`, `legal`, `casual`, `technical`
- `notes` (optional): Usage notes or restrictions

## Loading

Pass glossary as a file path or inline JSON when requesting translation.
Glossary terms override default translation choices. All matched overrides
are reported in the `glossary_terms` field of the output.