## Description:

Helps Kia owners check vehicle status, location, and EV charging and request confirmation-gated climate, charging, and door commands through their Kia Access account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Kia owners use the skill to ask an agent about their vehicle's status, location, and charge level, or to request confirmed climate, charging, and door actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration accesses Kia account credentials and vehicle telemetry, including location.

Mitigation: Install only if comfortable granting that access, keep credentials private, and use read-only mode when commands are unnecessary.

Risk: An exported refresh token can retain access to the vehicle account without another MFA challenge.

Mitigation: Never share exported tokens and forget the local session when access should end.

Risk: Door commands can leave a vehicle unsecured, and an accepted command may not have taken effect.

Mitigation: Enable door commands only when needed, confirm each requested action, and recheck vehicle status rather than blindly retrying.

## Reference(s):

- [Kiaaccess ClawHub listing](https://clawhub.ai/chrischall/skills/kiaaccess)
- [kiaaccess-mcp npm package](https://www.npmjs.com/package/kiaaccess-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Markdown and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Vehicle readings may be cached; command acceptance does not guarantee the vehicle changed state.]

## Skill Version(s):

1.1.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
