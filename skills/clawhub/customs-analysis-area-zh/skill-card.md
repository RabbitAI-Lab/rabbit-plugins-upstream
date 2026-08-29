## Description:

Queries country and region-level customs trade distribution data for a specified HS code, including trade count, amount, buyer count, and supplier count.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Trade analysts, market researchers, and import/export practitioners use this skill to compare export-country and import-country activity for an HS code and identify priority regional markets. It helps agents prepare customs trade geography analysis while handling API setup, pricing checks, and error-reporting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and reads a UPKUAJING API key from a plaintext file under the user's home directory.

Mitigation: Use a dedicated API key with limited exposure, avoid displaying the key in chat or logs, and remove the file when access is no longer needed.

Risk: The skill can perform paid customs queries and account or recharge-related API calls.

Mitigation: Confirm every paid query or recharge step in a separate user message before execution and check official pricing before estimating cost.

Risk: Error reports may include request context or response details.

Mitigation: Review the report content before submission and avoid sending secrets, personal data, or unrelated business-sensitive details.

## Reference(s):

- [区域分布 API 参考](artifact/references/customs-analysis-area-api.md)
- [Skill Error Report API Reference](artifact/references/skill-error-report-api.md)
- [跨境魔方](https://www.upkuajing.com)
- [跨境魔方 OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [跨境魔方 Developer Platform](https://developer.upkuajing.com/)
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-analysis-area-zh)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires UPKUAJING_API_KEY; paid API queries require explicit user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
