## Description:

Helps agents retrieve and manage OurFamilyWizard co-parenting messages, calendar events, expenses, and journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using OurFamilyWizard for co-parenting can ask an agent to review messages, calendar events, expenses, and journal entries, or prepare updates in their account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious because broad co-parenting triggers may route a general request to an OurFamilyWizard account; some review coverage is incomplete.

Mitigation: Use the skill only for clear OurFamilyWizard requests, and consider whether account access or read-status changes fit the request. Review the security findings before installation.

Risk: Some reads can change read or last-seen status, and writes can affect co-parenting records.

Mitigation: Explain the effect and get approval before sending, deleting, or making shared record changes. Avoid silently opening unread messages or fetching notifications that update last-seen status.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chrischall/skills/ofw)
- [ofw-mcp package](https://www.npmjs.com/package/ofw-mcp)

## Skill Output:

**Output Type(s):** [Text, Structured data, Files, Guidance]

**Output Format:** [Natural-language summaries and structured OurFamilyWizard records; optional calendar or attachment files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on account access, available tools, data freshness, and result completeness.]

## Skill Version(s):

2.29.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
