## Description:

Suggests conventional-commit messages from a staged diff summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmahmadcs](https://clawhub.ai/user/hmahmadcs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to draft a concise conventional-commit message and alternatives from their staged change summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A staged diff summary may disclose sensitive filenames or change details.

Mitigation: Review and redact the summary before sharing it with the agent.

Risk: A suggested commit message may not accurately describe the staged changes.

Mitigation: Check the proposed message against the staged changes before committing.

## Reference(s):

- [Git Commit Message Helper on ClawHub](https://clawhub.ai/hmahmadcs/skills/git-commit-message-helper)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One primary commit message and two alternatives; subject at most 72 characters, with an optional body.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
