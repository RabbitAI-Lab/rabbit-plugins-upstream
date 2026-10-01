## Description:

Helps agents access and manage QuickBooks Online accounting data through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Finance teams and business users can ask an agent to retrieve QuickBooks records and reports or perform specifically approved accounting updates. Optional hosted functions and triggers support user-approved automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An authorized agent could change sensitive accounting records or amounts.

Mitigation: Use a least-privileged connection, verify the selected account, default to reads, and approve each write only after checking the exact records, amounts, endpoint, and effect.

Risk: Hosted functions, triggers, or destinations can run actions or deliver data persistently.

Mitigation: Review and explicitly approve the handler, schedule or event, destination, data fields, and persistence before enabling automation.

Risk: Exposed credentials or full responses could disclose financial and personal data.

Mitigation: Keep credentials in the platform's credential store, avoid printing or logging secrets and raw responses, and retrieve only needed fields.

## Reference(s):

- [QuickBooks skill on ClawHub](https://clawhub.ai/byungkyu/skills/quickbooks)
- [QuickBooks API overview](https://developer.intuit.com/app/developer/qbo/docs/get-started)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API request examples, Code, Configuration instructions]

**Output Format:** [Markdown with shell, JSON, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accounting operations require an authorized connection; writes and automations require explicit user approval.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
