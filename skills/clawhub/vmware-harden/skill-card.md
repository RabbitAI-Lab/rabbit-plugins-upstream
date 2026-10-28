## Description:

Helps agents audit VMware compliance baselines, identify known vulnerabilities and configuration drift, and suggest remediations without applying changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure and security teams use this skill to assess vSphere, ESXi, and NSX compliance, review vulnerability exposure and drift, and plan remediation. It offers point-in-time scans and advice rather than applying changes to VMware systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scan data and reports reveal sensitive infrastructure security posture.

Mitigation: Restrict access to the local Twin database, reports, dashboard, and MCP responses; use a read-only, narrowly scoped VMware collection account.

Risk: Exposing the dashboard or MCP server beyond localhost can disclose sensitive findings.

Mitigation: Keep services bound to localhost unless protected with TLS, rotating tokens, roles, firewall rules, and audit review.

Risk: Optional AI-generated advice can transmit violation evidence outside the environment.

Mitigation: Do not configure ANTHROPIC_API_KEY when violation evidence must remain inside the environment.

## Reference(s):

- [VMware Harden project homepage (release metadata; not verified provenance)](https://github.com/vmware-skills/VMware-Harden)
- [Setup guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with scan findings and suggested commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include baseline coverage, violations, drift, and remediation suggestions; findings depend on completed scans.]

## Skill Version(s):

1.17.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
