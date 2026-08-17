## Description:

Goal Runner orchestrates roadmap or checkbox task files one task at a time, delegating implementation, review, and regression checks to sub-agents before marking items complete.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to work through roadmap or TODO checklists end to end while preserving sub-agent review, regression evidence, and explicit control over git side effects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can drive end-to-end code changes and optional git operations during a roadmap run.

Mitigation: Review the goal text before starting; mention commits or pushes only when those side effects are intended, and otherwise review the resulting working tree manually.

Risk: A roadmap item could be marked complete from incomplete or unobserved sub-agent evidence.

Mitigation: Require the documented close-out gates: zero review blockers, regression results with quoted output, and quoted task-specific verification before ticking a checkbox.

## Reference(s):

- [Sub-agent briefs](references/agent-briefs.md)
- [ClawHub skill page](https://clawhub.ai/dennisrongo/skills/goal-runner)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown guidance with task status updates, quoted command output, and optional git commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update roadmap checkboxes and annotations; commits or pushes occur only when explicitly authorized in the goal text.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
