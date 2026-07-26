## Description: <br>
Ship Position is a HiFleet skill for querying vessel position by ship name or MMSI and using related HiFleet maritime data workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[charleiwang](https://clawhub.ai/user/charleiwang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Maritime operators, analysts, and agents use this skill to identify a vessel, retrieve its latest position, and route related HiFleet queries such as archive, voyage, PSC, port, sanction, traffic, schedule, and charter lookups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a HiFleet API key for account, billing, console-login, and contact-detail workflows. <br>
Mitigation: Use environment variables for the API key, avoid placing keys in URLs or logs, and install only when the user accepts this level of HiFleet account access. <br>
Risk: Billing, subscription, invoice, and bulk contact retrieval actions can affect cost or expose sensitive commercial contact details. <br>
Mitigation: Require explicit user confirmation before billing changes, payment order creation, invoice actions, console-session creation, or bulk contact retrieval. <br>
Risk: Changing HIFLEET_API_BASE could send API-key-authenticated requests to an unintended host. <br>
Mitigation: Keep HIFLEET_API_BASE unset or pointed only at a trusted HiFleet endpoint. <br>


## Reference(s): <br>
- [Ship Position on ClawHub](https://clawhub.ai/charleiwang/skills/hifleet-skills) <br>
- [HiFleet Skills Homepage](https://skills.hifleet.com) <br>
- [Position API](references/position_api.md) <br>
- [API Base](references/api_base.md) <br>
- [Security Notes](SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown or text responses with optional shell commands and API request details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided HiFleet API key for most workflows.] <br>

## Skill Version(s): <br>
0.3.21 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
