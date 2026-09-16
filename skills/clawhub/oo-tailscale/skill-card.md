## Description:

Operate Tailscale through OOMOL-connected account actions for reading, creating, updating, and deleting tailnet resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and administrators use this skill to manage Tailscale tailnet devices, users, keys, webhooks, DNS, policy files, posture integrations, services, and account settings through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute unreviewed code.

Mitigation: Install the oo CLI through a verified method instead of letting an agent run the remote installer commands as written.

Risk: Some state-changing actions may be mislabeled or lack write and destructive tags.

Mitigation: Require explicit confirmation before any action affecting users, secrets, webhooks, devices, DNS, policy, or account settings.

Risk: Some actions can return secrets or sensitive tailnet configuration.

Mitigation: Treat returned keys, OAuth credentials, webhook secrets, and logging configuration as sensitive and avoid unnecessary display or persistence.

## Reference(s):

- [Tailscale homepage](https://tailscale.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tailscale)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include connector result JSON and should protect returned secrets or sensitive configuration.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
