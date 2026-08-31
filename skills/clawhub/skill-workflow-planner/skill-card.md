## Description:

Use when the user explicitly asks for help planning the sequence of several OpenClaw skills, producing a written plan with ordered steps rather than running them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineers, and OpenClaw users use this skill to plan multi-skill workflows, order dependencies, flag steps that need approval, and define lightweight verification checks before any action is taken.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated plans may include steps involving credentials, destructive changes, system configuration, or external skill installation.

Mitigation: Review each generated plan before approving real action, and require explicit approval for sensitive or high-impact steps.

Risk: A written workflow plan can be misapplied if environment details or dependencies are wrong.

Mitigation: Verify operating system, architecture, runtime, tool versions, dependencies, and success conditions before acting on the plan.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/skill-workflow-planner)
- [ClawHub publisher profile](https://clawhub.ai/user/pmuhammadagus-byte)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown checklist or ordered plan]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Planning-only output; execution remains with the user or agent after explicit approval.]

## Skill Version(s):

1.1.4 (source: frontmatter, evidence release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
