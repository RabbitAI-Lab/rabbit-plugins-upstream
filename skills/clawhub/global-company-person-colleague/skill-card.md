## Description:

Finds colleagues for a target person at a company using required company and person IDs, returning colleague identifiers and job titles from UpKuaJing's global company database.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External recruiters, sales teams, and B2B lead generation users can look up colleagues of a known person at a known company after they have the required company and person IDs. The skill supports professional contact discovery and stakeholder mapping while requiring authorization, API-key access, and fee confirmation before paid queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a persistent UpKuaJing API key and can read it from the environment or ~/.upkuajing/.env.

Mitigation: Install only when the user accepts this credential access, protect the key file, and rotate the key if it may have been exposed.

Risk: Colleague lookup and account operations may incur paid API charges or create top-up payment URLs.

Mitigation: Require explicit user confirmation before any paid query or top-up flow, and use the platform pricing endpoint or pricing page for current costs.

Risk: The skill supports personnel-data lookups and stakeholder mapping that may be sensitive or inappropriate without authorization.

Mitigation: Use it only for authorized professional research and avoid querying or retaining data outside the user's approved purpose.

Risk: Optional error reports may include request context, request parameters, or response details.

Mitigation: Ask for confirmation before reporting errors and avoid sending raw prompts, customer data, secrets, or full response payloads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/global-company-person-colleague)
- [Publisher profile](https://clawhub.ai/user/upkuajing)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [Detailed Price Description](https://www.upkuajing.com/web/openapi/price.html)
- [Colleague List API](references/person-colleague-list-api.md)
- [Skill Error Report API](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; colleague lookups are paginated and paid per API call after explicit user confirmation.]

## Skill Version(s):

1.0.5 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
