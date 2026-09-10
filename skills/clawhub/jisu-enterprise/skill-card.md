## Description:

Queries JisuAPI enterprise business records for basic company information, name search, change history, shareholders, and executives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jisuapi](https://clawhub.ai/user/jisuapi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up enterprise registry details from JisuAPI, including registered capital, legal representative, company status, address, change records, and shareholder or executive information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names, registry identifiers, and the JISU_API_KEY are sent to JisuAPI as part of normal operation.

Mitigation: Use the skill only when the organization approves JisuAPI as a provider and the submitted business identifiers are appropriate to share.

Risk: Returned company data can be stale, unavailable, or incomplete depending on JisuAPI coverage and response status.

Mitigation: Review API errors and corroborate important business decisions with an authoritative registry or approved data source.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jisuapi/skills/jisu-enterprise)
- [JisuAPI Enterprise Business Information API](https://www.jisuapi.com/api/enterprise/)
- [JisuAPI](https://www.jisuapi.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires JISU_API_KEY and sends submitted business identifiers to JisuAPI.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
