## Description:

Analyzes long-form web novels through a staged pipeline covering opening chapters, chapter summaries, plot pacing, character and setting extraction, aggregate reports, and style profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and story analysts use this skill to deconstruct legally held long-form fiction into local Markdown reports for craft study, benchmarking, and writing planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill saves source novel text and derived analysis locally under 拆文库/{书名}/.

Mitigation: Use the skill only with text you own or are authorized to analyze, and review or delete the output directory when retained copies are not desired.

Risk: Generated style profiles and reports may retain excerpts or close analysis of the provided source text.

Mitigation: Review generated artifacts before sharing them and remove source excerpts that should not leave the local workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-long-analyze)
- [Deconstruction notes](references/deconstruction-notes.md)
- [Material decomposition methodology](references/material-decomposition.md)
- [Output templates](references/output-templates.md)
- [Pipeline operations](references/pipeline-ops.md)
- [Style profile generator](references/style-profile-generator.md)
- [Style profile protocol](references/style-profile-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and local files under 拆文库/{书名}/]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates staged analysis artifacts including summaries, character and setting files, pacing and emotion indexes, a final report, and a style profile.]

## Skill Version(s):

1.1.14 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
