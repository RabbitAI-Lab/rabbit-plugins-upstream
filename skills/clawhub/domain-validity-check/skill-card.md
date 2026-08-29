## Description:

Checks corporate domain validity, security, and sensitivity status through the Upkuajing Open Platform API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams, marketers, researchers, and data operations users use this skill to validate corporate website domains before CRM cleanup, sales-lead verification, supplier checks, buyer verification, and email-list scrubbing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checked domains are sent to upkuajing.com for processing.

Mitigation: Use the skill only when sharing the target domains with Upkuajing is acceptable under the user's data handling rules.

Risk: The skill stores and reads an API key from ~/.upkuajing/.env.

Mitigation: Keep the API key out of shared transcripts, source control, and error reports, and protect the local credential file.

Risk: Domain checks and account top-up flows may involve paid API workflows.

Mitigation: Confirm fees and user intent before charged calls or top-up actions, using the documented pricing flow when needed.

Risk: Error reporting can include request context and diagnostic data.

Mitigation: Ask for confirmation before reporting and avoid sending raw customer data, secrets, tokens, or full CRM payloads.

Risk: The artifact includes account, billing, telemetry, and automatic version-check behavior beyond the core domain check.

Mitigation: Review those behaviors before installation and limit use to the required domain validation workflow.

## Reference(s):

- [Domain Validity API](artifact/references/domain-api.md)
- [Skill Error Report API](artifact/references/skill-error-report-api.md)
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/domain-validity-check)
- [Upkuajing Publisher Profile](https://clawhub.ai/user/upkuajing)
- [Upkuajing Homepage](https://www.upkuajing.com)
- [Upkuajing Open Platform](https://developer.upkuajing.com/)
- [Upkuajing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Upkuajing OpenAPI Endpoint](https://openapi.upkuajing.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python, httpx, and UPKUAJING_API_KEY for authenticated API calls.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
