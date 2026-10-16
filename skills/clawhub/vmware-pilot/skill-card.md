## Description:

Coordinates multi-step VMware workflows across companion skills with human approval checkpoints and explicit, best-effort rollback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

VMware operators and infrastructure engineers use this skill to plan, review, and coordinate multi-step changes, incident response, and compliance checks across VMware companion skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Destructive VMware operations or credential-returning steps can affect production systems or expose access tokens.

Mitigation: Require explicit human approval for high-impact and credential-returning steps, and use least-privileged companion skill accounts; do not print tokens or kubeconfigs.

Risk: Workflow, audit, and baseline files may contain sensitive infrastructure details.

Mitigation: Keep local VMware workflow, audit, and baseline files owner-only and avoid sharing their contents in chat.

Risk: Rollback is best-effort and does not automatically undo agent-dispatched steps.

Mitigation: Review rollback plans before changes and explicitly reverse completed steps when necessary, verifying the target systems afterward.

## Reference(s):

- [ClawHub release](https://clawhub.ai/zw008/skills/vmware-pilot)
- [Project homepage (listed in skill metadata)](https://github.com/vmware-skills/VMware-Pilot)
- [Setup guide](artifact/references/setup-guide.md)
- [Workflow design](artifact/references/workflow-design.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with workflow steps, commands, and YAML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workflow plans include approval checkpoints and optional rollback actions; rollback requires explicit initiation.]

## Skill Version(s):

2.3.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
