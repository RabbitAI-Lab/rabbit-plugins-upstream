## Description:

A design-first agent workflow for software and skill development that gates coding behind requirement clarification, critical self-checks, task planning, sub-agent review, and verification evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[muippt](https://clawhub.ai/user/muippt)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to structure coding, bug-fixing, refactoring, and skill-authoring work so agents clarify intent, propose reviewed designs, execute scoped plans, and verify results before delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow is gate-heavy and may slow down tasks where the user expects a lightweight or explicitly invoked process.

Mitigation: Install it only when the desired agent behavior includes clarification, design confirmation, and verification gates before delivery.

Risk: Broad triggers for development, implementation, and skill work can change an agent's normal response style across many coding tasks.

Mitigation: Review the trigger scope and Chinese-first workflow instructions before deployment, especially in environments that prefer lighter workflows.

Risk: Proposal or code changes may still contain incorrect guidance even after the workflow's self-check and review stages.

Mitigation: Review outputs and scan skill changes before deployment; require concrete verification evidence for delivered work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/muippt/skills/mu-dev-workflow)
- [mu-dev-workflow landing page](https://muippt.github.io/mu-dev-workflow/)
- [Superpowers inspiration](https://github.com/obra/superpowers)
- [Architecture patterns](references/architecture-patterns.md)
- [Anti-rationalization](references/anti-rationalization.md)
- [Subagent review templates](references/subagent-review-templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with design documents, implementation plans, review notes, command output, and file changes when coding is requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pure Markdown workflow skill with no runtime dependencies]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter and changelog state 2.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
