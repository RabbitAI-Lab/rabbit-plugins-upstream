## Description:

Read and change school dismissal plans on PickUp Patrol from a shell with curl, including students, weekly defaults, day-by-day changes, and school cutoff times.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents or authorized guardians use this skill to inspect PickUp Patrol account data and prepare shell commands for changing student dismissal plans. It is intended for authorized management of students, schools, dates, transportation options, notes, and related verification checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide live changes to child dismissal plans.

Mitigation: Use only accounts and students the operator is authorized to manage, and verify student, school, date, transportation option, and note before and after every write.

Risk: Passwords, cookies, tokens, or temporary authentication files may be exposed through logs or shared terminals.

Mitigation: Keep credentials and session artifacts out of logs and shared terminals, and remove temporary authentication files after use.

Risk: Rejected login attempts can count against the account and may lead to lockout.

Mitigation: Stop after one failed login attempt and correct credentials before retrying.

Risk: A successful HTTP response may not prove that a dismissal change was accepted, especially around school cutoff times.

Mitigation: Re-read the relevant plan after each write and compare the transportation option and note rather than relying only on status codes or modified timestamps.

## Reference(s):

- [PickUp Patrol API reference](artifact/references/api.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/pickuppatrol-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that authenticate to PickUp Patrol, read account data, and perform authorized write operations.]

## Skill Version(s):

0.1.1 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
