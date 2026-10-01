## Description:

Read and change your children's school dismissal plans on PickUp Patrol from a shell, including student records, weekly defaults, date-specific changes, and school cutoff times.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents or guardians with an authorized PickUp Patrol account can check their children's dismissal plans and update date-specific or weekly plans using shell commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized or mistaken changes could affect how a child leaves school.

Mitigation: Use only with your own authorized account; confirm the intended student, date, and transportation choice before any write request.

Risk: Passwords, session cookies, tokens, and temporary response files contain sensitive information.

Mitigation: Keep credentials and session artifacts private, and delete temporary session files after use.

Risk: A successful response may not mean a plan change was applied, especially after a school cutoff.

Mitigation: Require deliberate confirmation before writes, then re-read the plan and verify the transportation and note.

## Reference(s):

- [PickUp Patrol API reference](references/api.md)
- [PickUp Patrol skill release](https://clawhub.ai/chrischall/skills/pickuppatrol-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read or modify live school dismissal plans.]

## Skill Version(s):

1.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
