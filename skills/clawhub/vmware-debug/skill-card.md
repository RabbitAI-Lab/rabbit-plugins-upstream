## Description:

Correlates VMware and vSphere incident evidence into timelines, ranked root-cause hypotheses, and recommended next checks without changing VMware systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and engineers use this skill to investigate VMware, vSphere, ESXi, and NSX incidents, correlate collected events, track case evidence, and plan next checks. Remediation is handed to separate tools rather than executed by this skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Case evidence can contain hostnames, IP addresses, and log text and persists locally after case closure.

Mitigation: Choose a protected case-storage location and retention period before use; exclude credentials and delete old case folders when no longer needed.

Risk: Exposing the MCP server over HTTP or HTTPS can make diagnostic data and case-write tools reachable by network callers.

Mitigation: Use tokens, TLS, and host/origin restrictions; prefer read-only access unless operators need case-write tools.

## Reference(s):

- [Project homepage (ClawHub metadata)](https://github.com/vmware-skills/VMware-Debug)
- [Agent guardrails](references/agent-guardrails.md)
- [Event envelope](references/event-envelope.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, JSON]

**Output Format:** [Markdown diagnosis and local case records; structured JSON for event correlation and next checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Case records remain on disk until manually removed; no VMware remediation is performed.]

## Skill Version(s):

2.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
