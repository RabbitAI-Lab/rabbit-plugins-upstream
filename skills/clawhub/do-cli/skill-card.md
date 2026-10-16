## Description:

Guides agents in using the do CLI to manage tasks, habits, and other personal life-tracking data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbeverhelst](https://clawhub.ai/user/robbeverhelst)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and their agents use this skill to review personal tasks and habits, capture new tasks, and manage check-ins through the do CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can change remote personal tasks and habit data despite the skill's claim of limited write authority.

Mitigation: Require user confirmation before creating, updating, completing, snoozing, skipping, pausing, retiring, or canceling items; avoid broad autonomous write access.

Risk: An overly broad API key could expose or modify more personal data than needed.

Mitigation: Use a minimally scoped key and review its permissions before use.

Risk: The suggested remote installer script executes downloaded code in a shell.

Mitigation: Review installation steps and prefer safer Bun or package installation methods over piping a remote script into the shell.

## Reference(s):

- [do skill on ClawHub](https://clawhub.ai/robbeverhelst/skills/do-cli)
- [do source and documentation (linked by the skill)](https://github.com/robbeverhelst/do)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text and Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI results can be JSON when piped or requested with --json.]

## Skill Version(s):

1.0.4 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
