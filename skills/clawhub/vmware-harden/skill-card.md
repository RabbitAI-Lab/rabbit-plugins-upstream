## Description:

VMware Harden helps agents perform VMware cyber compliance auditing, baseline checks, drift detection, and remediation guidance for vSphere, ESXi, and NSX environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, infrastructure engineers, and security teams use this skill to scan VMware estates against CIS, vSphere SCG, STIG-aligned, Dengbao, PCI-DSS, BSI IT-Grundschutz, EU NIS2, or custom YAML baselines. It supports point-in-time compliance reporting, drift review, and remediation advice without directly modifying managed VMware resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security verdict is suspicious because the documentation inconsistently describes a path that can start real infrastructure changes through another tool.

Mitigation: Review the skill before installation, and do not use documented apply or remediation paths unless vmware-pilot approvals, tool allowlists, rollback, and audit logging are configured and tested.

Risk: Compliance scans and remediation advice can expose sensitive infrastructure state in the local Twin DB or through optional live Anthropic advice requests.

Mitigation: Treat the Twin DB as sensitive, review what evidence may be stored or shared, and avoid live Anthropic advice unless external sharing of violation evidence is acceptable.

Risk: The scanner depends on configured sibling skills and external package or source resolution, which can affect installation integrity and scan completeness.

Mitigation: Pin and verify the external package or source, install the documented collectors extra, and inspect coverage fields before reporting an estate as compliant or clean.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-harden)
- [VMware Harden homepage](https://github.com/vmware-skills/VMware-Harden)
- [Setup Guide](references/setup-guide.md)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Cross-Skill Workflows](references/cross-skill-workflows.md)
- [vSphere 9 STIG content sync](references/stig-content-sync.md)
- [Operating vmware-harden with a local / small model](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline shell commands, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compliance coverage summaries, drift findings, remediation advice, and local setup steps.]

## Skill Version(s):

1.10.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
