## Description:

Orchestrates multi-step VMware workflows across companion skills with human approval gates and explicit, best-effort rollback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use VMware Pilot to design and coordinate multi-step VMware operations across companion skills, review steps before risky actions, and request best-effort rollback when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workflow examples may allow infrastructure changes before approval, and some operations may be disruptive or incomplete.

Mitigation: Review the planned steps and approval order before execution, especially for production workflows; account for the incomplete scanner coverage when deciding whether to install.

## Reference(s):

- [Project homepage](https://github.com/vmware-skills/VMware-Pilot)
- [ClawHub release](https://clawhub.ai/zw008/skills/vmware-pilot)
- [Agent guardrails](references/agent-guardrails.md)
- [Integration patterns](references/integration-patterns.md)

## Skill Output:

**Output Type(s):** [Workflow plans, Guidance, Markdown, YAML configuration, Shell commands]

**Output Format:** [Structured workflow plans, Markdown guidance, YAML templates, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ordered steps may include approval gates and optional best-effort rollback metadata.]

## Skill Version(s):

2.5.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
