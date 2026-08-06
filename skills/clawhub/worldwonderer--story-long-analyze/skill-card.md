## Description:

Analyzes long-form web novels through a staged pipeline covering opening chapters, chapter summaries, plot aggregation, character and setting extraction, final reports, and style profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and story analysts use this skill to deconstruct legally held long-form web novels into reusable structural notes, plot rhythm references, character and setting files, reports, and style guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can retain complete novels, pasted manuscripts, and source-derived style samples in local project files.

Mitigation: Use it only with text you are authorized to analyze in a controlled workspace, and delete generated source backups, style profiles, and temporary style-sample files when retention is not intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-long-analyze)
- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode)
- [output-templates.md](references/output-templates.md)
- [material-decomposition.md](references/material-decomposition.md)
- [pipeline-ops.md](references/pipeline-ops.md)
- [style-profile-protocol.md](references/style-profile-protocol.md)
- [style-profile-generator.md](references/style-profile-generator.md)
- [deconstruction-notes.md](references/deconstruction-notes.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown files and concise interactive guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes analysis artifacts under a book-specific local workspace path and may use temporary style samples during style-profile generation.]

## Skill Version(s):

1.1.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
