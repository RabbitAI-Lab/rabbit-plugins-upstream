## Description:

Use when creating git commit messages, preparing to commit changes, or when commit history is messy, inconsistent, or hard to review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ink5725](https://clawhub.ai/user/ink5725)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to draft and review Conventional Commits messages for staged changes, amendments, and history cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may prompt an agent to inspect staged git changes before drafting a commit message.

Mitigation: Review any actual commit command before it runs.

Risk: Commit-message guidance can still produce an inaccurate or misleading summary of the staged diff.

Mitigation: Review the proposed message against the staged changes and Conventional Commits rules before committing.

## Reference(s):

- [Conventional Commits](https://www.conventionalcommits.org/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with commit-message examples and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
