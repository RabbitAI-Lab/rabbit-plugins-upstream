## Description:

ClawVision turns an explicitly selected OpenClaw chat session into a local, exportable visual summary as self-contained HTML, PNG tabs, Markdown, and PowerPoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[monaxamo](https://clawhub.ai/user/monaxamo)

### License/Terms of Use:

MIT

## Use Case:

OpenClaw users and developers use ClawVision to create visual, shareable summaries of chat sessions after confirming the session scope, design choices, and export formats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session history may contain secrets, credentials, personal data, or internal identifiers that could be included in exported summaries.

Mitigation: Run only after explicit confirmation and avoid exporting sensitive sessions unless the user has reviewed the scope and is comfortable with a sanitized summary.

Risk: The skill writes local HTML, PNG, Markdown, and PowerPoint files that may be shared outside the original workspace.

Mitigation: Review output paths and generated files before sharing, publishing, or opening them in another context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/monaxamo/skills/clawvision)
- [Project homepage](https://github.com/monaxamo/clawvision)
- [Publisher profile](https://clawhub.ai/user/monaxamo)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance plus local HTML, PNG, Markdown, and PowerPoint export files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user confirmation before session access; writes exports to a local output directory.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
