## Description:

Helps operators inspect, troubleshoot, and manage OPNsense and pfSense firewalls through CLI and MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network operators and administrators use this skill to assess firewall health, investigate rules and blocked traffic, and make controlled changes to OPNsense or pfSense appliances.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP write tools can change live firewall behavior or interrupt service without a built-in approval or read-only gate.

Mitigation: Use a read-only firewall API account by default; grant write access only during controlled maintenance and require explicit approval before disruptive operations.

Risk: Applying rules, restarting services, killing states, or rebooting can cause outages or management lockout.

Mitigation: Preview changes, confirm the intended target and management access, and arrange a recovery path before committing or rebooting.

Risk: Exposed firewall credentials or master passwords can enable unauthorized administration.

Mitigation: Protect the local secrets directory, avoid long-lived master passwords in shared environments, and migrate legacy plaintext secret variables.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/firewall-aiops)
- [Project homepage (listed in skill metadata; import provenance unavailable)](https://github.com/AIops-tools/Firewall-AIops)
- [Capabilities](references/capabilities.md)
- [Setup and security guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Text or Markdown with command examples and structured firewall findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live firewall diagnostics and proposed or executed changes; verify target and impact before acting.]

## Skill Version(s):

0.15.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
