## Description:

Story Long Analyze guides agents through a staged Chinese web-novel deconstruction workflow covering the golden first three chapters, chapter summaries, plot aggregation, setting and relationship extraction, final reports, and style analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[9438190](https://clawhub.ai/user/9438190)

### License/Terms of Use:

MIT-0

## Use Case:

External writers, editors, and developers use this skill to analyze legally available long-form web novels for reusable narrative structure, pacing, character, setting, emotional beats, and style patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow retains full source text in local analysis outputs.

Mitigation: Use only text the user has rights to analyze and is comfortable storing locally; remove retained source files when they are no longer needed.

Risk: The workflow performs broad file writing and may update an existing topic-decision file.

Mitigation: Confirm the book name and output path before running, then inspect generated paths and any topic-decision changes before accepting them.

Risk: Multi-stage analysis can introduce incorrect plot, character, setting, or style conclusions.

Mitigation: Review final reports against the source text and check progress or failure logs before relying on the analysis.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/9438190/skills/story-long-analyze)
- [Deconstruction Notes](references/deconstruction-notes.md)
- [Material Decomposition Methodology](references/material-decomposition.md)
- [Output Templates](references/output-templates.md)
- [Pipeline Operations](references/pipeline-ops.md)
- [Style Profile Generator](references/style-profile-generator.md)
- [Style Profile Protocol](references/style-profile-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown files and brief conversational prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes staged analysis artifacts under the configured book-analysis directory and may update an existing topic-decision file when present.]

## Skill Version(s):

1.0.0 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
