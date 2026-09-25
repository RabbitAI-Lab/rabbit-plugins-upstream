## Description:

Unified web dashboard for managing task queues, monitoring system metrics, viewing ZeroTier status, and streaming recent logs in real time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chris6970barbarian-hue](https://clawhub.ai/user/chris6970barbarian-hue)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use Dashboard to monitor OpenClaw hosts, manage local task queues, inspect ZeroTier network status, and review recent logs from one web interface.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dashboard exposes sensitive local OpenClaw and host controls through an unauthenticated network service.

Mitigation: Bind test deployments to localhost, add authentication before network exposure, and avoid exposing the service on LAN or ZeroTier until access is restricted.

Risk: The installers perform privileged setup and fetch remote installation scripts.

Mitigation: Do not run one-line installers as written; use a pinned, reviewed local install and make service persistence and ZeroTier installation explicit opt-in steps.

Risk: The dashboard can display token-related information.

Mitigation: Remove token display where possible, keep masking in place, and restrict dashboard access to trusted local users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chris6970barbarian-hue/skills/glitch-dashboard)
- [README](artifact/README.md)
- [Skill documentation](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe local dashboard setup, CLI usage, API endpoints, and operational status views.]

## Skill Version(s):

2026.2.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
