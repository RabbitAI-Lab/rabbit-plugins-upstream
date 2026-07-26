## Description: <br>
Use this skill for VMware compliance auditing, baseline checking, drift detection, remediation suggestions, and reporting across vSphere, ESXi, and NSX environments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, platform engineers, and compliance operators use this skill to scan VMware estates against built-in or custom baselines, inspect violations and drift, and prepare remediation advice without directly changing managed VMware resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The remediation workflow may be mistaken for a reporting-only path even though evidence says it can hand changes to vmware-pilot. <br>
Mitigation: Use the skill for scans, reports, drift review, and advice; for reporting-only use, avoid vmware-harden apply and route any real changes through normal vmware-pilot approval review. <br>
Risk: Compliance evidence is stored locally and may contain sensitive posture details about VMware environments. <br>
Mitigation: Protect the configured Twin DuckDB path and review who can read generated reports, dashboard output, and audit logs. <br>
Risk: LLM remediation advice can be incomplete, generic, or wrong, especially when the optional Anthropic key is not configured. <br>
Mitigation: Treat remediation output as a proposal, verify it against the actual violation evidence, and require human review before any change is submitted. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-harden) <br>
- [Project Homepage](https://github.com/zw008/VMware-Harden) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [Capabilities](references/capabilities.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>
- [Cross-Skill Workflows](references/cross-skill-workflows.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and text or JSON report references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local Twin DuckDB state, MCP tool outputs, web dashboard views, and optional LLM remediation suggestions.] <br>

## Skill Version(s): <br>
1.8.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
