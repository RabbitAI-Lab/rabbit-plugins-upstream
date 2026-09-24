## Description:

Read and change your children's school dismissal plans on PickUp Patrol (app.pickuppatrol.net) from a shell with curl, including students, weekly defaults, day-by-day changes, and school cutoff times.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable parents can use this skill to script authorized PickUp Patrol reads and updates from a shell. It helps inspect student dismissal data, transport options, daily overrides, weekly defaults, and cutoff-related verification steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Examples include live-looking student, school, transportation, date, note, and car-number details.

Mitigation: Replace all realistic identifiers and dismissal details with clearly synthetic examples before sharing or installing.

Risk: The skill handles PickUp Patrol passwords and session cookies.

Mitigation: Use only authorized accounts, keep passwords out of command history, protect the cookie jar, and remove temporary authentication files after use.

Risk: PUT, PATCH, and password-change examples can change real dismissal plans or account state.

Mitigation: Treat write commands as production changes, review inputs before execution, and re-read the affected plan or account data to verify the result.

## Reference(s):

- [PickUp Patrol API reference](references/api.md)
- [PickUp Patrol API endpoint](https://app.pickuppatrol.net/api/json/reply)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/pickuppatrol-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with curl and jq shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes authenticated API read/write examples; PUT, PATCH, and password-change commands can affect real PickUp Patrol accounts and dismissal plans.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
