## Description:

VMware Harden helps agents run VMware cyber-compliance scans, baseline checks, drift detection, and remediation-advice workflows across vSphere, ESXi, and NSX environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and security operators use this skill to scan VMware estates against supported compliance baselines, inspect drift, and produce remediation guidance without directly changing managed infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documentation conflicts about whether remediation can be initiated from this skill.

Mitigation: Review the installed CLI before production use and do not run or enable any apply workflow unless approved infrastructure changes through vmware-pilot are intended.

Risk: A web dashboard or upstream VMware credentials could expose sensitive operational information if broadly accessible.

Mitigation: Keep the dashboard bound to localhost or trusted access controls, and use least-privilege credentials in the upstream VMware collector skills.

Risk: Partial scan coverage can be mistaken for a clean compliance result.

Mitigation: Report coverage fields with every result and avoid calling an estate compliant when rules are undetermined or coverage tracking is absent.

Risk: Optional LLM remediation advice may be generic or depend on external API configuration.

Mitigation: Treat remediation output as a proposal, disclose when the advisor uses a mock fallback, and require human review before routing execution to another skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-harden)
- [Homepage](https://github.com/vmware-skills/VMware-Harden)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Capabilities](references/capabilities.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [STIG Content Sync](references/stig-content-sync.md)
- [Cross-Skill Workflows](references/cross-skill-workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline shell commands, configuration snippets, and optional JSON report guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local DuckDB scan state, custom YAML baselines, and optional LLM-generated remediation suggestions.]

## Skill Version(s):

1.9.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
