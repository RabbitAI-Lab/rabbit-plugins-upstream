## Description:

Batch-generates storyboard image prompts and image-to-video prompts for AI short drama and comic-drama workflows, with character consistency anchors, 9:16 vertical shot vocabulary, six model-specific prompt dialects, and optional CSV/JSON batch export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[plinkchan](https://clawhub.ai/user/plinkchan)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, AI short-drama studios, comic-drama teams, and developers use this skill to standardize scripts or storyboard tables, create reusable character anchors, generate model-specific first-frame and image-to-video prompts, and export prompt packs for batch production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted storyboard CSV input can carry spreadsheet formula content into generated manifest.csv files.

Mitigation: Treat third-party CSVs as untrusted and avoid opening generated manifest.csv files in spreadsheet software unless formula-leading cells are neutralized or the input source is trusted.

Risk: The optional Pro add-on link points to external content outside the reviewed free skill.

Mitigation: Use the reviewed free workflow without the external add-on, or evaluate the external Pro materials separately before relying on them.

Risk: Model duration, resolution, keyframe, and reference-image limits can change outside the skill.

Mitigation: Confirm current model documentation before generating final prompts, especially for Hailuo H3, Jimeng, Kling, Seedance, Vidu, and Runway.

Risk: User-supplied scripts, novels, or storyboards may include material the user is not authorized to adapt.

Mitigation: Use self-owned, licensed, or public-domain source material; pause and request clarification when ownership or adaptation rights are unclear.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/plinkchan/skills/short-drama-storyboard-pipeline)
- [Storyboard Table Spec](references/storyboard-spec.md)
- [Consistency Anchor](references/consistency-anchor.md)
- [Shot Vocabulary for 9:16 Vertical Drama](references/shot-vocabulary.md)
- [Model Dialects](references/model-dialects.md)
- [Optional Pro Add-on](https://afdian.com/item/2e33aad6ad3111f195dc52540025c377)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance plus per-shot TXT prompt files and CSV/JSON manifests when the optional exporter is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The exporter uses local Python 3.8+ standard-library code and validates storyboard columns, shot IDs, frame modes, duration ranges, and optional character anchors.]

## Skill Version(s):

1.0.2 (source: frontmatter, README, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
