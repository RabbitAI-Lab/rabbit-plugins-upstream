## Description:

Searches UpKuaJing customs trade data by product name and HS-code keyword to return matching HS codes for downstream trade analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade analysts, importers, exporters, and agents use this skill before deeper customs reporting to locate candidate HS classification codes from product names and HS-code keywords.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles an UpKuaJing API key stored locally and can expose secrets if the agent prints credential files.

Mitigation: Do not print the local environment file or include API keys in responses, logs, or diagnostic reports.

Risk: HS-code searches and account helper actions can incur charges or affect billing workflows.

Mitigation: Require explicit user confirmation before paid queries, recharge-order creation, or other billing-related actions, and use pricing information instead of estimating costs.

Risk: Product queries and diagnostic reports may send trade details, request context, or troubleshooting data to UpKuaJing.

Mitigation: Avoid including secrets, personal data, or proprietary trade details in queries or reports, and only submit diagnostics after the user confirms.

Risk: The skill includes account, pricing, recharge-order, error-report, and update-check helper calls beyond the narrow HS-code search path.

Mitigation: Review helper commands before execution and run only the helper needed for the user's confirmed task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-analysis-hscode-search-zh)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing developer platform](https://developer.upkuajing.com/)
- [UpKuaJing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [HS-code search API reference](references/customs-analysis-hscode-search-api.md)
- [Skill error report API reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [JSON API responses with concise natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns matching HS-code strings, pagination cursor, fee details, and request identifiers when available.]

## Skill Version(s):

1.0.1 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
