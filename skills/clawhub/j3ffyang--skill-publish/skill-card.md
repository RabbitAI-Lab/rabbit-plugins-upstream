## Description:

Publish SKILL.md files to ClawHub and diagnose publish failures across the history, ai-custom-skills, and ai-thoughts skill repositories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to operate the ClawHub skill publishing workflow, trigger or verify releases, and troubleshoot sync or versioning failures for the named repositories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Following the publishing runbook may push repository changes and trigger ClawHub publishing workflows.

Mitigation: Use it only for the named ClawHub skill repositories and verify workflow results against ClawHub before treating a release as complete.

Risk: The publishing flow depends on a ClawHub token for the j3ffyang account.

Mitigation: Keep the token scoped, stored as a repository secret, and out of skill content, logs, and command output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/skill-publish)
- [ClawHub publisher profile](https://clawhub.ai/user/j3ffyang)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
