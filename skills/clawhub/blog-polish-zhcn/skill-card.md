## Description:

Polishes and translates a technical blog draft into a 1200-1400 word, 4-5 section Markdown article in Simplified Chinese (zh-CN), preserving technical terms and code blocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical writers, and maintainers use this skill to turn an existing technical blog draft into a polished Simplified Chinese Markdown article without images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads from a configured draft path and writes the translated article under a configured output directory.

Mitigation: Confirm draftPath and outputDir before running, and use a dedicated workspace for drafts and polished outputs.

Risk: The documented target length differs between the release summary and artifact workflow text.

Mitigation: Review the generated article length before publication when an exact word-count target matters.

## Reference(s):


## Skill Output:

**Output Type(s):** [Markdown, Files, JSON]

**Output Format:** [Markdown article saved to a file, with a JSON object returning outputPath]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads draftPath, writes under outputDir, and requires jq.]

## Skill Version(s):

1.0.14 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
