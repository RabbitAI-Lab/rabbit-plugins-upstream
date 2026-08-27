## Description:

Queries UpKuaJing's global company database for a person's work-experience records by personnel ID, despite release metadata that describes education verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, HR teams, hiring managers, and agents can use the skill to retrieve a person's work-history records from the UpKuaJing global company database after confirming that work-history lookup, not education verification, is the intended task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release metadata advertises education verification, while the artifact retrieves work-history records.

Mitigation: Confirm that the intended use is work-history lookup before installation or execution, and update public release copy before production use.

Risk: Returned employment records can contain sensitive personal data.

Mitigation: Use the skill only with a lawful purpose and authorization, minimize retained data, and avoid exposing personnel details in downstream prompts, logs, or reports.

Risk: Each query and each paginated follow-up can incur fees.

Mitigation: Inform the user of fee-incurring behavior and require explicit confirmation before every chargeable API call.

Risk: The skill depends on an UpKuaJing API key stored in the environment or ~/.upkuajing/.env.

Mitigation: Protect the API key as a secret, restrict local file access, and rotate the key if it may have been exposed.

Risk: Error-reporting flows can transmit request context to the platform.

Mitigation: Report errors only after user confirmation and avoid sending raw personnel details or other unnecessary sensitive data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/global-company-person-experience)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing developer platform](https://developer.upkuajing.com/)
- [Detailed price description](https://www.upkuajing.com/web/openapi/price.html)
- [Work Experience List API](references/person-experience-list-api.md)
- [Skill Error Report API](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses and concise natural-language guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns paginated work-experience records with fee information and request IDs when the upstream API responds successfully.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
