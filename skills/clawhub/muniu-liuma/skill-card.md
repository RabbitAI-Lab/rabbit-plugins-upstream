## Description:

Src is a specification-driven development toolkit that helps agents choose and apply five step-focused skills for writing specs, designing architecture, planning tasks, generating implementation guidance, and auditing delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[timeaground](https://clawhub.ai/user/timeaground)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this toolkit to move from requirements to architecture, task breakdown, implementation guidance, and delivery audit while preserving explicit handoff checks between steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The spec-writer skill declares WebFetch while its resource manifest says network access is none, which may conflict with strict no-network deployment policy.

Mitigation: Review or fix the WebFetch/resource manifest mismatch before deployment, and disable web fetching unless the deployment explicitly permits it.

Risk: Short or broad trigger phrases could cause an agent to activate a planning or audit skill when the user intent is ambiguous.

Mitigation: Require explicit user intent for activation or tighten trigger phrases in environments where skills auto-activate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/timeaground/skills/muniu-liuma)
- [Toolkit overview](artifact/SKILL.md)
- [Test skeleton specification](artifact/TEST-SKELETON-SPEC.md)
- [spec-writer skill](artifact/skills/spec-writer/SKILL.md)
- [arch-designer skill](artifact/skills/arch-designer/SKILL.md)
- [task-planner skill](artifact/skills/task-planner/SKILL.md)
- [impl-guide skill](artifact/skills/impl-guide/SKILL.md)
- [audit-trace skill](artifact/skills/audit-trace/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown by default, with optional JSON or CSV for structured step outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Step outputs may include context-check markers; implementation guidance may include executable test skeletons but not business implementation code.]

## Skill Version(s):

1.2.0 (source: server release metadata and root SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
