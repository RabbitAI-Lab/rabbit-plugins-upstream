## Description:

Queries UpKuaJing customs overview summary data for annual trade totals, quarterly trade volume, and supplier and buyer counts by country pair.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External export teams, trade analysts, market researchers, and agents use this skill to retrieve high-level country-pair trade summaries for market analysis and partner ecosystem evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid trade-summary API calls and account or top-up flows can affect the user's UpKuaJing account balance.

Mitigation: Tell the user when an operation may incur fees and wait for explicit confirmation before running fee-incurring commands.

Risk: The skill can store an API key in a plaintext dotfile.

Mitigation: Use a dedicated API key, keep the dotfile private, and rotate the key if it may have been exposed.

Risk: Error reporting can send diagnostic request or response details to the provider.

Mitigation: Run error reports only after user confirmation and avoid sending sensitive request or response details.

Risk: The skill performs an undisclosed daily version check to the provider.

Mitigation: Review the version-check behavior before installation in environments with network disclosure or change-control requirements.

## Reference(s):

- [Customs Overview Summary API Reference](references/customs-overview-summary-api.md)
- [Skill Error Report API Reference](references/skill-error-report-api.md)
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-overview-summary)
- [UpKuaJing Publisher Profile](https://clawhub.ai/user/upkuajing)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing API Pricing](https://www.upkuajing.com/web/openapi/price.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls]

**Output Format:** [JSON API responses plus human-facing text or Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY. Paid API calls require explicit user confirmation before execution and may include fee details and request IDs.]

## Skill Version(s):

1.0.1 (source: evidence.release.version, evidence.parsed.metadata.version, SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
