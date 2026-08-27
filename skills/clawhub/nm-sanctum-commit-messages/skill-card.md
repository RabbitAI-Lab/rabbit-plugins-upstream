## Description:

Generates conventional commit messages from staged changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to inspect staged Git changes and recent history, then draft a conventional commit message for review before committing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads staged diffs and recent git history when invoked.

Mitigation: Use it only in repositories where sharing staged changes and recent history with the agent is acceptable.

Risk: The broad git and commit triggers may activate during adjacent repository work.

Mitigation: Invoke it deliberately for commit-message drafting and confirm staged changes before using the output.

Risk: The skill writes a local ./commit_msg.txt draft.

Mitigation: Check whether ./commit_msg.txt already exists before use when preserving an existing draft matters.

Risk: A generated commit message may omit or misstate the intent of a change.

Mitigation: Review the drafted subject, body, and footer before committing.

## Reference(s):

- [Sanctum plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown/plain text commit message draft with optional body and footer]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write and preview a local ./commit_msg.txt draft.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
