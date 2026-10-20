## Description:

Designs and coordinates multi-step VMware workflows with human approval checkpoints and explicit, best-effort rollback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

VMware operators and infrastructure engineers use this skill to plan, approve, run, and review multi-step workflows spanning virtual machines, networking, storage, and Kubernetes. It supports checkpointed changes, incident response, and explicit rollback rather than single-step operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workflows can make high-impact production changes or request credentials.

Mitigation: Limit use to authorized operators; use least-privilege companion accounts and read-only tools unless changes are required, and require explicit approval before sensitive steps.

Risk: Rollback is not automatic and may not reverse every completed change.

Mitigation: Review the rollback preview, verify affected systems, and invoke rollback explicitly when appropriate.

Risk: Local workflow, audit, baseline, and kubeconfig files can contain sensitive operational data.

Mitigation: Keep files under ~/.vmware owner-only and restrict access to the operator account.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-pilot)
- [Project homepage (listed in skill metadata)](https://github.com/vmware-skills/VMware-Pilot)
- [Setup guide](references/setup-guide.md)
- [Workflow design](references/workflow-design.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Guidance, Workflow plans, Shell commands, Configuration]

**Output Format:** [Markdown guidance and structured workflow steps, including YAML or JSON when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes approval checkpoints, workflow status, and explicit best-effort rollback guidance.]

## Skill Version(s):

2.4.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
