## Description:

Runs project Harness verification checks for working-tree, staged, and CI modes, then reports automated results separately from host smoke-test and manual review boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huiyonghkw](https://clawhub.ai/user/huiyonghkw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to run and interpret Harness verification for local, staged, and CI workflows. It helps distinguish automated checks from required host smoke tests, visual review, source review, and external side-effect confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Working-tree checks may inspect local Skill and Memory state.

Mitigation: Use CI mode when a fixture-based check is needed without local Skill or Memory dependencies.

Risk: Automated checks can be mistaken for full delivery approval.

Mitigation: Report host smoke tests, visual review, source review, and external side-effect confirmation separately from automated results.

Risk: Fix, commit, push, or external side-effect actions can change repository or external state.

Mitigation: Do not approve those actions unless the user explicitly intends them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huiyonghkw/skills/hekouwang-harness-check-skill)
- [Project Homepage](https://huiyonghkw.github.io/hekouwang-harness-check-skill/)
- [Harness Check Matrix](references/check-matrix.md)
- [Harness Check Flow Diagram](assets/harness-check-flow.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with inline shell commands, exit-status interpretation, failures, warnings, and next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates automated evidence from host smoke-test and manual review status]

## Skill Version(s):

1.0.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
