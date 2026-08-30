## Description:

Retrieves UpKuaJing customs analysis overview data with supplier and buyer counts grouped by country for a specified HS-code analysis workflow using cursor-based pagination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade analysts, market researchers, import-export professionals, and agents supporting them use this skill to compare supplier and buyer activity by country and identify target markets from aggregated customs overview data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores an UpKuaJing API key in a local plaintext dotfile.

Mitigation: Install only when local plaintext key storage is acceptable, protect the user account, and avoid sharing the dotfile or command output containing credentials.

Risk: The skill can make paid API calls and create account top-up orders.

Mitigation: Require explicit user confirmation before fee-incurring queries, key creation, or payment-order creation, and check current pricing through the documented price command or pricing page.

Risk: Optional error reporting may send troubleshooting context and request details to UpKuaJing.

Mitigation: Ask for confirmation before sending reports and avoid including secrets or sensitive business details in report context.

Risk: The skill performs automatic version checks against the UpKuaJing API.

Mitigation: Review network behavior before installation in restricted environments and treat update notices as informational until reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-analysis-overview)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing API pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Overview API reference](references/customs-analysis-overview-api.md)
- [Skill error report API reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python command examples and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include paginated country-level records with country code, supplier count, buyer count, latest trade date, fee information, and request ID when API calls succeed.]

## Skill Version(s):

1.0.1 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
