## Description:

Guides an agent to load a written implementation plan, review it critically, execute tasks sequentially without subagents, verify each step, and stop for help when blocked.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill when an agent must execute a prewritten implementation plan step by step in the current session, with verification at each step and stop-and-ask behavior for blockers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A written plan may include destructive commands, production changes, credential handling, or broad file operations.

Mitigation: Review the plan before execution and stop for human confirmation when the plan is unclear or high risk.

Risk: Manual verification can be misreported or skipped, allowing incomplete work to continue.

Mitigation: Require each step's verification to pass before advancing, and record deviations instead of claiming success.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/executing-plans)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown guidance with optional shell command interaction]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May pause for user confirmation before continuing when blockers, unclear instructions, or verification failures occur.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter and _meta.json report 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
