## Description:

Write git commit messages that follow the Conventional Commits spec.

This skill is ready for commercial/non-commercial use.

## Publisher:

[widoxm](https://clawhub.ai/user/widoxm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to draft or improve concise Git commit messages that follow the Conventional Commits format based on the current diff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The activation wording may trigger on vague uses of the word "commit".

Mitigation: Use the skill for commit-message drafting contexts and review the generated message before using it.

Risk: A generated commit message may omit or overstate the primary intent of a diff.

Mitigation: Compare the final message against the staged or working diff before committing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/widoxm/skills/conventional-commits)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown fenced code block containing a Conventional Commit message]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Subject line under 72 characters; optional body and footer when supported by the diff.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
