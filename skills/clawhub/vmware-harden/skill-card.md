## Description: <br>
Use this skill for VMware compliance auditing, baseline checking, and drift detection across vSphere, ESXi, and NSX environments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, platform engineers, and compliance operators use this skill to run VMware-focused compliance scans, inspect violations and drift, manage custom baselines, and generate remediation advice for human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Referenced documentation describes an apply path that can initiate real remediation even though the skill is presented as read-only or advice-only. <br>
Mitigation: Use local policy to prevent agents from invoking apply or vmware-pilot remediation unless explicit human approval and audit review are in place. <br>


## Reference(s): <br>
- [VMware Harden homepage](https://github.com/vmware-skills/VMware-Harden) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Capabilities](references/capabilities.md) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [Cross-Skill Workflows](references/cross-skill-workflows.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include compliance findings, drift summaries, baseline guidance, remediation suggestions, and dashboard or MCP setup instructions.] <br>

## Skill Version(s): <br>
1.8.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
