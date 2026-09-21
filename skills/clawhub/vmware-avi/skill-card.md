## Description:

VMware AVI helps agents inspect and operate AVI/NSX ALB virtual services, pool members, SSL certificates, analytics, service engines, and AKO Kubernetes workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to diagnose and manage VMware AVI/NSX ALB load balancing and AKO Kubernetes application delivery tasks, including virtual service checks, pool member drain or restore, SSL expiry review, analytics, logs, ingress diagnostics, and sync drift analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect and potentially change AVI/NSX ALB and AKO/Kubernetes state.

Mitigation: Install it only for intended infrastructure operations, use least-privilege controller and kubeconfig credentials, and review blast-radius previews before approving writes.

Risk: Production controller passwords and kubeconfig access can expose sensitive infrastructure control paths.

Mitigation: Prefer a secret manager or runtime environment injection over storing production passwords in local .env files, and keep kubeconfig access scoped to the required clusters.

Risk: Write actions such as virtual service toggles, pool member changes, AKO restarts, sync force, and AKO configuration upgrades can affect live traffic.

Mitigation: Use the documented confirmation gates, audit logging, policy rules, and dry-run or preview behavior before applying changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-avi)
- [Project homepage](https://github.com/vmware-skills/VMware-AVI)
- [VMware AVI setup guide](references/setup-guide.md)
- [VMware AVI capabilities](references/capabilities.md)
- [VMware AVI CLI reference](references/cli-reference.md)
- [Operating vmware-avi with a local / small model](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with inline shell commands, configuration paths, diagnostic summaries, and action recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include blast-radius previews, audit guidance, and dry-run or confirmation steps for write operations.]

## Skill Version(s):

1.11.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
