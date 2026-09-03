## Description:

vmware-pilot designs, tracks, and gates multi-step VMware workflows across companion skills with approval checkpoints, audit logging, and rollback support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use vmware-pilot to plan and coordinate multi-step VMware change, incident response, maintenance, and baseline workflows that require review before high-impact actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can coordinate high-impact VMware infrastructure workflows through companion skills.

Mitigation: Require explicit approval before any production-changing companion skill call and review plans before execution.

Risk: Rollback behavior may be manual and best-effort for some workflows.

Mitigation: Confirm rollback coverage before production use and keep an operator-approved recovery plan for each workflow.

Risk: Workflow, audit, baseline, and kubeconfig-related data can contain sensitive operational information.

Mitigation: Avoid printing kubeconfig contents in chat or logs and protect ~/.vmware workflow, audit, and baseline files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-pilot)
- [VMware Pilot homepage](https://github.com/vmware-skills/VMware-Pilot)
- [Setup Guide - vmware-pilot](artifact/references/setup-guide.md)
- [CLI Reference - vmware-pilot](artifact/references/cli-reference.md)
- [Capabilities - vmware-pilot](artifact/references/capabilities.md)
- [Cross-Skill Integration Patterns](artifact/references/integration-patterns.md)
- [Workflow Design Guide](artifact/references/workflow-design.md)
- [Built-in Templates Reference](artifact/references/templates.md)
- [Operating vmware-pilot with a local / small model](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [MCP-first workflow plans and state transitions; companion skills execute infrastructure steps.]

## Skill Version(s):

1.8.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
