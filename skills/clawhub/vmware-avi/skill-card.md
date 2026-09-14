## Description:

vmware-avi helps agents operate VMware AVI/NSX Advanced Load Balancer and AKO environments, including virtual services, pools, certificates, analytics, service engines, ingress diagnostics, sync checks, and guarded state changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inspect, troubleshoot, and safely manage VMware AVI Controller and AKO Kubernetes load-balancing workflows. It supports read-only diagnostics by default and gated write actions for operations such as virtual service toggles, pool member drains, AKO restarts, config upgrades, and sync force operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate against live VMware AVI and AKO environments, including traffic-affecting write operations.

Mitigation: Use least-privilege AVI and Kubernetes accounts, require explicit approval for writes, and keep production deny rules in vmware-policy.

Risk: AKO Helm upgrades and sync operations can alter load-balancing behavior in a live Kubernetes environment.

Mitigation: Use dry-run and diff workflows first, pin AKO chart versions for live upgrades, and apply changes only during approved maintenance windows.

Risk: Controller credentials may be configured through local environment files.

Mitigation: Prefer secret-manager injected passwords over persistent .env secrets and restrict local credential files to owner-only permissions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-avi)
- [Project Homepage](https://github.com/vmware-skills/VMware-AVI)
- [VMware AVI Capabilities](references/capabilities.md)
- [VMware AVI CLI Reference](references/cli-reference.md)
- [VMware AVI Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke CLI or MCP tools that return operational text, status summaries, logs, metrics, diffs, and configuration guidance.]

## Skill Version(s):

1.9.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
