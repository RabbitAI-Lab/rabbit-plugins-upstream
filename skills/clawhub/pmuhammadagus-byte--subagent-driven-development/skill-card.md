## Description:

Executes implementation plans by coordinating fresh subagents for independent tasks, task-scoped reviews, fix loops, and a final branch-wide review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to execute an existing implementation plan whose tasks are mostly independent. It keeps coordination in the current session while delegating implementation, review, fix verification, and final branch review to focused subagents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automates code changes and commits in a Git workspace.

Mitigation: Install only when that behavior is intended, and require review gates before accepting task or branch changes.

Risk: Final cleanup can remove the per-plan workspace used for briefs, reports, review packages, and the ledger.

Mitigation: Before cleanup, require the agent to print and verify that the path is the intended per-plan .superpowers/sdd directory.

## Reference(s):

- [Implementer Prompt Template](implementer-prompt.md)
- [Task Reviewer Prompt Template](task-reviewer-prompt.md)
- [Scoped Re-Review Prompt Template](re-review-prompt.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, Code, Files]

**Output Format:** [Markdown instructions with shell command snippets and generated workspace artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coordinates Git commits, task briefs, review packages, implementer reports, and a per-plan progress ledger.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
