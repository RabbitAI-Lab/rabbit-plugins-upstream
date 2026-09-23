## Description:

Bilibili Helper assists creators with Bilibili video titles, descriptions, tags, scripts, publishing strategy, creator operations, and audience interaction guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ckchzh](https://clawhub.ai/user/ckchzh)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content teams use this skill to draft Bilibili-ready titles, descriptions, tags, video scripts, cover guidance, posting schedules, channel diagnostics, and growth suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports unsafe shell helper input handling that could run local commands.

Mitigation: Review or patch the shell helper before deployment, and avoid passing untrusted values to command arguments.

Risk: The security guidance warns that draft names containing path characters may read or write Markdown files outside the draft folder.

Mitigation: Use simple draft names without path separators, or constrain the helper to a controlled data directory before enabling draft commands.

Risk: The security guidance notes that draft text and command topics may be stored locally.

Mitigation: Do not enter sensitive topics or draft content unless local storage is acceptable, and clear the helper data directory when needed.

## Reference(s):

- [Bilibili Helper on ClawHub](https://clawhub.ai/ckchzh/skills/bilibili-helper)
- [Publisher profile](https://clawhub.ai/user/ckchzh)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Plain text and Markdown-style templates with occasional inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some helper commands may store draft Markdown and command history in a local data directory.]

## Skill Version(s):

2.3.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
