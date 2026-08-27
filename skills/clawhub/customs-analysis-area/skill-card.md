## Description:

Query trade area distribution analysis for HS codes by retrieving country and region trade distribution data with exporter or importer type and recent-month filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Trade analysts, market researchers, import-export professionals, and agents acting on their behalf use this skill to identify which countries trade a specified HS code and compare exporter versus importer activity by region.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles an UpKuaJing API key stored locally or provided through the environment.

Mitigation: Keep the key private, avoid printing the local environment file, and install only when API-key access is acceptable.

Risk: Queries and account top-up actions can incur paid API charges.

Mitigation: Confirm every paid query or top-up step with the user before running the script.

Risk: Diagnostic error reports may include sensitive request or business context.

Mitigation: Review report payloads and remove sensitive business data before submitting them.

Risk: Server evidence marks the release security verdict as suspicious because credential handling, paid flows, and automatic network/cache behavior have limited safeguards.

Mitigation: Review and scan the skill before deployment, and restrict use to environments where these behaviors are acceptable.

## Reference(s):

- [Area Distribution API Reference](references/customs-analysis-area-api.md)
- [Skill Error Report API Reference](references/skill-error-report-api.md)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-analysis-area)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [JSON results and concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns per-country or per-region trade metrics, fee information, and request identifiers from the UpKuaJing Open Platform.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
