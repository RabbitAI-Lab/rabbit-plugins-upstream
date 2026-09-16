## Description:

Heartbeat helps agents search and read Heartbeat community data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to handle Heartbeat requests by listing and retrieving users, access groups, channels, and events in a connected Heartbeat community.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that are not verified by the skill artifact.

Mitigation: Review the oo CLI installation path before installing, and prefer an official package or installer with a verified signature or checksum.

Risk: Heartbeat access depends on the connected OOMOL account, connector scopes, and billing status.

Mitigation: Confirm the OOMOL account, Heartbeat connection, API-key scopes, and billing state are appropriate for the community data the agent should read.

## Reference(s):

- [Heartbeat homepage](https://www.heartbeat.chat)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Heartbeat skill page](https://clawhub.ai/oomol/skills/oo-heartbeat)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the oo CLI to return JSON connector responses from Heartbeat.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
