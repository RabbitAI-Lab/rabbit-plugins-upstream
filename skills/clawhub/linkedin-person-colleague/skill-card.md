## Description:

Finds LinkedIn colleagues for a specified company ID and person ID using UpKuaJing data, returning colleague identifiers and job titles for organizational mapping and account intelligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, sales teams, and B2B account researchers use this skill to discover colleagues connected to a known LinkedIn person and company, map team relationships, and expand account intelligence with person IDs and job titles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party UpKuaJing provider and stores an API key for authenticated requests.

Mitigation: Install only if the user is comfortable with UpKuaJing as the provider, protect the UPKUAJING_API_KEY value, and avoid sharing the key in prompts or logs.

Risk: Colleague lookup and account top-up flows may incur paid API charges.

Mitigation: Confirm current pricing and obtain explicit user confirmation before paid lookups, pagination requests, or top-up operations.

Risk: Optional error reports may include troubleshooting context.

Mitigation: Run error reporting only after user confirmation and avoid sending sensitive internal details in the report context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/linkedin-person-colleague)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing price description](https://www.upkuajing.com/web/openapi/price.html)
- [LinkedIn person colleague list API](references/linkedin-person-colleague-list-api.md)
- [Skill error report API](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a company ID and person ID; results are paginated with a cursor, and paid API calls require explicit user confirmation.]

## Skill Version(s):

1.0.5 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
