## Description:

Queries Juhe enterprise abnormal-operation registry data by company name, registration number, or unified social credit code and returns listing or removal reasons, dates, decision authority, and publication status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[juhemcp](https://clawhub.ai/user/juhemcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to check whether a business appears in current or historical abnormal-operation public records during cooperation review, due diligence, or company status checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company names, registration numbers, or unified social credit codes are sent to Juhe for lookup.

Mitigation: Use the skill only when sharing those lookup terms with Juhe is acceptable for the user and organization.

Risk: The Juhe API key could be exposed if passed on the command line or committed in a local .env file.

Mitigation: Prefer a managed environment variable for JUHE_ENTERPRISE_ABNORMAL_KEY, avoid command-line key arguments, and do not commit .env files containing the key.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/juhemcp/skills/juhe-enterprise-abnormal)
- [Juhe enterprise abnormal-operation API documentation](https://www.juhe.cn/docs/api/id/841)
- [Juhe data service platform](https://www.juhe.cn)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Formatted text with JSON result payloads and command-line examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and a JUHE_ENTERPRISE_ABNORMAL_KEY API key.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
