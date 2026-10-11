## Description:

Guides one-off Kia vehicle status checks and remote commands through shell requests to the Kia Owners API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Kia owners and their authorized assistants use the skill to inspect vehicle status, location, and charging information or request door, climate, and charging actions from the shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive account and vehicle location data and issue real vehicle commands.

Mitigation: Run only on a private machine and require explicit confirmation before unlock, climate, or charging actions.

Risk: Durable session credentials and temporary response files can expose account or vehicle data.

Mitigation: Protect the saved session file, restrict access to temporary files, and delete them when finished.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/kiaaccess-curl)
- [Ready-to-run requests](references/requests.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires account credentials and one-time MFA setup; command acceptance does not prove a vehicle state change.]

## Skill Version(s):

2.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
