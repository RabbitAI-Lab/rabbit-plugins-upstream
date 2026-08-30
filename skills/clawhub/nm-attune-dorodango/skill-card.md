## Description:

Polishes working code through successive quality passes in fresh subagents after tests pass and code needs multi-dimension refinement before release.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill after an implementation is working and tests pass to refine code across correctness, clarity, consistency, and production polish before review or release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can make iterative edits to selected code and run the project test suite.

Mitigation: Use it only on intended targets and review generated code changes before release.

Risk: The workflow may use subagents and local state tracking while refining code.

Mitigation: Inspect .attune/dorodango-state.json and pass summaries when resuming or auditing a polishing session.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-attune-dorodango)
- [Project Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune)
- [Publisher Profile](https://clawhub.ai/user/athola)
- [Pass Definitions](modules/pass-definitions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code edits, shell commands, and JSON state updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May store resumable progress in .attune/dorodango-state.json and may use subagents for separate quality passes.]

## Skill Version(s):

1.9.19 (source: server release evidence; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
