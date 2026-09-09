## Description:

ClawVision turns an approved OpenClaw chat session into local visual summaries and export files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[monaxamo](https://clawhub.ai/user/monaxamo)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use ClawVision to create user-approved visual and exportable summaries of OpenClaw chat sessions for review, sharing, or documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session exports can expose secrets, credentials, personal data, or internal identifiers if those details are present in the selected conversation.

Mitigation: Use the skill only on sessions whose export scope has been reviewed and approved, and avoid sessions containing sensitive content.

Risk: The skill writes transcript-derived HTML, PNG, Markdown, and PowerPoint files to disk.

Mitigation: Confirm the output location and review generated files before sharing, retaining, or publishing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/monaxamo/skills/clawvision)
- [Skill homepage](https://github.com/monaxamo/clawvision)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON-derived summaries plus local HTML, PNG, Markdown, and PowerPoint export files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads an approved session history and writes transcript-derived export files locally.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
