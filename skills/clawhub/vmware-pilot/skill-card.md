## Description: <br>
Designs, tracks, and gates multi-step VMware workflows across companion skills with human approvals, audited state, and rollback support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure engineers use this skill to plan and manage VMware incident response, maintenance, deployment, compliance, and change workflows that span companion VMware skills. It is intended for multi-step work that needs review checkpoints, workflow state, and recovery planning rather than single one-off VMware operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-impact infrastructure workflows may make changes through companion VMware skills. <br>
Mitigation: Require explicit human review before running custom templates or continuing through approval gates, and use companion-skill RBAC and policy controls for read/write authorization. <br>
Risk: Rollback is best-effort and may not restore every failed or partially completed operation. <br>
Mitigation: Treat rollback as recovery assistance, verify each plan before execution, and validate post-change infrastructure state with monitoring checks. <br>
Risk: Workflow, audit, and baseline files under ~/.vmware may contain operationally sensitive infrastructure details. <br>
Mitigation: Restrict filesystem access to ~/.vmware files and protect audit, workflow, and baseline data as sensitive operational records. <br>
Risk: Kubeconfig or guest credentials surfaced by companion workflows can be secrets even when associated operations are described as read-only. <br>
Mitigation: Handle kubeconfig and guest credential material as secrets and avoid exposing them in shared prompts, logs, or reports. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-pilot) <br>
- [Publisher Profile](https://clawhub.ai/user/zw008) <br>
- [Homepage](https://github.com/zw008/VMware-Pilot) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [Built-in Templates Reference](references/templates.md) <br>
- [Cross-Skill Integration Patterns](references/integration-patterns.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Workflow Design Guide](references/workflow-design.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>
- [Capabilities](references/capabilities.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured MCP workflow instructions with inline shell commands and YAML configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce workflow plans, approval prompts, rollback guidance, audit queries, and custom workflow template snippets.] <br>

## Skill Version(s): <br>
1.8.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
