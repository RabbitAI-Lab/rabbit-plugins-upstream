## Description:

Query Kia vehicle status, location, EV charge state, and remote controls from the shell using curl against the Kia Owners API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable Kia owners use this skill for one-off shell reads of vehicle state and location, or for explicit remote commands such as lock, unlock, climate, and charging actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a durable Kia refresh token that can re-authenticate the account without another MFA prompt.

Mitigation: Treat the saved rmtoken like a password, store it only on trusted machines, keep the session file permissions restricted, and remove temporary header files after use.

Risk: The skill provides shell commands that can locate or remotely control a vehicle.

Mitigation: Require explicit confirmation before commands that change door, climate, or charging state, and verify results by re-reading vehicle state rather than relying on HTTP status alone.

## Reference(s):

- [Ready-to-run requests](references/requests.md)
- [Kia Owners API endpoint](https://api.owners.kia.com/apigw/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with bash and jq command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes credential handling, MFA bootstrap, request construction, and command confirmation guidance.]

## Skill Version(s):

0.6.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
