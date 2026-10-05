## Description:

Prepare an agreement obligation schedule from supplied agreement text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Agreement operations teams use this skill to turn supplied renewal agreement text into an obligation schedule with a clause reference, owner, and notice due date.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Missing owner or notice terms default to unassigned or zero days, which can produce an incomplete schedule.

Mitigation: Check the generated owner and notice date against the agreement before relying on the schedule.

Risk: README guidance about output directories appears stale for this local parser.

Mitigation: Follow the active input and output configuration rather than assuming the README's output-directory instructions apply.

## Reference(s):

- [Agreement Obligation Reader on ClawHub](https://clawhub.ai/wxt-ai/skills/agreement-renewal-schedule-identifier)

## Skill Output:

**Output Type(s):** [Structured data]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [An obligation_schedule with an agreement ID and one obligation containing the clause ID, owner, notice days, and notice due date; no file is persisted.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
