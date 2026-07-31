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
    "sourceUrl": null,
    "title": "optional verified title",
    "observations": ["visible, supportable facts"],
    "warnings": ["source URL not supplied"]
  },
  "intention": "诗与远方",
  "journalType": "life",
  "style": "realistic",
  "requestedElementCount": 3,
  "backgroundMode": "mixed",
  "elements": [
    {
      "id": "element-01",
      "parentSourceId": "source-01",
      "title": "远山",
      "visibleEvidence": "层叠的蓝绿色山体",
      "storyRole": "hero",
      "generationMode": "redraw",
      "style": "realistic",
      "backgroundMode": "preserve-context",
      "assetUri": "relative/or/tool-specific/asset-reference",
      "sourceUrl": null,
      "promptSummary": "single-subject hand-drawn redraw preserving meaningful scene context",
      "warnings": []
    },
    {
      "id": "element-02",
      "parentSourceId": "source-01",
      "title": "山城背景",
      "visibleEvidence": "城市建筑、山体与道路",
      "storyRole": "setting",
      "generationMode": "redraw",
      "backgroundMode": "background-only",
      "assetUri": "relative/or/tool-specific/background-reference",
      "sourceUrl": null,
      "promptSummary": "environment redraw excluding foreground people",
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

Allowed `style` values:

- `handdrawn`: soft hand-drawn cartoon rendering;
- `comic`: high-contrast comic highlight rendering;
- `collage`: aged collage rendering;
- `realistic`: natural photographic light and materials with restrained refinement. It must preserve identity, people count, pose, anatomy, lens perspective, and scene relationships; it must not imply face replacement, body reshaping, aggressive HDR, or synthetic 3D treatment.

Allowed task-level `backgroundMode` values:

- `subject-only`: isolate the subject and remove unrelated background;
- `preserve-context`: keep one primary subject together with the environment needed to preserve its spatial, action, or narrative relationship;
- `mixed`: assign an explicit element-level mode to every output. It requires at least two elements and at least two distinct element-level modes.

Allowed element-level `backgroundMode` values:

- `subject-only`;
- `preserve-context`;
- `background-only`: keep the requested environment while removing excluded foreground subjects. This value is only valid for an element within a `mixed` task.

`sourceUrl` is nullable. A missing URL must be recorded as unavailable and must not block extraction or composition.

## Composition input and layout reference

Keep approved content and an optional reference structurally separate:

```json
{
  "contentMaterials": [
    {
      "id": "element-01",
      "kind": "element",
      "sourceUrl": null,
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
    "assessment": {
      "source": "user-story",
      "fidelityScore": 10,
      "narrativeScore": 8,
      "selectionScore": 9,
      "editingNotes": "remove repetition, preserve concrete turns and the original closing meaning",
      "retainedFacts": ["verified event or relationship that the final copy may not lose"]
    },
    "copyBlocks": [
      {
        "id": "copy-opening",
        "role": "opening",
        "text": "verified or carefully framed copy",
        "linkedElementIds": ["element-02"],
        "highlightPhrases": ["verbatim phrase already present in text"],
        "typography": {
          "fontFamily": "display",
          "fontWeight": 700,
          "fontSize": 16,
          "letterSpacing": 1.2,
          "lineHeight": 1.55,
          "align": "left",
          "container": "quote"
        }
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
        "role": "hero",
        "frameStyle": "polaroid",
        "tapeStyle": "top",
        "backgroundMode": "preserve-context"
      }
    ]
  }
}
```

Allowed `frameStyle` values are `none`, `paper`, and `polaroid`. Allowed `tapeStyle` values are `none`, `top`, and `corner`. Keep transparent subject cutouts unframed; use frames on contextual images and tape on only a few accents. Highlight phrases must occur verbatim in their copy block.

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
  "sourceLinks": [],
  "warnings": ["original source URL unavailable"],
  "generation": {
    "engine": "agent-specific",
    "status": "passed",
    "guideVersion": "auditable-version@content-fingerprint",
    "stages": [
      {
        "id": "story",
        "engine": "agent-specific",
        "summary": "user story scored, refined, and selected"
      }
    ],
    "interactive": {
      "enabled": true,
      "sessionId": "stable-continuation-id",
      "lastApprovedStage": "layout"
    },
    "localRepairs": [
      {
        "type": "controlled-overlap",
        "affectedIds": ["element-01", "element-02"],
        "summary": "moved the contextual image minimally and revalidated"
      }
    ]
  },
  "quality": {
    "story": 8,
    "copy": 8,
    "typography": 8,
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

## Portable editable journal interchange

Use a versioned envelope for round-trip import and export:

```json
{
  "format": "shiguang-journal",
  "schemaVersion": "1.0",
  "exportedAt": "ISO-8601",
  "journal": {
    "id": "original-journal-id",
    "title": "editable title",
    "canvasMode": "scrapbook",
    "canvasWidth": 720,
    "canvasHeight": 1080,
    "backgroundSrc": "data:image/png;base64,...",
    "annotations": [
      {
        "id": "copy-opening",
        "kind": "lead",
        "text": "editable factual opening",
        "highlightPhrases": ["factual opening"],
        "x": 44,
        "y": 215,
        "width": 632,
        "fontFamily": "display",
        "fontWeight": 700,
        "fontSize": 16,
        "letterSpacing": 1.2,
        "lineHeight": 1.55,
        "align": "left",
        "style": "quote"
      }
    ],
    "elements": [
      {
        "id": "element-01",
        "kind": "sticker",
        "title": "independent image layer",
        "src": "data:image/png;base64,...",
        "videoUrl": "",
        "x": 72,
        "y": 260,
        "width": 396,
        "height": 250,
        "rotation": -1.5,
        "zIndex": 4,
        "backgroundMode": "preserve-context",
        "frameStyle": "polaroid",
        "tapeStyle": "top"
      }
    ]
  },
  "provenance": {
    "originalJournalId": "original-journal-id",
    "sourceLinks": [],
    "warnings": ["original source URL unavailable"]
  }
}
```

Rules:

- generate a new stable journal ID on import; never silently overwrite the source record;
- persist embedded images before saving the imported journal and replace `data:` or temporary URLs with durable asset references;
- allow only declared raster image types and safe HTTP(S) source links, with explicit package and per-asset size limits;
- keep missing source links empty rather than inventing them;
- preserve explicit `canvasWidth` and `canvasHeight` when the project does not use the default canvas; use the same dimensions for editing bounds, thumbnails, responsive fit, and export;
- preserve independent element and text records, coordinates, dimensions, rotations, z-order, story metadata, and provenance;
- treat a flattened PNG, JPG, WebP, PDF, or screenshot as a single visual layer or background. It is not a substitute for this structured envelope and cannot truthfully restore original layers.

For target reconstruction, store a process manifest beside the portable journal. At minimum include the source and logical canvas sizes, clean-base URI, every independent layer URI and placement, z-order, element-level background mode, people-count audit, target/reconstructed preview URIs, and visual/browser validation results. Keep original full source images even when a placed element contains only the visible region recovered from an overlapping flattened target.

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
      "sourceLinks": [],
      "nextAction": "reopen the saved key frame or continue editing the journal"
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

Relative paths make the archive movable. Source URLs maintain the path back to the original content when supplied; otherwise preserve an explicit unavailable state and a useful next action.
