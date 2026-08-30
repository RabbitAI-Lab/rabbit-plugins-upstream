## Description:

vmware-harden helps agents perform VMware cyber compliance auditing, baseline checking, drift detection, and read-only compliance reporting for vSphere, ESXi, NSX, and related VMware environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Infrastructure, security, and compliance engineers use this skill to scan VMware estates against built-in or custom baselines, inspect violations and drift, and generate remediation guidance without directly modifying VMware resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports inconsistent documentation for a remediation apply path that can trigger real infrastructure changes through another tool.

Mitigation: Treat scan and report workflows as the intended safe path, restrict any apply workflow, and require explicit approval gates and scope before running remediation commands.

Risk: Optional LLM remediation advice can share compliance evidence externally when ANTHROPIC_API_KEY is configured.

Mitigation: Do not configure ANTHROPIC_API_KEY for sensitive estates unless external compliance-evidence sharing is approved.

Risk: Compliance results can be incomplete when collectors, privileges, or per-node coverage are missing.

Mitigation: Review the coverage fields before calling an environment compliant or clean, and re-scan after fixing missing collectors or access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-harden)
- [Publisher profile](https://clawhub.ai/user/zw008)
- [Project homepage](https://github.com/vmware-skills/VMware-Harden)
- [setup-guide.md](references/setup-guide.md)
- [cli-reference.md](references/cli-reference.md)
- [capabilities.md](references/capabilities.md)
- [agent-guardrails.md](references/agent-guardrails.md)
- [cross-skill-workflows.md](references/cross-skill-workflows.md)
- [stig-content-sync.md](references/stig-content-sync.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration notes, and references to JSON or text reports produced by the underlying tool.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may depend on local Twin DuckDB scan state, collector coverage, baseline selection, and optional LLM remediation advice.]

## Skill Version(s):

1.10.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
