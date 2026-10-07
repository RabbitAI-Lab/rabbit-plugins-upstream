## Description:

Guides one-off Kia vehicle status, location, charging, and remote-control requests through shell commands to the Kia Owners API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Kia owners and developers use this skill for one-off shell-based reads of vehicle status, location, and EV charging, or to issue remote door, climate, and charging commands after account authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote commands can unlock the car, change climate or charging, and location requests expose precise whereabouts.

Mitigation: Require explicit user confirmation before unlock, climate, charging, or location requests; share vehicle data only with the intended user.

Risk: Saved refresh tokens and temporary response files can expose Kia account or vehicle information.

Mitigation: Treat the refresh token as a password, store it with restricted permissions, avoid shared machines, and remove temporary files after use.

Risk: An accepted remote request does not establish that the vehicle completed the action.

Mitigation: Reread and compare the relevant vehicle-status field before reporting success.

Risk: Repeated failed logins can trigger account challenges that block shell access.

Mitigation: Stop after a rejected login and correct the credentials rather than retrying automatically.

## Reference(s):

- [KiaAccess Curl on ClawHub](https://clawhub.ai/chrischall/skills/kiaaccess-curl)
- [Ready-to-run requests](references/requests.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return account or vehicle data and may change vehicle state; verify command completion by rereading vehicle status.]

## Skill Version(s):

1.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
