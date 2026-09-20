## Description:

Query and command a Kia vehicle directly with curl against the Kia Owners API for one-off vehicle status, location, EV charge, lock, unlock, climate, and charging operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and vehicle owners use this skill to construct curl and jq commands for Kia Owners API reads and remote commands without running the related MCP server. It is intended for deliberate shell-based checks and actions against the user's own Kia account and vehicle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles durable Kia account credentials and a refresh token that can re-authenticate without another password prompt.

Mitigation: Store the refresh token only in the documented private session file with restrictive permissions, and protect or delete it when shell access is no longer needed.

Risk: The skill includes direct vehicle-affecting commands such as unlock, climate, charging, and location reads.

Mitigation: Require explicit user confirmation before running any command that changes vehicle state or reveals location.

Risk: The documented curl helper writes response headers to a fixed /tmp path.

Mitigation: Avoid shared machines or replace the fixed path with a private temporary file before relying on the helper in a multi-user environment.

## Reference(s):

- [Ready-to-run requests](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/kiaaccess-curl)
- [Kia Owners API endpoint](https://api.owners.kia.com/apigw/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash, curl, and jq command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Kia account credentials, a stable device ID, one-time MFA bootstrap, and careful confirmation of vehicle-affecting commands.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
