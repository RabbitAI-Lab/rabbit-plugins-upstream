## Description:

Helps agents use curl to check Kia vehicle status and EV charging, and to issue authorized door, climate, and charging commands through the Kia Owners API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Kia owners and authorized operators use this skill for one-off vehicle status and charging checks or remote door, climate, and charging controls from a shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved refresh tokens and temporary response files can expose account credentials and sensitive vehicle or location data on a shared machine.

Mitigation: Use a private machine, restrict or avoid persistent token storage, and remove /tmp/kia_* files after use.

Risk: Door, climate, and charging commands can change the vehicle's physical state; an accepted response does not prove completion.

Mitigation: Run commands only with the owner's authorization and re-check vehicle status to confirm the intended result.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/kiaaccess-curl)
- [Ready-to-run requests](references/requests.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Vehicle commands require authorization and a follow-up status check to confirm completion.]

## Skill Version(s):

1.1.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
