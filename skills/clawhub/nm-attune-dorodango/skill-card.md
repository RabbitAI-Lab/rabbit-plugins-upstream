## Description:

Polishes working code through successive quality passes in fresh subagents. Use after tests pass when code needs multi-dimension refinement before release

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill after tests pass to run iterative correctness, clarity, consistency, and polish passes on working code before review or release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow is designed to edit code and run tests, so using the wrong target scope could change files the user did not intend to polish.

Mitigation: Confirm the target files or directory before starting, review diffs after each pass, and keep normal version-control rollback available.

Risk: The workflow records local progress state while polishing code.

Mitigation: Review .attune/dorodango-state.json when resuming or sharing the workspace, and remove it if the polishing history should not persist.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-dorodango)
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance with pass summaries, command suggestions, and code-edit instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update target code and record local progress in .attune/dorodango-state.json when executed by an agent.]

## Skill Version(s):

1.9.18 (source: server release evidence; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
