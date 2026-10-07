## Description:

Helps users check their Kia vehicle and request confirmation-gated climate, charging, and door commands through their Kia account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Kia account holders use this skill to check vehicle status, location, and EV charging, or to request approved climate, charging, and door actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kia account credentials or exported refresh tokens can provide long-lived access to a real vehicle account.

Mitigation: Keep credentials out of project files and committed configuration; treat exported refresh tokens like passwords and use read-only mode unless commands are needed.

Risk: Vehicle commands, especially unlocking doors, can have real-world consequences.

Mitigation: Require explicit user confirmation for each command and enable only the write mode needed.

Risk: Cached vehicle status or an accepted command may not reflect the vehicle's current state.

Mitigation: Refresh and re-read status when freshness matters; distinguish command acceptance from confirmed state and avoid blindly resending commands.

## Reference(s):

- [ClawHub kiaaccess listing](https://clawhub.ai/chrischall/skills/kiaaccess)
- [kiaaccess-mcp npm package](https://www.npmjs.com/package/kiaaccess-mcp)

## Skill Output:

**Output Type(s):** [Text, Configuration instructions, Tool calls]

**Output Format:** [Markdown guidance and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports whether a vehicle command was merely accepted or its resulting state was confirmed.]

## Skill Version(s):

1.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
