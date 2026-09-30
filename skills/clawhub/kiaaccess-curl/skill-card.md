## Description:

Helps agents use curl to check a Kia vehicle's status, location, and charging state or request remote vehicle controls through the Kia Owners API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Kia owners and developers use this skill for one-off shell checks of vehicle status, location, or EV charging, and for explicitly requested door, climate, and charging controls. It requires Kia account credentials and an initial MFA sign-in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved refresh tokens and Kia credentials can grant account access.

Mitigation: Treat the saved token like a password, restrict file permissions, and avoid running the examples on shared machines.

Risk: The skill can reveal sensitive vehicle location.

Mitigation: Access location only when the user requests it and avoid exposing the results to others.

Risk: Remote door, climate, and charging commands can change the vehicle's physical state.

Mitigation: Require explicit user confirmation before each command and verify the outcome by rereading vehicle state.

## Reference(s):

- [Kia Owners API via curl request examples](references/requests.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/kiaaccess-curl)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Kia credentials and one-time SMS or email MFA; remote commands should be confirmed by rereading vehicle state.]

## Skill Version(s):

1.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
