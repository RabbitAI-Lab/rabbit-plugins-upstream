## Description:

VMware AVI helps agents inspect and operate VMware AVI/NSX ALB and AKO environments, including virtual services, pool members, SSL certificates, analytics, service engines, AKO health, Helm configuration, ingress diagnostics, sync checks, and multi-cluster status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use this skill to administer and troubleshoot AVI Controller and AKO Kubernetes load-balancing environments. It supports read-only inspection, diagnostics, configuration review, and approved state-changing maintenance actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform state-changing operations that affect live load-balancing or AKO behavior.

Mitigation: Use least-privilege or read-only accounts by default, and carefully review confirmed writes such as VS disable, pool drain, AKO restart, Helm upgrade, and force resync.

Risk: Disabling TLS verification can weaken controller connection security.

Mitigation: Keep TLS verification enabled in production and prefer trusted CA configuration over curl -k or verify_ssl: false.

Risk: Controller credentials can be exposed if local secret files are readable or committed.

Mitigation: Keep .env permissions restricted, avoid committing secrets, and prefer a secret manager for production credentials.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-avi)
- [Project Homepage](https://github.com/vmware-skills/VMware-AVI)
- [VMware AVI Capabilities](references/capabilities.md)
- [VMware AVI CLI Reference](references/cli-reference.md)
- [VMware AVI Setup Guide](references/setup-guide.md)
- [Operating vmware-avi with a local / small model](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, command output summaries, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or execute operational commands for AVI and AKO environments; state-changing actions require explicit confirmation and audit logging.]

## Skill Version(s):

1.8.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
