## Description:

Publish SKILL.md files to ClawHub and diagnose publish failures across the history, ai-custom-skills, and ai-thoughts skill repositories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to publish ClawHub skills, inspect publishing status, and interpret common workflow failures without creating duplicate publish paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide an agent to push repository changes or trigger publishing workflows.

Mitigation: Review the target repository, remote, and token environment before acting.

Risk: Publishing from the wrong repository copy or creating a manual publish path could duplicate releases.

Mitigation: Use the documented owner-guarded workflow and verify the expected publisher handle before triggering publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/skill-publish)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and procedural guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include read-only API checks and repository workflow verification steps.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
