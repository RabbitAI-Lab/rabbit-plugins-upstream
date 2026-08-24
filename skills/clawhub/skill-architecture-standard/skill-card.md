## Description:

Defines a mandatory OpenClaw skill architecture checklist for creating, reviewing, and upgrading agent skills, covering triggers, context, decision policy, verification, recovery, security, evaluation, observability, versioning, compatibility, knowledge sources, and exit conditions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill reviewers use this skill as an architecture standard when creating, reviewing, or upgrading OpenClaw agent skills. It helps structure skill instructions around activation, context handling, decision policy, tool use, verification, recovery, security, evaluation, and exit conditions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill claims mandatory authority over all OpenClaw skill creation and upgrades without trusted platform provenance.

Mitigation: Treat the standard as the publisher's policy unless ClawHub or OpenClaw governance independently confirms that it is authoritative.

Risk: Evaluation or observability guidance could influence agents to emit operational traces without a clearly defined destination or retention policy.

Mitigation: Review any evaluation or observability integration before use, and only enable trace emission when destination, retention, and secret-redaction behavior are known.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/skill-architecture-standard)
- [ClawHub publisher profile](https://clawhub.ai/user/pmuhammadagus-byte)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration]

**Output Format:** [Markdown guidance and structured checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Applies policy-style review criteria to skill authoring and upgrade work.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
