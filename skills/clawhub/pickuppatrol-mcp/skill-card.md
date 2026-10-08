## Description:

Read and change children's school dismissal plans on PickUp Patrol from a shell using curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and authorized caregivers can inspect student dismissal options and weekly defaults, then prepare and verify date-specific or recurring plan changes from a shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect dismissal changes can affect how a child leaves school, and changes after the cutoff may be silently ignored.

Mitigation: Review each update against the school's transportation rules and cutoff, then re-read the plan to verify its transportation and note.

Risk: Credentials, session cookies, and student records are sensitive; fixed temporary files may expose them.

Mitigation: Keep secrets out of command lines, use a private temporary directory with restrictive permissions, and remove temporary files after use.

Risk: Whole-record updates to weekly defaults can overwrite student data; repeated rejected logins can lock the account.

Mitigation: Back up student JSON before updating the complete record, review PUT commands, and stop after a failed login to correct credentials.

## Reference(s):

- [PickUp Patrol API reference](references/api.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/pickuppatrol-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use curl and jq to read or update dismissal plans.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
