## Description:

Helps operators inspect and manage VMware AVI load balancing and AKO Kubernetes ingress, including virtual services, pool members, certificates, analytics, and sync diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and developers use this skill to diagnose AVI/NSX ALB and AKO issues, check application delivery health, and perform approved load balancer or ingress changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-initiated changes to virtual services, pool members, or AKO can disrupt live traffic.

Mitigation: Use least-privilege accounts and production policy rules; review the blast-radius preview and require explicit approval before writes.

Risk: Controller credentials or Kubernetes access could be exposed or misused.

Mitigation: Avoid entering real passwords in shell commands and restrict controller and Kubernetes account permissions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-avi)
- [Project homepage (listed in skill metadata)](https://github.com/vmware-skills/VMware-AVI)
- [Setup guide](artifact/references/setup-guide.md)
- [Capabilities and compatibility](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report live infrastructure state or propose changes requiring operator review.]

## Skill Version(s):

2.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
