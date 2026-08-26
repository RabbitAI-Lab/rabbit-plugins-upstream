## Description:

Retrieves Chinese and English descriptions for a given HS code from UpKuaJing customs data to support product classification and trade analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Trade professionals, analysts, and import-export practitioners use this skill to look up what a specific HS code represents before preparing classification checks, customs interpretations, or trade analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill manages an UpKuaJing API key in a local plaintext file.

Mitigation: Use a dedicated API key with limited exposure, avoid storing unrelated secrets in the same file, and rotate the key if the local machine or file is shared.

Risk: HS-code lookups and account helper actions can trigger paid API usage or payment flows.

Mitigation: Confirm pricing and wait for explicit user approval before any paid call or top-up order is executed.

Risk: Confirmed error reports may send request context to the platform.

Mitigation: Review error-report parameters before submission and exclude unrelated secrets or sensitive business context.

Risk: The skill performs automatic version checks against the UpKuaJing service.

Mitigation: Account for outbound network access during use and review update notices before changing installed skill versions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-analysis-hscode-detail)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [UpKuaJing API Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [HS Code Detail API Reference](references/customs-analysis-hscode-detail-api.md)
- [Skill Error Report API Reference](references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful lookups return HS-code detail data, fee information, and a request ID. User-facing responses should explain parameters in natural language.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
