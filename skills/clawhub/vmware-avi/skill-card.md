## Description:

VMware AVI helps agents administer NSX Advanced Load Balancer and AKO environments, including virtual services, pool members, SSL expiry, analytics, service engines, ingress diagnostics, Helm configuration, and Kubernetes-to-Controller sync checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and operations teams use this skill to inspect and manage VMware AVI Controller and AKO Kubernetes load-balancing resources. It supports troubleshooting, certificate audits, pool member maintenance, ingress diagnostics, service engine health checks, and guarded changes that may affect traffic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can administer live AVI/NSX ALB and AKO resources, including operations that may affect application traffic.

Mitigation: Install it only in environments where that administration is intended, use least-privilege AVI and Kubernetes accounts, and require review of write previews before approval.

Risk: Controller and Kubernetes credentials may be exposed if stored or shared carelessly.

Mitigation: Prefer secret-manager or session environment injection, keep `.env` permissions at chmod 600, and avoid committing credentials to source control.

Risk: Destructive or disruptive operations such as virtual service disablement, pool member drain, AKO restart, AKO sync force, or Helm upgrade can interrupt traffic.

Mitigation: Use the built-in blast-radius preview or dry-run behavior first, confirm blockers are absent, and approve state-changing commands only after reviewing the affected resources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-avi)
- [Project homepage](https://github.com/vmware-skills/VMware-AVI)
- [VMware AVI capabilities](references/capabilities.md)
- [VMware AVI setup guide](references/setup-guide.md)
- [VMware AVI CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tool-selection guidance, blast-radius review prompts, diagnostics summaries, and configuration steps.]

## Skill Version(s):

1.10.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
