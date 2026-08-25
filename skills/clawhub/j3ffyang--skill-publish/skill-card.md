## Description:

Publishes SKILL.md files to ClawHub and helps diagnose publish failures across the history, ai-custom-skills, and ai-thoughts skill repositories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and repository maintainers use this skill to publish ClawHub skills, manually trigger or verify publish workflows, and diagnose skipped or failed releases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Following the skill with the wrong repository, owner, workflow permissions, or token environment could publish or update live ClawHub skills unintentionally.

Mitigation: Confirm the repository remotes, ClawHub account owner, workflow permissions, and token environment before running publish or verification steps.

Risk: Publishing the same skill from multiple repository copies can cause duplicate publish attempts or version collisions.

Mitigation: Use the documented single-source owner guard and verify the live ClawHub version before rerunning a publish workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/skill-publish)
- [ClawHub publisher profile](https://clawhub.ai/user/j3ffyang)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include repository workflow checks, ClawHub API verification steps, and troubleshooting guidance.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
