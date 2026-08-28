## Description:

Teamup Calendar lets agents read, create, update, and delete Teamup Calendar data through an OOMOL-connected account using the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Teamup Calendar events and subcalendars through an OOMOL-connected account without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Teamup Calendar access is mediated through OOMOL.

Mitigation: Confirm the user is comfortable with OOMOL acting as the intermediary before installing or using the connector.

Risk: The skill can create, update, and delete calendar events.

Mitigation: Require explicit user confirmation for the exact payload and target before write or destructive actions.

## Reference(s):

- [Teamup Calendar homepage](https://www.teamup.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-teamup)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before constructing payloads; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
