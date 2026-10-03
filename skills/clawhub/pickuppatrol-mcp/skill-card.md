## Description:

Helps authorized parents and guardians read and change children's school dismissal plans on PickUp Patrol using shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents or guardians with authorized PickUp Patrol accounts can check students' dismissal arrangements and update one-day plans or weekly defaults, subject to school rules and cutoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unauthorized or mistaken change could affect a child's dismissal arrangements.

Mitigation: Require explicit parent or guardian authorization, replace example student details with verified values, and confirm the intended plan before changing it.

Risk: Account credentials, session cookies, and dismissal records are sensitive.

Mitigation: Protect authentication files and captured responses like passwords; do not commit or share them.

Risk: A school may silently ignore changes submitted after its cutoff time.

Mitigation: Check school rules and re-read the dismissal plan and note after each change to verify the result.

## Reference(s):

- [PickUp Patrol skill listing](https://clawhub.ai/chrischall/skills/pickuppatrol-mcp)
- [PickUp Patrol API reference](artifact/references/api.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.1.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
