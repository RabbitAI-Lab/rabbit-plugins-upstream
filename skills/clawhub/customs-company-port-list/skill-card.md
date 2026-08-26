## Description:

Query paginated port trade data for a company to retrieve port-level trade statistics with counts, amounts, and percentages for logistics analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and logistics teams use this skill to query UpKuaJing customs data for a company's trade ports, including port-level transaction counts, amounts, quantities, weights, and trade percentages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid UpKuaJing API calls and top-up flows can incur costs.

Mitigation: Inform the user that a fee may be charged and wait for explicit confirmation before running a paid query or creating a top-up order.

Risk: The UPKUAJING_API_KEY grants access to the user's UpKuaJing account.

Mitigation: Keep the key private, store it only in the expected environment variable or ~/.upkuajing/.env file, and do not expose it in prompts, logs, or shared output.

Risk: Error reports may include request or response details that contain sensitive business data.

Mitigation: Ask for user confirmation before reporting an abnormal API call and avoid sending raw request or response bodies unless the user has reviewed them for sensitive content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-company-port-list)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [Detailed price description](https://www.upkuajing.com/web/openapi/price.html)
- [Company Port List API](references/customs-company-port-list-api.md)
- [Skill Error Report API](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API results and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python, httpx, and UPKUAJING_API_KEY; paid API calls require explicit user confirmation before execution.]

## Skill Version(s):

1.0.1 (source: evidence.release.version and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
