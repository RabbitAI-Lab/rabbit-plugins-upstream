## Description:

Provides agent guidance for working with HoneyBook client-portal data, including contracts, invoices, questionnaires, messages, meetings, tasks, and payments across wedding vendors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to inspect HoneyBook client-portal status, retrieve vendor documents and messages, and prepare confirmed actions such as signing contracts, paying invoices, or sending replies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive HoneyBook portal sessions and client/vendor data.

Mitigation: Install only for HoneyBook portal work and confirm the vendor or workspace before acting on generic requests.

Risk: Signing, paying, or replying could affect real vendor workflows.

Mitigation: Use the documented confirmation gates and preview message content before sending or opening action links.

Risk: Raw views can expose more vendor-side data than a normal portal summary.

Mitigation: Use compact or summary views by default and request raw views only when a needed field is absent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Text]

**Output Format:** [Markdown guidance with tool names, parameter notes, and concise text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports compact and raw views for selected read tools; write-like actions require explicit confirmation.]

## Skill Version(s):

0.10.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
