## Description:

ClawVision 1.0.7 - explicit permission disclosure for security audit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[monaxamo](https://clawhub.ai/user/monaxamo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use ClawVision to turn a selected chat session into an exportable visual summary. It creates local HTML, PNG, Markdown, and PowerPoint outputs after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads a user-selected chat session and may process sensitive session content.

Mitigation: Use it only after explicit confirmation, and avoid sessions containing secrets, credentials, personal data, or internal identifiers unless the export has been reviewed and approved.

Risk: The skill writes persistent local HTML, PNG, Markdown, and PowerPoint export files.

Mitigation: Write exports only to an approved local directory, review generated files before sharing, and remove files that should not be retained.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/monaxamo/skills/clawvision-publish-107)
- [Project homepage](https://github.com/monaxamo/clawvision)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, files, guidance]

**Output Format:** [Plain text guidance plus local HTML, PNG, Markdown, and PowerPoint files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the selected session transcript and user-selected design settings to create persistent local exports.]

## Skill Version(s):

1.0.7 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
