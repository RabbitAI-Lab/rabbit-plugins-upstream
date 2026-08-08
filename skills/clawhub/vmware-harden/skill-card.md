## Description:

VMware Harden helps agents run VMware cyber compliance scans, baseline checks, drift detection, remediation advice, and dashboard workflows for vSphere, ESXi, and NSX environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and security teams use this skill to audit VMware estates against compliance baselines, inspect drift, generate reports, and receive remediation guidance without directly modifying VMware resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized use could expose VMware compliance data or query environments the operator is not approved to assess.

Mitigation: Install and run the skill only in environments where the operator is authorized to query VMware compliance data, and use least-privilege upstream collector credentials.

Risk: The web dashboard can disclose local compliance findings if exposed beyond the intended host.

Mitigation: Keep the dashboard bound to localhost unless intentional exposure has been reviewed and approved.

Risk: Remediation advice or pilot workflows may lead to infrastructure changes if acted on without review.

Mitigation: Treat any apply or pilot workflow as a separate change action that requires human review and approval.

Risk: Optional LLM-driven advice may send structured violation evidence to Anthropic when ANTHROPIC_API_KEY is configured.

Mitigation: Set ANTHROPIC_API_KEY only when sharing structured violation evidence with Anthropic is acceptable for the deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-harden)
- [Project homepage](https://github.com/vmware-skills/VMware-Harden)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Capabilities](references/capabilities.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Cross-Skill Workflows](references/cross-skill-workflows.md)
- [vSphere 9 STIG content sync](references/stig-content-sync.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured command guidance, with optional JSON-oriented CLI and MCP outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include compliance findings, drift summaries, reports, remediation suggestions, dashboard launch commands, and configuration guidance.]

## Skill Version(s):

1.8.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
