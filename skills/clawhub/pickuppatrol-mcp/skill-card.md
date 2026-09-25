## Description:

Read and change children's school dismissal plans on PickUp Patrol from a shell with curl, including students, weekly defaults, day-by-day changes, and school cutoff times.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents or authorized guardians use this skill to inspect PickUp Patrol account data and prepare shell commands for changing school dismissal plans. It is most useful when an agent needs to guide API reads, date-specific plan changes, weekly default updates, and post-write verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can change how a child leaves school.

Mitigation: Use only an account you are authorized to manage, replace all example student IDs and notes with verified values, and re-read the relevant plan fields before and after every write.

Risk: Live-session-derived examples may contain sensitive child-dismissal context.

Mitigation: Replace examples with synthetic or user-verified values before use and avoid sharing generated commands or responses that include student, school, or dismissal details.

Risk: Session cookies and authentication responses may be written to temporary locations during shell use.

Mitigation: Keep session files out of shared temp locations, limit their lifetime, and remove cookie jars or auth response files after the task is complete.

Risk: Repeated failed login attempts can trigger account lockout.

Mitigation: Stop after one rejected login attempt and correct credentials or account state before retrying.

## Reference(s):

- [PickUp Patrol API reference](references/api.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/pickuppatrol-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include authenticated API calls that require user-provided PickUp Patrol credentials and careful verification after writes.]

## Skill Version(s):

1.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
