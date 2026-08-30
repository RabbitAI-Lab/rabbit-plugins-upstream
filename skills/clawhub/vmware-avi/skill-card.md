## Description:

VMware AVI helps agents operate AVI/NSX Advanced Load Balancer and AKO Kubernetes environments, including virtual services, pool members, SSL expiry checks, analytics, service engine health, ingress diagnostics, and controller sync troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform operators use this skill to inspect and administer VMware AVI load balancing and AKO Kubernetes application delivery workflows, including troubleshooting ingress issues, certificate expiry, pool member maintenance, and controller drift.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate against AVI Controller and Kubernetes AKO environments where write actions may affect live traffic or controller state.

Mitigation: Install only where the agent should have that access, prefer least-privilege or read-only accounts, and require approvals for state-changing operations.

Risk: Controller credentials and kubeconfig access can expose sensitive infrastructure access if handled casually.

Mitigation: Avoid entering real passwords in shell commands, keep ~/.vmware-avi/.env chmod 600, and use a secret manager for production environments.

Risk: Disabling TLS verification can hide connection interception or misconfiguration.

Mitigation: Keep TLS verification enabled for production and disable it only for temporary lab troubleshooting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-avi)
- [VMware AVI homepage](https://github.com/vmware-skills/VMware-AVI)
- [Setup guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Capabilities](references/capabilities.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline CLI commands and operational recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or execute read and write operations against AVI Controller and AKO environments when configured with appropriate tools and credentials.]

## Skill Version(s):

1.8.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
