## Description:

AI tender and bid analysis agent for querying Zhiliaobiaoxun tender data, evaluating market opportunities, company activity, competitors, suppliers, purchasing trends, and bid histories through natural-language requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External business, procurement, sales, and market-analysis users use this skill to query tender and bid records, analyze purchasers and suppliers, profile companies, evaluate competitors, identify opportunities, and generate concise market or project reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill integrates with a third-party external API and account onboarding flow.

Mitigation: Install only after reviewing the vendor relationship, API terms, and whether external tender-data calls are appropriate for the deployment environment.

Risk: Automatic onboarding can collect device-derived identifiers for trial deduplication.

Mitigation: Prefer manually configuring ZLBX_API_KEY; if auto-registration is used, require clear user consent before collecting platform, CPU architecture, or hashed MAC information.

Risk: The skill can store an API key in a local plaintext configuration file.

Mitigation: Review ~/.zlbx/config.json after use, restrict local file access, and rotate or remove the key when it is no longer needed.

Risk: The security verdict is suspicious because of the external API, onboarding flow, device-deduplication data collection, and local API-key storage.

Mitigation: Use evidence.security as the review baseline, scan before deployment, and avoid auto-login or recharge links unless the user expects account-management actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/ai-tender-bid-analyst)
- [API search reference](references/api-search.md)
- [API company reference](references/api-company.md)
- [API market reference](references/api-market.md)
- [API account reference](references/api-account.md)
- [Auto-registration reference](references/auto-register.md)
- [Zhiliaobiaoxun account portal](https://ai.zhiliaobiaoxun.com/?ch=s53)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON request examples, REST API calls, shell commands, and concise analysis summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY for API access; may create ~/.zlbx/config.json after user-approved auto-registration.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
