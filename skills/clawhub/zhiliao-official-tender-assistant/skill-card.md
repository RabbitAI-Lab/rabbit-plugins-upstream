## Description:

Helps users research Chinese tenders, awards, company records, competitors, procurement trends, and upcoming opportunities through Zhiliao Biaoxun data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, suppliers, and market researchers use this skill to find tender notices and awards, assess companies and competitors, and identify prospective bidding opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Business queries are sent to Zhiliao Biaoxun.

Mitigation: Check that sharing procurement and company queries with the service is acceptable before using sensitive inputs.

Risk: Automatic registration collects device-derived information and can create an account.

Mitigation: Prefer a manually configured API key; review the registration flow and consent to device-data collection before enabling it.

Risk: An API key may be stored in a local credential file.

Mitigation: Review the credential-file behavior and restrict access to locally stored credentials.

Risk: Hidden comment-based request rules may affect how requests are made.

Mitigation: Review the full skill text and request behavior before use in sensitive workflows.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/zhiliao-official-tender-assistant)
- [Zhiliao Biaoxun skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Tender search API reference](references/api-search.md)
- [Company data API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account registration guidance](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Conversational text or Markdown with tender results, company profiles, and market summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on available account access and the data returned by the service.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
