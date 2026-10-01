## Description:

Select a service capacity window and record a local capacity-window entry when requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Service planners and developers use this skill to select a requested service window and optionally record a capacity entry in a local ledger. The local entry does not confirm an external reservation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A downstream run can write a SQLite capacity ledger beneath the caller-selected output directory.

Mitigation: Use a dedicated writable output directory; do not point the skill at important application data.

Risk: A local ledger entry could be mistaken for a confirmed external booking.

Mitigation: Treat the entry as a local planning record and confirm any external reservation separately.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wxt-ai/skills/service-capacity-booking-desk)
- [Package usage guide](artifact/README.md)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON result and effect receipt; optional local SQLite ledger]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Upstream returns a timezone-aware capacity window; downstream returns a capacity entry and writes a local ledger under the chosen output directory.]

## Skill Version(s):

3.0.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
