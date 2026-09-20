## Description:

Everhour (everhour.com). Use this skill for ANY Everhour request - reading, creating, updating, and deleting data. Whenever a task involves Everhour, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Everhour through an OOMOL-connected account, including reading users, projects, tasks, timers, and time records and performing confirmed time tracking actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path tells an agent to run remote installer scripts directly in a shell.

Mitigation: Review the installer command before installation, prefer a trusted documented source with verification, and avoid running installer steps unless the oo CLI is actually missing.

Risk: Everhour write and destructive actions can change timers or time records.

Mitigation: Inspect the live action schema, verify the exact payload and effect, and obtain explicit user confirmation before running write or destructive actions.

## Reference(s):

- [ClawHub Everhour skill page](https://clawhub.ai/oomol/skills/oo-everhour)
- [Everhour homepage](https://everhour.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before constructing action payloads and to confirm write or destructive Everhour actions before execution.]

## Skill Version(s):

1.0.4 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
