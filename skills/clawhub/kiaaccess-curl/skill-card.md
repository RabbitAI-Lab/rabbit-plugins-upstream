## Description:

Guides one-off Kia vehicle status checks and remote commands through shell requests to the Kia Owners API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Kia owners and developers use this skill for one-off shell-based vehicle status, location, and EV charging checks, or to request door, climate, and charging actions on a vehicle they control. It requires account credentials and an initial SMS or email verification step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote commands can change vehicle door locks, climate, or charging state.

Mitigation: Use only for a vehicle and account you control, and obtain explicit confirmation before each command.

Risk: The example workflow writes reusable account credentials to predictable temporary files.

Mitigation: Run only on a trusted single-user machine; keep session credentials private and avoid running the example workflow as-is on shared systems.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/kiaaccess-curl)
- [Ready-to-run requests](references/requests.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown with shell examples and JSON response excerpts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Vehicle commands require confirmation and a subsequent status check to verify the requested change.]

## Skill Version(s):

1.1.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
