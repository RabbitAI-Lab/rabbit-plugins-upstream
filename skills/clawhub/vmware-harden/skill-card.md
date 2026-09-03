## Description:

vmware-harden helps agents run VMware cyber compliance scans, check baselines, detect drift, report violations, and generate remediation advice for vSphere, ESXi, and NSX environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security engineers, and infrastructure operators use this skill to audit VMware environments against built-in or custom compliance baselines, inspect drift, and produce remediation guidance. It is suited to point-in-time compliance reporting and agent-assisted investigation, while actual remediation is routed through approval-gated tooling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Compliance scan data and audit records may contain sensitive infrastructure posture details in local files.

Mitigation: Install only in environments where local VMware compliance data storage is acceptable, and protect the DuckDB and audit files with appropriate host and filesystem controls.

Risk: Optional LLM remediation advice can send remediation context outside the local environment when ANTHROPIC_API_KEY is configured.

Mitigation: Set ANTHROPIC_API_KEY only when external processing of remediation context is approved for the environment.

Risk: Remediation advice could be mistaken for an approved infrastructure change.

Mitigation: Treat advice as a proposal and use vmware-pilot approval gates for any actual remediation.

## Reference(s):

- [VMware Harden homepage](https://github.com/vmware-skills/VMware-Harden)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Cross-Skill Workflows](references/cross-skill-workflows.md)
- [vSphere 9 STIG Content Sync](references/stig-content-sync.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compliance findings, coverage caveats, drift summaries, remediation suggestions, CLI commands, and MCP configuration snippets.]

## Skill Version(s):

1.10.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
