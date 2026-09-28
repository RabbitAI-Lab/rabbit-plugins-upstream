## Description:

Prepares a simple renewal notice obligation schedule from supplied agreement text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Agreement operations staff use this skill to identify one renewal notice obligation and its due date from agreement text they supply.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A single derived renewal obligation may omit other agreement duties or misrepresent complex renewal terms.

Mitigation: Review the underlying agreement and verify the notice date before relying on the schedule; do not treat it as comprehensive contract analysis.

Risk: Agreement text may contain confidential information.

Mitigation: Supply only agreement text intended for processing.

## Reference(s):

- [Agreement Obligation Reader on ClawHub](https://clawhub.ai/wxt-ai/skills/agreement-renewal-schedule-identifier)

## Skill Output:

**Output Type(s):** [Structured data]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [An agreement ID and one obligation with a clause ID, owner, notice period, and notice due date.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
