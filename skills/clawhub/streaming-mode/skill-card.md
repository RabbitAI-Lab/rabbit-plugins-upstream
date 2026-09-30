## Description:

Install, verify, update, or roll back the bundled Streaming Mode Control UI for OpenClaw 2026.9.6 on Linux.

This skill is ready for commercial/non-commercial use.

## Publisher:

[svetlyoh](https://clawhub.ai/user/svetlyoh)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and administrators on Linux use this skill to check, install, update, or roll back a larger, stream-friendly Control UI for OpenClaw 2026.9.6.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation replaces the local OpenClaw Control UI, which handles normal browser session interactions.

Mitigation: Install only if you trust the publisher; check the supported version and retain the original UI backup for rollback.

Risk: Removing the skill alone does not restore the original application files.

Mitigation: Run the bundled rollback command before uninstalling, and preserve the saved state and backup until restoration is confirmed.

## Reference(s):

- [Streaming Mode on ClawHub](https://clawhub.ai/svetlyoh/skills/streaming-mode)
- [Project homepage (skill metadata; import provenance unavailable)](https://github.com/svetlyoh/web-wallet/tree/master/openclaw/skills/streaming-mode)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and status guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Status and rollback instructions depend on the detected OpenClaw installation.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
