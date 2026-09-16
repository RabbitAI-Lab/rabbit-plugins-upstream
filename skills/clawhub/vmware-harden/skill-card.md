## Description:

vmware-harden helps agents run VMware compliance audits, baseline checks, drift detection, and remediation advice workflows for vSphere, ESXi, NSX, and related VMware environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, infrastructure engineers, security teams, and compliance operators use this skill to inspect VMware estates against built-in or custom baselines, review violations and coverage, investigate drift, and prepare human-reviewed remediation plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says the bundled docs under-declare an apply path that can trigger real infrastructure remediation through vmware-pilot.

Mitigation: Review the skill before production use, disable or avoid vmware-harden apply, and require explicit vmware-pilot approval for every remediation, especially NSX firewall or host configuration changes.

Risk: The local DuckDB may contain sensitive infrastructure posture data.

Mitigation: Protect the Twin DuckDB with local access controls and avoid publishing scan artifacts or compliance reports outside approved channels.

Risk: Advisor workflows may send selected violation context to Anthropic when ANTHROPIC_API_KEY is configured.

Mitigation: Use the advisor only for data approved for that provider, or leave ANTHROPIC_API_KEY unset to use local mock remediation suggestions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-harden)
- [Project homepage](https://github.com/vmware-skills/VMware-Harden)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Capabilities](references/capabilities.md)
- [Cross-Skill Workflows](references/cross-skill-workflows.md)
- [vSphere 9 STIG Content Sync](references/stig-content-sync.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration snippets, and structured compliance report references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces compliance findings, coverage caveats, drift analysis, remediation suggestions, dashboard setup guidance, and MCP or CLI operating instructions.]

## Skill Version(s):

1.10.10 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
