## Description:

Batch-generates first-frame image prompts and image-to-video prompts for AI short drama or comic drama workflows, with character consistency anchors, 9:16 vertical shot vocabulary, six model prompt dialects, and CSV/JSON batch export support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[plinkchan](https://clawhub.ai/user/plinkchan)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, production teams, and agent users use this skill to turn scripts, rough shots, or storyboard tables into reusable prompt packs for short-drama image and video generation. It is suited to batch storyboard prompting, role-consistency anchors, and model-specific prompt dialect selection, not complete video editing or final film assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated manifest.csv files may contain spreadsheet formula-like cells when storyboard inputs come from untrusted sources.

Mitigation: Review or neutralize cells beginning with =, +, -, or @ before opening generated CSV files in spreadsheet software.

Risk: Storyboard source material may be copyrighted or unauthorized.

Mitigation: Use owned, licensed, or public-domain material and pause for rights review when user-provided source text appears to be infringing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/plinkchan/skills/short-drama-storyboard-pipeline)
- [Storyboard Table Spec](references/storyboard-spec.md)
- [Consistency Anchor](references/consistency-anchor.md)
- [Model Dialects](references/model-dialects.md)
- [Shot Vocabulary for 9:16 Vertical Drama](references/shot-vocabulary.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance, CSV/JSON manifests, and per-shot TXT prompt files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Python 3.8+ standard-library exporter can validate storyboard CSV files and generate prompt scaffolds plus manifest.csv and manifest.json.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
