## Description:

Obtains detailed school information, including classification, location, websites, and social media links, to support institution verification and academic network research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, researchers, analysts, and verification teams use this skill to look up a known school ID and enrich institution records with school names, types, geographic details, websites, and social media links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: School lookup requests are sent to the UpKuaJing provider API and may include institution identifiers.

Mitigation: Use the skill only when provider API processing is acceptable for the lookup and avoid including unrelated sensitive personal data.

Risk: The integration uses a paid API and each school detail query can incur charges.

Mitigation: Confirm pricing and obtain explicit user approval before running fee-incurring queries.

Risk: The API key may be stored locally in ~/.upkuajing/.env.

Mitigation: Protect the local environment file, avoid sharing the key, and rotate the key if exposure is suspected.

Risk: Optional error reports can send troubleshooting context and request details to the platform.

Mitigation: Submit error reports only after user confirmation and exclude secrets or sensitive personal data from the report context.

## Reference(s):

- [School Detail API Reference](artifact/references/school-detail-api.md)
- [Skill Error Report API Reference](artifact/references/skill-error-report-api.md)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing API Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/global-company-person-school-detail)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [JSON API responses and concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires UPKUAJING_API_KEY and explicit confirmation before fee-incurring lookup calls.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
