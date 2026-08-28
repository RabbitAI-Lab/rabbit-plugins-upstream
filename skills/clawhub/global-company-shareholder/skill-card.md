## Description:

Retrieves global company shareholder rosters, executive and ownership details, and beneficial-owner signals by company ID for corporate due diligence and risk analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External investors, industry analysts, sales teams, and risk management specialists use this skill to inspect shareholder rosters, ownership ratios, share classes, executive records, and control relationships for due diligence, investment research, competitor affiliation checks, related-party screening, and B2B prospecting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores an UpKuaJing API key in ~/.upkuajing/.env or reads it from the environment.

Mitigation: Use a dedicated key, restrict local file permissions, and remove or rotate the key when the skill is no longer needed.

Risk: Shareholder queries and account top-ups can incur fees through the UpKuaJing service.

Mitigation: Confirm pricing and require explicit user approval in a separate step before running any charged query or top-up flow.

Risk: The shared request helper performs a daily version-check call to the UpKuaJing API host.

Mitigation: Install only if that external call is acceptable in the deployment environment and review network egress policy before use.

Risk: Optional error reporting may send request context and troubleshooting details to the platform.

Mitigation: Report errors only after user approval and remove sensitive business, personal, or credential data from the report payload.

Risk: Request and response payload logging could expose company search data if enabled.

Mitigation: Keep payload logging disabled unless there is a specific operational need and logs are stored with appropriate access controls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/upkuajing/skills/global-company-shareholder)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing developer platform](https://developer.upkuajing.com/)
- [UpKuaJing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Shareholder List API reference](references/company-shareholder-list-api.md)
- [Skill Error Report API reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON API responses with concise Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python, httpx, and UPKUAJING_API_KEY; fee-bearing queries require explicit user confirmation before execution.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
