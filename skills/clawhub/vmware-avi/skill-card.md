## Description:

Helps operators inspect and manage AVI load balancing and AKO Kubernetes ingress, including virtual services, pool members, certificates, diagnostics, and configuration changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and developers use this skill to diagnose AVI Controller and AKO ingress issues, monitor application delivery, and perform approved traffic or AKO configuration changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Controller credentials and Kubernetes access may expose sensitive infrastructure.

Mitigation: Use least-privilege AVI accounts and kubeconfig; inject secrets from a secret manager when possible and restrict .env permissions to 600.

Risk: Changing virtual services, pool members, or AKO deployments can disrupt live traffic.

Mitigation: Review change previews and blast radius, then obtain explicit user approval before traffic-affecting or AKO write actions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-avi)
- [Project homepage listed in skill metadata](https://github.com/vmware-skills/VMware-AVI)
- [Setup guide](artifact/references/setup-guide.md)
- [Capabilities](artifact/references/capabilities.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operational status, diagnostics, and previews of proposed changes when applicable.]

## Skill Version(s):

2.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
