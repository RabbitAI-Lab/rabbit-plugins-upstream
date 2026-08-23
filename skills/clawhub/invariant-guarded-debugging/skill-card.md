## Description:

Guard diagnosis and repair with falsifiable hypotheses, executable invariants, verified guard integrity, semantic boundaries, state-drift checks, rollback, adversarial checks, and trajectory resets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pinguy](https://clawhub.ai/user/pinguy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill when debugging or repairing systems where known-good components, user constraints, or live state must be protected. It guides diagnosis through falsifiable hypotheses, executable invariants, guard validation, rollback, and trajectory resets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can cause an agent to spend more time gathering evidence or running verification commands around live services, databases, or APIs.

Mitigation: Use it for risky debugging or repair work where protected state matters, and keep verification commands scoped to the relevant target.

Risk: If required invariants, guard integrity, or rollback evidence cannot be established, the skill may direct the agent to stop rather than continue a repair.

Mitigation: Prepare observable acceptance checks, rollback material, and explicit protected-target boundaries before applying it to high-risk work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pinguy/skills/invariant-guarded-debugging)
- [Server-resolved GitHub provenance](https://github.com/pinguy/Skills/tree/main/skills/invariant-guarded-debugging)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with checklists, report templates, and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
