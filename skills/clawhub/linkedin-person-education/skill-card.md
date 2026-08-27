## Description:

Checks LinkedIn-sourced education history by personnel ID and returns schools, degrees, majors, minors, GPAs, pagination details, fee data, and request metadata for candidate screening.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, HR teams, and hiring managers use this skill to verify candidate education backgrounds, assess qualifications, and support background-check workflows from LinkedIn-sourced personnel data. It requires proper authorization for the person being checked.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive background-check data from LinkedIn-sourced education records.

Mitigation: Use it only with proper authorization for the person being checked and within approved recruiting, HR, or background-verification workflows.

Risk: The skill stores or reads an UpKuaJing API key from ~/.upkuajing/.env.

Mitigation: Protect the local key file, limit access to the account, and rotate the API key if it may have been exposed.

Risk: API calls incur fees and the skill includes account top-up support flows.

Mitigation: Confirm fee-bearing actions in a separate user message and verify current pricing through the provider pricing page or price-info script before running paid queries.

Risk: Error reports can include troubleshooting context from failed calls.

Mitigation: Submit error reports only after user confirmation and avoid including sensitive candidate or credential details in the report context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/linkedin-person-education)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing developer platform](https://developer.upkuajing.com/)
- [Detailed price description](https://www.upkuajing.com/web/openapi/price.html)
- [LinkedIn person education list API](references/linkedin-person-education-list-api.md)
- [Skill error report API](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Education lookup results include paginated records, fee information, and request IDs; error-reporting output returns report identifiers.]

## Skill Version(s):

1.0.3 (source: SKILL.md metadata, server release evidence, target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
