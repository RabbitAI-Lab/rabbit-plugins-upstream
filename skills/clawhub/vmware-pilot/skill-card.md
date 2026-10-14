## Description:

Coordinates multi-step VMware workflows across companion skills with human approval gates, checkpoints, and explicit best-effort rollback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and engineers use this skill to plan and coordinate VMware maintenance, incident response, and other multi-step changes across companion tools, pausing for human approval before sensitive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Coordinated steps can change production VMware infrastructure.

Mitigation: Review generated workflows before execution, use least-privilege companion credentials, and require human approval for sensitive changes.

Risk: Rollback is explicit and best-effort, so some changes may remain applied after failure.

Mitigation: Inspect workflow status and affected systems before invoking rollback; verify any remaining changes manually.

Risk: Kubeconfigs, workflow state, audit logs, and saved baselines may contain sensitive data.

Mitigation: Restrict access to these local files and handle retained records as sensitive information.

## Reference(s):

- [Project homepage (listed in release metadata)](https://github.com/vmware-skills/VMware-Pilot)
- [Setup guide](references/setup-guide.md)
- [Workflow design](references/workflow-design.md)
- [Integration patterns](references/integration-patterns.md)

## Skill Output:

**Output Type(s):** [Workflow plans, Configuration, Guidance]

**Output Format:** [Markdown and YAML workflow instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes approval checkpoints and explicit rollback steps where applicable.]

## Skill Version(s):

1.12.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
