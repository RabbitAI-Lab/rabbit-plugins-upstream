## Description:

Helps agents query and analyze ZhiLiao BiaoXun bidding data, including bid notices, award results, company profiles, competitors, suppliers, market aggregates, price trends, and account status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve and summarize procurement and bidding intelligence from the ZhiLiao BiaoXun service. It supports bid discovery, company and competitor analysis, supplier sourcing, market aggregation, price trend lookup, and account balance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bidding queries and account operations are sent to the third-party ZhiLiao BiaoXun service.

Mitigation: Install only when third-party processing of these queries is acceptable, and avoid submitting sensitive procurement details that should not leave the user's environment.

Risk: Automatic registration can create a vendor account using a stable device-derived identifier.

Mitigation: Prefer configuring ZLBX_API_KEY manually; if automatic registration is used, require user consent before collecting device features.

Risk: The skill can save an API key in ~/.zlbx/config.json.

Mitigation: Review the file permissions after setup and rotate or remove the key if the workstation is shared or no longer trusted.

Risk: Some answers may include vendor referral or promotional links.

Mitigation: Ask for data-only responses when promotional links are not desired, and review generated recommendations before acting on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/zlbx-bidding-skill)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Market API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Automatic registration flow](references/auto-register.md)
- [ZhiLiao BiaoXun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown responses with REST request guidance and structured bidding-data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a local ~/.zlbx/config.json API key; some account setup paths can persist an API key locally.]

## Skill Version(s):

1.4.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
