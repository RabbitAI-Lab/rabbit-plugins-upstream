## Description:

Query top N suppliers or buyers by trade volume for a country pair and year, with cursor-based pagination for supplier and buyer ranking analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External agents, sourcing teams, export teams, and trade analysts use this skill to retrieve ranked supplier or buyer lists for a trade route and year, then page through results to assess key counterparties and market concentration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid UpKuaJing API and each ranking query may incur fees.

Mitigation: Confirm current pricing and obtain explicit user approval before executing fee-incurring queries.

Risk: The UpKuaJing API key is stored locally in ~/.upkuajing/.env or read from UPKUAJING_API_KEY.

Mitigation: Protect the API key, restrict access to the local environment file, and avoid exposing the key in prompts, logs, or shared outputs.

Risk: Queries, account support, pricing checks, optional error reports, and version checks contact UpKuaJing services.

Mitigation: Do not include confidential business details in optional error-report context and review outbound data before reporting issues.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-overview-top-n)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing developer platform](https://developer.upkuajing.com/)
- [UpKuaJing pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Customs Overview Top N API Reference](references/customs-overview-top-n-api.md)
- [Skill Error Report API Reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; query calls return ranked company lists, pagination cursors, fee details, and request identifiers.]

## Skill Version(s):

1.0.1 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
