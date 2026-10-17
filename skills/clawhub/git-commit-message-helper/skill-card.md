## Description:

Suggests conventional-commit messages from a staged diff summary when the user asks for a commit message.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmahmadcs](https://clawhub.ai/user/hmahmadcs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to draft a concise conventional-commit subject and optional body from staged changes or a supplied diff summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A diff summary may omit context needed for an accurate commit message.

Mitigation: Review the suggested message against the staged changes before committing.

Risk: Inspecting staged changes through Git accesses local repository information.

Mitigation: Prefer a user-provided summary; run read-only Git commands only with user approval.

## Reference(s):

- [Git documentation](https://git-scm.com/doc)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Plain text conventional-commit suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One primary message and two short alternatives; subject at most 72 characters.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
