## Description:

Query import/export monthly trade volume trend data for a specified time range with cursor-based pagination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade analysts, supply chain managers, market researchers, and agents use this skill to retrieve monthly import/export trade volume trends for time-series analysis, seasonality review, and trade-flow forecasting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill manages an UpKuaJing API key in a local plaintext file.

Mitigation: Use a dedicated API key, restrict local file access, avoid sharing the key, and rotate it if exposure is suspected.

Risk: Trend queries, account helpers, and top-up flows may involve paid API usage or billing actions.

Mitigation: Review pricing and require explicit user confirmation before paid queries, top-up order creation, or account-related actions.

Risk: Diagnostic error reports can send troubleshooting context and request details to UpKuaJing services.

Mitigation: Send reports only after user confirmation and exclude confidential business data from report context, request parameters, responses, and logs.

Risk: The skill contacts UpKuaJing services and performs automatic version checks with local persistence.

Mitigation: Install only when outbound requests to UpKuaJing are acceptable and review local persistence behavior before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-overview-trend)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing developer platform](https://developer.upkuajing.com/)
- [UpKuaJing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Customs overview trend API reference](references/customs-overview-trend-api.md)
- [Skill error report API reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; successful trend queries return monthly records, fee information, and request identifiers.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
