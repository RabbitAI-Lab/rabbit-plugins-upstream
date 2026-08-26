## Description:

Query company-level trade share data for a specified HS code and return ranked customs trade results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

Trade analysts, sourcing agents, and market researchers use this skill to identify major companies trading a specific HS code, compare trade share, and discover potential partners across customs data. It supports exporter or importer views, country filtering, recent-month windows, and paginated ranked company results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid customs-data API calls and payment-related actions can incur charges.

Mitigation: Inform the user that a query or payment action may incur fees and wait for explicit confirmation before running it.

Risk: The skill persists API credentials locally and terminal output may reveal key prefixes or request details.

Mitigation: Use a dedicated low-privilege UpKuaJing API key, restrict access to ~/.upkuajing, and avoid sharing terminal output that contains credential or request metadata.

Risk: Normal API calls also perform automatic version-check network calls and create local files under ~/.upkuajing.

Mitigation: Review this network behavior and local file creation before installing the skill in environments with sensitive business data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/customs-analysis-trade-percent)
- [UpKuaJing homepage](https://www.upkuajing.com)
- [UpKuaJing developer platform](https://developer.upkuajing.com/)
- [UpKuaJing API pricing](https://www.upkuajing.com/web/openapi/price.html)
- [Trade Percent API reference](artifact/references/customs-analysis-trade-percent-api.md)
- [Skill Error Report API reference](artifact/references/skill-error-report-api.md)

## Skill Output:

**Output Type(s):** [API Calls, Analysis, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python and UPKUAJING_API_KEY; paid queries require explicit user confirmation and may return fee and request ID metadata.]

## Skill Version(s):

1.0.1 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
