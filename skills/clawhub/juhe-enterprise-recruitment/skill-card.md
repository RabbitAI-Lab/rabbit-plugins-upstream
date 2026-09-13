## Description:

Queries Juhe enterprise recruitment data by company name, registration number, or unified social credit code and returns openings with salary, location, requirements, descriptions, and source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[juhemcp](https://clawhub.ai/user/juhemcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to look up current enterprise recruiting records from Juhe and present job title, compensation, location, requirements, source, and related posting details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company lookup values are sent to Juhe for processing.

Mitigation: Use the skill only when sending the queried company name, registration number, or unified social credit code to Juhe is acceptable.

Risk: The Juhe API key can be exposed if passed on the command line or stored carelessly.

Mitigation: Prefer JUHE_ENTERPRISE_RECRUITMENT_KEY from a secure environment variable or secret manager, and avoid committing scripts/.env.

Risk: Queries depend on Juhe account approval, quota, billing, and service availability.

Mitigation: Confirm the Juhe application is approved and monitor quota or billing before relying on the skill in operational workflows.

## Reference(s):

- [Juhe Enterprise Recruitment API Documentation](https://www.juhe.cn/docs/api/id/852)
- [Juhe Data Platform](https://www.juhe.cn)
- [ClawHub Skill Page](https://clawhub.ai/juhemcp/skills/juhe-enterprise-recruitment)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Plain text summaries plus JSON from the helper script; setup and usage guidance in Markdown with shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and a JUHE_ENTERPRISE_RECRUITMENT_KEY secret; query results depend on Juhe API availability, approval, quota, and returned records.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
