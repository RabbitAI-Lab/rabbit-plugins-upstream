## Description:

OpenClaw bridge for listing Reasonix desktop projects and sessions, then resuming or creating project sessions through the shared Reasonix CLI storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaobod1](https://clawhub.ai/user/zhaobod1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when they need an agent to inspect local Reasonix desktop project/session records, list available project sessions, and continue or create Reasonix CLI sessions for a selected project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect local Reasonix project and session history.

Mitigation: Use it with explicit project paths and session files, and review which session will be loaded before resuming prior work.

Risk: Resume operations may load broad historical context from local Reasonix sessions.

Mitigation: Avoid vague continuation requests and only resume sessions after confirming the intended project and session file.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaobod1/skills/huo15-reasonix-bridge)
- [Publisher profile](https://clawhub.ai/user/zhaobod1)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the reasonix binary and may inspect local ~/.reasonix project and session metadata.]

## Skill Version(s):

1.0.0 (source: frontmatter, release evidence, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
