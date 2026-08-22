## Description:

Looks up China public holidays from the Nager.Date public holidays API for a full year, a month, or a specific date.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonyhuya](https://clawhub.ai/user/tonyhuya)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to check China statutory public holidays from the command line, including yearly listings, monthly filtering, and single-date holiday checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each lookup contacts the Nager.Date public API, which may be unsuitable for offline or privacy-restricted workflows.

Mitigation: Use only in environments where outbound requests to Nager.Date are allowed, or review the script before deployment and provide an approved data source.

Risk: The holiday source returns public holiday dates and does not include China adjusted workday makeup schedules.

Mitigation: Confirm final holiday and makeup workday arrangements against State Council notices for operational decisions.

## Reference(s):

- [Nager.Date](https://date.nager.at/)
- [Nager.Date Public Holidays API](https://date.nager.at/api/v3/PublicHolidays)
- [ClawHub skill page](https://clawhub.ai/tonyhuya/skills/cn-holidays)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Terminal text output with inline command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access to Nager.Date for lookups; does not include China adjusted workday makeup schedules.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
