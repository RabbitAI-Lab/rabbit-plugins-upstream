## Description:

fabric-aiops helps agents inspect and operate controller-managed network fabrics across Meraki, Catalyst Center, CloudVision, and UniFi with health analyses, guided remediation commands, audit logging, dry-run previews, and undo support where available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network engineers, operators, and agents use this skill to review fabric health, inspect controller inventory, diagnose uplink and configuration drift issues, and stage guarded remediation for supported controller-managed networks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform production-impacting controller writes without an in-skill approval or read-only gate.

Mitigation: Use read-only controller credentials by default, expose write-capable credentials only to supervised sessions, and require an external approval process for write-capable MCP use.

Risk: Remediation actions may affect live network devices, VLANs, template bindings, or device membership.

Mitigation: Prefer dry-run previews, confirm target identifiers against controller state, and use the recorded undo path only after checking that the inverse action is appropriate.

Risk: The artifact states that live controller verification has not yet been completed.

Mitigation: Treat first use on each controller platform as a staged rollout with low-privilege credentials, non-production targets where possible, and post-action validation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/fabric-aiops)
- [Project homepage](https://github.com/AIops-tools/Fabric-AIops)
- [fabric-aiops capabilities](references/capabilities.md)
- [fabric-aiops CLI reference](references/cli-reference.md)
- [fabric-aiops setup & security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run remediation steps, controller health analysis, audit or undo guidance, and configuration setup instructions.]

## Skill Version(s):

0.11.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
