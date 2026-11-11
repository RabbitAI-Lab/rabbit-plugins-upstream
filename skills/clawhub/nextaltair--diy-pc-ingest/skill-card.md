## Description:

Ingest pasted PC parts receipts or specs into Notion DIY_PC tables with classification, enrichment, verified upsert, and provisional records when serials are unknown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

PC owners use this skill to turn pasted receipts and hardware notes into organized records in their Notion DIY_PC tables. It can classify parts, enrich product details, match existing records, and keep provisional entries when a serial number is unknown.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan rates the skill suspicious with medium confidence, citing undeclared record archiving and unsafe page matching; scan coverage is incomplete.

Mitigation: Review the proposed targets and changes before applying them, and limit Notion integration access to the intended DIY_PC data sources.

Risk: Optional product enrichment may send partial product text to external web providers.

Mitigation: Skip web search and fetch enrichment when pasted receipts or notes should remain local.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/nextaltair/skills/diy-pc-ingest)
- [Notion target ID guidance](artifact/references/notion-ids.md)

## Skill Output:

**Output Type(s):** [API Calls, Structured data, Guidance]

**Output Format:** [Notion database records and concise clarification questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records can be provisional when serial numbers are unknown.]

## Skill Version(s):

2.2.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
