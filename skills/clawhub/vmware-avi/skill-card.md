## Description:

Use this skill for VMware AVI/NSX Advanced Load Balancer and AKO Kubernetes operations, including virtual service management, pool member drain and restore, SSL certificate checks, analytics, service engine health, ingress diagnostics, and K8s-to-Controller sync troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and infrastructure operators use this skill to inspect and administer AVI Controller and AKO environments from an agent, with guided diagnostics and gated write operations for live load-balancing infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access powerful AVI and Kubernetes administration surfaces.

Mitigation: Run it with least-privilege AVI and Kubernetes accounts, and use read-only RBAC when only inspection is needed.

Risk: Mutable package or chart resolution can change what is installed or applied.

Mitigation: Pin the vmware-avi package version and AKO chart versions where possible.

Risk: Controller credentials may be exposed if stored in shell history or plaintext files.

Mitigation: Prefer a secret manager or ephemeral environment injection, and avoid committing or logging controller password values.

Risk: Write operations can affect live traffic, AKO pods, or Helm-managed configuration.

Mitigation: Use the documented dry-run, double-confirmation, audit, and policy controls before applying changes.

## Reference(s):

- [VMware AVI GitHub repository](https://github.com/vmware-skills/VMware-AVI)
- [VMware AVI Setup Guide](references/setup-guide.md)
- [VMware AVI Capabilities](references/capabilities.md)
- [VMware AVI CLI Reference](references/cli-reference.md)
- [Operating vmware-avi with a local / small model](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with CLI commands, configuration snippets, diagnostics, and operational recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live infrastructure observations from AVI Controller or Kubernetes tools when the agent has configured access.]

## Skill Version(s):

1.9.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
