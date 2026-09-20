## Description:

Review code changes with the Bugbot or Security Review subagent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to choose between an existing Bugbot review and Security Review workflow for code changes. It asks for one review type and runs the selected review once.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The selected review workflow depends on existing `/review-bugbot` or `/review-security` behavior in the user's environment.

Mitigation: Confirm those underlying commands are trusted and appropriate before installing or running this chooser skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/eohmig/skills/review)

## Skill Output:

**Output Type(s):** [guidance, shell commands]

**Output Format:** [Markdown guidance with a single-select choice and command references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Model invocation is disabled by the skill metadata.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
