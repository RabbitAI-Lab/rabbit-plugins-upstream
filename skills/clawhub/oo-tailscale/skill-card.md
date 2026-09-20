## Description:

Operates Tailscale tailnets through the OOMOL oo CLI for reading, creating, updating, and deleting Tailscale resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Tailscale tailnets through OOMOL-connected credentials, including device, user, DNS, policy, route, webhook, OAuth app, log, and posture integration workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes high-impact administrative actions that can change, revoke, suspend, delete, or overwrite Tailscale resources.

Mitigation: Require explicit approval for each write or destructive action, confirm the target and payload, and inspect the live action schema before execution.

Risk: Setup guidance includes installing or invoking the oo CLI before using the Tailscale connector.

Mitigation: Review the oo CLI installer source or use a verified installation path before running setup.

Risk: Some actions create, rotate, or return secrets such as auth keys, OAuth client secrets, and webhook signing secrets.

Mitigation: Run secret-returning actions only when requested, treat returned values as sensitive, and avoid storing or exposing them unnecessarily.

Risk: Policy, DNS, routing, user, and device changes can disrupt tailnet access or security posture.

Mitigation: Review proposed policy, DNS, route, user, and device changes with the user before applying them, especially for deletions, suspensions, and full replacements.

## Reference(s):

- [Tailscale homepage](https://tailscale.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tailscale)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions can return JSON data and execution metadata; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
