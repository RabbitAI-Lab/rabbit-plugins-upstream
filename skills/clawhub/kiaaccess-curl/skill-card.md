## Description:

Helps agents query Kia vehicle status, location, and charging information or issue vehicle commands with curl through the Kia Owners API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Kia owners and authorized operators use this skill for one-off shell-based checks of vehicle status, location, and EV charging, or to control locks, climate, and charging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials and a durable refresh token could expose vehicle access if mishandled.

Mitigation: Use only on private machines, protect or rotate the saved token, and grant access only for vehicles you own or are authorized to control.

Risk: Fixed temporary files can expose session headers and sensitive vehicle or location data.

Mitigation: Replace fixed /tmp paths with private temporary files and restrict access to stored outputs.

Risk: Remote lock, climate, and charging commands affect a real vehicle; an accepted request may not have completed.

Mitigation: Confirm authorization before issuing commands, then reread vehicle state to verify the requested change.

## Reference(s):

- [Ready-to-run requests](references/requests.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/kiaaccess-curl)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return sensitive vehicle status and precise location; vehicle commands require confirmation by rereading vehicle state.]

## Skill Version(s):

1.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
