## Description:

vmware-harden helps agents perform VMware cyber compliance auditing, baseline checking, drift detection, remediation advice, and dashboard-guided review for vSphere, ESXi, NSX, and related environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and infrastructure engineers use this skill to scan VMware estates against built-in or custom compliance baselines, inspect violations and drift, and generate remediation guidance without directly modifying managed VMware resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags conflicting documentation about whether the skill only suggests fixes or can initiate remediation workflows through vmware-pilot.

Mitigation: Use the skill for scans, reports, drift, and advice by default; only allow apply or pilot-backed workflows after explicit authorization and review of approval gates.

Risk: Local scan results, audit records, and compliance evidence may contain sensitive infrastructure details.

Mitigation: Protect the local DuckDB and audit files and restrict access to systems where the skill is installed.

Risk: Optional LLM-backed remediation advice can send violation evidence outside the local environment when an API key is configured.

Mitigation: Leave `ANTHROPIC_API_KEY` unset when violation evidence must remain fully local.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-harden)
- [ClawHub publisher profile](https://clawhub.ai/user/zw008)
- [Source homepage from ClawHub metadata](https://github.com/vmware-skills/VMware-Harden)
- [Agent guardrails](references/agent-guardrails.md)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Cross-skill workflows](references/cross-skill-workflows.md)
- [Setup guide](references/setup-guide.md)
- [vSphere 9 STIG content sync](references/stig-content-sync.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON snippets, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compliance scan summaries, baseline and violation listings, drift analysis, remediation suggestions, and setup guidance.]

## Skill Version(s):

1.11.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
