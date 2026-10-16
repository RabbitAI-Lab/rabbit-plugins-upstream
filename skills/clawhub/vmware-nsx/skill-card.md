## Description:

Helps operators inspect and troubleshoot VMware NSX networking and make explicitly requested changes to segments, gateways, NAT, routing, and IP pools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network administrators and infrastructure engineers use this skill to inspect NSX networking and health, diagnose connectivity, and perform specifically requested network changes through NSX Manager.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network write actions can disrupt connectivity or change routing.

Mitigation: Allow administration only for authorized operators; prefer read-only access unless changes are needed, require an explicit user request for each write, and apply least-privilege accounts and environment-specific deny rules.

Risk: NSX credentials or connections could be exposed or intercepted.

Mitigation: Use a secret manager rather than long-lived passwords in .env, and keep TLS verification enabled with a trusted CA.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-nsx)
- [Project homepage listed in release metadata](https://github.com/vmware-skills/VMware-NSX)
- [Setup guide](artifact/references/setup-guide.md)
- [Capabilities](artifact/references/capabilities.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports NSX inventory, health, and change outcomes for the selected target.]

## Skill Version(s):

1.15.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
