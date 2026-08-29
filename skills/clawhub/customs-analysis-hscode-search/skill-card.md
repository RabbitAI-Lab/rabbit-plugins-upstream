## Description:

Searches UpKuaJing customs data for HS codes matching a product name and HS code keyword so analysts can use the codes in deeper trade analysis workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade analysts, exporters, import-export professionals, and agents use this skill to find matching HS codes before running customs trade analysis, market research, or competitor monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads and may write UPKUAJING_API_KEY in ~/.upkuajing/.env.

Mitigation: Use a dedicated API key, restrict access to the local .env file, and avoid sharing logs or outputs that may reveal credential material.

Risk: HS code searches and top-up flows can involve paid UpKuaJing account activity.

Mitigation: Review current pricing and require explicit user confirmation before any fee-incurring API call or payment-page flow.

Risk: Confirmed error reports may send troubleshooting context to the platform.

Mitigation: Send error reports only after user confirmation and avoid including sensitive business data beyond what is needed to diagnose the failed call.

Risk: The skill performs automatic version checks and writes local version-check cache state.

Mitigation: Review this behavior before installation in restricted environments and monitor local files under ~/.upkuajing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-analysis-hscode-search)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [HS Code Search API Reference](references/customs-analysis-hscode-search-api.md)
- [Skill Error Report API Reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with direct Python command examples and JSON API responses from the script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns matching HS code strings and may include pagination, fee, balance, and request identifier details from the API response.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
