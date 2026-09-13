## Description:

Read and change your children's school dismissal plans on PickUp Patrol (app.pickuppatrol.net) from a shell with curl — students, weekly defaults, day-by-day changes, school cutoff times.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and caregivers use this skill to retrieve student dismissal information and prepare curl-based updates for PickUp Patrol plans. It is useful for shell-driven workflows that need to review weekly defaults, date-specific overrides, school cutoff times, and transportation option rules before changing dismissal plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands can change live child dismissal plans.

Mitigation: Review student IDs, dates, transportation options, notes, and cutoff status before running write commands, then re-read the plan to verify the result.

Risk: Session cookies, credentials, and student data are sensitive and may be exposed through local shell state or temporary files.

Mitigation: Run only on trusted machines, avoid sharing command output, protect environment variables and cookie jars, and clean up temporary authentication files after use.

Risk: Rejected login attempts may count against the account and lead to lockout.

Mitigation: Stop after one failed login attempt and correct credentials before trying again.

## Reference(s):

- [PickUp Patrol API Reference](artifact/references/api.md)
- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/pickuppatrol-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, jq, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include commands that read or modify live PickUp Patrol dismissal plans and should be reviewed before execution.]

## Skill Version(s):

0.2.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
