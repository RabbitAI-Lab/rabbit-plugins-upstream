## Description:

China Company Search Fengniao helps agents query Riskbird for Chinese company registration, ownership, executive, investment, business-change, legal, and risk records and compile due-diligence reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xinshu001](https://clawhub.ai/user/xinshu001)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up Chinese company registration, ownership, management, investment, legal enforcement, and risk records before supplier onboarding, contracting, customer review, or due diligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names, person names, entids, due-diligence queries, and API credentials are sent to Riskbird, with private API keys transmitted in URL parameters.

Mitigation: Use the shared key only for low-sensitivity testing, avoid exposing request URLs or keys in shared logs or terminals, and review generated reports before relying on or redistributing corporate or personal risk data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xinshu001/skills/company-search-fengniao)
- [Riskbird Public Key and Quota Page](https://www.riskbird.com/skills)
- [Riskbird Website](https://www.riskbird.com/)
- [Due Diligence Report Guide](references/due_diligence_report.md)
- [Common Business Information Field Definitions](references/field_definitions_common_bizinfo.md)
- [Legal Field Definitions](references/field_definitions_legal.md)
- [Risk Field Definitions](references/field_definitions_risk.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries require a resolved company entid after fuzzy search; Riskbird API keys may be supplied through FN_API_KEY or the bundled shared key.]

## Skill Version(s):

1.0.2 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
