## Description:

thought-flow guides agents through an 8-stage collaboration loop for stating intent and constraints, proposing plans, handling pushback, investigating failures, codifying reusable knowledge, and checking scope.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineering teams, and agent operators use this skill to structure collaborative agent work, especially when scoping tasks, comparing plan options, investigating failures, and deciding whether repeated practices should become durable guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may lead an agent to propose plans, verify behavior against real systems, or codify repeated procedures into repository guidance.

Mitigation: Review proposed plans, live-system checks, and any AGENTS.md or SKILL.md edits before accepting them.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional inline shell commands and file-edit recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code; outputs depend on the user's task, constraints, and repository context.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
