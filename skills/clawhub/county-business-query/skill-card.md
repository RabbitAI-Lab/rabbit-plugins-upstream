## Description:

County Business Query helps agents query Chinese county-level bidding notices, award details, winning-company phone mappings, company registration information, and service status through the dcbmt.com service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[498617](https://clawhub.ai/user/498617)

### License/Terms of Use:

MIT-0

## Use Case:

External business researchers, sales teams, and procurement analysts use this skill to search county-level business opportunities in China, inspect bid and award records, retrieve winner contact mappings, and look up company registration records.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: API-key registration and payment onboarding may direct users to an off-platform QQ contact, increasing phishing, impersonation, or unrelated credential-disclosure risk.

Mitigation: Review onboarding language before installation, prefer the official service URL shown in the skill details, avoid short links, and do not share unrelated credentials or personal information with the script or support contact.

Risk: The skill returns business contact data such as company phone numbers, which may require careful handling in sales, procurement, or market-research workflows.

Mitigation: Use returned contact information only for legitimate business purposes and apply the organization's privacy, consent, and data-retention rules before storing or acting on it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/498617/skills/county-business-query)
- [Official County Query Service](https://dcbmt.com/county/?src=clawhub)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [JSON responses and concise Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bidding notice metadata, company names, phone numbers, notice URLs, pagination fields, API-key errors, quota messages, and registration guidance.]

## Skill Version(s):

8.13.0 (source: server release metadata and clawhub.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
