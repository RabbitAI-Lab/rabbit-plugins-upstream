## Description:

Reads agreement terms, prepares an obligation schedule, and adds entries to a renewal schedule with optional delivery to a configured destination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams use this skill to extract renewal obligations from agreement text, record schedule entries locally, and optionally deliver the result to a configured destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery can send agreement-derived data and a local file path to an external endpoint without strong safeguards.

Mitigation: Clear ambient delivery endpoint settings unless needed; authorize only trusted HTTPS destinations to receive agreement schedules.

Risk: Agreement data may be sensitive and the workflow writes a local business record.

Mitigation: Review before installing for sensitive agreements and use a dedicated output directory with appropriate access controls.

## Reference(s):


## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON schedule and receipts, plus a local renewal-schedule artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports local record status and, when configured, a delivery outcome.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
