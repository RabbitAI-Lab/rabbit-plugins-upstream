## Description:

Install, verify, update, or roll back the bundled Streaming Mode Control UI for OpenClaw 2026.9.6 on Linux.

This skill is ready for commercial/non-commercial use.

## Publisher:

[svetlyoh](https://clawhub.ai/user/svetlyoh)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and administrators on Linux use this skill to install a wider, more readable Control UI, check its status, and restore the original interface when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the bundled layout replaces the local OpenClaw Control UI and only supports the pinned OpenClaw 2026.9.6 build on Linux.

Mitigation: Confirm the host version and accept the UI replacement before installation; retain the OpenClaw backup and state until the replacement works.

Risk: Uninstalling the skill does not restore the original Control UI.

Mitigation: Run the provided rollback command before uninstalling the skill, then hard-refresh the browser.

## Reference(s):

- [Streaming Mode skill listing](https://clawhub.ai/svetlyoh/skills/streaming-mode)
- [Streaming Mode homepage (skill metadata)](https://github.com/svetlyoh/web-wallet/tree/master/openclaw/skills/streaming-mode)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands and status guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Installation changes the local OpenClaw Control UI; status checks report the detected version and whether Streaming Mode is active.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
