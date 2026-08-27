## Description:

Searches LinkedIn professional records with name, company, job title, industry, geography, and contact-availability filters to support recruiting, sales prospecting, and B2B lead enrichment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, sales teams, and B2B lead-generation specialists use this skill to find LinkedIn profiles and enrich prospect or candidate lists by company, role, industry, geography, and available contact fields. The skill can create or reuse an UpKuaJing API key, run paid LinkedIn person searches, and save returned records for follow-up workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles a paid UpKuaJing account credential stored in plaintext at ~/.upkuajing/.env.

Mitigation: Use a dedicated API key, avoid shared machines for the credential file, and rotate or remove the key when access is no longer needed.

Risk: LinkedIn searches and account top-ups can incur fees.

Mitigation: Check current pricing before use and require explicit user confirmation before paid calls, especially when the requested count requires multiple API calls.

Risk: Search results may contain personal profile and contact-related data.

Mitigation: Limit searches to legitimate recruiting, sales, or enrichment purposes and restrict access to generated JSONL result files.

Risk: Error reports may include request context or raw response details.

Mitigation: Submit error reports only after user confirmation and avoid sending secrets, raw personal data, or full API responses.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/linkedin-person-search)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [LinkedIn Person List API](references/linkedin-person-list-api.md)
- [Skill Error Report API](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands, JSON API responses, and JSONL result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search output is saved under artifact task_data as JSONL, and each run returns task status, result file path, request id, record count, and fee details.]

## Skill Version(s):

1.0.3 (source: SKILL.md metadata, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
