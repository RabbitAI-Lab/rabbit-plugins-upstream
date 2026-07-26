# Portable data contracts

Use these shapes as a common handoff language. Add implementation-specific fields without removing provenance.

## Source and element manifest

```json
{
  "memoryId": "memory-stable-id",
  "source": {
    "id": "source-01",
    "kind": "key-frame",
    "uri": "relative/or/tool-specific/frame-reference",
    "sourceUrl": "https://example.com/original",
    "title": "optional verified title",
    "observations": ["visible, supportable facts"],
    "warnings": []
  },
  "intention": "诗与远方",
  "journalType": "life",
  "requestedElementCount": 4,
  "elements": [
    {
      "id": "element-01",
      "parentSourceId": "source-01",
      "title": "远山",
      "visibleEvidence": "层叠的蓝绿色山体",
      "storyRole": "hero",
      "generationMode": "redraw",
      "assetUri": "relative/or/tool-specific/asset-reference",
      "sourceUrl": "https://example.com/original",
      "promptSummary": "single-subject hand-drawn redraw",
      "warnings": []
    }
  ]
}
```

Allowed `generationMode` values:

- `redraw`: a model or artist created a new visual interpretation;
- `crop`: the original visual was isolated without being redrawn;
- `prompt-only`: no asset was created; a reusable prompt was delivered;
- `user-provided`: the asset came directly from the user.

## Composition input and layout reference

Keep approved content and an optional reference structurally separate:

```json
{
  "contentMaterials": [
    {
      "id": "element-01",
      "kind": "element",
      "sourceUrl": "https://example.com/original",
      "approved": true
    }
  ],
  "layoutReference": {
    "id": "reference-01",
    "uri": "relative/or/tool-specific/reference",
    "mode": "layout-only",
    "focus": "主图、小图和文字区域的阅读节奏",
    "restrictions": "不要复制照片、人物、地点、品牌、原文字或事实",
    "analysis": {
      "readingPath": "top-left hero to right-side details",
      "heroStrategy": "one dominant image with two smaller supports",
      "textZones": ["beside hero", "lower closing area"],
      "whitespace": "calm center and generous footer",
      "overlapRhythm": "limited edge overlap"
    }
  }
}
```

Allowed `layoutReference.mode` values:

- `layout-only`: transfer only composition and reading logic;
- `allow-abstract-decoration`: may also transfer non-identifying paper, tape, line, and palette relationships.

Never copy reference-only content into `contentMaterials`.

## Story and layout plan

```json
{
  "story": {
    "spine": "从眼前出发，把向往留在可抵达的路上",
    "readingPath": "top-left to lower-right S-curve",
    "orderedElementIds": ["element-02", "element-01", "element-03", "element-04"],
    "layoutReferenceId": "reference-01",
    "copyBlocks": [
      {
        "id": "copy-opening",
        "role": "opening",
        "text": "verified or carefully framed copy",
        "linkedElementIds": ["element-02"]
      }
    ]
  },
  "paper": {
    "palette": ["#F4F0E6", "#7890A0", "#60745B"],
    "material": "warm fibrous paper with mist-blue wash",
    "reservedAreas": ["central content field", "footer source action"],
    "forbiddenMotifs": ["food table", "unrelated fruit", "readable fake text"]
  },
  "layout": {
    "canvas": { "width": 720, "height": 920 },
    "items": [
      {
        "id": "element-01",
        "x": 72,
        "y": 260,
        "width": 396,
        "height": 250,
        "rotation": -1.5,
        "z": 4,
        "role": "hero"
      }
    ]
  }
}
```

## Archive record

```json
{
  "schemaVersion": "1.0",
  "memoryId": "memory-stable-id",
  "createdAt": "ISO-8601 when known",
  "source": {},
  "elements": [],
  "story": {},
  "paper": {},
  "layout": {},
  "journalArtifact": {
    "uri": "relative/or/tool-specific/reference",
    "editable": true,
    "previewUri": "optional-preview-reference",
    "title": "可由用户快速整理的标题",
    "subtitle": "可搜索摘要",
    "location": "optional verified place",
    "date": "optional user-facing date",
    "tags": ["optional", "editable"],
    "journalType": "life",
    "updatedAt": "ISO-8601 when known"
  },
  "searchText": "combined factual and interpretive memory description",
  "sourceLinks": ["https://example.com/original"],
  "warnings": [],
  "quality": {
    "story": 8,
    "copy": 8,
    "hierarchy": 9,
    "paperFit": 8,
    "legibility": 8,
    "fidelity": 8,
    "factualIntegrity": 10,
    "provenance": 10
  }
}
```

## Collection mutation

Use a dry-run/confirm/apply sequence for destructive actions:

```json
{
  "operation": "bulk-delete",
  "collection": "journals",
  "selectedIds": ["journal-01", "journal-02"],
  "confirmed": true,
  "effects": {
    "deleteRecords": ["journal-01", "journal-02"],
    "unlinkMemoryIds": ["memory-01"],
    "removeArchiveUris": [
      "memory-01/journal/journal-01.json",
      "memory-01/previews/journal-01.png"
    ],
    "preserveSharedAssetIds": ["element-01", "background-02"]
  },
  "result": {
    "deletedIds": ["journal-01", "journal-02"],
    "failedIds": [],
    "warnings": []
  }
}
```

For library or memory collections, replace `collection` and keep the same stable-ID, confirmation, effects, and result fields. Add a tombstone or suppression record when automatic backfill could recreate an intentionally deleted item.

## Recall result

```json
{
  "query": "那次雨后骑车去山里的记录",
  "engine": "agent-specific semantic or disclosed fallback",
  "results": [
    {
      "memoryId": "memory-stable-id",
      "score": 0.87,
      "reason": "画面、描述与雨后、远山和出发的意象相符",
      "previewUri": "optional-preview-reference",
      "sourceLinks": ["https://example.com/original"]
    }
  ],
  "warnings": []
}
```

## Recommended portable folder

```text
memory-stable-id/
├── manifest.json
├── source/
├── elements/
├── journal/
├── previews/
└── notes/
```

Relative paths make the archive movable. Source URLs maintain the path back to the original content.
