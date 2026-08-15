## Description:

Operate Tailscale tailnets through the OOMOL-connected tailscale connector using the oo CLI for reading, creating, updating, and deleting tailnet data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, administrators, and operations teams use this skill to inspect and administer a Tailscale tailnet through OOMOL-connected actions. It covers device, user, DNS, policy, key, OAuth app, webhook, service, posture, and log-streaming workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connected Tailscale account may have administrative authority over tailnet users, devices, DNS, keys, webhooks, policies, secrets, and external event delivery.

Mitigation: Use the skill only where delegating tailnet administration through OOMOL is acceptable, and require explicit confirmation before any action that can change those resources.

Risk: The security summary reports that some high-impact actions may be untagged even though the skill allows untagged actions to run directly.

Mitigation: Treat untagged actions that affect users, devices, DNS, keys, webhooks, policy, secrets, or external events as state-changing and confirm the exact target, payload, and effect before execution.

Risk: Some actions can return credentials or secrets, including auth keys, OAuth client secrets, webhook signing secrets, or posture integration credentials.

Mitigation: Handle returned secrets as sensitive output, avoid unnecessary persistence or redistribution, and rotate or revoke credentials if they are exposed.

## Reference(s):

- [ClawHub Tailscale Skill](https://clawhub.ai/oomol/skills/oo-tailscale)
- [Tailscale Homepage](https://tailscale.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live connector schemas before execution and returns connector responses as JSON when actions are run.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
