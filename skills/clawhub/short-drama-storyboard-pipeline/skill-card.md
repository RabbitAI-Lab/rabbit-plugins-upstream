## Description:

Batch-generates first-frame image prompts and image-to-video prompt packs for AI short drama and comic drama storyboards, with character consistency anchors, 9:16 shot vocabulary, model-specific prompt dialects, and optional CSV/JSON export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[plinkchan](https://clawhub.ai/user/plinkchan)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, AI short-drama studios, and IP adaptation teams use this skill to turn scripts or rough storyboards into standardized shot tables, reusable character anchors, model-specific image/video prompts, and batch production manifests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Storyboard CSV files supplied by others may contain untrusted content that propagates into generated prompt files or manifests.

Mitigation: Use trusted inputs where possible, review storyboard CSV data as text before export, and check generated prompts before using them in production tools.

Risk: Generated manifest.csv files may be opened in spreadsheet software, where CSV content can behave differently than plain text.

Mitigation: Review generated manifests as text or only open manifests from trusted storyboard inputs.

Risk: Prompts generated from copyrighted or unauthorized source material can create downstream rights issues.

Mitigation: Confirm that user-provided scripts, story material, character descriptions, and references are owned, licensed, or public-domain before producing prompt packs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/plinkchan/skills/short-drama-storyboard-pipeline)
- [README](README.md)
- [Storyboard Specification](references/storyboard-spec.md)
- [Consistency Anchor](references/consistency-anchor.md)
- [Shot Vocabulary](references/shot-vocabulary.md)
- [Model Dialects](references/model-dialects.md)
- [Batch Exporter](scripts/export_prompts.py)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown tables and prompt text, with optional per-shot TXT files plus manifest.csv and manifest.json]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are designed for human review before pasting into external image or video generation tools.]

## Skill Version(s):

1.0.1 (source: frontmatter, README, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
