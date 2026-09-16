## Description:

Luma enables agents to search and read Luma calendars, events, guests, and user profile data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Luma connector schemas and run read-only Luma actions for calendars, events, guests, and the current user profile.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Install the oo CLI only from a trusted, reviewed, pinned, signed, or package-manager-based source before using this skill.

Risk: A connected Luma account can expose calendar, event, guest, and profile data available to the configured API key.

Mitigation: Connect only the intended Luma account and verify the requested read action and payload before execution.

## Reference(s):

- [Luma homepage](https://lu.ma)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-luma)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and execution metadata when actions run successfully.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
