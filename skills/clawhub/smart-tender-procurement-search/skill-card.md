## Description:

Searches Chinese tender and procurement notices by keyword, region, amount, date, and industry, and retrieves project details and related company and market data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, suppliers, and analysts use this skill to find Chinese tender opportunities, inspect notices and project timelines, and review company or market information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic registration collects device features, including a MAC-derived hash, and sends them to the provider.

Mitigation: Configure ZLBX_API_KEY manually where possible; obtain informed consent before automatic registration.

Risk: Automatic registration stores an API credential locally under ~/.zlbx/config.json.

Mitigation: Restrict access to the credential file and avoid exposing the key in responses or logs.

Risk: The skill makes account balance and update-check requests and sends package identity with API calls.

Mitigation: Review these provider requests and disclosed identifiers before enabling the skill.

Risk: Some company-data queries consume account credits.

Mitigation: Run only the queries the user requests, and confirm scope before additional pages or paid lookups.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/smart-tender-procurement-search)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](artifact/references/api-search.md)
- [Registration and credential reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown summaries and result tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the provider API and available account credits.]

## Skill Version(s):

1.0.7 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
