## Description:

Helps sales teams find, preview, export, and enrich U.S. small-business leads through SMB Sales Boost, and manage related searches, schedules, and integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomsonx232](https://clawhub.ai/user/tomsonx232)

### License/Terms of Use:

MIT

## Use Case:

Sales teams and agents use the skill to find and qualify U.S. small-business prospects, export or enrich contact lists, and manage outreach-related schedules and CRM connections.

### Deployment Geography for Use:

Global (lead database covers U.S. businesses)

## Known Risks and Mitigations:

Risk: Keyword-list changes or auto-refinement can change the leads sent by active email schedules without an enforced confirmation step.

Mitigation: Require explicit approval before editing keyword lists or enabling auto-refinement; review or pause affected schedules first and use a narrowly scoped API key where available.

Risk: Lead searches and exports spend credits; subscriptions, credit purchases, and automatic billing can charge real money.

Mitigation: Preview results, set credit limits, and obtain explicit user approval for paid actions and billing changes.

Risk: Exports and integrations can expose business contact details to files or third-party systems.

Mitigation: Confirm destinations and recipients before exporting or connecting integrations, and restrict access to downloaded files.

## Reference(s):

- [SMB Sales Boost](https://smbsalesboost.com)
- [ClawHub skill release](https://clawhub.ai/tomsonx232/skills/smb-sales-boost-skill)
- [Skill API reference](artifact/REFERENCE.md)
- [OpenAPI specification](artifact/openapi.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files]

**Output Format:** [Plain-language lead summaries, API command guidance, and downloadable CSV, JSON, or XLSX exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exports may contain business contact details; searches, exports, and enrichment can spend credits.]

## Skill Version(s):

1.9.5 (source: ClawHub release metadata and README.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
