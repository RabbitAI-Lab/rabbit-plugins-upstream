## Description:

Designs and coordinates multi-step VMware workflows with human approval gates and explicit, best-effort rollback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

VMware administrators and platform engineers use this skill to plan and coordinate multi-step operations across companion VMware skills, including incident response, maintenance, and deployments. It is intended for workflows that need approval checkpoints or rollback planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network setup instructions may place approval after network or firewall changes.

Mitigation: Require approval before the first network or firewall change, and review the targets and parameters.

Risk: Rollback is explicit and best-effort, and may require manual recovery.

Mitigation: Use narrowly privileged companion accounts, protect stored inventory and credentials, and plan manual recovery before production use.

## Reference(s):

- [Workflow design guide](references/workflow-design.md)
- [Agent guardrails](references/agent-guardrails.md)
- [Integration patterns and dispatch contract](references/integration-patterns.md)
- [Workflow templates](references/templates.md)
- [VMware Pilot homepage listed in ClawHub metadata](https://github.com/vmware-skills/VMware-Pilot)
- [ClawHub release page](https://clawhub.ai/zw008/skills/vmware-pilot)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance, shell commands]

**Output Format:** [Markdown workflow plans and YAML workflow templates, with explanatory text and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include approval checkpoints, execution steps, and best-effort rollback guidance.]

## Skill Version(s):

2.4.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
