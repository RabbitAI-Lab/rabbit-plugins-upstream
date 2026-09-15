## Description:

VMware AVI helps agents operate AVI and NSX Advanced Load Balancer application delivery plus AKO Kubernetes environments, including virtual services, pool members, SSL certificates, analytics, service engines, ingress diagnostics, sync checks, and multi-cluster views.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and operations teams use this skill to inspect and manage AVI Controller load-balancing resources and AKO Kubernetes integrations. It supports troubleshooting, certificate expiry review, traffic-drain workflows, Helm configuration review, and K8s-to-Controller sync diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive AVI Controller and AKO environments, including operations that affect live traffic.

Mitigation: Install it only for agents and operators that should manage those environments, use least-privileged controller and Kubernetes accounts, and keep policy and audit settings enabled before allowing write operations.

Risk: Controller credentials and Kubernetes access can expose privileged infrastructure control if stored or mounted carelessly.

Mitigation: Prefer secret-manager injected passwords over .env storage, protect kubeconfig access, and keep local credential files out of version control.

Risk: AKO Helm upgrades, pod restarts, forced syncs, virtual service disables, and pool-member drains can interrupt routing or application delivery.

Mitigation: Review diffs and current health first, pin AKO chart versions before upgrades, use dry-run where available, and require explicit approval for write operations.

Risk: Disabling TLS verification outside lab environments weakens controller connection security.

Mitigation: Keep TLS verification enabled for production and use valid controller certificates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-avi)
- [Project homepage](https://github.com/vmware-skills/VMware-AVI)
- [VMware AVI Setup Guide](artifact/references/setup-guide.md)
- [VMware AVI Capabilities](artifact/references/capabilities.md)
- [VMware AVI CLI Reference](artifact/references/cli-reference.md)
- [Operating vmware-avi with a local / small model](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown with inline shell commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce CLI or MCP-oriented instructions for read-only diagnostics and approval-gated write operations.]

## Skill Version(s):

1.9.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
