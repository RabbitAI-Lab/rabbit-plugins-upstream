## Description:

Manage installed skills lifecycle: suggest by context, track installations, check updates, and cleanup unused.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

Developers and agent users use this skill to manage installed ClawHub skills by suggesting context-relevant skills, tracking installed and declined skills, checking for updates, and guiding cleanup with user consent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill manages installed skills through unpinned remote ClawHub CLI commands that can execute changing code and alter the user's agent environment.

Mitigation: Prefer a reviewed and pinned ClawHub CLI version or a vetted local CLI, review skills before installing, and require explicit user consent before install, update, or removal.

Risk: Declined-skill reasons are stored locally and could include sensitive details if recorded too broadly.

Mitigation: Store only the minimal stated reason needed to avoid repeated suggestions, and avoid recording sensitive details.

## Reference(s):

- [Skill Manager ClawHub page](https://clawhub.ai/ivangdavila/skills/skill-manager)
- [Skill Lifecycle Management](lifecycle.md)
- [Context-Based Skill Suggestions](suggestions.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and inventory entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user consent before install, update, or removal actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
